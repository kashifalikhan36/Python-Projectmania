import random
from art import logo
#Number Guessing Game Objectives:

# Include an ASCII art logo.
print(logo)
track=10

def check_track(track):
    if track==0:
        print("You Lose")
        return False
def game(guess,track):
    guess_comp=random.randint(1,100)
    

    if guess_comp>guess:
        print("Too Low")
        return track-1
    elif guess_comp<guess:
        print("Too high")
        return track-1
    elif guess_comp==guess:
        print(f"Got the answer {guess}")
        return 
    while guess!=guess_comp:
    
        try:
            guess=int(input("Geuss no. in between 1 to 100"))
        except:
            print("Wrong And Invalid input")
            continue



game()



# Track the number of turns remaining.

# If they run out of turns, provide feedback to the player.

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
