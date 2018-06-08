# Author: Asish Kumar
import glob
import os
i = 0
extensions = ["*.mp4", "*.avi", "*.flv", "*.wmv", "*.mov", "*.mkv", "*.3gp"]
filenames = []
inp_name = input("Please enter the name of the files after conversion: ")
inp_ext = input("Please enter new extension: ")
remove = input("Enter 'y' or 'n'. Do you want to remove original file?").lower()
for ext in extensions:
    for filename in glob.glob(ext):
        with open(filename, "r+b") as videoFile:  # r+b is used for opening a file in byte readable mode
            with open("{}{}.{}".format(inp_name, i, inp_ext), 'a+b') as bacdFile:
                print(videoFile.read)
                bacdFile.write(b"$$Fe@xt..")
                i += 1
                bacdFile.write(videoFile.read())
            filenames.append(filename)
if remove == 'y':
    for files in filenames:
        os.remove(files)
