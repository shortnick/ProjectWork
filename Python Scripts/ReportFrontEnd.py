#! python3


"""
Field Report Generator
May 5: functions in basic mode, checks content/quality of job number-hours worked-name and last week.vs.today when OK clicked, 		exports as JSON
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


from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
import json
from pprint import pprint

formFill = {}
outGoingJson = str()
warnContents= []


def checkForm(): 
	global formFill
	formFill = {
		'name': str(worker.get()),
		'day_worked':str(dayChoice.get()),
		'last_week':LastWeek.get(),
		'job_num':entry_text1.get(),
		'job_desc':entry_text2.get(),
		'job_hours':entry_text3.get()
	}

def makeJson():
	return json.dumps(formFill)

	

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
	if (formFill['last_week']==True) and (json.loads(outGoingJson)['day_worked']=="Today"):
		warnContents.append("Please select day worked last week")


	

def okButton():
	global outGoingJson
	global formFill
	checkForm()
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
window=Tk()
window.wm_title("Daily Report")
window.geometry('600x250')

LastWeek=BooleanVar()

# Labels are displayed (can be paired with Entry)
l1=Label(window, height=1, width=20, text="Your Name")
l1.grid(row=0, column=0)
#l1.pack() will also do location, but more default-y behaviors, see http://effbot.org/tkinterbook/pack.htm

l2=Label(window, height=1, width=20, text="Day Worked")
l2.grid(row=0, column=1)


l4=Label(window, height=1, width=20, text="Job #")
l4.grid(row=2, column=0)

l5=Label(window, height=1, width=20, text="Job Name")
l5.grid(row=2, column=1)

l6=Label(window, height=1, width=10, text="Hours")
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

weekCheckBox=Checkbutton(text= "Last week?", variable=LastWeek, onvalue= True, offvalue= False, height=1, width = 20)
weekCheckBox.grid(row=1, column=2)
#needs class and __init__? - see: http://zetcode.com/gui/tkinter/widgets/


#Entry makes your standard text box
entry_text1=StringVar()
f1=Entry(window, textvariable=entry_text1, width=20)
#note the named StringVar() that it's linked to
f1.grid(row=3, column=0)

entry_text2=StringVar()
f2=Entry(window, textvariable=entry_text2, width=20)
#note the named StringVar() that it's linked to
f2.grid(row=3, column=1)

entry_text3=StringVar()
f3=Entry(window, textvariable=entry_text3, width=20)
#note the named StringVar() that it's linked to
f3.grid(row=3, column=2)



#Buttons
b1=Button(window, text="OK", width=10, command=okButton)
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