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
    
    def match(self, address: AddressQuery) -> bool:
        if all([self.region, address.region]) and fuzz.token_sort_ratio(self.region, address.region) < 80:
            return False

        if (
            all([self.area, address.area]) and max(
                fuzz.token_sort_ratio(area, address.area)
                for area in self.area
            ) < 80
        ):
            return False

        if (
            all([self.settlement, address.settlement]) and max(
                fuzz.token_sort_ratio(settlement, address.settlement)
                for settlement in self.settlement
            ) < 80
        ):
            return False

        if (
            all([self.street, address.street]) and max(
                fuzz.token_sort_ratio(street, address.street)
                for street in self.street
            ) < 80
        ):
            return False

        if (
            all([self.building, address.building]) and max(
                fuzz.token_sort_ratio(building, address.building)
                for building in self.building
            ) < 80
        ):
            return False

        return True

