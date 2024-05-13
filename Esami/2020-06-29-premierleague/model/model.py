import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._bestPath = []
        self._bestPeso = 0
        self.dict = {}
        self.grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self, mese, min):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllMatch(mese))
        for m in self.grafo.nodes():
            self._idMap[m.MatchID] = m

        archi = DAO.getAllConnessioni(min)
        for n1, n2, peso in archi:
            if n1 in self._idMap.keys() and n2 in self._idMap.keys():
                nodo1 = self._idMap[n1]
                nodo2 = self._idMap[n2]
                if self.grafo.has_edge(nodo1, nodo2) is False:
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)

    def getGradoMax(self):
        lista = []
        for arco in self.grafo.edges:
            self.dict[arco] = self.grafo[arco[0]][arco[1]]["weight"]
        dictOrder = list(sorted(self.dict.items(), key=lambda item: item[1], reverse=True))
        gradoMassimo = dictOrder[0][1]
        for arco in self.grafo.edges:
            if self.grafo[arco[0]][arco[1]]["weight"] == gradoMassimo:
                lista.append(arco)
        return lista, gradoMassimo

    def getCamminoOttimo(self, a1, a2):
        self._bestPath = []

        p1 = self._idMap[int(a1)]
        p2 = self._idMap[int(a2)]
        parziale = [p1]

        self.ricorsione(parziale, p2)

        return self._bestPath, self._bestPeso

    def ricorsione(self, parziale, a2):

        if parziale[-1] == a2:
            if self.getObjFun(parziale) > self._bestPeso:
                self._bestPeso = self.getObjFun(parziale)
                self._bestPath = copy.deepcopy(parziale)
                return

        for n in self.grafo.neighbors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                self.ricorsione(parziale, a2)
                parziale.pop()

    def getObjFun(self, listOfNodes):
        objVal = 0
        for i in range(0, len(listOfNodes) - 1):
            objVal += self.grafo[listOfNodes[i]][listOfNodes[i + 1]]['weight']
        return objVal
