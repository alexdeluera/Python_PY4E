# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the 
# score is out of range, print an error. If the score is between 0.0 and 
# 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and 
# exit. For the test, enter a score of 0.85.

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
