"""
Scrivere un programma Python che permetta di gestire un modello universitario.
Il programma dovrà definire una classe Voto, che rappresenta un singolo esame superato,
ed una classe Libretto, che contiene l'elenco dei voti di uno studente.
"""
from dataclasses import dataclass

"""
class Voto:
    def __init__(self, esame, cfu, punteggio, lode, data):
        self.esame = esame
        self.cfu = cfu
        self.punteggio = punteggio
        self.lode = lode
        self.data = data

        if self.lode and self.punteggio!=30:
            raise ValueError("Lode non applicabile")

    def __str__(self):
        return f"Esame {self.esame} superato con {self.punteggio}"

    def __repr__(self):
        return f"Voto('{self.esame}', {self.cfu}, {self.punteggio}, {self.lode}, '{self.data}')"
"""

@dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str


class Libretto:
    def __init__(self):
        self._voti = []

    def append(self, voto):
        self._voti.append(voto)

    def media(self):
        if len(self._voti)==0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)






voto_1 = Voto("Analisi Matematica 1", 10, 28, False, '2022-02-10')
voto_2 = Voto("Basi di Dati", 8, 30, True, '2023-06-15')

print(voto_1, voto_2)
#
# miei_voti = [voto_1, voto_2]
# print(miei_voti)

mio_libretto = Libretto()
mio_libretto.append(voto_1)
mio_libretto.append(voto_2)
# mio_libretto._voti.append(voto_1)  NO

print(mio_libretto.media())

# print(mio_libretto._voti)  NO