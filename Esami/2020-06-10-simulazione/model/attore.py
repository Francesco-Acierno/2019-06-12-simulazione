from dataclasses import dataclass


@dataclass
class Attore:
    id: int
    first_name: str
    last_name: str
    gender: str

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.id})"
