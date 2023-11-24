from typing import Annotated
from fastapi import Depends

import aiosqlite

from main.services.processed_messages_service import ProcessedMessagesService
from main.services.router_service import RouterService
from main.repositories.processed_message_repository import ProcessedMessageRepository
from main.repositories.router_repository import RouterRepository
from main.repositories.unit_of_work import UnitOfWork


async def get_db():
    db = await aiosqlite.connect("dbstorage/database.sqlite")
    try:
        yield db
    finally:
        await db.close()

async def get_unit_of_work(
    db: Annotated[aiosqlite.Connection, Depends(get_db)]
) -> UnitOfWork:
    return UnitOfWork(db)

async def get_processed_messages_repository(
    db: Annotated[aiosqlite.Connection, Depends(get_db)]
) -> ProcessedMessageRepository:
    return ProcessedMessageRepository(db)


async def get_router_repository(
    db: Annotated[aiosqlite.Connection, Depends(get_db)]
) -> RouterRepository:
    return RouterRepository(db)


async def get_processed_messages_service(
    processed_message_repository: Annotated[
        ProcessedMessageRepository, 
        Depends(get_processed_messages_repository)
    ]
) -> ProcessedMessagesService:
    return ProcessedMessagesService(processed_message_repository)


async def get_router_service(
    router_repository: Annotated[
        RouterRepository,
        Depends(get_router_repository)
    ],
    processed_messages_repository: Annotated[
        ProcessedMessageRepository,
        Depends(get_processed_messages_repository)
    ]
    ) -> RouterService:
    return RouterService(router_repository, processed_messages_repository)
