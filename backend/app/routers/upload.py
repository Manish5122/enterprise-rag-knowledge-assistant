from pathlib import Path
import shutil

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.document_service import process_document

router = APIRouter(
    prefix="/upload",
    tags=["Document Upload"],
)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )

    allowed_extensions = {".pdf"}

    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    file_path = UPLOAD_DIR / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_document(str(file_path))

    return {
        "status": "success",
        "filename": file.filename,
        "characters": result["characters"],
        "chunks": result["chunks"],
        "vectors": result["vectors"],
        "message": "Document indexed successfully"
    }