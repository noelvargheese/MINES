import tkinter as tk
import random

CELL = 30

MAZE = [
    [1]*20,
    [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1]*20
]

ROWS, COLS = len(MAZE), len(MAZE[0])

THEMES = [
    ("blue", "red"), ("purple", "cyan"), ("green", "orange"),
    ("teal", "pink"), ("#003366", "yellow"), ("magenta", "white"),
    ("brown", "lime"), ("navy", "violet"), ("maroon", "aqua"), ("gold", "crimson")
]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pac-Man (Basic Tkinter)")
        self.resizable(False, False)
        self.level = 1
        self.score = 0

        self.container = tk.Frame(self)
        self.container.pack()

        self.frames = {}
        for F in (HomeScreen, GameScreen):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_screen(HomeScreen)

    def show_screen(self, screen_class):
        frame = self.frames[screen_class]
        frame.tkraise()
        # If moving to home, make sure to stop the game loop
        if screen_class == HomeScreen:
            self.frames[GameScreen].stop()

    def start_game(self, reset_score=True):
        if reset_score:
            self.score = 0
            self.level = 1
        self.frames[GameScreen].start()
        self.show_screen(GameScreen)

class HomeScreen(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="black", width=COLS*CELL, height=ROWS*CELL + 40)
        self.app = app
        self.pack_propagate(False)

        tk.Label(self, text="PAC-MAN",
                 fg="yellow", bg="black",
                 font=("Arial Black", 36)).pack(pady=(ROWS*CELL//4, 40))

        tk.Button(self, text="START GAME",
                  font=("Arial", 14, "bold"),
                  width=15, bg="blue", fg="white",
                  command=lambda: app.start_game(reset_score=True)).pack(pady=10)

        tk.Button(self, text="EXIT",
                  font=("Arial", 14, "bold"),
                  width=15, bg="red", fg="white",
                  command=app.quit).pack(pady=10)

class GameScreen(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.paused = False
        self.running = False
        self.loop_id = None

        self.canvas = tk.Canvas(self,
                                width=COLS*CELL,
                                height=ROWS*CELL,
                                bg="black",
                                highlightthickness=0)
        self.canvas.pack()

        control = tk.Frame(self, bg="gray20", height=40)
        control.pack(fill="x")

        tk.Button(control, text="HOME", bg="cyan", font=("Arial", 10, "bold"),
                  command=lambda: app.show_screen(HomeScreen)).pack(side="left", padx=5, pady=5)

        tk.Button(control, text="RESTART", bg="lime", font=("Arial", 10, "bold"),
                  command=lambda: app.start_game(reset_score=True)).pack(side="left", padx=5, pady=5)

        self.pause_btn = tk.Button(control, text="PAUSE", bg="yellow", font=("Arial", 10, "bold"),
                                   command=self.toggle_pause)
        self.pause_btn.pack(side="left", padx=5, pady=5)
        
        self.score_label = tk.Label(control, text="Score: 0 | Level: 1", bg="gray20", fg="white", font=("Arial", 12, "bold"))
        self.score_label.pack(side="left", padx=20)

        tk.Button(control, text="EXIT", bg="red", fg="white", font=("Arial", 10, "bold"),
                  command=app.quit).pack(side="right", padx=5, pady=5)

        self.bind_all("<KeyPress>", self.key)

    def start(self):
        self.stop() # Ensure no previous loop is running
        self.canvas.delete("all")
        theme_idx = (self.app.level - 1) % len(THEMES)
        self.wall_color, self.ghost_color = THEMES[theme_idx]
        
        self.pacman = [1, 1]
        self.ghosts = [[ROWS-2, COLS-2], [ROWS-2, 1], [1, COLS-2]] # Initial ghost positions
        
        # Simple rule: limit min delay so game remains playable, speed up slightly by level
        self.delay = max(50, 200 - (self.app.level * 15))
        
        self.direction = (0, 0)
        self.next_direction = (0, 0)
        self.dots = set()
        self.running = True
        self.paused = False
        self.pause_btn.config(text="PAUSE")
        
        self.update_score_display()
        self.draw_maze()
        self.loop()

    def stop(self):
        self.running = False
        if self.loop_id:
            self.after_cancel(self.loop_id)
            self.loop_id = None

    def update_score_display(self):
        self.score_label.config(text=f"Score: {self.app.score} | Level: {self.app.level}")

    def draw_maze(self):
        for r in range(ROWS):
            for c in range(COLS):
                x1, y1 = c * CELL, r * CELL
                x2, y2 = x1 + CELL, y1 + CELL
                if MAZE[r][c] == 1:
                    self.canvas.create_rectangle(
                        x1, y1, x2, y2,
                        fill=self.wall_color, outline="black")
                else:
                    self.dots.add((r, c))
                    # Draw a dot and tag it so we can easily delete it later
                    self.canvas.create_oval(
                        x1 + 12, y1 + 12, x2 - 12, y2 - 12,
                        fill="white", tags=f"dot_{r}_{c}")
                    
        # Exclude initial pacman spot so it doesn't give a point immediately
        if tuple(self.pacman) in self.dots:
            self.dots.remove(tuple(self.pacman))
            self.canvas.delete(f"dot_{self.pacman[0]}_{self.pacman[1]}")

    def key(self, e):
        moves = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1),
                 "w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
        if e.keysym in moves:
            self.next_direction = moves[e.keysym]
        elif e.keysym.lower() == 'p':
            self.toggle_pause()

    def toggle_pause(self):
        if not self.running: return
        self.paused = not self.paused
        if self.paused:
            self.pause_btn.config(text="RESUME")
            self.canvas.create_text(COLS*CELL//2, ROWS*CELL//2, 
                                    text="PAUSED", fill="white", 
                                    font=("Arial Black", 30), tags="paused_text")
        else:
            self.pause_btn.config(text="PAUSE")
            self.canvas.delete("paused_text")

    def move_pacman(self):
        # Allow queueing turns (moves only apply when hitting a valid block path)
        dr, dc = self.next_direction
        nr, nc = self.pacman[0] + dr, self.pacman[1] + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and MAZE[nr][nc] != 1:
            self.direction = self.next_direction
        
        dr, dc = self.direction
        nr, nc = self.pacman[0] + dr, self.pacman[1] + dc
        
        # Stop at walls
        if 0 <= nr < ROWS and 0 <= nc < COLS and MAZE[nr][nc] != 1:
            self.pacman = [nr, nc]
            if (nr, nc) in self.dots:
                self.dots.remove((nr, nc))
                self.canvas.delete(f"dot_{nr}_{nc}")
                self.app.score += 10
                self.update_score_display()

    def move_ghosts(self):
        for g in self.ghosts:
            best = []
            dist = 9999
            
            # Simple AI: move towards pacman, but introduce some randomness
            options = []
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = g[0] + dr, g[1] + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and MAZE[nr][nc] != 1:
                    options.append((nr, nc))
                    
            if not options:
                continue
                
            for (nr, nc) in options:
                d = abs(nr - self.pacman[0]) + abs(nc - self.pacman[1])
                if d < dist:
                    dist = d
                    best = [(nr, nc)]
                elif d == dist:
                    best.append((nr, nc))
                    
            if best:
                # 20% chance to pick a random valid move instead of always the best move
                if random.random() < 0.2:
                    g[:] = random.choice(options)
                else:
                    g[:] = random.choice(best)

    def draw_entities(self):
        # Only delete dynamic elements
        self.canvas.delete("pacman", "ghost")
        r, c = self.pacman
        
        self.canvas.create_oval(
            c * CELL + 4, r * CELL + 4,
            c * CELL + CELL - 4, r * CELL + CELL - 4,
            fill="yellow", tags="pacman")

        for g in self.ghosts:
            gr, gc = g
            self.canvas.create_oval(
                gc * CELL + 4, gr * CELL + 4,
                gc * CELL + CELL - 4, gr * CELL + CELL - 4,
                fill=self.ghost_color, tags="ghost")

    def end_game(self, win):
        self.stop()
        self.canvas.delete("pacman", "ghost")
        msg = "LEVEL COMPLETE!" if win else "GAME OVER!"
        color = "lime" if win else "red"
        
        self.canvas.create_text(COLS*CELL//2, ROWS*CELL//2 - 20, 
                                text=msg, fill=color, 
                                font=("Arial Black", 30))
        
        if win:
            self.app.level += 1
            self.canvas.create_text(COLS*CELL//2, ROWS*CELL//2 + 30, 
                                    text="Starting next level...", fill="white", 
                                    font=("Arial", 16))
            self.after(2000, lambda: self.app.start_game(reset_score=False))
        else:
            self.canvas.create_text(COLS*CELL//2, ROWS*CELL//2 + 30, 
                                    text="Returning to home...", fill="white", 
                                    font=("Arial", 16))
            self.after(2000, lambda: self.app.show_screen(HomeScreen))

    def loop(self):
        if not self.running:
            return

        if not self.paused:
            self.move_pacman()
            self.move_ghosts()
            self.draw_entities()

            # Collision check
            pacman_pos = tuple(self.pacman)
            if any(tuple(g) == pacman_pos for g in self.ghosts):
                self.end_game(win=False)
                return

            if not self.dots:
                self.end_game(win=True)
                return

        self.loop_id = self.after(self.delay, self.loop)

if __name__ == "__main__":
    app = App()
    app.mainloop()
