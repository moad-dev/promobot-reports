from typing import Annotated
from fastapi import APIRouter, Depends
from main.dependencies import get_router_service
from main.dependencies import get_processed_messages_service
from main.services.router_service import RouterService
from main.services.processed_messages_service import ProcessedMessagesService

router = APIRouter()

@router.get("/api/rules")
async def get_all_rules(router_service: Annotated[RouterService, Depends(get_router_service)]):
    rules = await router_service.get_rules()
    return rules


@router.get("/api/processed-messages")
async def get_all_processed_messages(processed_messages_service: Annotated[ProcessedMessagesService, Depends(get_processed_messages_service)]):
    processed_messages = await processed_messages_service.get_processed_messages()
    return processed_messages
