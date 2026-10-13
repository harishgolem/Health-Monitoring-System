import tkinter as tk
from tkinter import ttk, messagebox
import math, random

def generate_signal():
    points = []
    for i in range(240):
        t = i / 20
        y = 0.55*math.sin(2*math.pi*8*t) + 0.22*math.sin(2*math.pi*2*t) + random.uniform(-0.18, 0.18)
        points.append(y)
    return points

def draw():
    canvas.delete("all")
    w = max(canvas.winfo_width(), 500)
    h = max(canvas.winfo_height(), 250)
    vals = generate_signal()
    canvas.create_line(0, h/2, w, h/2, fill="#9ca3af", dash=(3, 4))
    coords = []
    for i, v in enumerate(vals):
        coords.extend([i*w/(len(vals)-1), h/2 - v*h*0.32])
    canvas.create_line(*coords, fill="#2563eb", width=2, smooth=True)
    status.set("Demo signal generated. This is simulated data, not a real EEG recording.")

root = tk.Tk()
root.title("NeuroPulse — EEG Signal Explorer")
root.geometry("820x520")
root.minsize(650, 420)
ttk.Label(root, text="NeuroPulse", font=("Segoe UI", 22, "bold")).pack(pady=(16, 2))
ttk.Label(root, text="A beginner demo for exploring brain-signal patterns").pack()
ttk.Label(root, text="IMPORTANT: Simulated signal only. Not a medical tool and does not diagnose ADHD or any condition.",
          foreground="#b91c1c", wraplength=760).pack(pady=10)
canvas = tk.Canvas(root, bg="white", height=280, highlightthickness=1, highlightbackground="#d1d5db")
canvas.pack(fill="both", expand=True, padx=18, pady=8)
status = tk.StringVar(value="Click Generate demo signal to begin.")
ttk.Label(root, textvariable=status, wraplength=760).pack(pady=5)
ttk.Button(root, text="Generate demo signal", command=draw).pack(pady=(4, 16))
root.mainloop()
