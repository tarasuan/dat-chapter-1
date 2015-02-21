import csv
import operator

lines = csv.reader(open('/Users/tarasuan/Desktop/rock.csv'))

# lines.next()

# get the number of entries with 1981 as release year
# there are 2 dupes, not sure how to get rid of them.
counter = 0
newlist = ()

for line in lines:
  if line[2] == "1981":
    counter += 1
  newlist += (line[0],line[6])

print counter

#w what happened to the header row?
# why does this only work for 0 ??
sortnew = sorted(newlist,key=operator.itemgetter(0),reverse=True)


# sort the list by playcount (6), print the top 10 rows
# major problems with this. Can't figure out how to sort lines.

#sortedlines = sorted(lines,key=operator.itemgetter(6),reverse=True)
#print sortedlines


# lambda x: 

#print (line[1],line[6])

#inlines = lines.next()
#lineindex = inlines.index('PlayCount')
#sortedlines = sorted(inlines,key=operator.itemgetter(lineindex))
#outfile = open('playcount.csv', 'wb')
#outfile.writerow(inlines)

#for row in sortedlines:
  #outfile.writerow(row)

#outfile.close()

#play_count_lambda = sorted(lines,key=lambda x:float(x[6]))

#for row in play_count_lambda:
  #print(row[0],row[6])

#for row in play_count_itemgetter:
  #print(row[0],row[6])