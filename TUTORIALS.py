#INCOME TAX
#INVESTMENT
#FACTORIAL
#FIBONACCI
#ARMSTRONG
#SQUARE ROOT
#PRIME
#CAESAR CIPHER
#BINARY TO DECIMAL
#STRING
#REVERSE STRING
#PALINDROME
import tkinter as tk
from tkinter import messagebox
import math

# ================== FUNCTIONS ==================
def income_tax():
    win = tk.Toplevel(root)
    win.title("Income Tax")

    tk.Label(win, text="Income").pack()
    income_entry = tk.Entry(win)
    income_entry.pack()

    tk.Label(win, text="Dependents").pack()
    dep_entry = tk.Entry(win)
    dep_entry.pack()

    tk.Label(win, text="Exemption Amount").pack()
    ex_entry = tk.Entry(win)
    ex_entry.pack()

    def compute():
        income = float(income_entry.get())
        dependents = int(dep_entry.get())
        exemption = float(ex_entry.get())

        taxable = income - (dependents * exemption)

        if taxable <= 250000:
            tax = 0
        elif taxable <= 500000:
            tax = (taxable - 250000) * 0.05
        elif taxable <= 1000000:
            tax = 12500 + (taxable - 500000) * 0.2
        else:
            tax = 112500 + (taxable - 1000000) * 0.3

        messagebox.showinfo("Result", "Tax = ₹" + str(tax))

    tk.Button(win, text="Compute", command=compute).pack()


def investment():
    win = tk.Toplevel(root)
    win.title("Investment")

    tk.Label(win, text="Enter Principal").pack()
    e = tk.Entry(win)
    e.pack()

    def calc():
        p = float(e.get())
        r, t = 5, 2
        si = (p * r * t) / 100
        messagebox.showinfo("Result", f"Simple Interest = ₹{si}")

    tk.Button(win, text="Calculate", command=calc).pack()


def factorial():
    win = tk.Toplevel(root)
    win.title("Factorial")

    tk.Label(win, text="Enter Number").pack()
    e = tk.Entry(win)
    e.pack()

    tk.Button(
        win, text="Find",
        command=lambda: messagebox.showinfo("Result", math.factorial(int(e.get())))
    ).pack()


def fibonacci():
    win = tk.Toplevel(root)
    win.title("Fibonacci")

    tk.Label(win, text="Enter Limit").pack()
    e = tk.Entry(win)
    e.pack()

    def gen():
        n = int(e.get())
        a, b = 0, 1
        seq = []
        for _ in range(n):
            seq.append(str(a))
            a, b = b, a + b
        messagebox.showinfo("Result", ", ".join(seq))

    tk.Button(win, text="Generate", command=gen).pack()


def armstrong():
    win = tk.Toplevel(root)
    win.title("Armstrong")

    tk.Label(win, text="Enter Number").pack()
    e = tk.Entry(win)
    e.pack()

    def check():
        n = e.get()
        power = len(n)
        total = sum(int(d) ** power for d in n)
        messagebox.showinfo(
            "Result", "Armstrong" if total == int(n) else "Not Armstrong"
        )

    tk.Button(win, text="Check", command=check).pack()


def square_root():
    win = tk.Toplevel(root)
    win.title("Square Root")

    tk.Label(win, text="Enter Number").pack()
    e = tk.Entry(win)
    e.pack()

    tk.Button(
        win, text="Find",
        command=lambda: messagebox.showinfo("Result", math.sqrt(float(e.get())))
    ).pack()


def prime():
    win = tk.Toplevel(root)
    win.title("Prime")

    tk.Label(win, text="Enter Number").pack()
    e = tk.Entry(win)
    e.pack()

    def check():
        n = int(e.get())
        if n < 2:
            messagebox.showinfo("Result", "Not Prime")
            return
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                messagebox.showinfo("Result", "Not Prime")
                return
        messagebox.showinfo("Result", "Prime")

    tk.Button(win, text="Check", command=check).pack()


def caesar():
    win = tk.Toplevel(root)
    win.title("Caesar Cipher")

    tk.Label(win, text="Enter Text").pack()
    e = tk.Entry(win)
    e.pack()

    def encrypt():
        text = e.get()
        res = ""
        for c in text:
            if c.isalpha():
                base = ord('a') if c.islower() else ord('A')
                res += chr((ord(c) - base + 3) % 26 + base)
            else:
                res += c
        messagebox.showinfo("Result", res)

    tk.Button(win, text="Encrypt", command=encrypt).pack()


def binary_decimal():
    win = tk.Toplevel(root)
    win.title("Binary to Decimal")

    tk.Label(win, text="Enter Binary").pack()
    e = tk.Entry(win)
    e.pack()

    tk.Button(
        win, text="Convert",
        command=lambda: messagebox.showinfo("Result", int(e.get(), 2))
    ).pack()


def string_ops():
    win = tk.Toplevel(root)
    win.title("String Operations")

    tk.Label(win, text="Enter String").pack()
    e = tk.Entry(win)
    e.pack()

    tk.Button(win, text="Length",
              command=lambda: messagebox.showinfo("Result", len(e.get()))).pack()

    tk.Button(win, text="Reverse",
              command=lambda: messagebox.showinfo("Result", e.get()[::-1])).pack()

    tk.Button(win, text="Palindrome",
              command=lambda: messagebox.showinfo(
                  "Result", "Palindrome" if e.get() == e.get()[::-1] else "Not Palindrome"
              )).pack()

# ================== MAIN MENU ==================

root = tk.Tk()
root.title("Python Math & String Programs")
root.geometry("350x500")

tk.Label(root, text="Select Program", font=("Arial", 14, "bold")).pack(pady=10)

buttons = [
    ("Income Tax", income_tax),
    ("Investment", investment),
    ("Factorial", factorial),
    ("Fibonacci", fibonacci),
    ("Armstrong", armstrong),
    ("Square Root", square_root),
    ("Prime", prime),
    ("Caesar Cipher", caesar),
    ("Binary to Decimal", binary_decimal),
    ("String Operations", string_ops)
]

for txt, cmd in buttons:
    tk.Button(root, text=txt, width=25, command=cmd).pack(pady=4)

root.mainloop()

