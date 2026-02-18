from pydantic import BaseModel
from uuid import UUID

class RoasterCreate(BaseModel):
    name: str


class RoasterResponse(BaseModel):
    id: UUID
    name: str
    name_normalized: str
