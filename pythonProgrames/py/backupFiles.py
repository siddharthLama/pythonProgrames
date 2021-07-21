import os
import shutil
 
source = input("Enter the sorce folder")
destination = input("Enter the destination Folder")
listOfFiles = os.listdir(source)

for file in listOfFiles:
    shutil.copy(source + "/" + file , destination)
