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

with open(ipath, 'r', encoding = 'utf-16') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = '\t')
	for row in spamreader:
		newrow = row
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
		if(row[18] == "Width * Depth"):
			size = float(row[19])*float(row[20])
			newrow[19] = size
			newrow[20] = ''
			newrow[18] = 'Square Feet'
		if(row[18] == "Square Feet"):
			row[20] = ''
		# newrow.append()
		newrows.append(row)


with open(opath, 'a', newline = '') as f:
	writer = csv.writer(f)
	writer.writerows(newrows)

print("Success!")
