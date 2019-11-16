#!python3

import datetime
import os
import glob
import subprocess


def openSublime(filePath):
	path_sublime = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
	path_to_file = filePath
	subprocess.call([path_sublime, path_to_file])

def openExcel(filePath):
	path_sublime = 'C:\\Program Files\\ EXCEL .EXE here, probably program filex (x86)\Microsoft Office'
	path_to_file = filePath
	subprocess.call([path_sublime, path_to_file])


def openExplorer(location):
	os.startfile(os.path.realpath(location))

def openCivil3D2016():
	os.startfile("openCivil3D2016 location")

def openOutlook():
	os.startfile("Outlook location")

newest = os.path.join('N:\\Timesheets', max(glob.iglob('*'), key=os.path.getctime))
#openSublime(newest)
openExplorer("F:\\")
openExplorer("Y:\\Projects")
openOutlook()
openCivil3D2016()
print(newest)



all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
latest_subdir = max(all_subdirs, key=os.path.getmtime)

dayVar= datetime.datetime.today()
dayOfWeekVar= datetime.datetime.today().weekday()
#datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)

#print str(dayVar.timetuple()[1]),"-",str(dayVar.timetuple()[2]),"-",str(dayVar.timetuple()[0]), dayOfWeekVar
#print latest_subdir

#print(os.path.getmtime("C:\Users\user\Documents\GitHub\ProjectWork\Python Scripts"))