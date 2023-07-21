#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

bill = input("Total bill? ")
tip = input("Percentage tip? ")
split = input("How many people shares the bill? ")

new_bill = float(bill)
new_tip = (float(tip) + 100) / 100
new_split = int(split)

cost = (new_bill / new_split) * new_tip
new_cost = round(cost, 2)

print(f"Each person pays {new_cost} dollars!")