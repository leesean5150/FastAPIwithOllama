from pymilvus import connections, Collection
import numpy as np

def load_collection(collection_name):
    collection = Collection(collection_name)
    collection.load()

# def search_vectors(query_vector, top_k=5):
#     collection_name = "ask_collection"
#     collection = Collection(collection_name)
#     load_collection(collection_name)
    
#     search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
#     results = collection.search([query_vector], "embedding", param=search_params, limit=top_k)
#     return [{"id": res.id, "distance": res.distance} for res in results]

def search_vectors(query_vector, top_k=5):
    collection_name = "ask_collection"
    collection = Collection(collection_name)
    load_collection(collection_name)
    
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    try:
        results = collection.search([query_vector], "embedding", param=search_params, limit=top_k)
        hits = results[0]
        return [{"id": hit.id, "distance": hit.distance} for hit in hits]
    except MilvusException as e:
        print(f"Search failed: {e}")
        return []

def insert_vectors(collection, vectors):
    ids = collection.insert([vectors])
    collection.load()
    return ids
