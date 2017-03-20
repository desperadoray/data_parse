import csv
import sys
import re

maxInt = sys.maxsize
decrement = True
newrows = []

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

ipath = input("Please enter input path:")
opath = input("Please enter output path:")

newrows.append(['PID', 'unit number', 'street number', 'street name', 'land size', 'land unit', 'land value', 'improve value', 'total actual value'])

with open(ipath, 'r', encoding = 'utf-16') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = '\t')
	for row in spamreader:
		newrow = []
		newrow.append(row[10])
		r = re.search(r'^UNIT\s([0-9]+)\s([0-9]+)', row[7])
		if(bool(r)):
			unitNumber = r.group(1)
			streetNumber = r.group(2)
			newrow.append(unitNumber)
			newrow.append(streetNumber)
			# print(row[7], unitNumber, streetNumber)
		else:
			newrow.append('')
			newrow.append('')
		newrow.append(row[8])
		if(row[18] == "Width * Depth"):
			newrow.append(row[19])
			newrow.append('Squarefeet')
		else:
			newrow.append(row[19])
			newrow.append(row[18])
		# newrow.append()
		newrow.append(row[15])
		newrow.append(row[16])
		newrow.append(row[17])
		newrows.append(newrow)


with open(opath, 'a', newline = '') as f:
	writer = csv.writer(f)
	writer.writerows(newrows)

print("Success!")
