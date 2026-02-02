import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
from tool_kit import tools

# load a pre trained model
model = SentenceTransformer("models/minilm")

tool_texts = [tool.description for tool in tools]
tool_names = [tool.name for tool in tools]

embeddings = model.encode(tool_texts, normalize_embeddings=True)

index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, "faiss.index")

print(embeddings.shape)

# run with python -m src.Store.VectorStore
