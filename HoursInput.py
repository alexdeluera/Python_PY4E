# 2.3 Write a program to prompt the user for hours and rate per hour using 
# input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to 
# test the program (the pay should be 96.25).

hours=input('How many hours have you worked? ')
hours=int(hours)
rate=input('What is your hourly rate? ')
rate=int(rate)
pay=(hours*rate)
inputhours='Entered Hours: '+ str(hours)
inputrate='Entered Rate: '+ str(rate)
outputpay='Calculated Pay: '+ str(pay)
InputTable=[inputhours,inputrate,outputpay]
for item in InputTable:
    print(item)
