from fuzzywuzzy import fuzz
from address_query import AddressQuery

class Address:
    def __init__(
        self, 
        region: str | None, 
        area: list[str], 
        settlement: list[str], 
        street: list[str], 
        building: list[str]
    ):
        self.region = region
        self.area = area
        self.settlement = settlement
        self.street = street
        self.building = building
    
    def match(self, query: AddressQuery) -> bool:
        if not query.region:
            return True
        
        if not self.region:
            return False

        if fuzz.token_sort_ratio(query.region, self.region) < 80:
            return False

        if not query.area:
            return True

        if not self.area:
            return False

        if not any(fuzz.token_sort_ratio(query.area, area) > 80 for area in self.area):
            return False

        if not query.settlement:
            return True

        if not self.settlement:
            return False

        if not any(fuzz.token_sort_ratio(query.settlement, settlement) > 80 for settlement in self.settlement):
            return False

        if not query.street:
            return True

        if not self.street:
            return False

        if not any(fuzz.token_sort_ratio(query.street, street) > 80 for street in self.street):
            return False

        if not query.building:
            return True

        if not self.building:
            return False

        if not any(fuzz.token_sort_ratio(query.building, building) > 80 for building in self.building):
            return False

        return True
