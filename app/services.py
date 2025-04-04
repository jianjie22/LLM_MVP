# app/services.py

from openai import AsyncOpenAI
from app.models import Conversation, Prompt
from app.anonymizer import anonymize_text
from uuid import UUID

client = AsyncOpenAI()  # will use OPENAI_API_KEY from environment

async def handle_prompt(conversation_id: UUID, prompt: Prompt) -> str:
    conversation = await Conversation.get(conversation_id)
    if not conversation:
        raise ValueError("Conversation not found")

    # Append prompt to history
    history = conversation.prompts + [prompt]

    # Convert to OpenAI format
    openai_messages = [{"role": p.role, "content": anonymize_text(p.content)} for p in history]

    # Call GPT-4o
    response = await client.chat.completions.create(
        model=conversation.model,
        messages=openai_messages
    )

    # Extract assistant reply
    reply = response.choices[0].message

    # Append assistant reply to history
    assistant_prompt = Prompt(role="assistant", content=reply.content)
    conversation.prompts.append(prompt)
    conversation.prompts.append(assistant_prompt)

    await conversation.save()
    return reply.content
