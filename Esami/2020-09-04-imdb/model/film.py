from dataclasses import dataclass


@dataclass
class Film:
    id: int
    name: str
    year: int
    rank: float

    def __hash__(self):
        return hash(self.id)
