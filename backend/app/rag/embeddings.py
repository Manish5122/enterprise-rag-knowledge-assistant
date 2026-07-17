from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-base-en-v1.5"

embedding_model = SentenceTransformer(MODEL_NAME)


def create_embeddings(chunks):
    texts = [chunk.page_content for chunk in chunks]
    embeddings = embedding_model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )
    return embeddings