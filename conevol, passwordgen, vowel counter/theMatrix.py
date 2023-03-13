import math
import random

def cone_vol(height, radius):
    cone_vol = 1 / 3 * math.pi * radius ** 2 * height
    print(f"The volume of the cone is: {cone_vol}")

def password_generator(length):
    allCharacters = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "w", "e", "r",
                     "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z",
                     "x", "c", "v", "b", "n", "m", ",", ".", "/"]
    password = ''
    for i in range(length):
        random_num = random.randrange(0, len(allCharacters))
        newChar = allCharacters[random_num]
        password += newChar
    print(f"Your password is: {password}")

def vowel_counter():
    s = input("Enter your sentence:")
    vowels = ['a', 'e', 'u', 'i', 'o', 'E', 'A', 'U', 'O', 'I']
    num_vow = 0;
    for i in s:
        if i in vowels:
            num_vow += 1

    print(f"The number of vowels in the sentence is: {num_vow}")

CONE_VOL_CALC = "1"
PASSWORD_GENERATOR = "2"
VOWEL_COUNTER = '3'
EXIT = "4"
prompt = f"""
Choose from 1-{EXIT}:
{CONE_VOL_CALC} is cone volume calculator
{PASSWORD_GENERATOR} is password generator
{VOWEL_COUNTER} is vowel counter
{EXIT} is to exit the program
Enter your choice: """

print("Welcome to the main program")

while True:
    choice = input(prompt)
    if choice == CONE_VOL_CALC:
        try:
            height = float(input("Enter the height of the cone: "))
            radius = float(input("Enter the radius of the cone: "))
            cone_vol(height, radius)
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
    elif choice == PASSWORD_GENERATOR:
        try:
            length = int(input("Enter length for your password: "))
            password_generator(length)
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
    elif choice == VOWEL_COUNTER:
        vowel_counter()
    elif choice == EXIT:
        print("Goodbye!")
        break
    else:
        print("Invalid input\nTry again!\n")

