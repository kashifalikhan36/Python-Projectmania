from art import logo,vs
from game_data import data
import random

def list_maker():
    list=random.choice(data)
    return list



print(logo)
game=0
while True:
      
    print(f"Compare A: {user_1['name']}, {user_1['description']} or, from {user_1['country']}")
    print(vs)
    print(f"Against A: {user_2['name']}, {user_2['description']} or, from {user_2['country']}")
    user_1=list_maker()
    user_2=list_maker()
    ip=input("Who has more followers? Type 'A' or 'B':-").lower()
    
    if ip=="a":
        if user_1['follower_count']>user_2['follower_count']:
            game+=1
            print("Your Score is ",game)
            continue
        else:
            print("Your Score is ",game)
            print('Game Over')
            break
    elif ip=="b":
        if user_2['follower_count']>user_1['follower_count']:
            game+=1
            print("Your Score is ",game)
            continue
        else:
            print("Your Score is ",game)
            print('Game Over')
            break