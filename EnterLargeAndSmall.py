# 5.2 Write a program that repeatedly prompts a user for integer 
# numbers until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. If the user 
# enters anything other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number. Enter 7, 2, 
# bob, 10, and 4 and match the autograder.

largest=None
smallest=None
sval=[]
while True:
    sval=input("Enter a number: ")
    if sval == "done":
        break
    try: 
        fval=float(sval)
    except:
        print("Please enter an integer")
    if largest is None or fval>largest:
        largest=fval
    if smallest is None or fval<smallest:
        smallest=fval
print("Maximum is:", int(largest))
print("Minimum is:", int(smallest))
