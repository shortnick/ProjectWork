#!python3

#testing datetime work
import datetime as dt


daysDict = dict({0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'})
formFill = {
		'name': 'Jake',
		'day_worked':'Thursday',
		'last_week':True,
		'job_num':'1234567',
		'job_desc':'bob',
		'job_hours':'9'
	}

today=dt.datetime.today()

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

#print(dayLastWeek(today, "Wednesday"))
#dateHandler(today, formFill['last_week'],formFill['day_worked'])
#print(dayofHandler(today, False, "Saturday"))	 	
print(dateHandler(today, False, "Monday"))