balance = 5000
annualInterestRate = 0.2

maxx = balance
for i in range(12):
    maxx = maxx + maxx * (annualInterestRate / 12.00)

lower = balance / 12.0
upper = maxx / 12.0

epsilon = 0.01
temp = balance
answer = (lower + upper) / 2

while abs(temp) > epsilon:
    answer = (lower + upper) / 2
    temp = balance
     
    for i in range(1, 13):
        temp = (temp - answer) + (annualInterestRate / 12.00) * (temp - answer)
    
    if temp > 0:
        lower = answer
    elif temp < 0:
        upper = answer

print "Lowest Payment: " + str(round(answer, 2))