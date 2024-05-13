import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.idMap = {}

    def getGeneri(self):
        return DAO.getAllGeneri()

    def buildGraph(self, genere):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllNodi(genere))
        for a in self.grafo.nodes:
            self.idMap[a.id] = a

        archi = DAO.getAllConnessioni(genere)
        for n1, n2, peso in archi:
            if n1 in self.idMap.keys() and n2 in self.idMap.keys():
                nodo1 = self.idMap[n1]
                nodo2 = self.idMap[n2]
                if self.grafo.has_edge(nodo1, nodo2) is False:
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)

    import networkx as nx

    def getSimili(self, attore):
        nodo = self.idMap[attore.id]
        connected_component = nx.node_connected_component(self.grafo, nodo)
        simili = sorted(connected_component, key=lambda x: x.last_name)
        return simili
