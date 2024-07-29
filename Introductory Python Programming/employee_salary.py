"""
Let's consider you are paying monthly salary to your employee with bonus for eid. Write a program
/ pseudo-code so that you can correctly calculate the salary for your employee using the following
criteria:
“Employee base salary is 5000 bdt and all employees will get it. If your employee worked overtime,
you would pay 5% extra on their base salary or if the employee sold 300 products, then he will get
10% extra on their base salary. Finally, you will add 8000bdt as bonus for Eid with the calculated
salary to have the final payable amount.
"""

def salary(amount, overtime, sellExtra, eid):
    if overtime is True:
        amount += (amount *(5/100))

    if sellExtra is True:
        amount += (amount *(10/100))

    if eid is True:
        amount += 8000

    return float(amount)


print(f"{salary(amount=5000, overtime=True, sellExtra=True, eid=True)} BDT.")
print(f"{salary(amount=5000, overtime=True, sellExtra=True, eid=False)} BDT.")
print(f"{salary(amount=5000, overtime=True, sellExtra=False, eid=True)} BDT.")
print(f"{salary(amount=5000, overtime=True, sellExtra=False, eid=False)} BDT.")
print(f"{salary(amount=5000, overtime=False, sellExtra=True, eid=True)} BDT.")
print(f"{salary(amount=5000, overtime=False, sellExtra=True, eid=False)} BDT.")
print(f"{salary(amount=5000, overtime=False, sellExtra=False, eid=True)} BDT.")
print(f"{salary(amount=5000, overtime=False, sellExtra=False, eid=False)} BDT.")
