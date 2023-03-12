import random


options = ['R', 'P', 'S']

while True:
    player_win = 0
    comp_win = 0
    while True:
        player_choice = input("Please enter: R for Rock, P for Paper or S for Scissors:").upper()
        if player_choice not in options:
            print("Invalid choice. Please try again!")
            continue
        comp_choice = random.choice(options)
        print(f"You chose {player_choice}, computer chose {comp_choice}")
        if player_choice == comp_choice:
                print('It is a tie!')
        elif player_choice == 'R':
            if comp_choice == 'P':
                print('You lost!')
                comp_win += 1
            else:
                print('You win!')
                player_win += 1
        elif player_choice == 'P':
            if comp_choice == 'R':
                print('You win')
                player_win += 1
            else:
                print('You lost!')
                comp_win += 1
        elif player_choice == 'S':
            if comp_choice == 'R':
                print('You lost!')
                comp_win += 1
            else:
                print('You win!')
                player_win += 1
        if player_win == 3:
            print("You Win. Congrats!!!")
            break
        elif comp_win == 3:
            print("You Lost. Better luck next time!!!")
            break
    restart_game = input("Do you want to play again?(Y/N):").upper()
    if restart_game == 'Y':
        continue
    else:
        print("Thank you for playing. GoodBye!!!")
        break
