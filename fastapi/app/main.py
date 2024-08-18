from fastapi import FastAPI

from .routes.llm.ask import ask_router
from db.milvus_loader import connect_to_milvus, create_collection
from db.postgres import init_db, get_connection, get_session_local
from app.models.auth.user import User

app = FastAPI()

@app.on_event("startup")
async def startup():
    connect_to_milvus()
    global collection
    collection = create_collection()

    init_db()

    app.state.postgres_conn = get_connection()
    app.state.postgres_cursor = app.state.postgres_conn.cursor()

@app.on_event("shutdown")
def shutdown():
    app.state.postgres_cursor.close()
    app.state.postgres_conn.close()

@app.get('/')
def home():
    return {"Hello": "World"}

@app.get("/query-with-psycopg")
def query_psycopg():
    with app.state.postgres_cursor as cursor:
        cursor.execute("SELECT * FROM user;")
        result = cursor.fetchall()
        print(result)
    return {"result": result}

@app.get("/query-with-sqlalchemy")
def query_sqlalchemy():
    session = get_session_local()()
    users = session.query(User).all() 
    return {"result": users}  

app.include_router(ask_router, prefix="/llm")