#!python3

import pandas as pd 
from pandas import DataFrame
import csv


df = pd.DataFrame(columns = ['c0', 'ADR', 'DATA','MEASURE','c4','ELEV'], )


#dtype={'c0':'str', 'ADR':'str', 'DATA':'str','MEASURE':'str','c4':'str','ELEV':'str'}


with open('C:\\Users\\user\\Downloads\\050718.DAT') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='|')
	for row in spamreader:
		for (a, b, c, d, e, f) in row:
			df=df.append({a, b, c, d, e, f})

#tempDF = pd.DataFrame.append(rows)
#InfoDF = pd.concat([basicDF,tempDF])

#df=df.apply() , df['Employees'].apply(lambda x:float(x))


df = df.drop('c0', 1)#deletes a column
df = df.drop('c4', 1)#deletes a column
#df = df.drop('row_name', 0)#deletes a row
#df.drop('column_name', axis=1, inplace=True)#don't have to assign new variable this way

df.ADR = df.ADR.astype(str)
df.DATA = df.DATA.astype(str)
df.MEASURE = df.MEASURE.astype(str)
df.ELEV = df.ELEV.astype(str)

print(df.MEASURE)



#to change output directory, drop a dir string in front of 'test.xlsx'
#writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

#df.to_excel(writer, sheet_name='Sheet1')

