from address import Address
from processed_message import ProcessedMessage

class Message:
    def __init__(self, text: str):
        self.text = text

    def process() -> ProcessedMessage:
        return ProcessedMessage()
