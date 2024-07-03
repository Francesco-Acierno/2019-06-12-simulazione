import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._costoMigliore = None
        self._soluzione = None
        self.grafo = nx.DiGraph()
        self.idMap = {}

    def getAnni(self):
        return DAO.getAllAnni()

    def buildGraph(self, anno):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllStati(anno))

        for s in self.grafo.nodes:
            self.idMap[s.id] = s

        archi = DAO.getAllConnessioni(anno)
        for n1, n2, peso in archi:
            if n1.upper() in self.idMap.keys() and n2.upper() in self.idMap.keys():
                nodo1 = self.idMap[n1.upper()]
                nodo2 = self.idMap[n2.upper()]
                if peso > 0:
                    if self.grafo.has_edge(nodo1, nodo2) is False:
                        self.grafo.add_edge(nodo1, nodo2)
                elif peso < 0:
                    if self.grafo.has_edge(nodo2, nodo1) is False:
                        self.grafo.add_edge(nodo2, nodo1)

    def getPrecedenti(self, stato):
        return self.grafo.predecessors(stato)

    def getSuccessivi(self, stato):
        return self.grafo.out_edges(stato)

    def getRaggiungibili(self, stato):
        all=[]
        for nodi in nx.dfs_tree(self.grafo, stato):
            all.append(nodi)
        return all

    def getBestPath(self, nodoIniziale):
        self._soluzione = []
        self._costoMigliore = 0
        parziale = [nodoIniziale]
        self._ricorsione(parziale)
        return self._costoMigliore, self._soluzione

    def _ricorsione(self, parziale):
        if len(parziale) > self._costoMigliore:
            self._soluzione = copy.deepcopy(parziale)
            self._costoMigliore = len(parziale)

        for n in self.grafo.successors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                self._ricorsione(parziale)
                parziale.pop()
