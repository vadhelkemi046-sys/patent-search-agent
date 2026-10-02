import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="chroma_db")
col = client.get_collection("patents")


def search_patents(query, n=3):
    query_emb = model.encode([query]).tolist()
    res = col.query(query_embeddings=query_emb, n_results=n)

    results = []
    for i in range(len(res["ids"][0])):
        results.append({
            "id": res["ids"][0][i],
            "title": res["metadatas"][0][i]["title"],
            "text": res["documents"][0][i],
            "distance": res["distances"][0][i],
        })
    return results


if __name__ == "__main__":
    q = input("Search query: ")
    for r in search_patents(q):
        print(f"{r['id']} | {r['title']} | distance: {r['distance']:.3f}")