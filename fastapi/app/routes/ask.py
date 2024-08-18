from fastapi import APIRouter, Response
import requests
from llm.embedding import generate_query_vector
from app.db.milvus import search_vectors

ask_router = APIRouter()

# base ollama endpoint without using milvus
@ask_router.get('/ask')
def ask(prompt: str):
    res = requests.post('http://ollama:11434/api/generate', json={
        "prompt": prompt,
        "stream": False,
        "model": "llama3"
    })
    return Response(content=res.content, media_type='application/json')

# @ask_router.get('/ask')
# def ask(prompt: str):
#     query_vector = generate_query_vector(prompt)
    
#     milvus_results = search_vectors(query_vector)

#     if milvus_results:
#         augmented_prompt = f"Related information: {milvus_results[0]['id']}\n{prompt}"
#     else:
#         augmented_prompt = prompt

#     res = requests.post('http://ollama:11434/api/generate', json={
#         "prompt": augmented_prompt,
#         "stream": False,
#         "model": "llama3"
#     })
#     ollama_response = res.json()

#     # Option 2: Include Milvus search results in the final response (e.g., for display or further logic)
#     final_response = {
#         "ollama_response": ollama_response,
#         "milvus_related_info": milvus_results  # This could be used in your frontend or further processing
#     }
    
#     return Response(content=ollama_response, media_type='application/json')