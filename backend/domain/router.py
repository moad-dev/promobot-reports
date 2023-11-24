from rule import Rule
from message import Message
from processed_message import ProcessedMessage


class Router:
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def route(self, message: Message) -> ProcessedMessage:
        processed = message.process()

        for rule in self.rules:
            if rule.match(processed):
                processed.mark_as_sended(rule.agency)

        return processed
