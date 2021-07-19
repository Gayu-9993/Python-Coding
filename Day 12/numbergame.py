import random
from numbergame_art import logo

easy_mode_guesses = 10
hard_mode_guesses = 5


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You made it. The answer is: {answer}")


def set_difficulty():
    level = input("Choose an option: Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_mode_guesses
    else:
        return hard_mode_guesses


def game():
    print(logo)
    print("Welcome To Number Guessing Game.")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"the correct answer is : {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Run out of guesses. You Lose.")
        elif guess != answer:
            print("Guess again.")


game()
