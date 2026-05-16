import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

texts = []

for item in catalog:

    text = f"""
    Name: {item.get('name', '')}

    Description:
    {item.get('description', '')}

    Job Levels:
    {', '.join(item.get('job_levels', []))}

    Skills:
    {', '.join(item.get('keys', []))}
    """

    texts.append(text)

embeddings = model.encode(texts)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

faiss.write_index(index, "shl.index")

print("FAISS index created successfully")