import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
from tools import tools

# load a pre trained model
model = SentenceTransformer("all-MiniLM-L6-v2")

tool_texts = [tool.description for tool in tools]
tool_names = [tool.name for tool in tools]

embeddings = model.encode(tool_texts, normalize_embeddings=True)

index = faiss.IndexFlatIP(embeddings.shape[1])
index.add(np.array(embeddings))

print(embeddings.shape)