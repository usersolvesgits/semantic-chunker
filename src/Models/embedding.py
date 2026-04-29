from typing import Final
from sentence_transformers import SentenceTransformer

class Embedding:
    @staticmethod
    def Embedda(text: str):
        MODEL_NAME: Final[str] = "" # da rivedere
        model = SentenceTransformer(MODEL_NAME)
        embedding = model.encode(text)
        return embedding