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

with open(r'/Users/ray/coding/hausway/database/bca_raw_data/rui/feb_2017/monthly sales report6.csv', 'r', encoding = 'utf-16') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = '\t')
	for row in spamreader:
		newrow = []
		if(bool(re.search(r'-', row[10]))):
			newrow.append(row[10])
			for i in range(6):
				newrow.append(row[i])		
			r = re.search(r'^UNIT\s([0-9]+)\s([0-9]+)', row[7])
			if(bool(r)):
				unitNumber = r.group(1)
				streetNumber = r.group(2)
				newrow.append(unitNumber)
				newrow.append(streetNumber)
				# print(row[7], unitNumber, streetNumber)
			else:
				newrow.append('')
				r2 = re.search(r'([0-9]+)\s', row[7])
				if(bool(r2)):
					newrow.append(r2.group(1))
				else:
					newrow.append('')
			newrow.append(row[8])
			newrow.append('')
			newrow.append('BC')
			newrow.append('')
			newrow.append(row[9])
			for i in range(4):
				newrow.append(row[i+11])
			newrow.append(row[18])
			if(row[18] == "Width * Depth"):
				newrow.append(float(row[19])*float(row[20]))
				newrow.append(row[20])
				newrow.append(row[19])
			else:
				newrow.append(row[19])
				newrow.append(row[20])
				newrow.append('')
			newrow.append('')
			newrow.append('')
			newrow.append('')
			newrows.append(newrow)

del newrows[1]

with open(r'/users/ray/coding/profile.csv', 'a', newline = '') as f:
	writer = csv.writer(f)
	writer.writerows(newrows)

print("Success!")
