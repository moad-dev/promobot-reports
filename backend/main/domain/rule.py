from main.domain.address_query import AddressQuery
from main.domain.processed_message import ProcessedMessage

class Rule:
    def __init__(self, uuid: str, group: str | None, topic: str | None, address_query: AddressQuery | None, agency: str | None):
        self.uuid = uuid
        self.group = group
        self.topic = topic
        self.address_query = address_query
        self.agency = agency


    def match(self, processed_message: ProcessedMessage) -> bool:
        if self.group and self.group != processed_message.group:
            return False

        if self.topic and self.topic != processed_message.topic:
            return False

        if self.address_query and self.address_query and not any(
            address.match(self.address_query)
            for address in processed_message.addresses
        ):
            return False

        return True 
