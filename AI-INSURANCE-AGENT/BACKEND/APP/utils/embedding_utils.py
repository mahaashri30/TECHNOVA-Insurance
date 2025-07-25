import os
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Path to store/load embeddings
EMBEDDING_PATH = os.path.join("data", "embeddings", "plan_embeddings.pkl")

# Load SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_embeddings():
    """
    Load precomputed embeddings and plan data from pickle file.
    Returns:
        embeddings (np.ndarray): Precomputed vectors
        plans (list): List of plan dictionaries
    """
    if not os.path.exists(EMBEDDING_PATH):
        raise FileNotFoundError(f"Embedding file not found at {EMBEDDING_PATH}. Run embedding generation notebook.")
    
    with open(EMBEDDING_PATH, "rb") as f:
        data = pickle.load(f)
    
    embeddings = np.array(data['embeddings'])
    plans = data['plans']
    return embeddings, plans


def generate_embedding(text: str):
    """
    Generate embedding for a single query string.
    Args:
        text (str): Query text
    Returns:
        np.ndarray: Embedding vector
    """
    return model.encode([text])[0]


def semantic_search(query: str, top_k: int = 3):
    """
    Perform semantic search to find top insurance plans matching the query.
    Args:
        query (str): User query (e.g., 'health insurance with critical illness cover')
        top_k (int): Number of top results to return
    Returns:
        list: List of top matching plan dictionaries
    """
    # Load stored embeddings and plans
    embeddings, plans = load_embeddings()
    
    # Generate query embedding
    query_embedding = generate_embedding(query).reshape(1, -1)
    
    # Compute cosine similarity
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    
    # Get top-k matches
    top_indices = similarities.argsort()[-top_k:][::-1]
    
    results = []
    for idx in top_indices:
        plan = plans[idx]
        plan['similarity'] = round(float(similarities[idx]), 3)
        results.append(plan)
    
    return results
