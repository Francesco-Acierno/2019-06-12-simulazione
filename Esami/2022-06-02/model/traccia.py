from dataclasses import dataclass


@dataclass
class Traccia:
    TrackId: int
    Name: str
    AlbumId: int
    MediaTypeId: int
    GenreId: int
    Composer: str
    Milliseconds: int
    Bytes: int
    UnitPrice: float

    def __hash__(self):
        return hash(self.TrackId)
