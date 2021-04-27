# house hunting: determine how long it will take you to save enough money to make the down payment

annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter portion of your salary saved as a decimal:'))
total_cost = float(input('Enter total_cost of your dream home:'))

current_savings = 0.0
r = 0.04/12
portion_down_payment = 0.25 * total_cost
num = 0

while current_savings < portion_down_payment:
    r = current_savings * (1.04 / 12)
    current_savings = current_savings + ((annual_salary * portion_saved) / 12) + r
    num = num + 1

print(num)
print(current_savings)
print(r)
print(portion_down_payment)
