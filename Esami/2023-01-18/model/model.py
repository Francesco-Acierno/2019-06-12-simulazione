import copy

import networkx as nx
from database.DAO import DAO
from geopy.distance import geodesic


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self.dictMaggiore = {}
        self._bestPath = []
        self._bestObjFun = 0

    def getProvider(self):
        return DAO.getAllProvider()

    def getLocation(self, provider):
        return DAO.getAllLocation(provider)

    def buildGraph(self, provider, soglia):
        self._grafo.clear()
        self._grafo.add_nodes_from(DAO.getAllLocation(provider))

        connessioni = DAO.getAllGeolocalizzazione(provider)
        for c in connessioni:
            punto1 = (c.lat1, c.long1)
            punto2 = (c.lat2, c.long2)
            distance_km = geodesic(punto1, punto2).km
            if distance_km <= soglia:
                if self._grafo.has_edge(punto1,
                                        punto2) is False and c.n1 in self._grafo.nodes and c.n2 in self._grafo.nodes:
                    self._grafo.add_edge(c.n1, c.n2, weight=distance_km)
        return self._grafo

    def getAnalisi(self):
        dictn = {}
        for n in self._grafo.nodes:
            for v in self._grafo.neighbors(n):
                if n not in dictn:
                    dictn[n] = 1
                else:
                    dictn[n] += 1
        self.dictMaggiore = {}
        maggiorVicini = 0
        for l in dictn:
            if dictn[l] >= maggiorVicini:
                maggiorVicini = dictn[l]
        for a in dictn:
            if dictn[a] >= maggiorVicini:
                self.dictMaggiore[a] = maggiorVicini
        return self.dictMaggiore

    def getCamminoOttimo(self, v1, stringa):
        self._bestPath = []
        self._bestObjFun = 0

        for v0 in (self.dictMaggiore):
            if stringa not in v0.upper():
                parziale = [v0]

        self._ricorsione(parziale, v1, stringa)

        return self._bestPath, self._bestObjFun

    def _ricorsione(self, parziale, target, stringa):
        # Verificare che parziale sia una possibile soluzione
        # Verificare se parziale è meglio di best
        # esco
        if len(parziale) > self._bestObjFun and parziale[-1] == target and stringa not in parziale[-1].upper():
            self._bestPath = copy.deepcopy(parziale)
            self._bestObjFun = len(self._bestPath)

        # Posso ancora aggiungere nodi.
        # prendo i vicini e provo ad aggiungere
        # ricorsione
        for n in self._grafo.neighbors(parziale[-1]):
            if n not in parziale and stringa not in n.upper():
                parziale.append(n)
                self._ricorsione(parziale, target, stringa)
                parziale.pop()
