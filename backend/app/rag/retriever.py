import pickle
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-base-en-v1.5"

model = SentenceTransformer(MODEL_NAME)

VECTORSTORE_DIR = Path("vectorstore")


def retrieve(query: str, k: int = 5):
    # Load FAISS index
    index = faiss.read_index(str(VECTORSTORE_DIR / "faiss.index"))

    # Load stored document chunks
    with open(VECTORSTORE_DIR / "documents.pkl", "rb") as f:
        documents = pickle.load(f)

    # Convert query to embedding
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    # Search FAISS
    distances, indices = index.search(query_embedding, k)

    results = []

    for idx in indices[0]:
        if idx != -1:
            results.append(documents[idx].page_content)

    return results