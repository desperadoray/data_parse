import csv
import sys
import re

maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

with open(r'D:\Coding\hausway\database\bca\2017Feb\Monthly Sales Report.csv', newline = '') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = '\t')
	for row in spamreader:
		r = re.search(r'^UNIT\s([0-9]+)\s([0-9]+)', row[7])
		if(bool(r)):
			unitNumber = r.group(1)
			streetNumber = r.group(2)
		if(row[18] == "Width * Depth"):
			size = float(row[19])*float(row[20])
