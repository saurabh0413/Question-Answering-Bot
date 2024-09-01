from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI 
from app.core.config import settings 
from app.api.v1.qa_routes import router as qa_router

def create_app() -> FastAPI:
    app = FastAPI()
    return app  

app = create_app()

app.include_router(qa_router, prefix="/api/v1")

@app.get("/")
def home_root():
    return {"message":"Welcome to Questions Answering Bot"}