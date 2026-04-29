from typing import List

class TextChunking:
    @staticmethod
    def Chunck_Text(testo: str, max_tokens: int = 100, overlap: int = 20) -> List[str]:

        chunks = []
        startIndex = 0

        while startIndex <  len(testo):
            endIndex = startIndex + max_tokens
            chunk = testo[startIndex:endIndex]

            chunks.append(chunk)

            startIndex += max_tokens - overlap

        return chunks