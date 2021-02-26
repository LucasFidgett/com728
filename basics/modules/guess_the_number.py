import random as rnd
# from random import randrange


def number_guess():
    user_min = int(input("Please enter a minimum value\n"))
    user_max = int(input("Please enter a maximum value\n"))
    print(f"I am thinking of a number between {user_min} and {user_max}.\nCan you guess what it is?\n")
    random_number = rnd.randrange(user_min, user_max)
    user_guess = int(input())

    i = 0
    while i <= 1:
        if user_guess == random_number:
            print("You are correct!")
            i = 5
        elif user_guess != random_number:
            user_guess = int(input("Wrong! Guess again...\n"))
            i = i + 1
    if i == 1:
        print("Unlucky... You are out of guesses!")


number_guess()
