import tkinter as tk
import random

root = tk.Tk()
root.title("Color Reflex Arena")
root.geometry("400x450")
root.configure(bg="#222")

score = 0
time_left = 30
target_color = ""

colors = ["Red", "Blue", "Green", "Yellow"]

def start_game():
    global score, time_left
    score = 0
    time_left = 30
    update_target()
    countdown()

def update_target():
    global target_color
    target_color = random.choice(colors)
    target_label.config(text=f"Click: {target_color}")

    random.shuffle(buttons)
    for i, btn in enumerate(buttons):
        btn.grid(row=i//2, column=i%2, padx=10, pady=10)

def button_click(color):
    global score
    if color == target_color:
        score += 1
        score_label.config(text=f"Score: {score}")
        update_target()

def countdown():
    global time_left
    if time_left > 0:
        timer_label.config(text=f"Time: {time_left}")
        time_left -= 1
        root.after(1000, countdown)
    else:
        target_label.config(text="Game Over")

target_label = tk.Label(root, text="Click Color", fg="white", bg="#222", font=("Arial", 16))
target_label.pack(pady=10)

score_label = tk.Label(root, text="Score: 0", fg="cyan", bg="#222", font=("Arial", 14))
score_label.pack()

timer_label = tk.Label(root, text="Time: 30", fg="orange", bg="#222", font=("Arial", 14))
timer_label.pack()

frame = tk.Frame(root, bg="#222")
frame.pack(pady=20)

buttons = []
for c in colors:
    btn = tk.Button(frame, text=c, bg=c.lower(), fg="white",
                    width=12, height=2,
                    command=lambda col=c: button_click(col))
    buttons.append(btn)

start_btn = tk.Button(root, text="Start Game", bg="lime", command=start_game)
start_btn.pack(pady=10)

root.mainloop()
