from dataclasses import dataclass

@dataclass
class Artista:
    artist_id: int
    name: str

    def __hash__(self):
        return hash(self.artist_id)
