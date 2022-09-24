from replit import clear
from art import logo
dict = {}
print(logo)
while True:
    name = input("Tell Your Name?:-")
    bid = int(input("tell me the Bid?:-"))
    dict[name] = bid
    turn = input("If there any bet is pending:- (No,Yes").lower()
    if turn == "no":
        ans = 0
        for name in dict:
            if dict[name] > ans:
                ans == name
        break
    elif turn == "yes":
        clear()
        continue