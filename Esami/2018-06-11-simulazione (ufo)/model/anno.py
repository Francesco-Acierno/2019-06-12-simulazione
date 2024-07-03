from dataclasses import dataclass

@dataclass
class Anno:
    anno: int
    avvistamenti: int

    def __str__(self):
        return f"{self.anno} ({self.avvistamenti})"
