#!/usr/bin/env python

from operator import itemgetter
import sys

ETR=[]
# input comes from STDIN
for line in sys.stdin:
	if 'ETR (W/m^2)' in line:
		continue
	fields = line.split(',')
	date = fields[0]
	etr = fields[4]
	ETR.append(int(etr))


def split_seq(seq, size):
	newseq = []
	splitsize = 1.0/size*len(seq)
	for i in range(size):
		newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
	return newseq

num_lines = sum(1 for line in open('solardata.csv'))	
denominatorofAverage = num_lines -1
print denominatorofAverage

oneday = denominatorofAverage / 24
a=split_seq(ETR,oneday)

print reduce(lambda x, y: x + y, ETR) / len(ETR)



# to find sum of each group into ETR list
i=0
for each in a:
	while i<=oneday:	
		print "Average of day %s = " %(i+1) + str(sum(a[i]) / len(a[i]))
		i+=1
































   


	
