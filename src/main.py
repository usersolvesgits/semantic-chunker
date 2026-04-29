import os
from typing import Final
from typing import List
from Models.text_chunking import TextChunking

def Read_FileText(dirPath: str, fileName: str) -> str:
    fileText: str = ""
    for file in os.listdir(dirPath):
        filePath = os.path.join(dirPath, file)
        if os.path.isfile(filePath):
            if file == fileName:
                with open(filePath, "r") as f:
                    fileText = f.read()
    return fileText

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
    fileChunkato = TextChunking.Chunck_Text(fileText)


if __name__ == "__main__":
    main()