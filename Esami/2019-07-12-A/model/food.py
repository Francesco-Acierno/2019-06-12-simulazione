from dataclasses import dataclass


@dataclass
class Food:
    food_code: int
    display_name: str

    def __hash__(self):
        return hash(self.food_code)
