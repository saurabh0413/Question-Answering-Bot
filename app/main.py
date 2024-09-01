from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI 
from app.core.config import settings 

def create_app() -> FastAPI:
    app = FastAPI()
    return app  

app = create_app()

@app.get("/")
def home_root():
    return {"message":"Welcome to Questions Answering Bot"}