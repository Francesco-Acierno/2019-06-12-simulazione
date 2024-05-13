from dataclasses import dataclass


@dataclass
class Connessione:
    n1: str
    n2: str
    lat1: float
    long1: float
    lat2: float
    long2: float
