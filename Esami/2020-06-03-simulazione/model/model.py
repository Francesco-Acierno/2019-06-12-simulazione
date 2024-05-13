import copy

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._costoMigliore = 0
        self._soluzione = []
        self.grafo = nx.DiGraph()
        self.idMap = {}

    def buildGraph(self, media):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllNodes(media))

        for g in self.grafo.nodes():
            self.idMap[g.PlayerID] = g

        archi = DAO.getAllConnessioni()
        for n1, n2, peso in archi:
            if n1 in self.idMap.keys() and n2 in self.idMap.keys():
                nodo1 = self.idMap[n1]
                nodo2 = self.idMap[n2]
                if self.grafo.has_edge(nodo1, nodo2) is False:
                    if peso > 0:
                        self.grafo.add_edge(nodo1, nodo2, weight=peso)
                    elif peso < 0:
                        self.grafo.add_edge(nodo2, nodo1, weight=-peso)

    def getTopPlayer(self):
        dizio = {}
        lista = []
        for nodo in self.grafo.nodes:
            dizio[nodo.PlayerID] = self.grafo.out_degree(nodo)
        dizioOrdinato = list(sorted(dizio.items(), key=lambda item: item[1], reverse=True))
        giocatoreId = dizioOrdinato[0][0]
        giocatore = self.idMap[giocatoreId]
        for archi in self.grafo.out_edges(giocatore):
            lista.append((archi[1], self.grafo[archi[0]][archi[1]]["weight"]))
        return giocatore, sorted(lista, key=lambda x: x[1], reverse=True)

    def getBestPath(self, numeroGiocatori):
        self._soluzione = []
        self._costoMigliore = 0
        battuti = []
        for nodo in self.grafo.nodes:
            parziale = [nodo]
            for arcoUscente in self.grafo.out_edges(nodo):
                battuti.append(arcoUscente[1])
            self._ricorsione(parziale, numeroGiocatori, battuti)
        return self._costoMigliore, self._soluzione

    def _ricorsione(self, parziale, numeroGiocatori, battuti):
        if len(parziale)+1 == numeroGiocatori+1:
            if self.grado(parziale) > self._costoMigliore:
                self._soluzione = copy.deepcopy(parziale)
                self._costoMigliore = self.grado(parziale)

        if len(parziale) < numeroGiocatori:
            for n in self.grafo.nodes:
                if n not in parziale and n not in battuti:
                    parziale.append(n)
                    for arcoUscente in self.grafo.out_edges(n):
                        battuti.append(arcoUscente[1])
                    self._ricorsione(parziale, numeroGiocatori, battuti)
                    parziale.pop()
                    for arcoUscente in self.grafo.out_edges(n):
                        battuti.remove(arcoUscente[1])

    def grado(self, listaNodi):
        gradoTot = 0
        for nodo in listaNodi:
            pesoUscente = 0
            pesoEntrante = 0
            for arcoUscente in self.grafo.out_edges(nodo):
                pesoUscente += self.grafo[arcoUscente[0]][arcoUscente[1]]["weight"]
            for arcoEntrante in self.grafo.in_edges(nodo):
                pesoEntrante += self.grafo[arcoEntrante[0]][arcoEntrante[1]]["weight"]
            gradoTot += pesoUscente - pesoEntrante
        return gradoTot
