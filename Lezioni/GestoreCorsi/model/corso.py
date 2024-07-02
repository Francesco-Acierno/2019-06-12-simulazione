from dataclasses import dataclass

@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int

    #relazione
    studenti: set = None


    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)

    def __str__(self):
        return f"{self.nome} ({self.codins})"

    def get_studenti(self):
        return self.studenti