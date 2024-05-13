import copy
from time import time
from functools import lru_cache


class Model:
    def __init__(self):
        self._anagrammi = set()
        self._anagrammi_list = []

    def calcola_anagrammi(self, parola):
        self._anagrammi = set()
        self.ricorsione("", "".join(sorted(parola)))
        return self._anagrammi

    @lru_cache(maxsize=None)
    def ricorsione(self, parziale, lettere_rimanenti):
        # Caso terminale: non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self._anagrammi.add(parziale)
            return
        else:
            #Caso non terminale: dobbiamo provare ad aggiungere una
            #lettera per volta, ed andare avanti nella ricorsione
            for i in range(len(lettere_rimanenti)):
                parziale += lettere_rimanenti[i]
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                self.ricorsione(parziale, nuove_lettere_rimanenti)
                parziale = parziale[:-1]

    @lru_cache(maxsize=None)
    def calcola_anagrammi_list(self, parola):
        self._anagrammi_list = []
        self.ricorsione_list([], parola)
        return self._anagrammi_list

    def ricorsione_list(self, parziale, lettere_rimanenti):
        # Caso terminale: non ci sono lettere rimanenti
        if len(lettere_rimanenti) == 0:
            self._anagrammi_list.append(copy.deepcopy(parziale))
            return
        else:
            #Caso non terminale: dobbiamo provare ad aggiungere una
            #lettera per volta, ed andare avanti nella ricorsione
            for i in range(len(lettere_rimanenti)):
                parziale.append(lettere_rimanenti[i])
                nuove_lettere_rimanenti = lettere_rimanenti[:i] + lettere_rimanenti[i+1:]
                self.ricorsione_list(parziale, nuove_lettere_rimanenti)
                parziale.pop()

if __name__ == "__main__":

    model = Model()

    start_time = time()
    print(model.calcola_anagrammi_list(["c", "s", "a"]))
    end_time = time()
    print(end_time - start_time)

    # print(model.calcola_anagrammi_list("Dog"))
