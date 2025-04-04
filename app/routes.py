# app/routes.py

from fastapi import APIRouter, HTTPException
from app.models import Conversation
from typing import List
from fastapi import HTTPException, status, Path
from uuid import UUID
from app.models import ConversationPUT
from beanie import PydanticObjectId
from pydantic import Field
from uuid import UUID, uuid4
from beanie import Document

router = APIRouter()

@router.post("/conversations", status_code=201)
async def create_conversation(data: Conversation):
    try:
        convo = await data.create()
        return {"id": str(convo.id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/conversations", response_model=List[Conversation])
async def get_conversations():
    try:
        return await Conversation.find_all().to_list()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/conversations/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_conversation(
    id: UUID,
    body: ConversationPUT
):
    try:
        conversation = await Conversation.get(id)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")

        if body.name is not None:
            conversation.name = body.name
        if body.params is not None:
            conversation.params = body.params

        await conversation.save()
        return

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/conversations/{id}", response_model=Conversation)
async def get_conversation(id: UUID):
    conversation = await Conversation.get(id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation

@router.delete("/conversations/{id}", status_code=204)
async def delete_conversation(id: UUID):
    conversation = await Conversation.find_one(Conversation.id == id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    await conversation.delete()