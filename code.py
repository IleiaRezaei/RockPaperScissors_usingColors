#you need to install termcolor2 from pypi.org

import random
import termcolor2

user_wins = 0
computer_wins = 0


yourColor = input("What color do you want?: ").lower()
enemyColor = input("What color do you want the enemy?: ").lower()
tieColor = input("What do you want the color for tie to be?: ").lower()

print("Rock, Paper, Scissors")

moves = ["rock", "paper", "scissors"]

while user_wins != 3 and computer_wins != 3:
    
    random_index = random.randint(0,2)
    cpu_choice = moves[random_index]

    user_choice = input("Rock, Paper, or Scissors? ").lower()

    while user_choice not in moves:
        user_choice = input("That is not a valid choice. Please try again: ").lower()

    print("--------------------")
    print("Your choice:", user_choice)
    print("Computer's choice:", cpu_choice)

    if user_choice == 'rock':
        if cpu_choice == 'rock':
            print(termcolor2.colored("It's a tie!", color = tieColor))
        elif cpu_choice == 'scissors':
            print(termcolor2.colored("You win!", color = yourColor))
            user_wins += 1
        elif cpu_choice == 'paper':
            print(termcolor2.colored("You lose!", color = enemyColor))
            computer_wins += 1
    elif user_choice == 'paper':
        if cpu_choice == 'paper':
            print(termcolor2.colored("It's a tie!", color = tieColor))
        elif cpu_choice == 'rock':
             print(termcolor2.colored("You win!", color = yourColor))
             user_wins+=1
        elif cpu_choice == 'scissors':
            print(termcolor2.colored("You lose!", color = enemyColor))
            computer_wins+=1
    elif user_choice == 'scissors':
        if cpu_choice == 'scissors':
            print(termcolor2.colored("It's a tie!", color = tieColor))
        elif cpu_choice == 'paper':
            print(termcolor2.colored("You win!", color = yourColor))
            user_wins+=1
        elif cpu_choice == 'rock':
            print(termcolor2.colored("You lose!", color = enemyColor))
            computer_wins+=1

    print("You have "+str(user_wins)+" wins")
    print("The computer has "+str(computer_wins)+" wins")
    
    print("Good Game")

if user_wins == 3:
    print(termcolor2.colored("The game is done, you win", color = "green"))
if computer_wins == 3:
    print(termcolor2.colored("The game is done, computer win", color = "red"))
print("------------------")
