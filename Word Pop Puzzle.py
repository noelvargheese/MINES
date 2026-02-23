import tkinter as tk
import random

root = tk.Tk()
root.title("Word Pop Puzzle")
root.geometry("500x400")

canvas = tk.Canvas(root, bg="black")
canvas.pack(fill="both", expand=True)

words = ["python", "tkinter", "code", "game", "logic", "loop"]
current_word = ""
word_text = None
y_pos = 0
score = 0
lives = 3
running = True

def new_word():
    global current_word, y_pos, word_text
    canvas.delete("word")
    current_word = random.choice(words)
    y_pos = 0
    word_text = canvas.create_text(
        250, y_pos, text=current_word,
        fill=random.choice(["red", "yellow", "cyan", "lime"]),
        font=("Arial", 20),
        tags="word"
    )

def move_word():
    global y_pos, lives
    if not running:
        return

    y_pos += 5
    canvas.move(word_text, 0, 5)

    if y_pos > 380:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        if lives == 0:
            canvas.create_text(250, 200, text="Game Over", fill="red", font=("Arial", 30))
            return
        new_word()

    root.after(300, move_word)

def check_word(event=None):
    global score
    if entry.get() == current_word:
        score += 1
        score_label.config(text=f"Score: {score}")
        entry.delete(0, tk.END)
        new_word()

def toggle_pause():
    global running
    running = not running
    if running:
        move_word()

score_label = tk.Label(root, text="Score: 0")
score_label.place(x=10, y=10)

lives_label = tk.Label(root, text="Lives: 3")
lives_label.place(x=420, y=10)

entry = tk.Entry(root)
entry.place(x=180, y=350)
entry.bind("<Return>", check_word)

pause_btn = tk.Button(root, text="Pause / Resume", command=toggle_pause)
pause_btn.place(x=200, y=310)

new_word()
move_word()
root.mainloop()
