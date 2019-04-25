#!/bin/env python
# Requires: youtube_dl module
# Requires: ffmpeg
# Usage:
#
# python youtube2mp3.py <URL>, ...
# 
# Example:
# 
# python youtube2mp3.py https://www.youtube.com/watch?v=dQw4w9WgXcQ

import glob
import subprocess as sp
import sys
import youtube_dl


default_dir="/media/backpack/music/Sorted/"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filenames = sys.argv[1:]
        ydl.download(filenames)

while True:

    move = input("\nMove all .mp3 files to {0} (y/n) ? ".format(default_dir))
    if move == "y":
        files = glob.glob("*.mp3")
        for f in files:
            sp.call(["mv", f, default_dir])
        break
    elif move == "n":
        break
