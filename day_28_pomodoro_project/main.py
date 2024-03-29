from tkinter import *
import math
# ---------------------------- CONSTANTS -------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=None

# ---------------------------- TIMER RESET ----------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text,text="00:00")
    title_label.config(text="timer")
    global reps
    reps= 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec= WORK_MIN * 60
    short_brake_sec=SHORT_BREAK_MIN*60
    long_brake_sec= LONG_BREAK_MIN*60

    if reps %8==0:
        count_down(long_brake_sec)
        title_label.config(text="long 20 min Brake")
    elif reps %2 ==0:
        count_down(short_brake_sec)
        title_label.config(text="short 5 min Brake")
    else:
        count_down(work_sec)
        title_label.config(text="Working time!!")




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min=math.floor(count/60)
    count_sec= count % 60
    if count_sec == 0:
        count_sec="00"
    elif count_sec <10:
        count_sec=F"0{count_sec}"

    canvas.itemconfig(time_text,text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



canvas = Canvas(height=223,width=200,bg=YELLOW ,highlightthickness=0)
pomodoro_photo = PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=pomodoro_photo)

title_label = Label(text="Timer",fg=GREEN,bg=YELLOW ,font=(FONT_NAME,40,"bold"))
title_label.grid(column=2,row=1)

time_text= canvas.create_text(100,132,text="00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)



start_button = Button(text="Start",command=start_timer)

start_button.grid(column=1,row=3)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=3,row=3)

check_marks=Label(fg=GREEN,bg=YELLOW,font=36)
check_marks.grid(column=2,row=4)

window.mainloop()
