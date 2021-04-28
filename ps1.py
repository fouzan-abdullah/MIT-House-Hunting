# house hunting: determine how long it will take you to save enough money to make the down payment

annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter portion of your salary saved as a decimal:'))
total_cost = float(input('Enter total_cost of your dream home:'))

current_savings = 0.0
monthly_savings = (annual_salary / 12) * portion_saved
r = 0.04
investment_rate = current_savings * (r / 12)  # monthly investment rate
portion_down_payment = 0.25 * total_cost
num = 0
print(num)
while current_savings < portion_down_payment:
    investment_rate = current_savings * (r / 12)
    current_savings = current_savings + monthly_savings + investment_rate
    num += 1

print(num)
print(investment_rate)
print(current_savings)
print(portion_down_payment)
