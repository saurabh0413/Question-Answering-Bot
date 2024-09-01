from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from typing import List

class VectorStore:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.store = Chroma(embedding_function=self.embeddings)

    def add(self, texts: List[str], metadatas: List[dict] = None):
        self.store.add_texts(texts, metadatas)

    def query(self, query: str) -> List[str]:
        docs = self.store.similarity_search(query)
        return [doc.page_content for doc in docs]

vector_store = VectorStore()

def store_embeddings(chunks: List[str]):
    vector_store.add(chunks)

def retrieve_embeddings(query: str, max_results: int = 4) -> List[str]:
    all_results = vector_store.query(query)
    return all_results[:max_results]