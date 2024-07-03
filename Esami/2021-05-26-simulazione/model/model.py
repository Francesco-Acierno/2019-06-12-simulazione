import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._bestWeight = 0
        self._solBest = []
        self._grafo = nx.DiGraph()
        self._idMap = {}
        self.migliore = None

    def getCitta(self):
        return DAO.getAllCitta()

    def buildGraph(self, citta, anno):
        self._grafo.clear()
        self._grafo.add_nodes_from(DAO.getAllNodes(citta, anno))

        for b in self._grafo.nodes():
            self._idMap[b.business_id] = b

        archi = DAO.getAllConnessioni(citta, anno)
        for n1, n2, peso in archi:
            if n1 in self._idMap.keys() and n2 in self._idMap.keys():
                nodo1 = self._idMap[n1]
                nodo2 = self._idMap[n2]
                if self._grafo.has_edge(nodo1, nodo2) is False:
                    if peso > 0:
                        self._grafo.add_edge(nodo1, nodo2, weight=peso)
                    elif peso < 0:
                        self._grafo.add_edge(nodo2, nodo1, weight=-peso)

    def getMigliore(self):
        migliori = {}
        pesoUscenti = 0
        pesoEntranti = 0
        peso = 0
        for n in self._grafo.nodes():
            peso = 0
            pesoEntranti = 0
            pesoUscenti = 0
            for v in self._grafo.out_edges(n):
                pesoUscenti += self._grafo[n][v[1]]['weight']
            for e in self._grafo.in_edges(n):
                pesoEntranti += self._grafo[e[0]][n]['weight']
            peso = pesoEntranti - pesoUscenti
            migliori[n] = peso
        miglioriOrdinati = sorted(migliori.items(), key=lambda x: x[1], reverse=False)
        self.migliore = miglioriOrdinati[0][0]
        return miglioriOrdinati[0]

    def getBestPath(self, nodoIniziale, miglioramento):
        self._soluzione = []
        self._costoMigliore = 0
        nodoFinale = self.migliore
        print(nodoIniziale)
        parziale = [nodoIniziale]
        self._ricorsione(parziale, miglioramento, nodoFinale)
        return self._soluzione, self._costoMigliore

    def _ricorsione(self, parziale, miglioramento, nodoFinale):
        if parziale[-1] == nodoFinale:
            if len(parziale) > self._costoMigliore:
                self._soluzione = copy.deepcopy(parziale)
                self._costoMigliore = len(parziale)

        for n in self._grafo.neighbors(parziale[-1]):
            if len(parziale) > 1:
                if self._grafo[parziale[-1]][n]["weight"] > miglioramento + self._grafo[parziale[-2]][parziale[-1]]["weight"] and n not in parziale:
                    parziale.append(n)
                    self._ricorsione(parziale, miglioramento, nodoFinale)
                    parziale.pop()
            else:
                if n not in parziale:
                    parziale.append(n)
                    self._ricorsione(parziale, miglioramento, nodoFinale)
                    parziale.pop()
