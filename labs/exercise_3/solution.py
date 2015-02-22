import csv
# tried to use itemgetter, couldn't. import operator

reader = csv.DictReader(open('/Users/tarasuan/Desktop/rock.csv'))
lines = [line for line in reader]

# there are 2 dupes, not sure how to get rid of them.
release_1981 = 0

for line in lines:
  if line['Release Year'] == '1981':
    release_1981 += 1

print release_1981

# sort on playcount
sort_playcount = sorted( lines,key = lambda line: int( line['PlayCount'] ),reverse = True )

# get top 20 and print
top_20 = sort_playcount[0:19]
print top_20