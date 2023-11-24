from address_query import AddressQuery
from processed_message import ProcessedMessage

class Rule:
    def __init__(self, group: str, topic: str, address_query: AddressQuery, phone: str, agency: str):
        self.group = group
        self.topic = topic
        self.address_query = address_query
        self.agency = agency


    def match(self, processed_message: ProcessedMessage) -> bool:
        if self.group != processed_message.group:
            return False

        if self.topic != processed_message.topic:
            return False

        if self.address_query and not any(
            address.match(self.address_query)
            for address in processed_message.addresses
        ):
            return False

        return True 
