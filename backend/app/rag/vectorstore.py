import faiss
import numpy as np
import pickle
from pathlib import Path


VECTOR_DIR = Path("vectorstore")
VECTOR_DIR.mkdir(exist_ok=True)


def save_index(embeddings, chunks):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    faiss.write_index(index, str(VECTOR_DIR / "faiss.index"))

    with open(VECTOR_DIR / "documents.pkl", "wb") as f:
        pickle.dump(chunks, f)

    return len(chunks)