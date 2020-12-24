from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, checkmark, timer
    window.after_cancel(timer)
    reps = 0
    checkmark = ""
    timer = None
    canvas.itemconfig(timer_text, text="00:00")
    label_1.config(text="Timer", fg=GREEN)
    label_2.config(text=f"{checkmark}")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        global checkmark
        checkmark += "✓"
        label_2.config(text=f"{checkmark}")

    if reps % 8 == 0:
        label_1.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_1.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_1.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # if reps == 8:
        #     reset_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

label_1 = Label(text="Timer", font=("Arial Rounded MT Bold", 30, "normal"), fg=GREEN, bg=YELLOW)
label_1.grid(column=1, row=0)

label_2 = Label(font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
label_2.grid(column=1, row=3)

button_1 = Button()
button_1.config(text="Start", bg=PINK, command=start_timer)
button_1.grid(column=0, row=2)

button_2 = Button()
button_2.config(text="Reset", bg=PINK, command=reset_timer)
button_2.grid(column=2, row=2)

window.mainloop()
