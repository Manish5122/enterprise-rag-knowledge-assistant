import requests

BASE_URL = "http://127.0.0.1:8000"


def login(email, password):
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": email,
            "password": password
        }
    )

    return response.json()


def register(username, email, password):
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={
            "username": username,
            "email": email,
            "password": password
        }
    )

    return response.json()


def upload_pdf(file):

    files = {
        "file": (
            file.name,
            file,
            "application/pdf"
        )
    }

    response = requests.post(
        f"{BASE_URL}/upload/",
        files=files
    )

    return response.json()


def ask_question(question):

    response = requests.post(
        f"{BASE_URL}/chat/",
        json={
            "question": question
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()