birth_year = int(input("Enter your date of birth: "))

# if user turned 18
turning_18_year = birth_year + 18

# if the user is 18 or older in 2009
if turning_18_year <= 2009:
    starting_year = 2009
else:
    starting_year = turning_18_year

# start of contribution room
contribution_room = 0

# loop from the starting year to 2022
for year in range(starting_year, 2023):
    if year >= 2009 and year <= 2012:
        contribution_room += 5000
    elif year == 2013 or year == 2014:
        contribution_room += 5500
    elif year == 2015:
        contribution_room += 10000
    elif year >= 2016 and year <= 2018:
        contribution_room += 5500
    elif year >= 2019 and year <= 2022:
        contribution_room += 6000

# final contribution room
print("Your TFSA contribution room is:", contribution_room, "$")


