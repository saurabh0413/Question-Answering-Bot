from app.services.vector_store.vector_store import retrieve_embeddings
from typing import List

#retrieve relevant document chunks based on the provided query
def retrieve_relevant_chunks(query: str, max_results: int = 4) -> List[str]:
    return retrieve_embeddings(query, max_results)