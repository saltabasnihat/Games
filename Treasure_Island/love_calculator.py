# Take both people's names and check for the number of times the letters 
# in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

added_name = name1 + name2
lower_case_name = added_name.lower()

letter_1 = lower_case_name.count("t")
letter_2 = lower_case_name.count("r")
letter_3 = lower_case_name.count("u")
letter_4 = lower_case_name.count("e")

decimal_1 = letter_1 + letter_2 + letter_3 + letter_4

letter_5 = lower_case_name.count("l")
letter_6 = lower_case_name.count("o")
letter_7 = lower_case_name.count("v")
letter_8 = lower_case_name.count("e")

decimal_2 = letter_5 + letter_6 + letter_7 + letter_8 

point = str(decimal_1) + str(decimal_2)
new_point = int(point)

if new_point < 10 or new_point > 90:
    print(f"Your score is {new_point}, you go together like coke and mentos.")
elif new_point>40 and new_point <50:
    print(f"Your score is {new_point}, you are alright together.")
else:
    print(f"Your score is {new_point}.")




