# from dataclasses import dataclass

import dataclasses
import operator


@dataclasses.dataclass(order=True)  # @dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str

    def str_punteggio(self):
        """
        Costruisce la stringa che rappresenta in forma leggibile il punteggio tenendo conto della possibilità di lode
        :return: "30 e lode" oppure il punteggio (senza lode), sotto forma di stringa
        """
        if self.punteggio == 30 and self.lode:
            return "30 e lode"
        else:
            return f"{self.punteggio}"
            # return self.punteggio NO

    def copy(self):
        return Voto(self.esame, self.cfu, self.punteggio, self.lode, self.data)

    def __str__(self):
        return f'{self.esame} ({self.cfu} CFU): voto {self.punteggio} il {self.data}'


def estrai_campo_esame(self):
    return v.esame


class Libretto:
    def __init__(self):
        self._voti = []

    def append(self, voto):
        if self.has_voto(voto) is False and self.has_conflitto(voto) is False:
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

    def copy(self):
        nuovo = Libretto()
        # nuovo._voti = self._voti.copy()
        # nuovo._voti self._voti[:] uguale a quella di sopra
        for v in self._voti:
            nuovo._voti.append(v.copy())
        return nuovo

    def crea_migliorato(self):
        """
        Crea una copia del libretto e "migliora" i voti in esso presenti.
        :return:
        """
        nuovo = self.copy()
        # nuovo._voti[0] = self._voti[0]

        for v in nuovo._voti:
            if 18 <= v.punteggio <= 23:
                v.punteggio += 1
            elif 24 <= v.punteggio <= 28:
                v.punteggio += 2
            elif v.punteggio == 29:
                v.punteggio = 30

        return nuovo

    def crea_ordinato_per_esame(self):
        nuovo = self.copy()
        # ordina i nuovo._voti
        nuovo.ordina_per_esame()
        return nuovo

    def ordina_per_esame(self):
        # ordina self._voti per nome esame
        # self._voti.sort(key=estrai_campo_esame)
        self._voti.sort(key=operator.attrgetter('esame'))
        # self._voti.sort(key=lambda v: v.esame)
        # self._voti.sort()

    def crea_ordinato_per_punteggio(self):
        nuovo = self.copy()
        self._voti.sort(key=lambda v: (v.punteggio, v.lode), reverse=True)
        return nuovo

    def stampa(self):
        print(f"Hai {len(self._voti)} voti")
        for v in self._voti:
            print(v)
        print(f"La media vale {self.media():.2f}")

    def stampaGUI(self):
        outList = []
        outList.append(f"Hai {len(self._voti)} voti")
        for v in self._voti:
            outList.append(v)
        outList.append(f"La media vale {self.media():.2f}")
        return outList

    def cancella_inferiori(self, punteggio):
        #     for v in self._voti:
        #        if v.punteggio < punteggio:
        #            self._voti.remove(v)
        #
        #     for i in range(len(self._voti)):
        #        if self._voti[i] < punteggio:
        #           self._voti.pop(i)
        # [18, 30, 30, 30 ]
        """
        voti_nuovi = []
        for v in self._voti:
            if v.punteggio >= punteggio:
                voti_nuovi.append(v)
        self._voti = voti_nuovi
        """

        self._voti = [v for v in self._voti if v.punteggio >= punteggio]

    """
    Opzione 1: 
    metodo stampa_per_nome e metodo stampa_per_punteggio, che semplicemente stampano e non modificano nulla
    
    Opzione 2:
    metodo crea_libretto_ordinato_per_nome, ed un metodo crea_libretto_ordinato_per_punteggio, che creano delle copie 
    separate, sulle quali potrò chiamare il metodo stampa()
    
    Opzione 3:
    metodo ordina_per_nome, che modifica il libretto stesso riordinando i Voti, e ordina_per_punteggio, poi userò 
    stampa() 
    + aggiungiamo gratis un metodo copy()
    
    Opzione 2bis:
    crea una copia shallow del libretto
    """


def _test_voto():
    print(__name__)
    v1 = Voto("nome esame", 8, 28, False, '2024-03-11')
    l1 = Libretto()
    l1.append(v1)
    print(l1.media())


if __name__ == "__main__":
    _test_voto()
