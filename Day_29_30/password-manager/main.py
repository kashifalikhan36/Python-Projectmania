from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters)
                        for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(numbers)
                        for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(symbols)
                        for _ in range(random.randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# website | Email | password


def save():
    web = str(web_input.get())
    user = str(user_input.get())
    password = str(password_input.get())
    new_data = {
        web: {
            "email": user,
            "password": password
        }
    }
    print(new_data)
    if len(web) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops", message="I think u had missed something to write and leave Empty")
    else:
        task = messagebox.askokcancel(
            title="website", message=f"These are the details entered: \n Email:- {user}\n Password:- {password}")
        if task:
            try:
                with open("Day_29\password-manager\data.json", mode="r") as file:
                    data=json.load(file)
            except:
                with open("Day_29\password-manager\data.json", mode="w") as file:
                    json.dump(new_data,file)
            else:
                data.update(new_data)
                with open("Day_29\password-manager\data.json", mode="w") as file:
                    json.dump(dict(data),file,indent=4)
            finally:
                web_input.delete(0, END)
                password_input.delete(0, END)
        else:
            pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    with open("Day_29\password-manager\data.json", mode="r") as file:
        try:
            data=json.load(file)
            website_email=data[web_input.get()]["email"]
            website_password=data[web_input.get()]["password"]
        except:
            messagebox.showerror(title="Oops",message="Data doesn't exist")
        else:
            copy_data=messagebox.askokcancel(
                title="ID and Pass", message=f"User: {website_email} \n Password: {website_password}")
            pyperclip.copy(website_password)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="Day_29\password-manager\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

user_text = Label(text="Email/Username:")
user_text.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

web_input = Entry(width=26)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

user_input = Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "kashifalikhan093@gmail.com")

password_input = Entry(width=26)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3, columnspan=1)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, columnspan=1)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
