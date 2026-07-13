from fastapi import FastAPI

app = FastAPI(
    title="Enterprise RAG Knowledge Assistant",
    version="1.0.0",
    description="Enterprise-grade Retrieval Augmented Generation Assistant"
)


@app.get("/")
async def root():
    return {
        "message": "Enterprise RAG Knowledge Assistant",
        "status": "running",
        "version": "1.0.0"
    }