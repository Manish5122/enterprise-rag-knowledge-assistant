from langchain_ollama import ChatOllama

from app.rag.prompt import SYSTEM_PROMPT
from app.rag.memory import get_history

llm = ChatOllama(
    model="qwen3:8b",
    temperature=0
)


def generate_answer(question, context):

    history = get_history()

    prompt = f"""
{SYSTEM_PROMPT}

Conversation History:

{history}

Context:

{context}

Question:

{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content