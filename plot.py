import numpy as np
import matplotlib.pyplot as plt

fig1 = plt.figure()
ax = fig1.add_subplot(111)

## the data
N = 5
first = [14789, 648, 109 , 0, 0]
second = [16990, 772, 135, 0, 0]
third = [14437, 775, 110, 0, 0]
fourth = [12903, 960, 230, 0, 0]
fifth = [10499, 1071, 123, 0, 0] 


## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.15                      # the width of the bars

## the bars
rects1 = ax.bar(ind, first, width,
                color='orange',
               
                error_kw=dict(elinewidth=2,ecolor='red'))

rects2 = ax.bar(ind+width, second, width,
                    color='red',
                   
                    error_kw=dict(elinewidth=2,ecolor='orange'))

rects3 = ax.bar(ind+width+width, third, width,
                    color='yellow',
                   
                    error_kw=dict(elinewidth=2,ecolor='green'))

rects4 = ax.bar(ind+width+width+width, fourth, width,
                    color='green',
                   
                    error_kw=dict(elinewidth=2,ecolor='yellow'))

rects5 = ax.bar(ind+width+width+width+width, fifth, width,
                    color='black',
                   
                    error_kw=dict(elinewidth=2,ecolor='black'))


# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,18000)
ax.set_ylabel('Number of ~ ')
ax.set_title('Austin Police Department Crime Results')
xTickMarks = ['  ~ most occured crime','    ~ crime', '    ~ occurence']
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=10)

## add a legend
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('2008', '2009', '2010', '2011', '2014') )

plt.show()
