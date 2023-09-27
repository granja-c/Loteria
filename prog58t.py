import math
total = float(input("Total: "))
paid = float(input("Given:"))

change = paid - total
dollar = math.floor(change)
coins = round((change - dollar), 2)
quarter = coins // 0.25
dime = (coins - quarter * 0.25) // 0.1
nickel = (coins - (quarter * 0.25 + dime * 0.1)) // 0.05 
penny = (coins - (quarter * 0.25 + dime * 0.1 + nickel * 0.05)) // 0.01

print(dollar)
print(coins)
print(quarter)
print(dime)
print(nickel)
print(penny)