balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalPaid = 0

for i in range(1,13):
    monthlyPaid = monthlyPaymentRate * balance
    totalPaid += monthlyPaid
    balance = balance - monthlyPaid
    balance = balance + (annualInterestRate / 12.00) * balance
    
    print "Month: " + str(i)
    print "Minimum monthly payment: " + str(round(monthlyPaid, 2))
    print "Remaining balance: " + str(round(balance, 2))

print ""
print "Total paid: " + str(round(totalPaid, 2))
print "Remaining balance: " + str(round(balance, 2))