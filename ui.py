THEME_COLOR = "#375362"
CANVA_CLOR ="#000000"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.right = PhotoImage(file="t.png")
        self.wrong = PhotoImage(file = "f.png")
        self.window.config(padx=20,pady=20,bg =THEME_COLOR)
        self.window.title("QUIZZLER")

        self.canvas = Canvas(height=250,width=300,bg=CANVA_CLOR,highlightthickness=0)
        self.question = self.canvas.create_text( 150,
                                                 125,
                                                 text = "hello",
                                                 font=("Arial",18,"italic"),
                                                 width = 270,
                                                 fill = THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)  # Add bottom padding

        self.label = Label(text=f"SCORE:{0}",bg=THEME_COLOR,fg="white",font=("Arial",10,"bold"))
        self.label.grid(column=0,row=0,columnspan=2,pady =(0, 20))

        self.right_b = Button(image=self.right,highlightthickness=0,command=self.true_press,bg=THEME_COLOR)
        self.right_b.grid(column=0,row=2,padx = 20)
        self.wrong_b = Button(image=self.wrong,highlightthickness=0,command=self.false_press,bg=THEME_COLOR)
        self.wrong_b.grid(column=1,row =2,padx=20)

        self.get_ques()



        self.window.mainloop()

    def get_ques(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg = "black")
            self.label.config(text=f"SCORE:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text = q_text)
        else:
            self.canvas.itemconfig(self.question,text="Your Quiz is Over")
            self.right_b.config(state = "disabled")
            self.wrong_b.config(state = "disabled")


    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,ans):
        if ans:
            self.canvas.config(bg ="green")
        else:
            self.canvas.config(bg ="red")

        self.window.after(700,self.get_ques)


#quiz_ui = QuizInterface()











