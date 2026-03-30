from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once (VERY IMPORTANT)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Your dataset (replace later with real dataset)
documents = [
    "Artificial intelligence is transforming industries like healthcare and finance",
    "Machine learning models improve automatically with experience",
    "Deep learning uses neural networks for complex pattern recognition",
    "Search engines rank pages using algorithms like PageRank",
    "Binary search works efficiently on sorted arrays",
    "Graph algorithms are used in social networks and maps",
    "Natural language processing helps computers understand human language",
    "AI is used in self-driving cars and recommendation systems",
    "Big data analytics extracts insights from massive datasets",
    "Cloud computing enables scalable machine learning applications"
]

# Convert docs to embeddings
doc_embeddings = model.encode(documents)

def semantic_search(query, top_k=5):
    query_embedding = model.encode([query])

    similarity = cosine_similarity(query_embedding, doc_embeddings)
    results = similarity.flatten().argsort()[::-1]

    return results[:top_k]