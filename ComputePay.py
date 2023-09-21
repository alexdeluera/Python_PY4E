def computepay(hours, rate):
    if hours>40:
        pay=((40*rate)+((hours-40)*(rate*1.5)))
    pay=(hours*rate)
    return pay

h=input("Enter hours:")
h=float(h)
r=input("Enter rate:")
r=float(r)
payout = computepay(h, r)
print("Pay", payout)