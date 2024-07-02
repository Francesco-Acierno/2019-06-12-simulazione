from dataclasses import dataclass


@dataclass
class Paese:
    id: str
    Name: str
    Capital: str
    Lat: float
    Lng: float
    Area: int
    Population: int
    Neighbors: str

    def __hash__(self):
        return hash(id)
