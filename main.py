from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="TIMER")
    canvas.itemconfig(werey, text="00:00")
    check_label.config(text="")
    global reps
    reps= 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_min_sec = WORK_MIN * 60
    SHORT_BREAK_MIN_sec = SHORT_BREAK_MIN * 60
    LONG_BREAK_MIN_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(SHORT_BREAK_MIN_sec)
        timer_label.config(text="Short Break", fg=RED)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN_sec)
        timer_label.config(text="Long Break", fg=PINK)
    else:
        count_down(work_min_sec)
        timer_label.config(text="Work Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(werey, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            mark += "✔"
            check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("my Pomodoro")
window.config(padx=100, pady=40, bg=YELLOW)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(104, 112, image=tomato_img)
werey = canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

timer_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

check_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold",))
check_label.grid(column=1, row=3)

start_button = Button(text="START", command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="RESET", command=reset_timer)
reset_button.grid(column=2, row=3)
window.mainloop()
