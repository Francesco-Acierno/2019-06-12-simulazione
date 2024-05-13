from dataclasses import dataclass

@dataclass
class Utente:
    user_id: str
    votes_funny: int
    votes_useful: int
    votes_cool: int
    name: str
    average_stars: float
    review_count: int

    def __hash__(self):
        return hash(self.user_id)

