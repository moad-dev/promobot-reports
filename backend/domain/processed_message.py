from address import Address

class ProcessedMessage:
    def __init__(
            self, uuid: str, text: str, group: str, topic: str, addresses: list[Address],
            agencies: list[str] = []
        ):
        self.uuid = uuid
        self.text = text
        self.group = group
        self.topic = topic
        self.addresses = addresses
        self.agencies = agencies

    def mark_as_sended(self, agency: str):
        self.agencies.append(agency)
