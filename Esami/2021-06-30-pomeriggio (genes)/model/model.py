import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.bestScore = 0
        self._solBest = []
        self.grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllLocalizzazioni())

        for l in self.grafo.nodes():
            self._idMap[l] = l

        archi = DAO.getAllConnessione()
        for n1, n2, peso in archi:
            if n1 in self._idMap.keys() and n2 in self._idMap.keys():
                nodo1 = self._idMap[n1]
                nodo2 = self._idMap[n2]
                if self.grafo.has_edge(nodo1, nodo2) is False:
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)

    def getConnessi(self, localizzazione):
        connessi = {}
        nodo = self._idMap.get(localizzazione)

        connected_component = nx.node_connected_component(self.grafo, nodo)

        for v in connected_component:
            if v != nodo:
                try:
                    peso = self.grafo[nodo][v]["weight"]
                    connessi[v] = peso
                except KeyError:
                    pass

        connessiOrdinati = sorted(connessi.items(), key=lambda x: x[1], reverse=True)
        return connessiOrdinati

    def searchPath(self, localizzazione):
        nodoSource = self._idMap[localizzazione]

        parziale = [nodoSource]

        self.ricorsione(parziale, nodoSource)
        return self._solBest, self.bestScore

    def ricorsione(self, parziale, nodoSource):
        if self._getScore(parziale) > self.bestScore:
            self._solBest = copy.deepcopy(parziale)
            self.bestScore = self._getScore(parziale)

        for vicino in self.grafo.neighbors(parziale[-1]):
            if vicino not in parziale:
                parziale.append(vicino)
                self.ricorsione(parziale, nodoSource)
                parziale.pop()

    def _getScore(self, listOfNodes):
        score = 0
        for i in range(len(listOfNodes) - 1):
            nodo_attuale = listOfNodes[i]
            nodo_successivo = listOfNodes[i + 1]
            score += self.grafo[nodo_attuale][nodo_successivo]["weight"]
        return score
