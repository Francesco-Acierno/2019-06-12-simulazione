import copy
from time import time

class Model:
    def __init__(self):
        self.N_soluzioni = 0
        self.N_iterazioni = 0
        self.soluzioni = []


    def risolvi_n_regine(self, N):
        self.N_soluzioni = 0
        self.N_iterazioni = 0
        self.soluzioni = []
        self._ricorsione([], N)


    def _ricorsione(self, parziale, N):
        self.N_iterazioni += 1
        # condizione terminale
        if len(parziale) == N:
            # print(parziale)
            if self._is_soluzione_nuova(parziale):
                self.N_soluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
        #caso ricorsivo
        else:
            for row in range(N):
                for col in range(N):
                    parziale.append((row,col))
                    if self._regina_ammissibile(parziale):
                        self._ricorsione(parziale, N)
                    parziale.pop()

    def _regina_ammissibile(self, parziale):
        if len(parziale) == 1:
            return True

        ultima_regina = parziale[-1]
        for regina in parziale[:len(parziale)-1]:
            # controllare righe
                if ultima_regina[0] == regina[0]:
                    return False
            # controllare colonne
                if ultima_regina[1] == regina[1]:
                    return False
            # controllare diagonali
                # check row-col
                if (ultima_regina[0] - ultima_regina[1]) == (regina[0] - regina[1]):
                    return False
                # check row+col
                if (ultima_regina[0] + ultima_regina[1]) == (regina[0] + regina[1]):
                    return False
        return True

    def _is_soluzione_nuova(self, parziale):
        # Versione vecchia
        # for s in self.soluzioni:
        #     answer = False
        #     for regina in parziale:
        #         # se almeno una regina di parziale non si trova nella soluzione precedente
        #         # la soluzione è nuova
        #         if regina not in s:
        #             answer = True
        #     if not answer:
        #         return answer
        # return True

        def _is_soluzione_nuova(self, parziale):
            # per ogni soluzione
            for s in self.soluzioni:
                regine_nuove_in_s = [n in s for n in parziale] # <- vettore di booleani fatto come [regina1 in parziale, regina2 in parziale, ...]
                if all(regine_nuove_in_s): # se  tutte le regine sono in parziale, allora ritorna False (non è una soluzione nuova)
                    return False
            return True


if __name__ == '__main__':
    model = Model()
    start_time = time()
    model.risolvi_n_regine(5)
    end_time = time()
    print(f"L'algoritmo ha trovato {model.N_soluzioni} soluzioni")
    print(f"L'algoritmo ha a chiamato la funzione ricorsiva {model.N_iterazioni} volte")
    print(f"L'algoritmo ha impiegato {end_time - start_time} secondi")
    print("Le soluzione sono:")
    print(model.soluzioni)