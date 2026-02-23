import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Smart To-Do Planner")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

def update_clock():
    time_label.config(text=datetime.now().strftime("%H:%M:%S"))
    root.after(1000, update_clock)

def add_task():
    task = task_entry.get()
    priority = priority_var.get()

    if task:
        listbox.insert(tk.END, task)
        index = listbox.size() - 1

        if priority == "High":
            listbox.itemconfig(index, bg="red", fg="white")
        elif priority == "Medium":
            listbox.itemconfig(index, bg="yellow")
        else:
            listbox.itemconfig(index, bg="lightgreen")

        task_entry.delete(0, tk.END)

def delete_task():
    try:
        listbox.delete(listbox.curselection())
    except:
        pass

time_label = tk.Label(root, font=("Arial", 20), bg="#f0f0f0", fg="blue")
time_label.pack(pady=10)
update_clock()

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

priority_var = tk.StringVar(value="Medium")
priority_menu = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_menu.pack()

add_btn = tk.Button(root, text="Add Task", bg="green", fg="white", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Selected", bg="red", fg="white", command=delete_task)
delete_btn.pack()

root.mainloop()
