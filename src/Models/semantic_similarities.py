from sentence_transformers import util
from torch import Tensor

class SemanticSimilarities:
    @staticmethod
    def Semanta(firstSentence,secondSentence) -> Tensor:
        cosine_scores = util.cos_sim(firstSentence, secondSentence)[0]
        return cosine_scores