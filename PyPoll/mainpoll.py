
import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

Kh=0 
Co=0
Li=0
Ot=0
winner= 0
row_count=0


with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	for row in csvreader:
		if row[2] == "Khan":
			Kh= Kh + 1
		elif row[2] == "Correy":
			Co+=1
		elif row[2] == "Li":
			Li+=1
		else:
			Ot+=1
		
		row_count +=1

#Group the four sums together
	cand = [Kh, Co, Li, Ot]

	for x in cand:
		if x>winner:
			winner=x

	if winner == Kh:
		winwin="Winner: Khan"
	elif winner == Co:
		winwin="Winner: Correy"
	elif winner == Li:
		winwin="Winner: Li"
	else:
		winwin="O'Tooley"
#print(winwin)
total = sum(cand)
perkh = "{:.3%}".format(Kh / total)
perCo = "{:.3%}".format(Co / total)
perLi = "{:.3%}".format(Li / total)
perOt = "{:.3%}".format(Ot / total)

#print(perkh)
#print(total)
print("Election Results")
print("-"*20)
print(f"Total Votes: {row_count}")
print("-"*20)
print(f"Khan: {perkh}({Kh})")
print(f"Correy: {perCo}({Co})")
print(f"Li: {perLi}({Li})")
print(f"O'Toolet: {perOt}({Ot})")
print("-"*20)
print(winwin)
print("-"*20)

one = "Election Results"
two="-"*20
three=f"Total Votes: {row_count}"
four="-"*20
five=f"Khan: {perkh}({Kh})"
six=f"Correy: {perCo}({Co})"
seven=f"Li: {perLi}({Li})"
eight=f"O'Toolet: {perOt}({Ot})"
nine="-"*20
ten = winwin
eleven="-"*20

out = open("final.txt", "w")
out.write(one+'\n')
out.write(two+'\n')
out.write(three+'\n')
out.write(four+'\n')
out.write(five+'\n')
out.write(six+'\n')
out.write(seven+'\n')
out.write(eight+'\n')
out.write(nine+'\n')
out.write(winwin+'\n')
out.write(eleven+'\n')

out.close









