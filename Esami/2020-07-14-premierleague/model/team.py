from dataclasses import dataclass


@dataclass
class Team:
    TeamID: int
    Name: str

    def __hash__(self):
        return hash(self.TeamID)
