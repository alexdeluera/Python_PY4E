# 10.2 Write a program to read through the mbox-short.txt and figure out 
# the distribution by hour of the day for each of the messages. You can 
# pull the hour out from the 'From ' line by finding the time and then 
# splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below.

fname=input('Please input the file name:')
if len(fname)<1:
    fname='mbox_short.txt'
fhandle=open(fname)

time=[]
revtime=[]
count=0
hourcount=dict()
for line in fhandle:
    if not line.startswith('From '):
        continue
    line=line.rstrip()
    length=len(line)
    colon=line.find(':')
    hour=line[colon-2:colon]
    time.append(hour)

for hour in time:
    hourcount[hour]=hourcount.get(hour,0)+1

for hour,count in hourcount.items():
    revtime.append((hour,count))

revtime.sort()
for hour,count in revtime:
    print(hour,count)
