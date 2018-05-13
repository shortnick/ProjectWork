#!python3

import panadas as pd 
from pandas import DataFrame

inputFile = pd.read_csv("directory\\subdir\\file.csv")

df = DataFrame(read_clients,columns=['colName', 'colName2', 'etc'])

df = df.drop('column_name', 1)#deletes a column
df = df.drop('row_name', 0)#deletes a row
df.drop('column_name', axis=1, inplace=True)#don't have to assign new variable this way

#to change output directory, drop a dir string in front of 'test.xlsx'
writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

