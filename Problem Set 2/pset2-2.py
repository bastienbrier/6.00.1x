balance = 5000
annualInterestRate = 0.2

temp = 1
lowestPaid = 0

while temp > 0:
    lowestPaid += 10
    temp = balance
    
    for i in range(1, 13):
        temp = (temp - lowestPaid) + (annualInterestRate / 12.00) * (temp - lowestPaid)

print "Lowest Payment: " + str(lowestPaid)