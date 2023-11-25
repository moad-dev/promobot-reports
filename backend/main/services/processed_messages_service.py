from main.repositories.processed_message_repository import ProcessedMessageRepository
from main.schemas import ProcessedMessageGet,  FuzzyAddressSchema

class ProcessedMessagesService:
    def __init__(
        self,
        processed_message_repository: ProcessedMessageRepository,

    ):
        self.processed_message_repository = processed_message_repository
    
    async def get_processed_message(self, uuid: str) -> ProcessedMessageGet:
        model = await self.processed_message_repository.get_by_id(uuid)
        addresses = []
        for address in model.addresses:
            addresses.append(
                FuzzyAddressSchema(
                    region=address.region,
                    area=address.area,
                    settlement=address.settlement,
                    street=address.street,
                    building=address.building
                )
            )

        return ProcessedMessageGet(
            uuid=model.uuid,
            text=model.text,
            group=model.group,
            topic=model.topic,
            is_trash=model.is_trash,
            address=addresses,
            agency=model.agencies
        )


            

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
                    is_trash=item.is_trash,
                    address=addresses,
                    agency=item.agencies
                )
            )

        return results
