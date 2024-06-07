# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
paymentE = 3684.11
check = 0
total_paid = 0.0

while principal > 0:
    
    if check != 13:
        principal = principal * (1+rate/12) - paymentE
        total_paid = total_paid + paymentE
        check = check + 1 
    else: 
        
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid', total_paid)