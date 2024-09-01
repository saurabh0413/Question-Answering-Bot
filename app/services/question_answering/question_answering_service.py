from app.services.document.pdf_loader import load_pdf
from app.services.document.json_loader import load_json
from app.services.vector_store.vector_store import store_embeddings
from app.services.retrieval.retrieval_service import retrieve_relevant_chunks
from app.services.generation.generation_service import generate_answer
from typing import List, Dict, Union
import json
import logging

#service for processing questions and documents to provide answers based on the content of the document
class QuestionAnsweringService:
    async def process_qa(self, questions_content: bytes, document_content: bytes) -> List[Dict[str, str]]:
        try:
            questions = json.loads(questions_content.decode('utf-8'))
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding questions JSON: {e}")
            raise

        try:
            if document_content.startswith(b'%PDF'):
                document = load_pdf(document_content)
                document_text = document 
            else:
                document = json.loads(document_content.decode('utf-8'))
                document_text = document.get("text", "")
        except (json.JSONDecodeError, KeyError) as e:
            logging.error(f"Error loading document content: {e}")
            raise

        try:
            chunks = self.split_document(document_text)
            store_embeddings(chunks)
        except Exception as e:
            logging.error(f"Error processing document chunks: {e}")
            raise

        # generate answers for each question
        answers = []
        for question in questions:
            try:
                relevant_chunks = retrieve_relevant_chunks(question)
                answer = await generate_answer(relevant_chunks, question)
                answers.append({"question": question, "answer": answer})
            except Exception as e:
                logging.error(f"Error processing question '{question}': {e}")
                answers.append({"question": question, "answer": "Error occurred"})

        return answers

    #splits the document text into chunks of specified size
    def split_document(self, document: str, chunk_size: int = 1000) -> List[str]:
       
        words = document.split()
        return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
