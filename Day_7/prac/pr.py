import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
wordlist=["ardvark","baboon","camel"]
display=[]
chosen_word=wordlist[random.randint(0,2)].lower()
print(f'Pssst, the solution is {chosen_word}.')
for word_no in range(len(chosen_word)):
        #display.append("_")
        display+="_"


while True:
    print(display)
    guess=input("Geuss the word").lower()
    
    for position in range(len(chosen_word)):
     letter = chosen_word[position]
     if letter == guess:
        display[position] = letter
    if "_" in display:
        continue
    elif "_" not in display:
        print("You win")
        break
    