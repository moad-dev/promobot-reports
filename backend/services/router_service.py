from ..repositories.router_repository import RouterRepository
from ..repositories.processed_message_repository import ProcessedMessageRepository
from ..domain.message import Message
from ..domain.processed_message import ProcessedMessage
from ..domain.rule import Rule
from ..domain.address_query import AddressQuery

from ..ner.extract_address import extract_address_query

class RouterService:
    def __init__(
        self, 
        router_repository: RouterRepository,
        processed_message_repository: ProcessedMessageRepository,
    ):
        self.router_repository = router_repository
        self.processed_message_repository = processed_message_repository

    async def route(self, message: Message):
        router = await self.router_repository.get()

        processed_message: ProcessedMessage = router.route(message)

        await self.processed_message_repository.save(processed_message)


    async def add_rule(self, rule: dict):
        router = await self.router_repository.get()

        address_query = extract_address_query(rule['address_query'])

        router.rules.append(
            Rule(
                uuid=rule['uuid'],
                group=rule['group'],
                topic=rule['topic'],
                address_query=AddressQuery(
                    region=address_query['region'],
                    area=address_query['area'],
                    settlement=address_query['settlement'],
                    street=address_query['street'],
                    building=address_query['building']
                ),
                agency=rule['agency']
            )
        )

        await self.router_repository.save(router)
    
