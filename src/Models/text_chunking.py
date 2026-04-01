from typing import List
from transformers import AutoTokenizer as AT

class TextChunking:
    @staticmethod
    def chunck_text(testo, max_tokens=100, overlap=20) -> List[str]:
        tokenizer = AT.from_pretrained("bert-base-uncased")
        tokens = tokenizer.encode(testo, add_special_tokens=False)

        chunks = []
        startIndex = 0

        while startIndex <  len(tokens):
            endIndex = startIndex + max_tokens
            chunk = tokens[startIndex::endIndex]

            chunks.append(tokenizer.decode(chunk))

            startIndex += max_tokens - overlap

        return chunks