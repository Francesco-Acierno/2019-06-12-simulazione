import copy

import networkx as nx

from database.DAO import DAO

from geopy.distance import geodesic


class Model:
    def __init__(self):
        self._bestObjVal = 0
        self._bestPath = []
        self._dictPesi = {}
        self._graph = nx.Graph()

    def buildGraph(self, anno, forma):
        self._graph.clear()
        self._paesi = DAO.getAllPaesi()
        self._idMap = {}
        for p in self._paesi:
            self._idMap[p.id] = p
        self._graph.add_nodes_from(self._paesi)

        confini = DAO.getPaeseiConfinanti(self._idMap)
        for b in confini:
            self._graph.add_edge(b.c1, b.c2)
            self._graph[b.c1][b.c2]["weight"] = DAO.getPeso(anno, forma, b.c1.id, b.c2.id)

    def getPesiAdiacenti(self):
        self._dictPesi = {}
        for n in self._graph.nodes:
            totAdiacenti = 0
            for v in self._graph.neighbors(n):
                totAdiacenti += self._graph[n][v]['weight']
            self._dictPesi[n] = totAdiacenti
        return self._dictPesi

    def getDistance(self, a, b):
        return self.getDistanceBetweenPointsNew(a.Lat, a.Lng, b.Lat, b.Lng)

    def searchPath(self):

        for nodo in self._graph.nodes():
            parziale = []
            self.ricorsione(nodo, parziale)
        return self._bestPath, self._bestObjVal

    def ricorsione(self, n, parziale):
        archiViciniAmmissibili = self.getArchiViciniAmm(n, parziale)

        if len(archiViciniAmmissibili) == 0:
            if self._getMaxDistance(parziale) > self._bestObjVal:
                self._bestPath = copy.deepcopy(parziale)
                self._bestObjVal = self._getMaxDistance(parziale)

        for a in archiViciniAmmissibili:
            parziale.append(a)
            self.ricorsione(a[1], parziale)
            parziale.pop()

    def getArchiViciniAmm(self, nodoLast, parziale):
        archiVicini = self._graph.edges(nodoLast, data=True)
        result = []
        for a1 in archiVicini:

            if self.isAscendent(a1, parziale) and self.isNovel(a1, parziale):
                result.append(a1)
        return result

    def isAscendent(self, e, parziale):
        if len(parziale) == 0:
            return True
        return e[2]["weight"] > parziale[-1][2]["weight"]

    def isNovel(self, e, parziale):
        if len(parziale) == 0:
            return True
        e_inv = (e[1], e[0], e[2])
        return (e_inv not in parziale) and (e not in parziale)

    def _getMaxDistance(self, listOfNodes):

        if len(listOfNodes) == 1:
            return 0

        maxDistance = 0
        for i in range(0, len(listOfNodes) ):
            maxDistance += self.getDistance(listOfNodes[i][0], listOfNodes[i][1])
        return maxDistance

    def getDistanceBetweenPointsNew(self, latitude1, longitude1, latitude2, longitude2):
        punto1 = (latitude1, longitude1)
        punto2 = (latitude2, longitude2)
        distanza = geodesic(punto1, punto2).km
        return distanza

    def graphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getForme(self, anno):
        return DAO.getAllForme(anno)
