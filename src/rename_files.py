# Run this script from the repository's root.
import re
import os
# We learned shutil.move in class, but we can't use it here since it would require an import. idk if thats intentional?
def rename(path):
    pat = re.compile("^snap[0-9]{3}.txt")
    try:
        files = [file for file in os.listdir(path) if pat.search(file) != None]
    except: return
    if files == []: return
    files.sort()
    fileNum = int(files[0][4:7])-1
    for file in files:
        if int(file[4:7]) != fileNum+1:
            os.rename(path + file, path + "snap" + f"{(fileNum+1):03}" + ".txt")
        fileNum += 1
