from dataclasses import dataclass

@dataclass
class Retailer:
    """
    Class representing a retailer from the table go_retailers
    """
    retailer_code: int
    retailer_name: str
    type: str
    country: str

    # Relations? Do we need them? I chose not, because I am not going to use them

    def __eq__(self, other):
        return self.retailer_code == other.retailer_code

    def __hash__(self):
        return hash(self.retailer_code)