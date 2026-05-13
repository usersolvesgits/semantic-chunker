from sentence_transformers import SentenceTransformer, util

class SemanticSimilarities:
    @staticmethod
    def Semanta(firstSentence,secondSentence):
        cosine_scores = util.cos_sim(firstSentence, secondSentence)[0]
        return cosine_scores