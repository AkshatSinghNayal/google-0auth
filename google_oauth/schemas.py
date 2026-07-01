from pydantic import BaseModel
from typing import Optional


class GoogleUser(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    picture: Optional[str] = None
