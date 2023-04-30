from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS=0
TIMER=None
# TIMER RESET
def reset():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_var,text="00:00")
    timer.config(text="Timer",fg=GREEN) 
    check.config(text=" ")
    REPS=0

#TIMER MECHANISM 
def start_timer():
    global REPS
    REPS+=1
    if REPS%8==0:
        countdown(LONG_BREAK_MIN)
        timer.config(text="Break",fg=RED)
    elif REPS%2==0:
        countdown(SHORT_BREAK_MIN)
        timer.config(text="Break",fg=PINK)

    else:
        countdown(WORK_MIN)
        timer.config(text="Work",fg=GREEN)





# COUNTDOWN MECHANISM 
def countdown(count):
    global TIMER
    count_min=count//60
    count_sec=count%60
    if count_min<10:
        count_min=(f"0{count_min}")
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_var, text=f"{count_min}:{count_sec}")
    if count>0:
        TIMER=window.after(1000,countdown,count-1)
    else:
        start_timer()
        marks=""
        for i in range(REPS//2):
            marks+="✔️"
        check.config(text=marks)

#UI SETUP 
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


# Tomato
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_var=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

# Timer text
timer=Label(text="Timer")
timer.config(font=(FONT_NAME,45,"bold"),fg=GREEN,bg=YELLOW)
timer.grid(column=2,row=1)

# Buttons
start=Button(text="Start",command=start_timer)
reset=Button(text="Reset",command=reset)
start.grid(row=3,column=1)
reset.grid(row=3,column=3)

# Check
check=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,15,"bold"))
check.grid(row=4,column=2)

window.mainloop()