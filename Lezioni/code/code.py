import queue


class Coda_prioritaria:
    def __init__(self):
        self._lista = []

    def put(self, valore):
        self._lista.append(valore)

    def pop(self):
        """
        Restituisce il valore minimo presente nella lista, e lo cancella dalla lista stessa
        :return:
        """
        "[2, 5, 1, 9]"
        "enumarete restituisce [(0, 2), (1,5), (2,1), (3,9)]"
        "[2, 5, 1, 9] è la lista su cui calcolo il minimo"
        pos_min, val_min = min(enumerate(self._lista), key=lambda x: x[1])
        self._lista.pop(pos_min)
        return val_min


c = queue.PriorityQueue()

c.put((2, "Paolo"))
c.put((1, "Giulia"))
c.put((2, "Antonio"))
print(c.get())
c.put((1, "Anna"))
print(c.get())
print(c.get())
print(c.get())
