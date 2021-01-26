import os
import shutil
source = input("Enter The Source Folder Name ")
dest = input("Enter The Dest Folder Name ")
source = source+'/'
dest = dest+'/'
listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),dest)