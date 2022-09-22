import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image=[rock,paper,scissors]
pc_choice=random.randint(0,2)
try:
 user_choice=int(input("WHat do you Choose/ Type 0 for Rock, 1 for Paper, 2 for scissos? :-"))
except:
 print("Something wents wrong please try again,,,")
print(game_image[user_choice])
print("Your choice")
print(game_image[pc_choice])
print("computer choice")
if user_choice==pc_choice:
    print("you It's Draw")
elif user_choice==0 and pc_choice==2:
    print("You Lose")
elif user_choice > pc_choice:
    print("You win")
elif user_choice>=3 or pc_choice:
    print("nvalid input , Try again later....")
