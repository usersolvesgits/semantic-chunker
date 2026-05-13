from typing import List

class TextChunking:
    @staticmethod
    def ChunkaTesto(testo: str, max_tokens: int = 100, overlap: int = 20) -> List[str]:
        chunks: List[str] = []
        startIndex: int = 0

        while startIndex <  len(testo):
            endIndex: int = startIndex + max_tokens
            chunk: str = testo[startIndex:endIndex]

            chunks.append(chunk)

            startIndex += max_tokens - overlap

        return chunks