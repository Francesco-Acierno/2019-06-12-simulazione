# from dataclasses import dataclass

import dataclasses

@dataclasses.dataclass # @dataclass
class Voto:
    esame: str
    cfu: int
    punteggio : int
    lode: bool
    data: str

    def str_punteggio(self):
        """
        Costruisce la stringa che rappresenta in forma leggibile il punteggio tenendo conto della possibilità di lode
        :return: "30 e lode" oppure il punteggio (senza lode), sottoforma di stringa
        """
        if self.punteggio == 30 and self.lode:
            return "30 e lode"
        else:
            return f"{self.punteggio}"
            # return self.punteggio NO



class Libretto:
    def __init__(self):
        self._voti = []

    def append(self, voto):
        if self.has_voto(voto) == False and self.has_conflitto(voto) == False:
            self._voti.append(voto)
        else:
            raise ValueError("Voto non valido")

    def media(self):
        if len(self._voti) == 0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi) / len(punteggi)

    def findByPunteggio(self, punteggio, lode):
        """
        Seleziona tutti e soli i voti che hanno un punteggio definito
        :param punteggio: numero intero che rappresenta il punteggio
        :param lode: booleano che indica la presenza della lode
        :return: lista di oggetti di tipo voto che hanno il punteggio specificato (può anche essere vuota)
        """
        corsi = []
        for v in self._voti:
            if v.punteggio == punteggio and v.lode == lode:
                corsi.append(v)
        return corsi

    def findByEsame(self, esame):
        """
        Cerca il voto a partire dal nome dell'esame
        :param esame: Nome dell'esame da cercare
        :return: l'oggetto Voto corrispondente al nome trovato, oppure None se non viene trovato
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        return None

    def findByEsame2(self, esame):
        """
        Cerca il voto a partire dal nome dell'esame
        :param esame: Nome dell'esame da cercare
        :return: l'oggetto Voto corrispondente al nome trovato, oppure un'eccezione ValueError se
        l'elemento non viene trovato
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        raise ValueError(f"Esame '{esame}' non presente nel libretto")

    def has_voto(self, voto):
        """
        Ricerca se nel libretto esiste già un esame con lo stesso nome e con lo stesso punteggio
        :param voto: oggetto Voto da confrontare
        :return: True se esiste, False se non esiste
        """
        for v in self._voti:
            if v.esame == voto.esame and v.punteggio == voto.punteggio and v.lode == voto.lode:
                return True
        return False


    def has_conflitto(self, voto):
        """
        Ricerca se nel libretto esiste già un esame con lo stesso nome ma con punteggio diverso
        :param voto: oggetto Voto da confrontare
        :return: True se esiste, False se non esiste
        """
        for v in self._voti:
            if v.esame == voto.esame and not (v.punteggio == voto.punteggio and v.lode == voto.lode):
            # Scrittura errata: if (v.esame == voto.esame and v.punteggio != voto.punteggio) or v.lode != voto.lode:
            # if v.esame == voto.esame and (v.punteggio != voto.punteggio or v.lode != voto.lode):
                return True
        return False



def _test_voto():
    print(__name__)
    v1 = Voto("nome esame", 8, 28, False, '2024-03-11')
    l1 = Libretto()
    l1.append(v1)
    print(l1.media())

if __name__ == "__main__":
        _test_voto()