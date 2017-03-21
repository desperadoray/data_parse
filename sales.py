import csv
import sys
import re

maxInt = sys.maxsize
decrement = True
newrows = []
datamap = {'JAN':'01','FEB':'02','MAR':'03','APR':'04','MAY':'05','JUN':'06','JUL':'07','AUG':'08','SEP':'09','OCT':'10','NOV':'11','DEC':'12'}

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
newrows.append(['PID', 'Doc Num', 'Sale Date', 'Sale Price', 'Sale Type', 'Sale Catagory', 'Sale Status', 'Multi Sale Flag'])
with open(r'/Users/ray/coding/hausway/database/bca_raw_data/rui/feb_2017/monthly sales report6.csv', 'r', encoding = 'utf-16') as csvfile:
	spamreader = csv.reader(csvfile, delimiter = '\t')
	for row in spamreader:
		newrow = []
		if(bool(re.search(r'-', row[10]))):
			if(row[21]!=''):
				newrow.append(row[10])
				newrow.append(row[21])
				dater = re.search(r'([0-9]+)([A-Z]+)([0-9]+)',row[22])
				if(bool(dater)):
					newrow.append(dater.group(3)+'/'+datamap[dater.group(2)]+'/'+dater.group(1))
				else:
					newrow.append('')
				for i in range(5):
					newrow.append(row[23+i])
				newrows.append(newrow)
				newrow = []
			if(row[28]!=''):
				newrow.append(row[10])
				newrow.append(row[28])
				dater = re.search(r'([0-9]+)([A-Z]+)([0-9]+)',row[29])
				if(bool(dater)):
					newrow.append(dater.group(3)+'/'+datamap[dater.group(2)]+'/'+dater.group(1))
				else:
					newrow.append('')
				for i in range(5):
					newrow.append(row[30+i])
				newrows.append(newrow)
				newrow = []
			if(row[35]!=''):
				newrow.append(row[10])
				newrow.append(row[35])
				dater = re.search(r'([0-9]+)([A-Z]+)([0-9]+)',row[36])
				if(bool(dater)):
					newrow.append(dater.group(3)+'/'+datamap[dater.group(2)]+'/'+dater.group(1))
				else:
					newrow.append('')
				for i in range(5):
					newrow.append(row[37+i])
				newrows.append(newrow)
				newrow = []
			
del newrows[1]

with open(r'/users/ray/coding/sales.csv', 'a', newline = '') as f:
	writer = csv.writer(f)
	writer.writerows(newrows)

print("Success!")
