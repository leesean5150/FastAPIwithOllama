from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests

from llm.embedding import generate_query_vector
from db.milvus import search_vectors

ask_router = APIRouter()

# old router without milvus
# @ask_router.get('/ask')
# def ask(prompt: str):
#     res = requests.post('http://ollama:11434/api/generate', json={
#         "prompt": prompt,
#         "stream": False,
#         "model": "llama3"
#     })
#     return Response(content=res.content, media_type='application/json')

@ask_router.get('/ask')
def ask(prompt: str):
    query_vector = generate_query_vector(prompt)

    milvus_results = search_vectors(query_vector)

    if milvus_results:
        augmented_prompt = f"Related information: {milvus_results[0]['id']}\n{prompt}"
    else:
        augmented_prompt = prompt

    res = requests.post('http://ollama:11434/api/generate', json={
        "prompt": augmented_prompt,
        "stream": False,
        "model": "llama3"
    })

    ollama_response = res.json()

    final_response = {
        "ollama_response": ollama_response,
        "milvus_related_info": milvus_results
    }
    
    return JSONResponse(content=final_response)