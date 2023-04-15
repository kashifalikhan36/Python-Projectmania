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
REPS=0
timer_clock=None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer_clock)
    timer.config(text="Timer",fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    check_mark.config(text="")
    global REPS
    REPS=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global WORK
    global REPS
    REPS+=1
    work_min=int(WORK_MIN*60)
    short_break_min=int(SHORT_BREAK_MIN*60)
    long_break_min=int(LONG_BREAK_MIN*60)
    if REPS%8==0:
        timer.config(text="BREAK",fg=RED)
        count_down(int(short_break_min/60))
    elif REPS%2==0:
        timer.config(text="BREAK",fg=PINK)
        count_down(int(long_break_min/60))
        
    else:
        timer.config(text="WORK",fg=GREEN)
        count_down(int(work_min/60))
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=int(count/60)
    count_sec=int(count%60)
    if 0<=count_sec<10:
        count_sec=f"0{count}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer_clock
        timer_clock=window.after(1000,count_down,count-1)
    else:
        start_timer()
        WORK=""
        for _ in range(int(REPS/2)):
            WORK+="✓"
        check_mark.config(text=WORK)

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

reset=Button(text="reset",command=reset)
reset.grid(column=3,row=3)

check_mark=Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column=2,row=4)

window,mainloop()