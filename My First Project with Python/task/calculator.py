# Write your code here
bubblegum_earned_amount = 202
toffee_earned_amount = 118
ice_cream_earned_amount = 2250
milk_chocolate_earned_amount = 1680
doughnut_earned_amount = 1075
pancake_earned_amount = 80

total_earnings = bubblegum_earned_amount + toffee_earned_amount + ice_cream_earned_amount + milk_chocolate_earned_amount + doughnut_earned_amount + pancake_earned_amount

print("Earned amount:")

print('Bubblegum: $', bubblegum_earned_amount)
print('Toffee: $', toffee_earned_amount)
print('Ice cream: $', ice_cream_earned_amount)
print('Milk chocolate: $', milk_chocolate_earned_amount)
print('Doughnut: $', doughnut_earned_amount)
print('Pancake: $', pancake_earned_amount)

print()
print('Income: $', total_earnings)

staff_expenses = int(input("Staff expenses:"))
other_expenses = int(input("Other expenses:"))
net_income = total_earnings - staff_expenses - other_expenses
print("Net income: %", net_income, sep="")