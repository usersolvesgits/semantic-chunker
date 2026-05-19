from typing import List
from torch import Tensor
from sentence_transformers import SentenceTransformer

class Embedding:
    def __init__(self, model: str="all-MiniLM-L6-v2") -> None:
        MODEL_NAME: str = model
        self.model: SentenceTransformer = SentenceTransformer(MODEL_NAME)

    def EmbeddaList(self, text: List[str]) -> Tensor:
        embedding = self.model.encode(text)
        return embedding

    def EmbeddaText(self, text: str) -> Tensor:
        embedding = self.model.encode(text)
        return embedding