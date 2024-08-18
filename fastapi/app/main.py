from fastapi import FastAPI

from .routes.llm.ask import ask_router
from db.milvus_loader import connect_to_milvus, create_collection

app = FastAPI()

@app.on_event("startup")
async def startup():
    connect_to_milvus()
    global collection
    collection = create_collection()

@app.get('/')
def home():
    return {"Hello": "World"}

app.include_router(ask_router, prefix="/llm")