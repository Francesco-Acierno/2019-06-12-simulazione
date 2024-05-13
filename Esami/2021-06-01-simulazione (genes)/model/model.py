import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllNodes())
        print(self.grafo.nodes())

        for g in self.grafo.nodes():
            self._idMap[g.GeneID] = g

        archi = DAO.getAllConnessione()
        for a in archi:
            if a.n1 in self._idMap.keys() and a.n2 in self._idMap.keys():
                if a.cromosoma1 == a.cromosoma2:
                    pesoSC = 2 * abs(a.peso)
                    nodo1 = self._idMap[a.n1]
                    nodo2 = self._idMap[a.n2]
                    if self.grafo.has_edge(nodo1, nodo2) is False:
                        self.grafo.add_edge(nodo1, nodo2, weight=pesoSC)
                elif a.cromosoma1 != a.cromosoma2:
                    pesoDC = abs(a.peso)
                    nodo1 = self._idMap[a.n1]
                    nodo2 = self._idMap[a.n2]
                    if self.grafo.has_edge(nodo1, nodo2) is False:
                        self.grafo.add_edge(nodo1, nodo2, weight=pesoDC)

    def getVicini(self, gene):
        vicini = {}
        for v in self.grafo.neighbors(gene):
            vicini[v] = self.grafo[gene][v]["weight"]
        viciniOrdinati = sorted(vicini.items(), key=lambda x: x[1], reverse=True)
        return viciniOrdinati




