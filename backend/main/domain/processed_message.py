from main.domain.address import Address

class ProcessedMessage:
    def __init__(
            self,
            uuid: str,
            text: str,
            group: str | None,
            topic: str | None,
            is_trash: bool | None,
            addresses: list[Address],
            agencies: list[str] = []
        ):
        self.uuid = uuid
        self.text = text
        self.group = group
        self.topic = topic
        self.is_trash = is_trash
        self.addresses = addresses
        self.agencies = agencies


    def mark_as_sended(self, agency: str):
        self.agencies.append(agency)
