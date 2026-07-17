from fastapi import FastAPI

from app.database.database import Base, engine
from app.routers.auth import router as auth_router
from app.routers.upload import router as upload_router
from app.routers.chat import router as chat_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise RAG Knowledge Assistant",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "Enterprise RAG Knowledge Assistant API",
        "status": "running",
    }