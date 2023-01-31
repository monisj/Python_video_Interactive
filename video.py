import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    install("pytube") #Necessary if the package is not installed
except:
    pass

import pytube
link = input("Enter URL=")
video=pytube.YouTube(link)
video.streams.first().download()
print("Download Link =",link)