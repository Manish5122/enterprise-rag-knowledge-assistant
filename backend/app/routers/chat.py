from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.retriever import retrieve
from app.rag.generator import generate_answer
from app.rag.memory import add_message

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


class ChatRequest(BaseModel):
    question: str


@router.post("/")
def chat(request: ChatRequest):

    # Retrieve relevant chunks
    chunks = retrieve(request.question)

    # Convert chunks into a single context string
    context = "\n\n".join(chunks)

    # Save user message
    add_message("User", request.question)

    # Generate answer using Ollama
    answer = generate_answer(
        request.question,
        context
    )

    # Save assistant response
    add_message("Assistant", answer)

    return {
        "status": "success",
        "question": request.question,
        "answer": answer,
        "sources": len(chunks)
    }