from typing import Annotated
from fastapi import APIRouter, Depends
from main.dependencies import get_router_service
from main.services.router_service import RouterService

router = APIRouter()

@router.get("/api/rules")
async def root(router_service: Annotated[RouterService, Depends(get_router_service)]):
    rules = await router_service.get_rules()
    return rules


