from typing import Annotated
from fastapi import APIRouter, Depends, status
from main.dependencies import (
    get_router_service,
    get_processed_messages_service,
    get_unit_of_work
)
from main.domain.processed_message import ProcessedMessage

from main.services.router_service import RouterService
from main.services.processed_messages_service import ProcessedMessagesService
from main.schemas import ProcessedMessageGet, RuleCreation, RuleGet, MessagePost

router = APIRouter()

@router.get("/api/rules")
async def get_all_rules(
    router_service: Annotated[RouterService, Depends(get_router_service)]
) -> list[RuleGet]:
    rules = await router_service.get_rules()
    return rules


@router.post("/api/rules", status_code=status.HTTP_201_CREATED)
async def add_rule(
    rule_data: RuleCreation, 
    router_service: Annotated[RouterService, Depends(get_router_service)],
    uow=Depends(get_unit_of_work)
):
    async with uow: # should be in service layer
        await router_service.add_rule(rule_data)


@router.delete("/api/rules/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_rule(
    uuid: str,
    router_service: Annotated[RouterService, Depends(get_router_service)],
    uow=Depends(get_unit_of_work)
):
    async with uow:
        pass

@router.get("/api/processed-messages")
async def get_all_processed_messages(
    processed_messages_service: Annotated[
        ProcessedMessagesService, Depends(get_processed_messages_service)
    ]
) -> list[ProcessedMessageGet]:
    processed_messages = await processed_messages_service.get_processed_messages()
    return processed_messages

@router.get("/api/processed_messages/{uuid}")
async def get_processed_message_by_uuid(
    uuid: str,
    processed_messages_service: Annotated[
        ProcessedMessagesService, Depends(get_processed_messages_service)
    ]
):
    processed_message = await processed_messages_service.get_processed_message(uuid)
    
    return processed_message


@router.post("/api/messages", status_code=status.HTTP_201_CREATED)
async def add_processed_message(
    message_data: MessagePost,
    router_service: Annotated[RouterService, Depends(get_router_service)],
    uow=Depends(get_unit_of_work)
) -> str:
    async with uow: # should be in service layer
        uuid = await router_service.route(message_data)
    
    return uuid 
