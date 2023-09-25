# 8.4 Open the file romeo.txt and read it line by line. For each line, 
# split the line into a list of words using the split() method. The program 
# should build a list of words. For each word on each line check to see if 
# the word is already in the list and if not append it to the list. When the 
# program completes, sort and print the resulting words in python sort() 
# order as shown in the desired output.

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
