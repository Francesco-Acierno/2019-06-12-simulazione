import networkx as nx

from Lezioni.ArtsMia.database.DAO import DAO


class Model:
    def __init__(self):
        self._artObjectList = DAO.getAllObjects()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap = {}
        for v in self._artObjectList:
            self._idMap[v.object_id] = v

    def getConnessa(self, v0int):
        v0 = self._idMap[v0int]

        # Modo 1: successori di v0 in DFS
        successors = nx.dfs_successors(self._grafo, v0)
        allSucc = []
        for v in successors.values():
            allSucc.extend(v)

        print(f"Metodo 1 (pred): {len(allSucc)}")

        # Modo 2: predecessori di vo in DFS
        predecessors = nx.dfs_predecessors(self._grafo, v0)
        print(f"Metodo 2 (succ): {len(predecessors.values())}")

        # Modo 3: conto i nodi dell'albero di visita
        tree = nx.dfs_tree(self._grafo, v0)
        print(f"Metodo 3 (tree): {len(tree.nodes)}")

        # Modo 4: node_connected_components
        connComp = nx.node_connected_component(self._grafo, v0)
        print(f"Metodo 4 (connected comp): {len(connComp)}")

        return len(connComp)

    def creaGrafo(self):
        self.addEdges()

    def addEdges(self):
        self._grafo.clear_edges()

        # Soluzione 1: Ciclare sui nodi (se i grafi sono piccoli conviene)
        # for u in self._artObjectList:
        #    for v in self._artObjectList:
        #        peso = DAO.getPeso(u,v)
        #        self._grafo.add_edges(u, v, weight=peso)

        # Soluzione 2: una sola query
        allEdges = DAO.getAllConnessioni(self._idMap)
        for e in allEdges:
            self._grafo.add_edge(e.v1, e.v2, weight=e.peso)

    def checkExistence(self, idOggetto):
        return idOggetto in self._idMap

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)
