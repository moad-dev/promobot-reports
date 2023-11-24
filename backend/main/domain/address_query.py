class AddressQuery:
    def __init__(
        self,
        region: str | None,
        area: str | None,
        settlement: str | None,
        street: str | None,
        building: str | None
    ):
        self.region = region
        self.area = area
        self.settlement = settlement
        self.street = street
        self.building = building

