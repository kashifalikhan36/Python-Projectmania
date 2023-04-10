import random
from art import logo
#Number Guessing Game Objectives:

# Include an ASCII art logo.
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def track_calc():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level =="easy":
        return EASY_LEVEL_TURNS
    elif level=="hard":
        return HARD_LEVEL_TURNS


def check_answer(guess,guess_comp,turns):
    if guess_comp>guess:
        print("Too Low")
        return turns-1
    elif guess_comp<guess:
        print("Too high")
        return turns-1
    elif guess_comp==guess:
        print(f"Got the answer {guess}")
        return 

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer=random.randint(1,100)
    try:
        guess=int(input("Geuss no. in between 1 to 100"))
    except:
        print("Wrong And Invalid input")
    turns=track_calc()
    guess=0
    while guess!=answer:
    


    
    game()
