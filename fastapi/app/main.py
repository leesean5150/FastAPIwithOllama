from fastapi import FastAPI
from .routes.ask import ask_router

app = FastAPI()

@app.get('/')
def home():
    return {"Hello": "World"}

app.include_router(ask_router, prefix="/llm")