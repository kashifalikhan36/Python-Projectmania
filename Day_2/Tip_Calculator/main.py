print("Welcome to the tip calculator")
try:
 bill=int(input("WHat was the bill? $"))
#percentage to give tip
 percent=int(input("What percentage tip do you want to give? 10,20, or 15? "))
 split=int(input("How many people to split the bill?"))
except:
 print("Something wents wrong try again")
total_bill=((bill*percent/100)+bill)/split
print("Each person should pay: $",total_bill)