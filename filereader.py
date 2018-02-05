import sys


with open("/home/surasys/Desktop/pythonsamples/testdata.txt", "r") as ins:
	array = []
	for line in ins:
		print line
		array=line.split(',')
		for i in range(len(array)):
			print array[i]
		#~ array.append(line)
		print len(array)