# needs youtube-dl: https://github.com/rg3/youtube-dl
#and ffmpeg: http://ffmpeg.zeranoe.com/builds/
from __future__ import unicode_literals
import os
import youtube_dl
import time

#working dir here
os.chdir("C:\\Users\\Admin\\Music")

# set/create destination directory, update to current working directory command
savedir = "C:\\Users\\Admin\\Music\\WorkingPlaylist"
if not os.path.exists(savedir):
    os.makedirs(savedir)
    print("Directory created. Please move url list text file into this directory and re run.")
else: 
    os.chdir(savedir)

#opens a text file frpm the savedir. format: plain urls (http://...), one per line
bob = os.path.join(savedir, "playlisttest.txt")
with open(bob, "r") as ins:
    to_get = []
    for line in ins:
        to_get.append(line)

# create YouTube downloader
options = {
    # fill in first two, if your playlist is private    
    #'username':''
    #'password':''
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
    
failed = []


# uses to_get list to download youtube videos as mp3s
for line in to_get:
    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            ydl.download([line])
            time.sleep(15)
            print("thunk")
        except: 
            failed.append(line)

print("writing finished")

if len(failed) > 0:
    with open("failureLog.txt", "w+") as fileout:
        for x in failed:
            fileout.write(x + "\n")
            fileout.close()
print("fail list done")

# rename function, remove last 12 char of file name, loses the YT designator
for name in os.listdir(savedir):
    if os.path.splitext(name)[1] ==".mp3":
        name2 = os.path.splitext(name)[0][0:-12]+".mp3"
        os.rename(os.path.join(savedir,name),os.path.join(savedir,name2))
