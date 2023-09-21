name = input("Enter file:")
if len(name) < 1:
    name = "mbox_short.txt"
handle = open(name)
emails=[]

for line in handle:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    words=line.split()
    email=words[1]
    emails.append(email)

EmailList=dict()
for email in emails:
    EmailList[email]=EmailList.get(email,0)+1

wordcount=None
wordname=None
for email, count in EmailList.items():
    if wordcount is None or wordcount<count:
        wordcount=count
        wordname=email

print(wordname, wordcount)
#print(EmailList)