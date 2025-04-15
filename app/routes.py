# app/routes.py

# Standard library imports
from uuid import UUID, uuid4

# Third-party imports
from fastapi import APIRouter, Body, HTTPException, Path, status
from beanie import Document, PydanticObjectId
from pydantic import Field
from typing import Any, Dict, List, Optional

# Local application imports
from app.models import (
    Conversation,
    ConversationCreate,
    ConversationOut,
    ConversationPUT,
    Prompt
)
from app.services import handle_prompt


router = APIRouter()

@router.post(
    "/conversations",
    status_code=201,
    responses={
        201: {
            "description": "Successfully created resource with ID",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {"id": "123e4567-e89b-12d3-a456-426614174000"}
                }
            },
        },
        400: {
            "description": "Invalid parameters provided",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {"code": 400, "message": "Invalid parameters provided"}
                }
            },
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {"code": 500, "message": "Internal server error"}
                }
            },
        },
    },
)
async def create_conversation(data: ConversationCreate):
    try:
        # Construct a new full Conversation doc from the smaller model
        new_convo = Conversation(
            name=data.name,
            model=data.model,
            params=data.params,
            # No prompts/tokens because they're default
        )
        saved_convo = await new_convo.create()
        return {"id": str(saved_convo.id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/conversations",
    response_model=List[ConversationOut],
    responses={
        200: {
            "description": "Successfully retrieved a list of Conversations",
            "content": {
                "application/json": {
                    # example or schema as needed
                    "example": [
                        {
                            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                            "name": "string",
                            "params": {},
                            "tokens": 0
                        }
                    ]
                }
            },
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {
                        "code": 500,
                        "message": "Internal server error"
                    }
                }
            },
        },
    },
)
async def get_conversations():
    try:
        return await Conversation.find_all().to_list()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put(
    "/conversations/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Successfully updated specified resource"},
        400: {
            "description": "Invalid parameters provided",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {"code": 400, "message": "Invalid parameters provided"}
                }
            },
        },
        404: {
            "description": "Conversation not found",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {"code": 404, "message": "Conversation not found"}
                }
            },
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {"code": 500, "message": "Internal server error"}
                }
            },
        },
    },
)
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

@router.delete(
    "/conversations/{id}",
    status_code=204,
    responses={
        404: {
            "description": "Specified resource(s) was not found",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {
                        "code": 404,
                        "message": "Specified resource(s) was not found"
                    }
                }
            },
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {
                        "code": 500,
                        "message": "Internal server error"
                    }
                }
            },
        },
    },
)
async def delete_conversation(id: UUID):
    conversation = await Conversation.find_one(Conversation.id == id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    await conversation.delete()


@router.post(
    "/queries/{id}",
    status_code=201,
    responses={
        201: {
            "description": "Successfully created resource with LLM prompt reply",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {"reply": "LLM response message"}
                }
            },
        },
        400: {
            "description": "Invalid parameters provided",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {"code": 400, "message": "Invalid parameters provided"}
                }
            },
        },
        404: {
            "description": "Conversation not found",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {"code": 404, "message": "Conversation not found"}
                }
            },
        },
        422: {
            "description": "Failed to query OpenAI",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {
                        "code": 422,
                        "message": "Failed to query OpenAI: [error details]"
                    }
                }
            },
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/vnd.launchpad.v1+json": {
                    "example": {"code": 500, "message": "Internal server error"}
                }
            },
        },
    },
)
async def query_llm(
    id: UUID,
    prompt_data: Prompt  
):

    conversation = await Conversation.get(id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    reply_text = await handle_prompt(
        conversation_id=id,
        prompt=prompt_data  # or build a new Prompt if needed
    )

    return {"reply": reply_text}

