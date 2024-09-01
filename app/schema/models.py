from pydantic import BaseModel
from typing import List

class QuestionSchema(BaseModel):
    question: str

class DocumentSchema(BaseModel):
    text: str

class QARequestSchema(BaseModel):
    questions: List[QuestionSchema]
    document: DocumentSchema
