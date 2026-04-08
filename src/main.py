import os
from typing import List 

def main():
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

    userInput = input("> ")
    fileText: str = ""
    match (userInput):
        case "1":
            for file in os.listdir(textDir):
                filePath = os.path.join(textDir, file)
                if os.path.isfile(filePath):
                    if file == "Armed_Conflicts.txt":
                        with open(filePath, "r", encoding="utf-8") as f:
                            fileText = f.read()

        case "2":
            for file in os.listdir(textDir):
                filePath = os.path.join(textDir, file)
                if os.path.isfile(filePath):
                    if file == "Body_Shaming.txt":
                        with open(filePath, "r", encoding="utf-8") as f:
                            fileText = f.read()

        case "3":
            for file in os.listdir(textDir):
                filePath = os.path.join(textDir, file)
                if os.path.isfile(filePath):
                    if file == "Racism.txt":
                        with open(filePath, "r", encoding="utf-8") as f:
                            fileText = f.read()

        case _:
            print("Opzione non supportata, riprovare!")
            return

    """
    Continuare con la logica di chunkaggio
    """

if __name__ == "__main__":
    main()