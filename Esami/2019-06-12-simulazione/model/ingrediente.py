from dataclasses import dataclass


@dataclass
class Ingrediente:
    condiment_code: int
    display_name: str
    condiment_portion_size: str
    condiment_portion_code: int
    condiment_grains: float
    condiment_whole_grains: float
    condiment_vegetables: float
    condiment_dkgreen: float
    condiment_orange: float
    condiment_starchy_vegetables: float
    condiment_other_vegetables: float
    condiment_fruits: float
    condiment_milk: float
    condiment_meat: float
    condiment_soy: float
    condiment_drybeans_peas: float
    condiment_oils: float
    condiment_solid_fats: float
    condiment_added_sugars: float
    condiment_alcohol: float
    condiment_calories: float
    condiment_saturated_fats: float

    def __hash__(self):
        return hash(self.condiment_code)

    def __str__(self):
        return f'{self.display_name}'
