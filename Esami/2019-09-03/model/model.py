import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._solBest = []
        self._costBest = 0

    def buildGraph(self, cal):
        self._grafo.clear()
        self._grafo.add_nodes_from(DAO.getAllNodes(cal))

        archi = DAO.getAllConnessioni(cal)
        for n1, n2, peso in archi:
            if n1 in self._grafo.nodes and n2 in self._grafo.nodes:
                if self._grafo.has_edge(n1, n2) is False:
                    self._grafo.add_edge(n1, n2, weight=peso)

    def getConnesse(self, tipo):
        if tipo in self._grafo.nodes():
            vicini = self._grafo.neighbors(tipo)
        return vicini

    def getBestPath(self, npassi, v0):
        self._solBest = []
        self._costBest = 0
        parziale = [v0]
        for v in self._grafo.neighbors(v0):
            parziale.append(v)
            self.ricorsione(parziale, npassi)
            parziale.pop()
        return self._solBest, self._costBest

    def ricorsione(self, parziale, npassi):
        if len(parziale) - 1 == npassi:
            if self.peso(parziale) > self._costBest:
                self._costBest = self.peso(parziale)
                self._solBest = copy.deepcopy(parziale)

        if len(parziale) - 1 < npassi:
            for v in self._grafo.neighbors(parziale[-1]):
                if v not in parziale:
                    parziale.append(v)
                    self.ricorsione(parziale, npassi)
                    parziale.pop()

    def peso(self, parziale):
        peso = 0
        for i in range(0, len(parziale) - 1):
            peso += self._grafo[parziale[i]][parziale[i + 1]]["weight"]
        return peso