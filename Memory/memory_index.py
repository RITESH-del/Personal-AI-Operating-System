from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np

if __name__ == "__main__":
    model = SentenceTransformer("models/minilm")

    with open("Memory/memory.json", "r") as f:
        memory = json.load(f)

    texts = [item["rag"] for item in memory]
    embeddings = model.encode(texts, normalize_embeddings=True)

    print(embeddings.shape)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)  # Inner Product = cosine
    index.add(np.array(embeddings))

    faiss.write_index(index, "memory_faiss.index")
