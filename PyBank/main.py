

import os
import csv

csvpath = os.path.join('Resources','budget_data23.csv')

csvpath = "/Users/patriciaescalante/Desktop/GWARL201808DATA3/03-Python/Homework/Instructions/PyBank/Resources/budget_data23.csv"
print(csvpath)

#load data

with open(csvpath, newline='') as csvfile:

	#CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')

	print(csvreader)
