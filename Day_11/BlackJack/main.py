from art import logo
import random
card_list=[1,2,3,4,5,6,7,8,9,10,11]

def data(game_us,game_cp):
    user_sum=card_sum(game_us)
    return (f"Your cards: {game_us}, current score: {user_sum} Computer's first card: {game_cp[0]}")

def add_card():
    card=random.randint(1,11)
    return card
def card_sum(card):
    final_card=0
    for cards in card:
        final_card+=cards
    return final_card
  
def game():
        game_us=[]
        game_cp=[]
        for i in range(0,2):
            game_us.append(add_card())
            game_cp.append(add_card())
        print(data(game_us,game_cp))     
        while True:
            ask=input("DO u want to Pass/ Add ?--->").lower()
            if ask=="pass":
                game_cp.append(add_card())
            elif ask=="add":
                game_us.append(add_card())
                game_cp.append(add_card())
            user=card_sum(game_us)
            comp=card_sum(game_cp)
            print(data(game_us,game_cp))
            if user>21 or comp>21:
                print(result(user,comp))
                break

def result(user,comp):
    if user>comp:
        return ("You WIn")
    elif user<comp:
        return ("YOu Loss")
    elif user==comp:
        return ("Tie")
while True:
    print(logo)
    ask=input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if ask=="y":
        game()
    elif ask=="n":
        break