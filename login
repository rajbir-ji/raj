import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
import sqlite3
import os

# === DATABASE SETUP ===
DB_FILE = 'quiz_registrations.db'
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll TEXT NOT NULL,
            UNIQUE(name, roll)
        )
    ''')
    conn.commit()
    conn.close()

def is_registered(name, roll):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM students WHERE name=? AND roll=?', (name, roll))
    res = c.fetchone()
    conn.close()
    return res is not None

def register_student(name, roll):
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('INSERT INTO students (name, roll) VALUES (?, ?)', (name, roll))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

# === GUI AND ANIMATION ===
def animate_bar(bar, direction=[1]):
    x = bar.winfo_x()
    if x > 220:
        direction[0] = -1
    elif x < 10:
        direction[0] = 1
    bar.place(x=x+direction[0]*4)
    bar.after(10, lambda: animate_bar(bar, direction))

def login():
    name = name_var.get().strip()
    roll = roll_var.get().strip()
    if not name or not roll:
        messagebox.showerror("Error", "Please fill all fields.")
        return
    if is_registered(name, roll):
        messagebox.showinfo("Already Registered", f"{name} (Roll: {roll}) has already registered for the quiz.")
    else:
        if register_student(name, roll):
            messagebox.showinfo("Success", f"Hello {name}! You are now registered for the quiz.")
        else:
            messagebox.showerror("Error", "Registration failed. Please try again.")

# === MAIN APP ===
init_db()

root = tk.Tk()
root.title("Quiz Competition Registration")
root.geometry("400x350")
root.resizable(False, False)

style = Style(theme="cyborg")
frame = tk.Frame(root, bg="#191970")
frame.place(relwidth=1, relheight=1)

heading = tk.Label(frame, text="Quiz Competition Registration", font=("Arial", 17, "bold"), bg="#191970", fg="#fff")
heading.pack(pady=30)

# Animated bar
bar = tk.Label(frame, bg="#00BFFF", width=20, height=1)
bar.place(x=10, y=70)
animate_bar(bar)

name_var = tk.StringVar()
roll_var = tk.StringVar()

tk.Label(frame, text="Student Name", bg="#191970", fg="#fff", font=("Arial", 12)).pack(pady=10)
tk.Entry(frame, textvariable=name_var, font=("Arial", 12)).pack(pady=5)

tk.Label(frame, text="Roll Number", bg="#191970", fg="#fff", font=("Arial", 12)).pack(pady=10)
tk.Entry(frame, textvariable=roll_var, font=("Arial", 12)).pack(pady=5)

tk.Button(frame, text="Register", command=login, font=("Arial", 12), bg="#00BFFF", fg="#fff").pack(pady=30)

root.mainloop()