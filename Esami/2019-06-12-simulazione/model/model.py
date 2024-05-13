import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}
        self._solBest = []
        self._costBest = 0

    def buildGraph(self, cal):
        self._grafo.clear()
        self._grafo.add_nodes_from(DAO.getAllIngredienti(cal))
        for n in self._grafo.nodes():
            self._idMap[n.condiment_code] = n

        archi = DAO.getAllConnessioni()
        for n1, n2, peso in archi:
            if n1 in self._idMap.keys() and n2 in self._idMap.keys():
                nodo1 = self._idMap[n1]
                nodo2 = self._idMap[n2]
                if self._grafo.has_edge(nodo1, nodo2) is False:
                    self._grafo.add_edge(nodo1, nodo2, weight=peso)
        return self._grafo

    def getIngredienti(self):
        dictP = {}
        peso = 0
        for n in self._grafo.nodes:
            peso = 0
            for v in self._grafo.neighbors(n):
                peso += self._grafo[v][n]['weight']
            if n not in dictP.keys():
                dictP[n] = (n.condiment_calories, peso)
        return dictP

    def getBestPath(self, v0):
        self._solBest = []
        self._costBest = 0

        parziale = [v0]
        visited = {v0}

        self.ricorsione(parziale, v0, visited)

        return self._solBest, self._costBest

    def ricorsione(self, parziale, v0, visited):
        # Controllo se parziale è una sol valida, e in caso se è migliore del best
        if v0 in parziale:
            current_cost = self.peso(parziale)
            if current_cost > self._costBest:
                self._costBest = current_cost
                self._solBest = copy.deepcopy(parziale)

        # Se arrivo qui, allora len(parziale) < lun
        for v in self._grafo.nodes:
            if v not in visited:
                parziale.append(v)
                visited.add(v)
                self.ricorsione(parziale, v0, visited)
                parziale.pop()
                visited.remove(v)

    def peso(self, listObject):
        p = 0
        for node in listObject:
            p += node.condiment_calories
        return p




