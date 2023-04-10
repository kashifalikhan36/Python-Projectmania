import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list=[]
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=""
for letter in range(0,nr_letters):
    password=password+letters[random.randint(1,nr_letters+1)]
for symbol in range(0,nr_symbols):
    password=password+symbols[random.randint(1,nr_symbols+1)]
for number in range(0,nr_numbers):
    password=password+numbers[random.randint(1,nr_numbers+1)]
for digit in range(0,len(password)):
    password_list.append(password[digit])

random.shuffle(password_list)
new_password=""
for char in range(0,len(password_list)):
    new_password+=password_list[char]
print("Here is your password: ",new_password)