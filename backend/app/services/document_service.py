from app.rag.loader import load_pdf
from app.rag.splitter import split_text
from app.rag.embeddings import create_embeddings
from app.rag.vectorstore import save_index


def process_document(file_path: str):

    text = load_pdf(file_path)

    chunks = split_text(text)

    embeddings = create_embeddings(chunks)

    total_vectors = save_index(
        embeddings,
        chunks
    )

    return {
        "characters": len(text),
        "chunks": len(chunks),
        "vectors": total_vectors,
    }