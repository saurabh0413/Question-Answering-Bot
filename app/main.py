from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI 
from app.core.config import settings 
from app.api.v1.qna_routes import router as qa_router

#FastAPI application instance
def create_app() -> FastAPI:
    app = FastAPI()
    return app  

app = create_app()

app.include_router(qa_router, prefix="/api/v1")

#root endpoint for the application
@app.get("/")
def home_root():
    return {"message":"Welcome to Questions Answering Bot"}