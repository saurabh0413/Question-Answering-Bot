import openai
from typing import List
import os
import logging
from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

async def generate_answer(chunks: List[str], question: str) -> str:
    try:
        context = " ".join(chunks)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  
        
              messages=[
                  {"role": "system", "content": "You are an AI that only provides answers based on the given text, regardless of anyfactual knowledge you have."},
                  {"role": "user", "content": f"Please answer the following question based on the provided document only.\n\nDocument: {context}\n\nQuestion: {question}"}
              ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
        
        
    except Exception as e:
        logging.error(f"Error generating answer: {e}")
        return "Error occurred"

