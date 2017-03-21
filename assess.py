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
newrows.append(['PID', 'Land Actual Value', 'Improvement Actual Value', 'Total Actual Value', 'Tax Year', 'Property Tax', 'Currency'])
with open(r'/Users/ray/coding/hausway/database/bca_raw_data/rui/jan_2017/monthly sales report6.csv', 'r', encoding = 'utf-16') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = '\t')
	for row in spamreader:
		newrow = []
		if(bool(re.search(r'-', row[10]))):
			newrow.append(row[10])
			newrow.append(row[15])
			newrow.append(row[16])
			newrow.append(row[17])
			newrow.append('2017')
			newrow.append('')
			newrow.append('CAD')
			newrows.append(newrow)
del newrows[1]

with open(r'/users/ray/coding/assessment.csv', 'a', newline = '') as f:
	writer = csv.writer(f)
	writer.writerows(newrows)

print("Success!")
