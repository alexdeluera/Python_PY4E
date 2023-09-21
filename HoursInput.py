hours=input('How many hours have you worked? ')
hours=int(hours)
rate=input('What is your hourly rate? ')
rate=int(rate)
pay=(hours*rate)
inputhours='Entered Hours: '+str(hours)
inputrate='Entered Rate: '+str(rate)
outputpay='Calculated Pay: '+str(pay)
InputTable=[inputhours,inputrate,outputpay]
for item in InputTable:
    print(item)