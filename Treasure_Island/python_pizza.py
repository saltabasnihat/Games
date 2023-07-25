# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

cost = 0
if extra_cheese == "Y":
    cost +=1

if size == "S":
    cost += 15
    if add_pepperoni == "Y":
        cost += 2
    else:
        cost += 0
elif size == "M":
    cost += 20
    if add_pepperoni == "Y":
        cost += 3
    else:
        cost += 0
elif size == "L":
    cost += 25
    if add_pepperoni == "Y":
        cost += 3
    else:
        cost += 0
else:
    print("Please only input S, M or L")

print(f"Your total is {cost}$. ")

   
        

    

    
