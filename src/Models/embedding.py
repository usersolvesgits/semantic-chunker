from typing import Final, List
from sentence_transformers import SentenceTransformer

class Embedding:
    def __init__(self) -> None:
        MODEL_NAME: Final[str] = "all-MiniLM-L6-v2"
        self.model: SentenceTransformer = SentenceTransformer(MODEL_NAME)

    def Embedda(self, text: List[str]):
        embedding = self.model.encode(text)
        return embedding