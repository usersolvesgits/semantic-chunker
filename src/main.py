import os
from typing import Final, List
import torch
from torch import Tensor
from Models.text_chunking import TextChunking
from Models.embedding import Embedding
from Models.semantic_similarities import SemanticSimilarities

def Read_FileText(dirPath: str, fileName: str) -> str:
    fileText: str = ""
    for file in os.listdir(dirPath):
        filePath = os.path.join(dirPath, file)
        if os.path.isfile(filePath):
            if file == fileName:
                with open(filePath, "r") as f:
                    fileText = f.read()
    return fileText

def GetRisultatoChunking(fileChunkato: List[str]) -> None:
    inputUtente: str = ""

    print("Vuoi mostrare il risultato del chunking? (Y/n)")
    inputUtente = input("> ").lower()
    if inputUtente == "y":
        print(fileChunkato)
def GetRisultatoSemantico(chunkSimile: str) -> None:
    inputUtente: str = ""

    print("Vuoi mostrare il chunk più simile al tuo messaggio? (Y/n)")
    inputUtente = input("> ").lower()
    if inputUtente == "y":
        print(chunkSimile)

def main() -> None:
    dir = os.path.dirname(os.path.abspath(__file__))
    textDir = os.path.join(dir, "text-files")

    if not os.path.isdir(textDir):
        print("Errore: directory non esistente!")
        return

    files: List[str] = []
    for file in os.listdir(textDir):
        fullPath = os.path.join(textDir, file)
        if os.path.isfile(fullPath):
            files.append(fullPath)

    print("=====================================================")
    print("             Quale file vorresti chunkare?           ")
    print("             1) Armed_Conflicts.txt                  ")
    print("             2) Body_Shaming.txt                     ")
    print("             3) Racism.txt                           ")
    print("=====================================================")

    ARMED_CONFLICTS_TXT: Final[str] = "Armed_Conflicts.txt"
    BODY_SHAMING_TXT: Final[str] = "Body_Shaming.txt"
    RACISM_TXT: Final[str] = "Racism.txt"

    userInput = input("> ")
    fileText: str = ""
    match (userInput):
        case "1":
            fileText = Read_FileText(textDir, ARMED_CONFLICTS_TXT)

        case "2":
            fileText = Read_FileText(textDir, BODY_SHAMING_TXT)

        case "3":
            fileText = Read_FileText(textDir, RACISM_TXT)

        case _:
            print("Opzione non supportata, riprovare!")
            main()

    fileChunkato: List[str] = []
    fileChunkato = TextChunking.ChunkaTesto(fileText, overlap=15)

    GetRisultatoChunking(fileChunkato)

    embedder: Embedding = Embedding()
    textEmbedding = embedder.EmbeddaList(fileChunkato)


    print("\n\n\n--- Ricerca Semantica ---")
    inputUtente: str = input("Inserisci una frase per cercare nei chunk: ")
    userEmb: Tensor = embedder.EmbeddaText(inputUtente)

    primaRicerca: bool = True
    maxSimiliraty: Tensor = torch.tensor(0)
    chunkSimile: str = ""
    numeroChunk: int = 0
    for i in range(len(textEmbedding)) :
        similarity: Tensor = SemanticSimilarities.Semanta(userEmb,textEmbedding[i])
        if primaRicerca or similarity > maxSimiliraty:
            maxSimiliraty = similarity
            chunkSimile = fileChunkato[i]
            numeroChunk = i
            primaRicerca = False

    print("\n\nINFORMAZIONI:")
    print(f"Il chunk più simile al messaggio dell'utente è il numero {numeroChunk}")
    GetRisultatoSemantico(chunkSimile)

if __name__ == "__main__":
    main()