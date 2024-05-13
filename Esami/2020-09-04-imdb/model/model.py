import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._idMap = {}
        self._grafo = nx.Graph()
        self._nodi = DAO.getAllFilm()
        self._grafo.add_nodes_from(self._nodi)
        self._idMap = dict()
        for f in self._grafo.nodes:
            self._idMap[f.id] = f
        self.nodoGradoMax = []
        self._solBest = []
        self.peso = 0

    def buildGraph(self, rank):
        self._grafo.clear_edges()
        archi = DAO.getPeso(rank)
        for n1, n2, peso in archi:
            if self._grafo.has_edge(self._idMap[n1], self._idMap[n2]) is False:
                self._grafo.add_edge(self._idMap[n1], self._idMap[n2], weight=peso)

    def getGradoMax(self):
        self.nodoGradoMax = []
        for n in self._grafo.nodes:
            peso = 0
            for s in self._grafo.neighbors(n):
                peso += self._grafo[n][s]['weight']
            self.nodoGradoMax.append((n, peso))
        ordinata = sorted(self.nodoGradoMax, key=lambda x: x[1], reverse=True)
        return ordinata[0][0], ordinata[0][1]

    def searchPath(self, film):
        nodoSource = film

        parziale = []

        self.ricorsione(parziale, nodoSource, 0)
        return self._solBest

    def ricorsione(self, parziale, nodoLast, livello):
        archiViciniAmmissibili = self.getArchiViciniAmm(nodoLast, parziale)

        if len(archiViciniAmmissibili) == 0 and parziale[-1] != parziale[0]:
            if len(parziale) > len(self._solBest):
                self._solBest = list(parziale)

        for a in archiViciniAmmissibili:
            parziale.append(a)
            self.ricorsione(parziale, a[1], livello + 1)
            parziale.pop()

    def getArchiViciniAmm(self, nodoLast, parziale):

        archiVicini = self._grafo.edges(nodoLast, data=True)
        result = []
        for a1 in archiVicini:
            if self.isAscendent(a1, parziale) and self.isNovel(a1, parziale):
                result.append(a1)
        return result

    def isAscendent(self, e, parziale):
        if len(parziale) == 0:
            return True
        return e[2]["weight"] >= parziale[-1][2]["weight"]

    def isNovel(self, e, parziale):
        if len(parziale) == 0:
            return True
        e_inv = (e[1], e[0], e[2])
        return (e_inv not in parziale) and (e not in parziale)
