import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from .model_loader import get_model


def embed_text(text: str):
    model = get_model()
    return model.encode([text])[0]


def compute_similarity(text1: str, text2: str) -> float:
    vec1 = embed_text(text1)
    vec2 = embed_text(text2)
    similarity = cosine_similarity([vec1], [vec2])[0][0]
    return float(similarity)