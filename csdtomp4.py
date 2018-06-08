# Author: Asish Kumar
import glob
import os
i = 0
filenames = []
bef_ext = input("Please enter the file's extension for conversion: ")
inp_name = input("Please enter the common name of the files after conversion: ")
inp_ext = input("Please enter new extension: ")

for filename in glob.glob('*.{}'.format(bef_ext)):
    with open(filename, "r+b") as videoFile:  # r+b is used for opening a file in byte readable mode
        with open("{}{}.{}".format(inp_name, i, inp_ext), 'w+b') as bacdFile:
            print(videoFile.read)
            i += 1
            bacdFile.write(videoFile.read().strip(b"$$Fe@xt.."))
            filenames.append(filename)
for files in filenames:
    os.remove(files)
