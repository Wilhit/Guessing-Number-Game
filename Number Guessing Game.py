########### Number Guessing Game ###############
from art import logo
from random import randint

#Declare and set a global variables

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turn = 0

print(logo)
print()

def check_answer(guess, answer, turns):
    """Checks answer agains guess and returns the number of turns remaining"""
    if guess > answer:
        print("Too High!!!")
        return turns - 1
    elif guess < answer:
        print("Too Low!!!")
        return turns - 1
    else:
        print(f"You got it, The answer is {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("Wrong Level!!!!")

def game():
    print("Welcome to the Number Guessing Game.")

    answer = randint(1, 100)

    print("I'm Thinking of a number between 1 and 100")
    turns = set_difficulty()
    

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You have run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again.")
            print()

game()


