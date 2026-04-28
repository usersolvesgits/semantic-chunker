from typing import List
from transformers import AutoTokenizer as AT

class TextChunking:
    def __init__(self) -> None:
        self.tokenizer = AT.from_pretrained("bert-base-uncased")

    def Chunck_Text(self, testo, max_tokens=100, overlap=20) -> List[str]:
        tokens = self.tokenizer.encode(testo, add_special_tokens=False)

        chunks = []
        startIndex = 0

        while startIndex <  len(tokens):
            endIndex = startIndex + max_tokens
            chunk = tokens[startIndex:endIndex]

            chunks.append(self.tokenizer.decode(chunk))

            startIndex += max_tokens - overlap

        return chunks