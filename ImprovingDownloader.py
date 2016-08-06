# needs youtube-dl: https://github.com/rg3/youtube-dl
#and ffmpeg: http://ffmpeg.zeranoe.com/builds/
#add both to system path after installation

from __future__ import unicode_literals
import os
import youtube_dl
from subprocess import call
import time 

# TO DO:
# CCCCXXXXline 39- if folder DOESNT exist, make it
# replace time.time() -at same-point- with something better
# added youtube-naming switch, but gotta fix naming options map for soundcloud
# refactor into functions(), universalize the options for diff websites by passing in a tag
# make the audio/ffmpeg normalization work
# wrap whole thing for command line: take input list and destination folder

#working dir here
#os.chdir("C:\\Users\\user\\Music")
workDir = "..."
listFile = "..."
incoming = []
siteSelector = "..."
options = "..."
failed = []

#pass in saveList as a bare variable name referring to the .txt of same name
def setFileLocations(saveList):
    '''takes saveList, sets current working directory, sets listFile as saveList.txt, incoming is list of lines from listFile, creates or moves to saveList directory, makes specific folder for this download within, and moves working directory there'''
    global listFile
    #set working directory
    workDir = os.getcwd()
    
    listFile = str(saveList+".txt")
    #text file (with .txt) that has urls in it. format: plain urls (http://...), 
    #one per line. playlist url also allowed
    #--deprecate?:make sure it's located in the saveList dir
    
    #ingest the .txt file, line by line
    with open(listFile, "r") as ins:
        for line in ins:
            incoming.append(line)

    #make sure there's a directory specifically for the list of files to download
    if not os.path.exists(saveList):
        os.mkdir(saveList)
        print("Directory created.")
    else: 
        os.chdir(saveList)
'''
    #make/change to a folder for this specific download
    outfolder = os.path.join(listFile[0:-4],str(time.time()))
    os.mkdir(outfolder)
    os.chdir(outfolder)
'''

def siteSelectorSwitch():
    '''Reads first line of listFile.txt, selects proper website as tag'''
    global siteSelector
    if incoming[0].find("youtube", 0, 22) > -1:
        siteSelector = "youtube"
    elif incoming[0].find("soundcloud", 0, 22) > -1:
        siteSelector = "soundcloud"
    elif incoming[0].find("spotify", 0, 22) > -1:
        siteSelector = "spotify"
    else:
        print(incoming[0])





def optionSelector():
    global options
    if siteSelector == 'youtube':
        options = {
            'format': 'bestaudio/best', # choice of quality
            'extractaudio' : True,      # only keep the audio
            'audioformat' : "mp3",      # convert to mp3 
            'output': "unicode(%(title)s)",        # name the file the title of the video
            'write-description': True,  #? include as metadata?
            'noplaylist' : False,        # only download single song, not playlist
            'add-metadata' : True,      #write metadata in, too. maybe just technical?
            #'exec':"ffmpeg -af {} dynaudnorm {}",    
            'postprocessors': [{        #takes the downloaded info, exports in this format
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
                
                        }],
            'sleep-interval': '5'
            
            } 
    elif siteSelector == 'soundcloud':
        options = {
            'format': 'bestaudio/best', # choice of quality
            'extractaudio' : True,      # only keep the audio
            'audioformat' : "mp3",      # convert to mp3 
            'output': "unicode(%(title)s)",        # name the file the title of the video
            'write-description': True,  #? include as metadata?
            'noplaylist' : False,        # only download single song, not playlist
            'add-metadata' : True,      #write metadata in, too. maybe just technical?
            #'exec':"ffmpeg -af {} dynaudnorm {}",    
            'postprocessors': [{        #takes the downloaded info, exports in this format
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
                
                        }],
            'sleep-interval': '5'
            }
    elif siteSelector == 'spotify':
        options = {} 
    else:
        print("siteSelector error")

#   need to map the following command into the above lambda
#ffmpeg -i "Wolfmother - Woman.mp3" -af dynaudnorm newwolfy.mp3   
#--postprocessor-args ARGS        Give these arguments to the postprocessor
# --exec CMD    Execute a command on the file after downloading, similar to find's -exec syntax. 
#Example: --exec 'adb push {} /sdcard/Music/ && rm {}' see post-processor section of docs


# uses saveList/options to download youtube videos as mp3s
def downloader():
    for lineItem in incoming:
        with youtube_dl.YoutubeDL(options) as ydl:
            try:
                print(options)
                ydl.download([lineItem])
            except: 
                failed.append(lineItem)

    print("writing finished")


def failtextout():
    '''writes failed[] as a text file, unless failed[] is empty. '''
    if len(failed) > 0:
        with open((saveList[0:-4]+"FailureLog.txt"), "w+") as fileout:
            for x in failed:
                fileout.write(x + "\n")
                fileout.close()
    print("fail list done")
"""
# use this logic to pass args into the -exec part of options?
def filerenamer():
    '''Cleans up/removes symbols from file names'''
    if siteSelector == 'youtube':
        for name in os.listdir(outfolder):
            if os.path.splitext(name)[1] ==".mp3":
                name1 = os.path.splitext(name)[0][0:-12]+".mp3"
                os.rename(os.path.join(outfolder,name),os.path.join(outfolder,name1))
        print("renaming complete")
    elif siteSelector == 'soundcloud':
        for name in os.listdir(outfolder):
            if os.path.splitext(name)[1] ==".mp3":
                name1 = os.path.splitext(name)[0][0:-8]+".mp3"
                os.rename(os.path.join(outfolder,name),os.path.join(outfolder,name1))
        print("renaming complete")
    else:
        print("names skipped")
"""

'''
for name in os.listdir(outfolder):
    if os.path.splitext(name)[1] ==".mp3":
        me = "ffmpeg -i \""+name+"\" -af dynaudnorm \""+name+"\""
        print(me)
        call(me)
print("normalization complete")
'''
print(listFile)
print(incoming)
print(siteSelector)
print(options)
setFileLocations("playlisttest")
siteSelectorSwitch()
optionSelector()
print(listFile)
print(incoming)
print(siteSelector)
print(options)
downloader()
print("job done")