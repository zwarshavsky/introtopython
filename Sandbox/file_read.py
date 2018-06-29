# fh = open("test1.txt")
# fp = fh.read()
# print(fp.rstrip())

from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in '%s': %s" % (cwd, files))

track = input("Enter track filename: ")
mp3 = MP3File(track)
print(mp3.genre)
