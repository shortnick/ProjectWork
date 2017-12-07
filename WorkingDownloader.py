# needs youtube-dl: https://github.com/rg3/youtube-dl
#and ffmpeg: http://ffmpeg.zeranoe.com/builds/
#add both to system path after installation

from __future__ import unicode_literals
import os
import youtube_dl
import time

#working dir here
os.chdir("C:\\Users\\user\\Music")

# set/create destination directory, update to current working directory command
savedir = "C:\\Users\\user\\Music\\xxxxxxxxx"
if not os.path.exists(savedir):
    os.makedirs(savedir)
    print("Directory created. Please move url list text file into this directory and re run.")
else: 
    os.chdir(savedir)

#text file (with .txt) that has urls in it. format: plain urls (http://...), 
#one per line. playlist url also allowed
#make sure it's located in the savedir
listfile= "playlisttest.txt"

#opens listfile from the savedir. 
bob = os.path.join(savedir, listfile)
with open(bob, "r") as ins:
    to_get = []
    for line in ins:
        to_get.append(line)
        
#makes folder out of listfile, then changes working directory to that one
newfolder=listfile[0:-4]+str(time.time())
outfolder = os.path.join(savedir,newfolder)
os.mkdir(outfolder)
os.chdir(outfolder)

# spell out YouTube downloader options
options = {
    # fill in first two, if your playlist is private    
    #'username':''
    #'password':''
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3 
    'output': "unicode(%(title)s)",        # name the file the title of the video
    'write-description': True,  #? include as metadata?
    'noplaylist' : False,        # only download single song, not playlist
    'add-metadata' : True,      #write metadata in, too. maybe just technical?
    'postprocessors': [{        #takes the downloaded info, exports in this format
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
                }],
    'sleep-interval': '5'       #youtube-dl's native timing 'tween downloads
    }       
    
failed = []


# uses to_get list/options to download youtube videos as mp3s
for line in to_get:
    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            ydl.download([line])
        except: 
            failed.append(line)

print("writing finished")

if len(failed) > 0:
    with open((listfile[0:-4]+"FailureLog.txt"), "w+") as fileout:
        for x in failed:
            fileout.write(x + "\n")
            fileout.close()
print("fail list done")

# rename function, remove last 12 char of file name, loses the YT designator
for name in os.listdir(outfolder):
    if os.path.splitext(name)[1] ==".mp3":
        name1 = os.path.splitext(name)[0][0:-12]+".mp3"
        os.rename(os.path.join(outfolder,name),os.path.join(outfolder,name1))
print("renaming complete")


