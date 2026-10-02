import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

# 1. Data load karo
df = pd.read_csv("data/patents.csv").dropna(subset=["title", "abstract"])
df["text"] = df["title"] + ". " + df["abstract"]

# 2. Embedding model (free, local)
model = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Vector DB
client = chromadb.PersistentClient(path="chroma_db")
col = client.get_or_create_collection("patents")

# 4. Embeddings banake store karo
embeddings = model.encode(df["text"].tolist()).tolist()
col.upsert(
    ids=df["id"].astype(str).tolist(),
    documents=df["text"].tolist(),
    metadatas=[{"title": t} for t in df["title"]],
    embeddings=embeddings,
)

print("Done:", col.count(), "patents indexed")