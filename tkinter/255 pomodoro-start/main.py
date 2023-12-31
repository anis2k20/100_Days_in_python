from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    time.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    ok_sign.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec =  SHORT_BREAK_MIN * 60
    long_break_sec =  LONG_BREAK_MIN * 60

    if reps%8==0:
        count_down(long_break_sec)
        time.config(text="Long Break", fg=RED, font=(FONT_NAME, 30, "bold"))
    elif reps%2==0:
        count_down(short_break_sec)
        time.config(text="Short Break", fg=PINK, font=(FONT_NAME, 30, "bold"))
    else:
        count_down(work_sec)
        time.config(text="Work", fg=GREEN, font=(FONT_NAME, 30, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec < 10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        ok_sign.config(text=marks,fg=GREEN)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


time = Label(text="Timer",fg=GREEN,font=(FONT_NAME, 30, "bold"))
time.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)


start = Button(text="Start", font=(FONT_NAME, 22, "normal"), command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", font=(FONT_NAME, 22, "normal"), command=reset)
reset.grid(column=2, row=2)

ok_sign = Label(text="",  font=(FONT_NAME, 25, "normal"))
ok_sign.grid(column=1, row=3)





window.mainloop()