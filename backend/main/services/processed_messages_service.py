from main.repositories.processed_message_repository import ProcessedMessageRepository
from main.domain.processed_message import ProcessedMessage

class ProcessedMessagesService:
    def __init__(
        self,
        processed_message_repository: ProcessedMessageRepository,

    ):
        self.processed_message_repository = processed_message_repository

    async def get_processed_messages(self) -> list[ProcessedMessage]:
        return await self.processed_message_repository.get()