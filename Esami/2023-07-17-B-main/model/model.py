import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._solBest = []
        self.grafo = nx.Graph()
        self._idMap = {}
        self.dict = {}
        self.ndictOrder = []

    def getBrand(self):
        return DAO.getAllBrand()

    def buildGraph(self, brand, anno):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getAllNodi(brand))

        for p in self.grafo.nodes:
            self._idMap[p.Product_number] = p

        archi = DAO.getAllConnessioni(anno)
        for n1, n2, peso in archi:
            if n1 in self._idMap.keys() and n2 in self._idMap.keys():
                nodo1 = self._idMap[n1]
                nodo2 = self._idMap[n2]
                if self.grafo.has_edge(nodo1, nodo2) is False:
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)

    def getGradoMax(self):
        for arco in self.grafo.edges:
            self.dict[arco] = self.grafo[arco[0]][arco[1]]["weight"]
        dictOrder = list(sorted(self.dict.items(), key=lambda item: item[1], reverse=True))
        self.ndictOrder = []
        for i in range(0, 3):
            self.ndictOrder.append(dictOrder[i])
        return self.ndictOrder

    def ripetuti(self):
        dictr = {}
        for n in self.ndictOrder:
            if n[0][0] not in dictr.keys():
                dictr[n[0][0]] = 1
            else:
                dictr[n[0][0]] += 1
            if n[0][1] not in dictr.keys():
                dictr[n[0][1]] = 1
            else:
                dictr[n[0][1]] += 1

        dictOrder = []
        for n in dictr:
            if dictr[n] >= 2:
                dictOrder.append(n)
        return dictOrder

    def searchPath(self, prodotto):
        nodoSource = self._idMap[int(prodotto)]

        parziale = []

        self.ricorsione(parziale, nodoSource, 0)
        return self._solBest

    def ricorsione(self, parziale, nodoLast, livello):
        archiViciniAmmissibili = self.getArchiViciniAmm(nodoLast, parziale)

        if len(archiViciniAmmissibili) == 0:
            if len(parziale) > len(self._solBest):
                self._solBest = list(parziale)

        for a in archiViciniAmmissibili:
            parziale.append(a)
            self.ricorsione(parziale, a[1], livello + 1)
            parziale.pop()

    def getArchiViciniAmm(self, nodoLast, parziale):

        archiVicini = self.grafo.edges(nodoLast, data=True)
        result = []
        for a1 in archiVicini:
            if self.isAscendent(a1, parziale) and self.isNovel(a1, parziale):
                result.append(a1)
        return result

    def isAscendent(self, e, parziale):
        if len(parziale) == 0:
            return True
        return e[2]["weight"] >= parziale[-1][2]["weight"]

    def isNovel(self, e, parziale):
        if len(parziale) == 0:
            return True
        e_inv = (e[1], e[0], e[2])
        return (e_inv not in parziale) and (e not in parziale)




