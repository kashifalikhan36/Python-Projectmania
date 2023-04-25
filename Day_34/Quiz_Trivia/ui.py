THEME_COLOR = "#375362"
from tkinter import *
#from quiz_brain import QuizBrain


class QuizInterface():
    def __init__(self,quiz_brain) -> None:
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizer")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR,highlightthickness=0)
        
        self.score_text=Label(background=THEME_COLOR,text="Scorre:0",fg="white", padx=20, pady=20)
        self.score_text.grid(column=1,row=0)

        self.canvas=Canvas(height=300,width=350,highlightthickness=0)

        self.question_text=self.canvas.create_text(150,125,width=200,text="Some question text",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.get_next_qus()

        self.right_image=PhotoImage(file="Day_31\\images\\right.png")
        self.right=Button(image=self.right_image,command=self.true_pressed)
        self.right.grid(column=0,row=2)

        self.wrong_image=PhotoImage(file="Day_31\images\wrong.png")
        self.wrong=Button(image=self.wrong_image,command=self.false_pressed)
        self.wrong.grid(column=1,row=2)

        

        self.window.mainloop()

    def get_next_qus(self):
        self.canvas.config(bg="white")
        self.score_text.config(text=f"Score:{self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
            
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self,is_right):
        if is_right==True:
            self.canvas.config(bg="green")
            
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_qus)