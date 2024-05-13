import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._bestObjVal = 0
        self._bestPath = []
        self.grafo = nx.Graph()
        self.idMap = {}

    def getRuoli(self):
        return DAO.getAllRuoli()

    def buildGraph(self, ruolo):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllNodi(ruolo))
        for a in self.grafo.nodes:
            self.idMap[a.artist_id] = a

        archi = DAO.getAllConnessioni(ruolo)
        for n1, n2, peso in archi:
            if n1 in self.idMap.keys() and n2 in self.idMap.keys():
                nodo1 = self.idMap[n1]
                nodo2 = self.idMap[n2]
                if self.grafo.has_edge(nodo1, nodo2) is False:
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)

    def artistiConnessi(self):
        listaArtisti = self.grafo.edges(data=True)
        listaArtistiOrdinata = sorted(listaArtisti, key=lambda x: x[2]['weight'], reverse=True)
        return listaArtistiOrdinata

    def searchPath(self, artista_id):
        artista = self.idMap[artista_id]
        parziale = []
        listaNodi = [artista]
        self.ricorsione(artista, parziale, listaNodi)
        return self._bestPath, self._bestObjVal

    def ricorsione(self, n, parziale, listaNodi):
        archiViciniAmmissibili = self.getArchiViciniAmm(n, parziale, listaNodi)

        if len(archiViciniAmmissibili) == 0:
            if len(parziale) > self._bestObjVal:
                self._bestPath = copy.deepcopy(parziale)
                self._bestObjVal = len(self._bestPath)

        for a in archiViciniAmmissibili:
            parziale.append(a)
            self.ricorsione(a[1], parziale, listaNodi)
            parziale.pop()

    def getArchiViciniAmm(self, nodoLast, parziale, listaNodi):
        archiVicini = self.grafo.edges(nodoLast, data=True)
        result = []
        for a1 in archiVicini:
            if a1[1] not in listaNodi and self.isAscendent(a1, parziale) and self.isNovel(a1, parziale):
                result.append(a1)
                listaNodi.append(a1[1])
        return result

    def isAscendent(self, e, parziale):
        if len(parziale) == 0:
            return True
        return e[2]["weight"] == parziale[-1][2]["weight"]

    def isNovel(self, e, parziale):
        if len(parziale) == 0:
            return True
        e_inv = (e[1], e[0], e[2])
        return (e_inv not in parziale) and (e not in parziale)
