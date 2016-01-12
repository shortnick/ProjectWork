from __future__ import unicode_literals
import os
import youtube_dl
import time

#working dir here
os.chdir("C:\\Users\\Admin\\Music")

# set/create destination directory, update to current working directory command
savedir = "Working Playlist"
if not os.path.exists(savedir):
    os.makedirs(savedir)
    print "Directory created. Please move url list text file into this directory and re run."
else: 
    os.chdir(savedir)

#opens a text file frpm the savedir. format: plain urls (http://...), one per line
with open("metal_songs.txt", "r") as ins:
    to_get = []
    for line in ins:
        to_get.append(line)

# create YouTube downloader
options = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'output': "unicode(%(title)s)",        # name the file the title of the video
    'write-description': True,  #? include as metadata?
    'noplaylist' : True,        # only download single song, not playlist
    'add-metadata' : True,      #write metadata in, too. maybe just technical?
    'postprocessors': [{        #takes the downloaded info, exports in this format
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
                }]
    }       
# play with a rename function, remove last 11 char of file name, to lose YT designator?

failed = []
# uses to_get list to download youtube videos as mp3s

for line in to_get:
    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            ydl.download([line])
            time.sleep(270)
            print "thunk"
        except: 
            failed.append(line)

with open("failureLog.txt", "w") as fileout:
    for x in failed:
        fileout.write(x + "\n")
    fileout.close()



