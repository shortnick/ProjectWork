#! python3
# -*- coding: utf-8 -*-


# !!! Gotta fix the time crunch

"""
Field Report Generator
May 5: functions in basic mode, checks content/quality of job number-hours worked-name and last week.vs.today when OK clicked, 		exports as JSON
May 27: timedate handling added, but needs to account for Today and Yesterday in the logic
Oct 4: added a character stripper to job number (catches anything non numeral), still need Today/Yesterday, but timedate does have the ordinal day of the week as a simple output. Should be able to chain that straight into the dictionary lookup, no?

To Do
- add list field, scroll bar, button for multijob entry
- add system clock connection and logic to check for today vs. end of week
- add pane for Daily Report
- add pane for Expenses
"""
#answers most of the basics, plus accessing Explorer/files and making tabs inside program window
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/

#list of tkinter objects
#https://www.tutorialspoint.com/python/python_gui_programming.htm


import tkinter as TK
from tkinter import messagebox
from tkinter.ttk import Combobox
import json
from pprint import pprint
import datetime as dt
import re 


daysDict = dict({0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'})
formFill = {}
outGoingJson = str()
warnContents= []


today=dt.datetime.today()
print(today.timetuple(), dt.datetime.today().weekday())


def checkForm(): 
	global formFill
	"""
	Generates a json from 
	"""
	formFill = {
		'name': str(worker.get()),
		'day_worked':str(dayChoice.get()),
		'last_week':LastWeek.get(),
		'job_num':numberFilter(entry_text1.get()),
		'job_desc':entry_text2.get(),
		'job_hours':entry_text3.get()
	}

def makeJson():
	return json.dumps(formFill)

def numberFilter(userSequence):
	notNumber=re.compile(r'\D')
	result=notNumber.findall(userSequence)
	for x in result:
		userSequence=userSequence.replace(x, "")
	return userSequence
	

def nextSaturday(todayVar, weekBool):
	# checks difference between given day of week (in x = datetime.datetime.today() object) and the next Saturday, returns datetime obj of Saturday. takes a timedate obj from the today variable and a last_week boolean
	inputDay=todayVar.timetuple()[6]

	if weekBool==True:
		todayVar=todayVar-dt.timedelta(days=7)
		inputDay=todayVar.timetuple()[6]
	
	if inputDay<5:
		return todayVar+dt.timedelta(days=(5-inputDay))
	elif inputDay==5:
		return todayVar
	else:
		return todayVar+dt.timedelta(days=6)

def dayLastWeek(todayVar, workDay):
	# takes date object of today (x) and the str value of a day from daysDict (d),  and returns the timedate obj of d last week(e.g. if d is Tuesday/1, returns date from last Tuesday)
	
	#inputDay is ordinal day of week for today
	inputDay=int(todayVar.timetuple()[6])
	#workedDay is ordinal day last week of the day worked
	workedDay=int(list(daysDict.keys())[list(daysDict.values()).index(workDay)])
	#number of days to roll back the date
	dayDelta=inputDay+(7-workedDay)
	
	#returns timedate obj of the day worked lastweek
	return todayVar-dt.timedelta(days=dayDelta)

def dayofHandler(todayVar, weekBool, formFillDay):
	if weekBool==False:
		todayDay=todayVar.timetuple()[6]
	
		if formFillDay=="Today":
			checkDay=today.weekday()
		else:
			checkDay=int(list(daysDict.keys())[list(daysDict.values()).index(formFillDay)])

		
		if checkDay==todayDay:
			return todayVar
		elif checkDay<todayDay:
			dayDelta= todayDay-checkDay
			return(todayVar-dt.timedelta(days=dayDelta))
		else: 
			return(todayVar+dt.timedelta(days=checkDay))
	else:
		dayLastWeek(todayVar, formFillDay)



def dateHandler(todayVar, weekBool, formFillDay):
	#takes 'today' timedate obj, checks current date and 'day worked' inputs, should return date of day worked and following Saturday
	# needs difference between that day and today- dayLastWeek(today)
	outSaturday=nextSaturday(today, weekBool)
	
	if weekBool==True:
		return "day ", dayLastWeek(today, formFillDay), "sat", outSaturday

	else: 
		return dayofHandler(todayVar, weekBool, formFillDay), outSaturday
		print("dateHandler today")


def inputInfoCheck():
	#check data to make sure there's at least a person, a job number and hours, and it's not Today/last week
	#this checks this checks the formFill[] dict and then adds warning messages to the warnContents list
	global warnContents
	warnContents=[]

	if len(formFill['job_num'])<7 or len(formFill['job_num'])>7 or formFill['job_num'].isdigit()==False:
		warnContents.append('Job number seems wrong')
	if formFill['job_hours'].isdigit()==False or len(formFill['job_hours'])<1:
		warnContents.append("Job hours seem wrong")
	if formFill['job_hours'].isdigit()==True and int(formFill['job_hours'])>16:
		warnContents.append("Please enter this many hours directly onto the timesheet.")
	if formFill['name']=='Your Name':
		warnContents.append("What's your name?")
	if (formFill['last_week']==True) and (formFill['day_worked']=="Today"):
		warnContents.append("Please select day worked last week")
	if (formFill['day_worked']=="Today" and today.timetuple()[6]==6) or (formFill['day_worked']=="Sunday"):
		warnContents.append("Please enter Sunday hours directly onto the timesheet.")


	

def okButton():
	global outGoingJson
	global formFill
	
	checkForm()
	dateHandler(today, formFill['last_week'],formFill['day_worked'])
	inputInfoCheck()
	
	if len(warnContents) >0:
		info=""
		for item in warnContents:
			info= info+("- "+item+" \n")
		messagebox.showinfo('Message title', info)
	else:
		#stores form data as json under outGoingJson
		outGoingJson = makeJson()
		pprint(outGoingJson)


#basic building block
window=TK.Tk()
window.wm_title("Daily Report")
window.geometry('600x250')

LastWeek=TK.BooleanVar()


# Labels are displayed (can be paired with Entry)
l1=TK.Label(window, height=1, width=20, text="Your Name")
l1.grid(row=0, column=0)
#l1.pack() will also do location, but more default-y behaviors, see http://effbot.org/tkinterbook/pack.htm

l2=TK.Label(window, height=1, width=20, text="Day Worked")
l2.grid(row=0, column=1)


l4=TK.Label(window, height=1, width=20, text="Job #")
l4.grid(row=2, column=0)

l5=TK.Label(window, height=1, width=20, text="Job Name")
l5.grid(row=2, column=1)

l6=TK.Label(window, height=1, width=10, text="Hours")
l6.grid(row=2, column=2)

#Combobox dropdowns
worker = Combobox(window)
worker['values']= ("Your Name", "Jake", "Nick", "Jim", "Robert")
worker.current(0) #set the selected item
worker.grid(column=0, row=1)

dayChoice = Combobox(window)
dayChoice['values']= ("Today", "Yesterday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
dayChoice.current(0) #set the selected item
dayChoice.grid(column=1, row=1)

weekCheckBox=TK.Checkbutton(text= "Last week?", variable=LastWeek, onvalue=True, offvalue= False, height=1, width = 20)
weekCheckBox.grid(row=1, column=2)
#needs class and __init__? - see: http://zetcode.com/gui/tkinter/widgets/


#Entry makes your standard text box
entry_text1=TK.StringVar()
f1=TK.Entry(window, textvariable=entry_text1, width=20)
#note the named StringVar() that it's linked to
f1.grid(row=3, column=0)

entry_text2=TK.StringVar()
f2=TK.Entry(window, textvariable=entry_text2, width=20)
#note the named StringVar() that it's linked to
f2.grid(row=3, column=1)

entry_text3=TK.StringVar()
f3=TK.Entry(window, textvariable=entry_text3, width=20)
#note the named StringVar() that it's linked to
f3.grid(row=3, column=2)



#Buttons
b1=TK.Button(window, text="OK", width=10, command=okButton)
b1.grid(row=4, column=2)






def get_selected_row(event):
	#make this var available outside function
	global selected_tuple
	#this selector returns a tuple with one item, so we just select that with var-index
	index=listing.curselection()[0]
	selected_tuple=listing.get(index)

	#these clear the field for the Entry and then populate it 
	f1.delete(0,END)
	f1.insert(END, selected_tuple[1])


#runs the program window
window.mainloop()