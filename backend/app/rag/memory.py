from collections import deque

# Stores last 10 messages
chat_history = deque(maxlen=10)


def add_message(role: str, content: str):
    chat_history.append({
        "role": role,
        "content": content
    })


def get_history():
    history = ""

    for msg in chat_history:
        history += f"{msg['role']}: {msg['content']}\n"

    return history


def clear_history():
    chat_history.clear()