from app.services.vector_store.vector_store import retrieve_embeddings
from typing import List

def retrieve_relevant_chunks(query: str, max_results: int = 4) -> List[str]:
    return retrieve_embeddings(query, max_results)