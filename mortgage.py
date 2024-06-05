# mortgage.py
#

principal = 500000
rate = 0.05 
monPayment = 2684.11 
totalPay = 0


while principal > 0: 
    principal = principal + (principal * (rate/12)) - monPayment
    totalPay = totalPay + monPayment 

print ('Total payment made:',totalPay)

# Exercise 1.7
