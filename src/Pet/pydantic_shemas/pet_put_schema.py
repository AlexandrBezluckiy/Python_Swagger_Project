from pydantic import BaseModel, field_validator, HttpUrl
from typing import List
from src.enums.global_enums import GlobalErroreMessage

class Pet_full_schema(BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list[str]
    tags: list[dict]
    status: str