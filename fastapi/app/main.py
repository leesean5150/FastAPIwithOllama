from fastapi import FastAPI
from .routes.ask import ask_router
from llm.model_loader import connect_to_milvus, create_collection

app = FastAPI()

# deprecated logic for reference
# @app.on_event("startup")
# async def startup():
#     connect_to_milvus()
#     global collection
#     collection = create_collection()

# async def startup():
#     connect_to_milvus()
#     global collection
#     collection = create_collection()

@app.get('/')
def home():
    return {"Hello": "World"}

app.include_router(ask_router, prefix="/llm")

# async def on_startup():
#     await startup()

# async def on_shutdown():
#     # Add any necessary cleanup or shutdown logic here (e.g., closing Milvus connection)
#     pass  

# app.add_event_handler("startup", on_startup)
# app.add_event_handler("shutdown", on_shutdown)