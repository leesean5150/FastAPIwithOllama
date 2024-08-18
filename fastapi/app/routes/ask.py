from fastapi import APIRouter, Response
import requests

ask_router = APIRouter()

@ask_router.get('/ask')
def ask(prompt: str):
    res = requests.post('http://ollama:11434/api/generate', json={
        "prompt": prompt,
        "stream": False,
        "model": "llama3"
    })
    return Response(content=res.content, media_type='application/json')