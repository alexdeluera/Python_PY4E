# 7.2 Write a program that prompts for a file name, then opens that file and reads 
# through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below. Do 
# not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when 
# you are testing below enter mbox-short.txt as the file name.

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

print("Average spam confidence: ", average)

