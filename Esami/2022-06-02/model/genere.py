from dataclasses import dataclass


@dataclass
class Genere:
    GenreId: int
    Name: str

    def __str__(self):
        return f"{self.GenreId}"
