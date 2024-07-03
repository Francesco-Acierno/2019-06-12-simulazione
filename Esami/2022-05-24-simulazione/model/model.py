import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._maxCanzoni = 0
        self._grafo = nx.Graph()
        self._idMap = {}
        self._soluzione = []

    def getGeneri(self):
        return DAO.getAllGeneri()

    def getMinMax(self, genere):
        return DAO.getMinMax(genere)

    def buildGraph(self, minG, maxG, genere):
        self._grafo.clear()
        self._grafo.add_nodes_from(DAO.getAllTracce(minG, maxG, genere))

        for c in self._grafo.nodes():
            self._idMap[c.TrackId] = c

        archi = DAO.getAllConnessioni(genere)
        for n1, n2, peso in archi:
            if n1 in self._idMap.keys() and n2 in self._idMap.keys():
                nodo1 = self._idMap[n1]
                nodo2 = self._idMap[n2]
                if self._grafo.has_edge(nodo1, nodo2) is False:
                    self._grafo.add_edge(nodo1, nodo2, weight=peso)

    def getBest(self):
        migliori = sorted(self._grafo.edges(data=True), key=lambda x: x[2]['weight'], reverse=True)
        migliorDelta = migliori[0][2]['weight']
        best = []
        for a in self._grafo.edges(data=True):
            if a[2]['weight'] == migliorDelta:
                best.append(a)
        return best

    def getBestPath(self, canzone_preferita, memoria_massima):
        componente_connessa = list(nx.node_connected_component(self._grafo, canzone_preferita))
        parziale = [canzone_preferita]
        self._ricorsione(parziale, componente_connessa, memoria_massima)
        return self._soluzione, self._maxCanzoni

    def _ricorsione(self, parziale, componente_connessa, memoria_massima):
        memoria_utilizzata = self._calcolaMemoria(parziale)
        if memoria_utilizzata > memoria_massima:
            return

        if len(parziale) > self._maxCanzoni:
            self._soluzione = copy.deepcopy(parziale)
            self._maxCanzoni = len(parziale)

        for canzone in componente_connessa:
            if canzone not in parziale:
                parziale.append(canzone)
                self._ricorsione(parziale, componente_connessa, memoria_massima)
                parziale.pop()

    def _calcolaMemoria(self, lista_canzoni):
        memoria_totale = 0
        for canzone in lista_canzoni:
            memoria_totale += canzone.Bytes
        return memoria_totale
