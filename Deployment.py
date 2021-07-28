import zipfile as zip
import platform
import shutil


def unZipFile(target, path):
    zipFile = zip.ZipFile(target)
    zipFile.extractall(path)
    zipFile.close()
    if platform.system() == "Darwin":
        shutil.rmtree("/Users/maxime/Desktop/__MACOSX")


def moveFile(name, path1, path2):
    shutil.move(path1 + name, path2 + name)
