

import os
import csv

csvpath = os.path.join('Resources','budget_data23.csv')

#load data
s = 0
monthsnum = 0
empty = []
difftotal = []
diff_num = 0
monthname = []
diff = 0
maxnum = 0
minnum = 0

with open(csvpath, newline='') as csvfile:

	#CSV reader specifies delimiter and variable that holds contents
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)
	
	for row in csvreader:
		s = int(row[1]) + s
		monthsnum = 1 + monthsnum
		empty.append(row[1])
		monthname.append(row[0])
	#print(monthname)
	#print(empty)
	
	for val in range(len(empty) - 1):
		diff = int(empty[val+1]) - int(empty[val])
		difftotal.append(diff)
		diff_num = diff_num + diff
		avediff = round(diff_num / (monthsnum - 1),2)
		
		for x in range(len(difftotal)):
			if maxnum < int(difftotal[x]):
				maxnum = difftotal[x]
				max_mon = monthname[x]
			if minnum > int(difftotal[x]):
				minnum = difftotal[x]
				min_mon = monthname[x]
	
#print(str(max_mon))
print("Financial Analysis")
print("---------------------")
print("Total Months: " + str(monthsnum))
print("Total: $" + str(s))
print(f"Average Change: ${avediff}")
print(f"Great Increase in Profits: {max_mon}(${maxnum})")
print(f"Great Increase in Profits: {min_mon}(${minnum})")

#one = (str(max_mon))
two = "Financial Analysis"
three = "---------------------"
four = "Total Months: " + str(monthsnum)
five = "Total: $" + str(s)
six = "Average Change: $" + str(avediff)
seven = f"Great Increase in Profits: {max_mon}(${maxnum})"
eight = f"Great Increase in Profits: {min_mon}(${minnum})"

out = open("final.txt", "w")
#out.write(one+'\n\n')
out.write(two+'\n\n')
out.write(three+'\n\n')
out.write(four+'\n')
out.write(five+'\n')
out.write(six+'\n')
out.write(seven+'\n')
out.write(eight+'\n')
out.close
