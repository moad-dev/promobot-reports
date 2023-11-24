from typing import Annotated
from fastapi import APIRouter, Depends
from main.services.processed_messages_service import ProcessedMessagesService
from main.services.router_service import RouterService
from main.repositories.processed_message_repository import ProcessedMessageRepository
from main.repositories.router_repository import RouterRepository

import aiosqlite

"""
async def get_db():
    db = await aiosqlite.connect("database/database.sqlite")
    try:
        yield db
    finally:
        await db.close()
"""


router = APIRouter()

async def get_db():
    db = await aiosqlite.connect("dbstorage/database.sqlite")
    try:
        yield db
    finally:
        await db.close()


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


@router.get("/")
async def root(router_service = Annotated[RouterService, Depends(get_router_service)]):
    rules = await router_service.get_rules()
    return {"message": rules }
