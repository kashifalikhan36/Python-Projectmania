import tkinter
window=tkinter.Tk()
window.title("My first gui pro")
window.minsize(300,300)
#Label
my_label=tkinter.Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.grid(column=1,row=1)
#button
def click():
    my_label.config(text=input.get())
    
button_1=tkinter.Button(text="new",command=click)
button_1.grid(column=2,row=2)
button=tkinter.Button(text="new",command=click)
button.grid(column=1,row=3)

input=tkinter.Entry()
input.grid(column=4,row=3)


"""
text=tkinter.Text(width=25,height=5)
text.focus()

def spinbox_used():
    print(spinbox.get())
spinbox=tkinter.Spinbox(from_=0,to=1092323,width=5,command=spinbox_used)

def scale(values):
    print(values)
scale_point=tkinter.Scale(from_=0,to=323232,command=scale)
radio_state=tkinter.IntVar()
def ch():
    print(radio_state.get())
check=tkinter.Checkbutton(text="Is On",variable=radio_state,command=ch)

rad_sat=tkinter.IntVar()
def rad_use():
    print(rad_sat.get())
rad=tkinter.Radiobutton(text="Dopla",value=1,variable=rad_sat)
rad_2=tkinter.Radiobutton(text="Dopla_2",value=2,variable=rad_sat)

Listbox=tkinter.Listbox()
def listbox_use(event):
    print(Listbox.get(Listbox.curselection()))

fruits=["banan","ajsjnz","ksdcmjks","sjakx"]
for i in fruits:
    Listbox.insert(fruits.index(i),i)
Listbox.bind("<<ListboxSelect>>",listbox_use)
Listbox.pack()
rad_2.pack()
rad.pack()
check.pack()
scale_point.pack()
spinbox.pack()
text.pack()

button.pack()

my_label.pack()
"""
window.mainloop()