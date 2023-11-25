from pydantic import BaseModel


class RuleCreation(BaseModel):
    group: str | None = None
    topic: str | None = None
    address: str | None = None
    agency: str | None = None


class AddressSchema(BaseModel):
    region: str | None = None
    area: str | None = None
    settlement: str | None = None
    street: str | None = None
    building: str | None = None

class FuzzyAddressSchema(BaseModel):
    region: str | None = None
    area: list[str] = []
    settlement: list[str] = []
    street: list[str] = []
    building: list[str] = []

class RuleGet(BaseModel):
    uuid: str
    group: str | None = None
    topic: str | None = None
    address: AddressSchema | None = None
    agency: str | None = None


class MessagePost(BaseModel):
    text: str

class ProcessedMessageGet(BaseModel):
    uuid: str
    text: str
    group: str | None = None
    topic: str | None = None
    is_trash: bool | None = None
    address: list[FuzzyAddressSchema] = []
    agency: list[str]
