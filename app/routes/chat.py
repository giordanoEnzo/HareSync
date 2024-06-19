from fastapi import APIRouter, HTTPException
from ..models import Prompt

router = APIRouter()

@router.post("/chat")
async def chat(prompt: Prompt):
    pass