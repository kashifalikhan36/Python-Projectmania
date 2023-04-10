from replit import clear
from art import logo
import random
print(logo)

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
def card(use):
  use.append(random.choice(cards))
def sum_card(output):
  sum=0
  for i in output:
   sum+=i
  return sum
def play(start_choice):
  
  user=[]
  comp=[]
  if start_choice=="y":
    for i in range(0,2):
     card(user)
     card(comp)  
    print(f"Your cards: {user}, current score: {sum(user)}")
    print(f"Computer's first card: {comp[0]}")
    while True:
      opt=input("Type 'y' to get another card, type 'n' to pass:-").lower()
      if opt=="y":
        card(user)
        if sum_card(user)>=21:
         print(f"Your cards: {user}, current score: {sum(user)}")
         print(f"Computer's first card: {comp}")
         print("You Lose")
         break
        card(comp)
        if sum_card(comp)>=21:
         print(f"Your cards: {user}, current score: {sum(user)}")
         print(f"Computer's first card: {comp}")
         print("You Win")
         break
      else:
        pass
      print(f"Your cards: {user}, current score: {sum(user)}")
      print(f"Computer's first card: {comp[0]}")
    

while True:
  start_choice=input("Do you want to play a game of Blackjack? Type 'y' or 'n':-").lower()
  clear()
  play(start_choice)
##################### Hints #