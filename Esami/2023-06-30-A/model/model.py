import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.peso = None
        self.nodi = None
        self.grafo = nx.Graph()
        self._idMap = {}

    def getSquadre(self):
        return DAO.getAllSquadre()

    def buildGraph(self, squadra):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllNodi(squadra))

        for a in self.grafo.nodes():
            self._idMap[a] = a

        archi = DAO.getAllConnessioni(squadra)
        for n1, n2, peso in archi:
            if n1 in self._idMap.keys() and n2 in self._idMap.keys():
                nodo1 = self._idMap[n1]
                nodo2 = self._idMap[n2]
                if self.grafo.has_edge(nodo1, nodo2) is False:
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)

    def getAdiacenti(self, anno):
        vicini = {}
        for v in self.grafo.neighbors(anno):
            vicini[v] = self.grafo[anno][v]['weight']
        viciniOrdinati = sorted(vicini.items(), key=lambda x: x[1], reverse=True)

        return viciniOrdinati

