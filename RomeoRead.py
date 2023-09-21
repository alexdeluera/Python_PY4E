fname=input("Please enter file name:")
#fname=('romeo.txt')
fhand=open(fname)
wlist=[]
words=[]
for line in fhand:
    line=line.strip()
    word=line.split()
    words=words+word
    i=len(words)
    for i in words:
        if i not in wlist:
            wlist.append(i)
wlist.sort()
#print(words)
print(wlist)