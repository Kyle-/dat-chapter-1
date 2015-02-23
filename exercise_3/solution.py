#Using the csv library (https://docs.python.org/2/library/csv.html), 
#read in this data on classic rock songs and answer the following 2 questions:

#How many songs were released in 1981?
#What are the top 20 songs by playcount? (Hint: use the built-in sorted() function, 
#documentation here: https://wiki.python.org/moin/HowTo/Sorting)

import csv
import operator

num_of_1981 = 0

with open('rock.csv','r') as csvfile:
	readcsv = csv.reader(csvfile, delimiter=',')

	for row in readcsv:
			if row[2] == '1981':
				num_of_1981 = num_of_1981 + 1


	print "Number of records in 1981 is %d! " % num_of_1981


	# I can't figure out sorting to determine "top 20 songs by playcount"	
	#sort = sorted(readcsv, key=operator.itemgetter(6)	

	#print sort

csvfile.close()