text = "X-DSPAM-Confidence:    0.8475"
length = len(text)
spacegap=text.find(":")
numfind=text[spacegap+1:(length)]
numfind=numfind.strip()
numfind=float(numfind)
print(numfind)