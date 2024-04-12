from dataclasses import dataclass

from database import Review


@dataclass
class Business:
    business_id: str
    full_address: str
    active: str
    categories: str
    city: str
    review_count: int
    business_name: str
    neighborhoods: str
    latitude: float
    longitude: float
    state: str
    stars: float

    reviews_id: list[str]
    reviews: list[Review] = None

    def __eq__(self, other):
        return self.business_id == other.business_id

    def __hash__(self):
        return hash(self.business_id)

    def get_reviews(self):
        if self.reviews is None:
            # vado a leggerele dal DAOe popolo la lista
            dao. get_review(self.reviews_id)
            pass
        else:
            return self.reviews
