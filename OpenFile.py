fname=input("Enter the file name:")
try:
    fhand=open(fname)
except:
    print("File type not recognized for", fname,"please try another file.")
    quit()

#fhand=open("mbox_short.txt")
count=0
nline=0
lcount=0
for line in fhand:
    line=line.rstrip()
    count = count+1
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lcount=lcount+1
    length=((len(line)))
    spacegap=(line.find(":"))
    line=line[spacegap+1:length]
    line=line.strip()
    line=float(line)
    nline=line+nline
    average=(nline/lcount)

#print(line)
#print(nline)
print(average)
#print(lcount)
#print(count)
#print("The line count is ",count)

