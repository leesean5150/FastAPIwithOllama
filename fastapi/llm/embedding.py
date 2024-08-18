from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

def generate_query_vector(query):
    inputs = tokenizer(query, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embedding