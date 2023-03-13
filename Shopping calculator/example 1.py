# Item list and prices
prices = {
    'Apples': 1.00,
    'Eggs': 0.25,
    'Bread': 2.50,
    'Meat': 10.00,
    'Orange Juice': 2.00
}

# Variables of quantities of each item
apples_quantity = float(input("Enter the quantity of Apples: "))
eggs_quantity = float(input("Enter the quantity of Eggs: "))
bread_quantity = float(input("Enter the quantity of Bread: "))
meat_weight = float(input("Enter the weight of Meat in pounds: "))
juice_volume = float(input("Enter the volume of Orange Juice in litres: "))

# Calculate the cost of every item with tax
apples_cost = prices['Apples'] * apples_quantity * 1.13
eggs_cost = prices['Eggs'] * eggs_quantity * 1.13
bread_cost = prices['Bread'] * bread_quantity * 1.13
meat_cost = prices['Meat'] * meat_weight * 1.13
juice_cost = prices['Orange Juice'] * juice_volume * 1.13

# Total Cost
total_cost = apples_cost + eggs_cost + bread_cost + meat_cost + juice_cost

# Display in terminal rounded to 2 decimals
print(total_cost)

