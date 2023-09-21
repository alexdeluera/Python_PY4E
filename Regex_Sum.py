#The basic outline of this problem is to read the file, look for integers 
#using the re.findall(), looking for a regular expression of '[0-9]+' and
#then converting the extracted strings to integers and summing up the integers.

#fname=input("Please input the file name:")
import re

fname=("regex_sum_final.txt")
fhand=open(fname)
numset=[]

for line in fhand:
    for item in re.findall('[0-9]+',line.rstrip()):
        numset.append(int(item))
print(sum(numset))
