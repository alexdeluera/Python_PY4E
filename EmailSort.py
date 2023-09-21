fname=input("Please input the file name: ")
#fname="mbox_short.txt"
fhand=open(fname)
emails=[]
count=0

for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    count=count+1
    line=line.split()
    email=line[1]
    emails.append(email)

for email in emails:
    print(email)

print('There were',count,'lines in the file with From as the first word')