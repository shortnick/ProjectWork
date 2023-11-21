#!python3

import pandas as pd 
from pandas import DataFrame
import numpy as np
import csv


inFile = pd.read_csv('C:\\Users\\user\\Downloads\\050718.DAT',sep='|', )

df=DataFrame(inFile,columns = ['c0', 'ADR', 'DATA','MEASURE','c4','ELEV'],dtype='object')
#dtype={'c0':'object', 'ADR':'object', 'DATA':'object','MEASURE':'object','c4':'object','ELEV':'object'}


"""
with open('C:\\Users\\user\\Downloads\\050718.DAT') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='|')
	for row in spamreader:
		for (a, b, c, d, e, f) in row:
			df=df.append({a, b, c, d, e, f})
"""
#tempDF = pd.DataFrame.append(rows)
#InfoDF = pd.concat([basicDF,tempDF])

#df=df.apply() , df['Employees'].apply(lambda x:float(x))


df = df.drop('c0', 1)#deletes a column
df = df.drop('c4', 1)#deletes a column
#df = df.drop('row_name', 0)#deletes a row
#df.drop('column_nam

"""
df["ADR"] = df["ADR"].astype(np.dtype(object))
df["DATA"] = df["DATA"].astype('object')
df["MEASURE"] = df["MEASURE"].astype('object')
df["ELEV"] = df["ELEV"].astype('object'
	)
	"""
print(df.ADR)
#print(df.MEASURE)



#to change output directory, drop a dir string in front of 'test.xlsx'
#writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

#df.to_excel(writer, sheet_name='Sheet1')

