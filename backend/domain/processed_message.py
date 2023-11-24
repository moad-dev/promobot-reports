from address import Address

class ProcessedMessage:
    def __init__(self, group: str, topic: str, addresses: list[Address]):
        self.group = group
        self.topic = topic
        self.addresses = addresses
        self.agency = None

    def mark_as_sended(self, agency: str):
        self.sended = agency  
