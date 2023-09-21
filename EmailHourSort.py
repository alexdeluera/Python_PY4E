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
