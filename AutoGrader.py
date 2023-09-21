given=input("Please enter score: ")

try:
    given=float(given)
except:
    given=-1

if 1>=given>=0.9:
    print("A")
elif 0.9>given>=0.8:
    print("B")
elif 0.8>given>=0.7:
    print("C")
elif 0.7>given>=0.6:
    print("D")
elif 0<given<0.6:
    print("F")
elif given<0:
    print("Please input score, formatted as a numerical value between 0 and 1!")
else:
    print("Number is too large, input must be between 0 and 1!")
