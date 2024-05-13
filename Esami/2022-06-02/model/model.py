import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self._idMap = {}
        self.maggioreConnessa = {}
        self._bestPath = []
        self._bestPeso = 0

    def getGeneri(self):
        return DAO.getAllGeneri()

    def getMinMax(self, genere):
        return DAO.getMinMax(genere)

    def buildGraph(self, minG, maxG, genere):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllTracce(minG, maxG, genere))

        for t in self.grafo.nodes():
            self._idMap[t.TrackId] = t

        nodi = DAO.getAllConnessioni(genere, minG, maxG)
        for n in nodi:
            if n[0] in self._idMap and n[1] in self._idMap:
                if self.grafo.has_edge(self._idMap[n[0]], self._idMap[n[1]]) is False:
                    self.grafo.add_edge(self._idMap[n[0]], self._idMap[n[1]])
        return self.grafo

    def getConnesse(self):
        componenti_connesse = list(nx.connected_components(self.grafo))

        risultati = []
        for componente in componenti_connesse:
            num_vertici = len(componente)

            playlist_dict = set()
            for nodo in componente:
                for playlist in DAO.getPlaylist(nodo.TrackId):
                    playlist_dict.add(playlist)

            num_playlist = len(playlist_dict)
            risultati.append((num_vertici, num_playlist))
            risultati_ordinati = sorted(risultati, key=lambda x: x[0], reverse=True)
            if num_vertici == risultati_ordinati[0][0]:
                self.maggioreConnessa = componente
        return risultati

    def getCamminoOttimo(self, dTot):
        self._bestPath = []
        self._bestPeso = 0

        connessa = list(self.maggioreConnessa)
        for c in connessa:
            parziale = set([c])
            connessa.remove(c)

        self._ricorsione(parziale, connessa, dTot)

        return self._bestPath, self._bestPeso

    def _ricorsione(self, parziale, connessa, dTot):
        # verificare se parziale è una sol ammissibile
        if self.getObjFun(parziale) > dTot:
            return

        # verificare se parziale è migliore del best
        if len(parziale) > self._bestPeso:
            self._bestPath = copy.deepcopy(parziale)
            self._bestPeso = len(parziale)

        # ciclo sui nodi raggiungibili -- ricorsione
        for c in connessa:
            if c not in parziale:
                parziale.add(c)
                rimanenti = copy.deepcopy(connessa)
                rimanenti.remove(c)
                self._ricorsione(parziale, rimanenti, dTot)
                parziale.remove(c)

    def getObjFun(self, listOfNodes):
        objVal = 0
        for n in listOfNodes:
            objVal += n.Milliseconds
        return objVal
