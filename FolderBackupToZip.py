import os
import sys
import pathlib
import zipfile
dirname= input("Enter directory name that you want to backup:")
if not os.path.isdir(dirname):
    print("directory",dirname,"doesn't exist")
    sys.exit(0)
curDirectory=pathlib.Path(dirname)
with zipfile.ZipFile("myZip.zip",mode="w")as archive:
    for file_path in curDirectory.rglob("*"):
        archive.write(file_path,arcname=file_path.relative_to(curDirectory))
if os.path.isfile("myZip.zip"):
   print("Archive","myZip.zip","created successfully")
else:
   print("Error in creating zip archive")
                
