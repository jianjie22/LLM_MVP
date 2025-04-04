# app/models.py

from beanie import Document
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict, Any
from typing import Literal

class Prompt(BaseModel):
    role: Literal["system", "user", "assistant", "function"]
    content: str

class Conversation(Document):
    id: UUID = Field(default_factory=uuid4, alias="_id")
    name: str
    model: str
    params: Dict[str, Any] = Field(default_factory=dict)
    prompts: List[Prompt] = Field(default_factory=list)
    tokens: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "conversations"

class ConversationPUT(BaseModel):
    name: Optional[str]
    params: Optional[Dict[str, Any]]
    