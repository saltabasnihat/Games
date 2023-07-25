import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]

person_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if person_choice == 0:
    print("You chose rock!\n")
    print(list[0])
elif person_choice == 1:
    print("You chose paper!\n")
    print(list[1])
elif person_choice == 2:
    print("You chose scissors!")
    print(list[2])
else:
    print("Invalid input!")

computer_choice = random.randint(0, len(list)-1)
if computer_choice == 0:
    print("Computer chose rock!")
    print(list[0])
elif computer_choice == 1:
    print("Computer chose paper!")
    print(list[1])
elif computer_choice == 2:
    print("Computer chose scissors!")
    print(list[2])
else:
    print("Invalid input!")

if person_choice == computer_choice:
    print("Draw!")
elif (person_choice == 0 and computer_choice == 1):
    print("You lost! Loser...")
elif (person_choice == 1 and computer_choice == 2):
     print("You lost! Loser...")
elif (person_choice == 2 and computer_choice == 0):
 print("You lost! Loser...")
else:
    print("You won. Lucky...")








