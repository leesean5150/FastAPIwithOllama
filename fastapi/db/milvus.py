from pymilvus import connections, Collection
import numpy as np

def search_vectors(query_vector, top_k=5):
    collection = Collection("ask_collection")
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    results = collection.search([query_vector], "embedding", param=search_params, limit=top_k)
    return [{"id": res.id, "distance": res.distance} for res in results]

def insert_vectors(collection, vectors):
    ids = collection.insert([vectors])
    collection.load()
    return ids
