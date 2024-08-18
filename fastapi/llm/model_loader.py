from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

MILVUS_HOST = "milvus-standalone"
MILVUS_PORT = "19530"

def connect_to_milvus():
    connections.connect("default", host=MILVUS_HOST, port=MILVUS_PORT)

def create_collection():
    id_field = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True)
    embedding_field = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128)

    schema = CollectionSchema(fields=[id_field, embedding_field], description="Ask endpoint embeddings")

    collection = Collection(name="ask_collection", schema=schema)
    return collection