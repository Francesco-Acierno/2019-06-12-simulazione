from dataclasses import dataclass

@dataclass
class Match:
    MatchID: int
    TeamHomeID: int
    TeamAwayID: int
    TeamHomeFormation: int
    TeamAwayFormation: int
    ResultOfTeamHome: int
    Date: int

    def __hash__(self):
        return hash(self.MatchID)
