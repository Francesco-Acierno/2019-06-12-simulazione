import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._bestObjFun = 0
        self._bestPath = []
        self._graph = nx.DiGraph()
        self._album = []
        self.dizionario_bilanci = {}
        self._idMapAlbums = {}

    def buildGraph(self, nItems):
        self._graph.clear()
        self._album = DAO.getAllNodi(nItems)
        self._graph.add_nodes_from(self._album)
        for f in self._album:
            self._idMapAlbums[f.AlbumId] = f
        for album1 in self._album:
            for album2 in self._album:
                if album2 != album1:
                    weight = album1.numeroTracce - album2.numeroTracce
                    if weight > 0:
                        self._graph.add_edge(album2, album1, weight=weight)
                    elif weight < 0:
                        self._graph.add_edge(album1, album2, weight=-weight)

    def getBilancio(self):
        self.dizionario_bilanci = {}
        for s in self._graph.nodes:
            successori = sum(self._graph[s][suc]['weight'] for suc in self._graph.successors(s))
            predecessori = sum(self._graph[pred][s]['weight'] for pred in self._graph.predecessors(s))
            self.dizionario_bilanci[s.AlbumId] = predecessori - successori
        return self.dizionario_bilanci

    def getVicini(self, a1):
        if not self.dizionario_bilanci:
            self.getBilancio()

        vicini_dizionario = {}
        for album in self._album:
            if album == a1:
                continue
            if album in self._graph.neighbors(a1):
                vicini_dizionario[album] = self.dizionario_bilanci[album.AlbumId]

        dizionario_ordinato = sorted(vicini_dizionario.items(), key=lambda x: x[1], reverse=True)
        return dizionario_ordinato

    def getCamminoOttimo(self, a1, a2, peso_min):
        self._bestPath = []

        parziale = [a1]

        self.ricorsione(parziale, a2, peso_min)

        return self._bestPath

    def ricorsione(self, parziale, a2, peso_min):
        print(a2)
        if parziale[-1].AlbumId == a2.AlbumId:
            if len(parziale) > len(self._bestPath):
                self._bestPath = copy.deepcopy(parziale)
        for v in self._graph.successors(parziale[-1]):
            print(v)
            if v not in parziale:
                if self._graph[parziale[-1]][v]['weight'] >= peso_min:
                    if self.dizionario_bilanci[v.AlbumId] > self.dizionario_bilanci[parziale[0].AlbumId]:
                        parziale.append(v)
                        self.ricorsione(parziale, a2, peso_min)
                        parziale.pop()
                    else:
                        if v.AlbumId == a2.AlbumId:
                            if len(parziale) + 1 > len(self._bestPath):
                                parziale.append(v)
                                self._bestPath = copy.deepcopy(parziale)
                                return
                else:
                    if v.AlbumId == a2.AlbumId:
                        if len(parziale) + 1 > len(self._bestPath):
                            parziale.append(v)
                            self._bestPath = copy.deepcopy(parziale)
