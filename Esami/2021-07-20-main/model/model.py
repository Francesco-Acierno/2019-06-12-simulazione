import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self, rec, anno):
        self._grafo.clear()
        self._grafo.add_nodes_from(DAO.getAllUtenti(rec))
        for n in self._grafo.nodes():
            self._idMap[n.user_id] = n

        archi = DAO.getAllConnessioni(anno)
        for n1, n2, peso in archi:
            if n1 in self._idMap.keys() and n2 in self._idMap.keys():
                nodo1 = self._idMap[n1]
                nodo2 = self._idMap[n2]
                if self._grafo.has_edge(nodo1, nodo2) is False:
                    self._grafo.add_edge(nodo1, nodo2, weight=peso)
        return self._grafo
