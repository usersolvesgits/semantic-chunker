from typing import Final, Union, List
from sentence_transformers import SentenceTransformer

class Embedding:
    def __init__(self, model: str="all-MiniLM-L6-v2") -> None:
        MODEL_NAME: Final[str] = "all-MiniLM-L6-v2"
        self.model: SentenceTransformer = SentenceTransformer(MODEL_NAME)

    def Embedda(self, text: Union[str, List:[str]]):
        embedding = self.model.encode(text)
        return embedding # controllare che cosa restituisce