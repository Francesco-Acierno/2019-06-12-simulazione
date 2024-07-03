import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._mappaRicavi = {}
        self._idMap = {}

    def getMetodi(self):
        return DAO.getAllMetodi()

    def buildGraph(self, anno, metodo, s):
        self._grafo.clear()
        self.nodi = DAO.getAllNodi(anno, metodo)
        self._grafo.add_nodes_from(self.nodi)
        self.addEdges(s)
        for v in self.nodi:
            self._idMap[v.Product_number] = v

    def addEdges(self, s):
        self._grafo.clear_edges()
        for nodo1 in self._grafo:
            for nodo2 in self._grafo:
                if nodo1 != nodo2 and self._grafo.has_edge(nodo1, nodo2) is False:
                    prezzoMinimo = float(nodo1.ricavo) + float(nodo1.ricavo) * s
                    if nodo2.ricavo > prezzoMinimo:
                        self._grafo.add_edge(nodo1, nodo2)

    def getAnalisi(self):
        dizio = {}
        lista = []
        for nodo in self._grafo:
            dizio[nodo.Product_number] = self._grafo.in_degree(nodo)
        dizioOrdinato = list(sorted(dizio.items(), key=lambda item: item[1], reverse=True))
        contatore = 0
        for (nodoId, grado) in dizioOrdinato:
            if contatore < 5:
                nodo = self._idMap[nodoId]
                lista.append((nodoId, grado, nodo.ricavo))
                contatore += 1
        return lista

    def getBestPath(self):
        self._soluzione = []
        self._costoMigliore = 0
        for n in self._grafo.nodes:
            if self._grafo.in_degree(n) == 0:
                parziale = [n]
        self._ricorsione(parziale)
        return self._soluzione, self._costoMigliore

    def _ricorsione(self, parziale):

        if self._grafo.out_degree(parziale[-1]) == 0:
            if len(parziale) > self._costoMigliore:
                self._soluzione = copy.deepcopy(parziale)
                self._costoMigliore = len(parziale)

        for n in self._grafo.neighbors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                self._ricorsione(parziale)
                parziale.pop()



