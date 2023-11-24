from main.repositories.processed_message_repository import ProcessedMessageRepository
from main.domain.processed_message import ProcessedMessage, FuzzyAddressSchema
from main.schemas import ProcessedMessageGet

class ProcessedMessagesService:
    def __init__(
        self,
        processed_message_repository: ProcessedMessageRepository,

    ):
        self.processed_message_repository = processed_message_repository

    async def get_processed_messages(self) -> list[ProcessedMessageGet]:
        models = await self.processed_message_repository.get()
        
        results = [] 
        for item in models:
            addresses = []
            for address in item.addresses:
                addresses.append(
                    FuzzyAddressSchema(
                        region=address.region,
                        area=address.area,
                        settlement=address.settlement,
                        street=address.street,
                        building=address.building
                    )
                )

             
                results.append(
                    ProcessedMessageGet(
                        uuid=item.uuid,
                        text=item.text,
                        group=item.group,
                        topic=item.topic,
                        address=addresses,
                        agency=item.agencies
                    )
                )

        return results
