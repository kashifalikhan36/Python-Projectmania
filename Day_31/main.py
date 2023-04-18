BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
try:
    words={row.French:row.English for index,row in pandas.read_csv("Day_31\\data\\learn_words.csv").iterrows()}
except:
    words={row.French:row.English for index,row in pandas.read_csv("Day_31\\data\\french_words.csv").iterrows()}
finally:
    french_word=random.choice(list(words.keys()))
    english_word=words[french_word]

def data_helper():
    global words
    dict_items = list(words.items())
    dict_items.insert(0, ("French", "English"))
    words=dict(dict_items)
def right_button_del():
    del words[french_word]
    data_helper()
    learn=pandas.DataFrame.from_dict(words, orient='index')
    learn.to_csv("Day_31\\data\\learn_words.csv",header=False)
    del words["French"]
    next_card()
    
def next_card():
    global french_word
    global english_word
    french_word=random.choice(list(words.keys()))
    english_word=words[french_word]
    canvas.itemconfig(card_image,image=card_front)
    canvas.itemconfig(title,text="French")
    canvas.itemconfig(word,text=french_word)
    window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_image,image=card_back)
    canvas.itemconfig(title,text="English")
    canvas.itemconfig(word,text=english_word)

    

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR,highlightthickness=0)

window.after(3000,func=flip_card)

canvas=Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)

card_back=PhotoImage(file="Day_31\images\card_back.png")
card_front=PhotoImage(file="Day_31\images\card_front.png")
right=PhotoImage(file="Day_31\\images\\right.png")
wrong=PhotoImage(file="Day_31\images\wrong.png")

card_image=canvas.create_image(400,270,image=card_front)
title=canvas.create_text(400,150,text="French",font=("Arial",40,"italic"),fill="black")
word=canvas.create_text(400,263,text=french_word,font=("Arial",40,"bold"),fill="black")

canvas.grid(column=1,row=0,columnspan=2)

wrong_button=Button(image=wrong,highlightthickness=0,command=next_card)
wrong_button.grid(column=1,row=2)

right_button=Button(image=right,highlightthickness=0,command=right_button_del)
right_button.grid(column=2,row=2)

window.mainloop()