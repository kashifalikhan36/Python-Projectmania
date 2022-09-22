import random
from replit import clear
from hangman_art import logo,stages
from hangman_project import wordlist
print(logo)
display=[]
chosen_word=wordlist[random.randint(0,2)].lower()
print(f'Pssst, the solution is {chosen_word}.')
for word_no in range(len(chosen_word)):
        #display.append("_")
        display+="_"

lives=6
while True:
    print(stages[lives])
    print(display)
    guess=input("Geuss the word").lower()
    clear()
    if guess in display:
        print(f"Guess letter is allready in display{guess}")
    for position in range(len(chosen_word)):
     letter = chosen_word[position]
     if letter == guess:
        display[position] = letter
    if guess not in chosen_word:
        lives-=1
    if "_" in display:
        if lives==0:
            print("You lose")
            break
        continue
    elif "_" not in display or lives>0:
        print("You win")
        break