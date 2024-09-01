from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

@router.post("/answer-questions/")
async def answer_questions(questions_file: UploadFile = File(...), document_file: UploadFile = File(...)):
    service = QuestionAnsweringService()
    
    if not questions_file.content_type == "application/json":
        raise HTTPException(status_code=400, detail="Invalid file type for questions. Only JSON is supported.")
    
    if not document_file.content_type in ["application/pdf", "application/json"]:
        raise HTTPException(status_code=400, detail="Invalid file type for document. Only PDF or JSON is supported.")
    
    questions_content = await questions_file.read()
    document_content = await document_file.read()

    return "check"
  
