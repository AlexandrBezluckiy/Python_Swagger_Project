from pydantic import BaseModel, field_validator, HttpUrl
from typing import List
from src.enums.global_enums import GlobalErroreMessage

class Pet_Post(BaseModel):
    id: int
    photoUrls: list[HttpUrl]
    tags: list[dict]


    @field_validator('id')
    def validate_id(cls, id):
        if not (id):
            raise ValueError(GlobalErroreMessage.WRONG_ID.value)
        else:
            return id
