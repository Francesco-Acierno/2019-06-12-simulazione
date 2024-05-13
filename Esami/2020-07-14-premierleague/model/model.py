import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.squadre = DAO.getAllTeams()
        self.idMap = {}
        for t in self.squadre:
            self.idMap[t.TeamID] = t

    def buildGraph(self):
        self.grafo.clear()
        self.grafo.add_nodes_from(self.squadre)

        teams = DAO.getAllPunteggi()
        for t in teams:
            for t1 in teams:
                squadra1 = self.idMap[t[0]]
                squadra2 = self.idMap[t1[0]]
                if squadra1 != squadra2:
                    peso = t[1] - t1[1]
                    if peso > 0:
                        self.grafo.add_edge(squadra1, squadra2, weight=peso)
                    elif peso < 0:
                        self.grafo.add_edge(squadra2, squadra1, weight=-peso)

    def getClassifica(self, squadra_id):
        listaMigliori = []
        listaPeggiori = []
        nodo = self.idMap[squadra_id]
        for n in self.grafo.nodes:
            if self.grafo.has_edge(n, nodo):
                listaMigliori.append((n, self.grafo[n][nodo]['weight']))
            if self.grafo.has_edge(nodo, n):
                listaPeggiori.append((n, self.grafo[nodo][n]['weight']))
        listaMiglioriOrdinata = sorted(listaMigliori, key=lambda x: x[1], reverse=True)
        listaPeggioriOrdinata = sorted(listaPeggiori, key=lambda x: x[1], reverse=False)
        return listaMiglioriOrdinata, listaPeggioriOrdinata
