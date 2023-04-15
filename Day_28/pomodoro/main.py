from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text,text=f"{int(count/60)}:{int(count%60)}")
    if count>0:
        window.after(1000,count_down,count-1)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,bg=YELLOW, highlightthickness=0)


tomato=PhotoImage(file="Day_28\pomodoro\\tomato.png")
canvas=Canvas(width=200,height=224,bg=YELLOW)
canvas.create_image(102,112,image=tomato)
timer_text=canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

timer=Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
timer.grid(column=2,row=1)

start=Button(text="Start",command=start_timer)
start.grid(column=1,row=3)

reset=Button(text="reset")
reset.grid(column=3,row=3)

check_mark=Label(text="✓",fg=GREEN)
check_mark.grid(column=2,row=4)

window,mainloop()