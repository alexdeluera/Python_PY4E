hrs=input("Enter Hours:")
h=float(hrs)
rate=input("Enter rate of pay:")
r=float(rate)
pay=0

if h<40:
    pay=h*r
else:
    remain=h-40
    pay=(remain*r*1.5)+(40*r)
print("Pay is",pay)
print("Done")