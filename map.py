#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	if 'ETR (W/m^2)' in line:
		continue
    # remove leading and trailing whitespace
   	 # split the line into words
    #words = line.split()
	#print line
	fields = line.split(',')
	date = fields[0]
	etr = fields[4]

	print date +"   "+etr
    

