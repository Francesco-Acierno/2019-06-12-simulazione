import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.idMap = {}

    def buildGraph(self, soglia):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllNodes(soglia))
        for n in self.grafo.nodes:
            self.idMap[n.food_code] = n

        archi = DAO.getAllConnessioni()
        for n1, n2, peso in archi:
            if n1 in self.idMap.keys() and n2 in self.idMap.keys():
                nodo1 = self.idMap[n1]
                nodo2 = self.idMap[n2]
                if self.grafo.has_edge(nodo1, nodo2) is False:
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)

        return self.grafo

    def getMax(self, cibo):
        listaVicini = {}
        massimo = 0
        for vicini in self.grafo.neighbors(cibo):
            listaVicini[vicini] = self.grafo[cibo][vicini]["weight"]
        listaViciniordinata = sorted(listaVicini.items(), key=lambda x: x[1], reverse=True)
        listatop5 = []
        for i in range(0, 5):
            listatop5.append(listaViciniordinata[i])
        print(listatop5)
        return listatop5



