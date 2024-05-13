from dataclasses import dataclass


@dataclass
class Giocatore:
    PlayerID: int
    Name: str
    gol: int
    partite: int

    def __hash__(self):
        return hash(self.PlayerID)
