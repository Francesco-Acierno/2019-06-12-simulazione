import copy

import networkx as nx

from Laboratorio.Lab_12.database.DAO import DAO


class Model:
    def __init__(self):
        self._bestObjFun = 0
        self._bestPath = []
        self._graph = nx.Graph()

    def buildGraph(self, nazione, anno):
        self._retailers = DAO.getAllRetailers(nazione)
        self._idMap = {}
        for r in self._retailers:
            self._idMap[r.Retailer_code] = r
        self._graph.clear()
        self._graph.add_nodes_from(self._retailers)
        for v0 in self._graph.nodes:
            for v1 in self._graph.nodes:
                if v0 != v1:
                    peso = DAO.getAllConnessioni(anno, v0, v1)
                    if int(peso) > 0:
                        self._graph.add_edge(v0, v1, weight=int(peso))
        return self._graph

    def getNazioni(self):
        return DAO.getAllNazioni()

    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)

    def getVolumeVendite(self):
        peso = 0
        volume_retailer = {}
        for nodo in self._graph.nodes:
            peso = 0
            for v1 in self._graph.neighbors(nodo):
                peso += self._graph[nodo][v1]['weight']
                volume_retailer[nodo] = peso
        return volume_retailer

    def getCamminoOttimo(self, t):
        self._bestPath = []
        self._bestObjFun = 0

        for v0 in self._graph.nodes:
            parziale = [v0]
            self._ricorsione(parziale, t)

        return self._bestPath, self._bestObjFun

    def _ricorsione(self, parziale, t):
        if len(parziale) == t+1:
            if self.getObjFun(parziale) > self._bestObjFun:
                self._bestObjFun = self.getObjFun(parziale)
                self._bestPath = copy.deepcopy(parziale)
            return

        if len(parziale) == t and parziale[0] in self._graph.neighbors(parziale[-1]):
            parziale.append(parziale[0])
            if self.getObjFun(parziale) > self._bestObjFun:
                self._bestObjFun = self.getObjFun(parziale)
                self._bestPath = copy.deepcopy(parziale)
            parziale.pop()
            return

        for n in self._graph.neighbors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                self._ricorsione(parziale, t)
                parziale.pop()

    def getObjFun(self, listOfNodes):
        objVal = 0
        for i in range(0, len(listOfNodes) - 1):
            objVal += self._graph[listOfNodes[i]][listOfNodes[i + 1]]['weight']
        return objVal
