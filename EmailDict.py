# 9.4 Write a program to read through the mbox-short.txt and figure out who 
# has sent the greatest number of mail messages. The program looks for 'From ' 
# lines and takes the second word of those lines as the person who sent the 
# mail. The program creates a Python dictionary that maps the sender's mail 
# address to a count of the number of times they appear in the file. After the 
# dictionary is produced, the program reads through the dictionary using a 
# maximum loop to find the most prolific committer.

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
