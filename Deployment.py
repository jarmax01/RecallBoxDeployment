import os
import zipfile as zip
import platform
import shutil
import patoolib
import time

def unZipFile(target, path):
    zipFile = zip.ZipFile(target)
    zipFile.extractall(path)
    zipFile.close()
    if platform.system() == "Darwin":
        shutil.rmtree("/Users/maxime/Desktop/__MACOSX")


def unRarFile(target, path):
    patoolib.extract_archive(target, verbosity=0, outdir=path)
    os.remove(target)


def moveFile(name, path1, path2):
    shutil.move(path1 + name, path2 + name)


sdCard = ""
saveRar = ""
saveRarFileName = ""
currentFolder = os.getcwd()

with open((currentFolder + "\\config.txt"), encoding='utf8') as f:
    lineNumber = 0
    for line in f:
        lineNumber += 1
        if lineNumber == 1:
            sdCard = line.strip()
        elif lineNumber == 2:
            saveRarFileName = line.strip()
            saveRar = (currentFolder + "\\" + saveRarFileName)
    f.close()

print("")
print("Le système de stockage " + sdCard + " va être former en FAT32")
print("Le fichier " + saveRar + " va ensuite être copier dedans")

d1 = input("Clickez sur Y pour lancer le processus et N pour stopper le programme: ")

if d1 == "Y":
    os.system("format /FS:FAT32 "+ sdCard[0:2])
    moveFile(saveRarFileName, currentFolder, sdCard)
    time.sleep(10)
    unRarFile((sdCard + saveRarFileName), sdCard)
elif d1 == "N":
    print("")
    print("Pour modifier les informations accéder au fichier " + (currentFolder + "\\config.txt"))
    print("A bientot !")
    time.sleep(5)
    pass
