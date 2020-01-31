"""You are to develop an “Rock, Paper, Scissors” game that is intended to be played between user and computer itself.
Winning Rules as follows :
Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.

"""
import random
print("RULES: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

while True:
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
    # take the input from user
    choice = int(input("User turn: "))
    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input("enter true input: "))
        # We define value of choice_name variable
        # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
     # print user choice
    print("user choice is: " + choice_name)
    print("\nNow its computer turn....")

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)

    # while looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

        # We define value of comp_choice_name
          # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    # condition for winning
    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("paper wins.....", end="")
        result = "paper"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("Rock wins.....", end="")
        result = "Rock"
    else:
        print("scissor wins.....", end="")
        result = "scissor"

    #We  Print  "user or computer wins"
    if result == choice_name:
        print("< User wins >")
    else:
        print("< Computer wins >")

    print("Do you want to play again? (Y/N)")
    answer = input()
    # if user input n or N then condition is True
    if answer == 'n' or answer == 'N':
        break




