import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self.cromosomi = DAO.getAllCromosomi()
        self.grafo = nx.DiGraph()
        self.idMap = {}
        for c in self.cromosomi:
            self.idMap[c] = c

    def buildGraph(self):
        self.grafo.clear()
        self.grafo.add_nodes_from(self.cromosomi)
        self.minimo = None
        self.massimo = None
        archi = DAO.getArchi()
        for cromo1, cromo2, id1, id2, corr in archi:
            if cromo1 != cromo2:
                if self.grafo.has_edge(cromo1, cromo2) is False:
                    self.grafo.add_edge(cromo1, cromo2, weight=corr)
                    if self.minimo is None and self.massimo is None:
                        self.massimo = corr
                        self.minimo = corr
                    else:
                        if corr < self.minimo:
                            self.minimo = corr
                        elif corr > self.massimo:
                            self.massimo = corr

    def contaArchi(self, soglia):
        self.contMax = 0
        self.contMin = 0
        for e in self.grafo.edges:
            peso = self.grafo[e[0]][e[1]]['weight']
            if peso < soglia:
                self.contMin += 1
            else:
                self.contMax += 1
        return self.contMin, self.contMax

    def getCamminoOttimo(self, soglia):
        self._bestPath = []
        self._bestObjFun = 0

        for v in self.grafo.nodes:
            parziale = []
            visited_edges = set()
            self._ricorsione(v, parziale, soglia, visited_edges)

        return self._bestPath, self._bestObjFun

    def _ricorsione(self, current_node, parziale, soglia, visited_edges):
        for neighbor in self.grafo.neighbors(current_node):
            edge = (current_node, neighbor)
            reverse_edge = (neighbor, current_node)

            if edge not in visited_edges and reverse_edge not in visited_edges:
                weight = self.grafo[current_node][neighbor]['weight']
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
