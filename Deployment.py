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

with open("C:\\Users\\Dell\\Desktop\\runner\\config.txt", encoding='utf8') as f:
    lineNumber = 0
    for line in f:
        lineNumber += 1
        if lineNumber == 1:
            sdCard = line.strip()
        elif lineNumber == 2:
            saveRar = line.strip()
    f.close()
print("Le système de stockage " + sdCard + " va être former en FAT32")
print("Le fichier " + saveRar + " va ensuite être copier dedans")
d1 = input("Clickez sur Y pour lancer le processus et N pour stopper le programme: ")

if d1 == "Y":
    os.system("format /FS:FAT32 D:")
    moveFile("save.rar", "C:\\Users\\Dell\\Desktop\\", "D:\\")
    time.sleep(10)
    unRarFile("D:\\save.rar", "D:\\")
elif d1 == "N":
    pass
