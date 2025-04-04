# app/models.py

from beanie import Document
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Prompt(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class Conversation(Document):
    name: str
    model: str
    prompts: List[Prompt]
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "conversations"  # This will be the MongoDB collection name

'''
example document:

{
  "name": "My Chat",
  "model": "gpt-3.5-turbo",
  "prompts": [
    {"role": "user", "content": "Hi!"},
    {"role": "assistant", "content": "Hello there!"}
  ],
  "created_at": "2025-04-04T11:28:00Z"
}

'''