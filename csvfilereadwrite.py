'''import csv
with open('/home/surasys/Desktop/pythonsamples/testdata.txt', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print row
		print ', '.join(row)'''
		
		
import csv
with open('/home/surasys/Desktop/pythonsamples/testdata.txt', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        print row