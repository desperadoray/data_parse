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

# ipath = input("Please enter input path:")
# opath = input("Please enter output path:")

newrows.append(['PID','Area code', 'Area description', 'Jur code', 'Jur description', 'roll number', 'neigh number', 'unit number', 'street number', 'street name','city name','province name','postal code', 'legal description','primary actual use code', 'primary actual use description', 'pred manual class code', 'pred manual class description', 'land unit', 'land size', 'land depth', 'land frontage','zoning','big improvement year','year built'])

with open(r'/Users/ray/coding/hausway/database/Vanpropertlist.csv', 'r', encoding = 'utf-8') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = ',')
	for row in spamreader:
		newrow = []
		if(bool(re.search(r'-', row[1]))):
			newrow.append(row[1])
			for i in range(6):
				newrow.append('')		
			newrow.append(row[5])
			newrow.append(row[4])
			newrow.append(row[7])
			newrow.append(row[6])
			newrow.append(row[9])
			newrow.append(row[8])
			newrow.append(row[10])
			newrow.append('')
			newrow.append(row[13])
			newrow.append('')
			newrow.append('')
			newrow.append('')
			newrow.append('')
			newrow.append('')
			newrow.append('')
			newrow.append(row[14])
			newrow.append(row[19])
			newrow.append(row[20])
			newrows.append(newrow)
		

#del newrows[1]

with open(r'/users/ray/coding/profile.csv', 'a', newline = '') as f:
	writer = csv.writer(f)
	writer.writerows(newrows)

print("Success!")
