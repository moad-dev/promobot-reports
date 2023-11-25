from main.repositories.router_repository import RouterRepository
from main.repositories.processed_message_repository import ProcessedMessageRepository
from main.domain.message import Message
from main.domain.processed_message import ProcessedMessage
from main.domain.rule import Rule
from main.domain.address_query import AddressQuery
from main.schemas import (
    RuleCreation,
    RuleGet, 
    AddressSchema,
    MessagePost
)
from main.ner.extract_address import extract_address_query

import uuid



class RouterService:
    def __init__(
        self, 
        router_repository: RouterRepository,
        processed_message_repository: ProcessedMessageRepository,
    ):
        self.router_repository = router_repository
        self.processed_message_repository = processed_message_repository

    async def route(self, message_post: MessagePost) -> str:
        router = await self.router_repository.get()

        processed_message: ProcessedMessage = router.route(Message(message_post.text))

        await self.processed_message_repository.save(processed_message)

        return processed_message.uuid


    async def add_rule(self, rule: RuleCreation):
        router = await self.router_repository.get()

        if rule.address:
            address_query = extract_address_query(rule.address)
            address_query = AddressQuery(
                region=address_query.get('region'),
                area=address_query.get('area'),
                settlement=address_query.get('settlement'),
                street=address_query.get('street'),
                building=address_query.get('building')
            )
        else:
            address_query = None

        router.rules.append(
            Rule(
                uuid=uuid.uuid4().hex,
                group=rule.group,
                topic=rule.topic,
                address_query=address_query,
                agency=rule.agency
            )
        )

        await self.router_repository.save(router)
   
    
    async def delete_rule(self, rule_uuid: str):
        router = await self.router_repository.get()

        for rule in router.rules:
            if rule.uuid == rule_uuid:
                router.rules.remove(rule)
                break

        await self.router_repository.save(router)
    

    async def get_rules(self) -> list[RuleGet]:
        router = await self.router_repository.get()


        return [
            RuleGet(
                uuid=rule.uuid,
                group=rule.group,
                topic=rule.topic,
                is_trash=rule.is_trash,
                address=AddressSchema(
                    region=rule.address_query.region,
                    area=rule.address_query.area,
                    settlement=rule.address_query.settlement,
                    street=rule.address_query.street,
                    building=rule.address_query.building
                ) if rule.address_query else None,
                agency=rule.agency
            )
            for rule in router.rules
        ]
