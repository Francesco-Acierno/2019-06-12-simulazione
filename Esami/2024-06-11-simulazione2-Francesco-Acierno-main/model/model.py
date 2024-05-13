import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._bestPath = []
        self._bestObjFun = 0
        self._grafo = nx.DiGraph()
        self.nodi = set()
        for s in DAO.getNodes():
            self.nodi.add(s.Chromosome)
        self._grafo.add_nodes_from(self.nodi)
        self.minimo = None
        self.massimo = None
        self.contMax = 0
        self.contMin = 0

    def buildGraph(self):
        self.addEdges()

    def addEdges(self):
        self._grafo.clear_edges()
        self.minimo = None
        self.massimo = None
        archi = DAO.getArchi()
        for cromo1, cromo2, id1, id2, corr in archi:
            if cromo1 != cromo2:
                if self._grafo.has_edge(cromo1, cromo2) is False:
                    self._grafo.add_edge(cromo1, cromo2, weight=corr)
                    if self.minimo is None and self.massimo is None:
                        self.massimo = corr
                        self.minimo = corr
                    else:
                        if corr < self.minimo:
                            self.minimo = corr
                        elif corr > self.massimo:
                            self.massimo = corr

    def getMaxEMin(self):
        return self.minimo, self.massimo

    def count(self, soglia):
        self.contMax = 0
        self.contMin = 0
        for e in self._grafo.edges:
            peso = self._grafo[e[0]][e[1]]['weight']
            if peso < soglia:
                self.contMin += 1
            else:
                self.contMax += 1
        return self.contMin, self.contMax

    def getCaratteristiche(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getCamminoOttimo(self, soglia):
        self._bestPath = []
        self._bestObjFun = 0

        for v in self._grafo.nodes:
            parziale = []
            visited_edges = set()
            self._ricorsione(v, parziale, soglia, visited_edges)

        return self._bestPath, self._bestObjFun

    def _ricorsione(self, current_node, parziale, soglia, visited_edges):
        for neighbor in self._grafo.neighbors(current_node):
            edge = (current_node, neighbor)
            reverse_edge = (neighbor, current_node)

            if edge not in visited_edges and reverse_edge not in visited_edges:
                weight = self._grafo[current_node][neighbor]['weight']
                if weight > soglia:
                    parziale.append((current_node, neighbor, weight))
                    visited_edges.add(edge)
                    visited_edges.add(reverse_edge)

                    objFun = self.getObjFun(parziale)
                    if objFun > self._bestObjFun:
                        self._bestObjFun = objFun
                        self._bestPath = copy.deepcopy(parziale)

                    self._ricorsione(neighbor, parziale, soglia, visited_edges)

                    parziale.pop()
                    visited_edges.remove(edge)
                    visited_edges.remove(reverse_edge)

    def getObjFun(self, listOfArcs):
        total_weight = 0
        for arc in listOfArcs:
            node1, node2, weight = arc
            total_weight += weight
        return total_weight

