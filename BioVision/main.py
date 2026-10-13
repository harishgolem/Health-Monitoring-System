import tkinter as tk
from tkinter import ttk
import random

def make_image():
    canvas.delete("all")
    w = max(canvas.winfo_width(), 500)
    h = max(canvas.winfo_height(), 260)
    canvas.create_rectangle(0, 0, w, h, fill="#101827", outline="")
    # Synthetic abstract image-like shapes, not a real medical image.
    for _ in range(90):
        x, y = random.randint(15, w-15), random.randint(15, h-15)
        r = random.randint(2, 11)
        color = random.choice(["#64748b", "#94a3b8", "#cbd5e1", "#475569"])
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline="")
    result.set("Demo visualization created from random shapes — no patient image or diagnosis is involved.")

root = tk.Tk()
root.title("BioVision — Medical Image Learning Demo")
root.geometry("820x540")
root.minsize(650, 430)
ttk.Label(root, text="BioVision", font=("Segoe UI", 22, "bold")).pack(pady=(16, 2))
ttk.Label(root, text="A starter interface for medical-image computing concepts").pack()
ttk.Label(root, text="DEMO ONLY: This screen uses synthetic shapes, not medical scans. No diagnosis or clinical prediction.",
          foreground="#b91c1c", wraplength=760).pack(pady=10)
canvas = tk.Canvas(root, bg="#101827", height=300, highlightthickness=1, highlightbackground="#d1d5db")
canvas.pack(fill="both", expand=True, padx=18, pady=8)
result = tk.StringVar(value="Click Create demo visualization.")
ttk.Label(root, textvariable=result, wraplength=760).pack(pady=5)
ttk.Button(root, text="Create demo visualization", command=make_image).pack(pady=(4, 16))
root.mainloop()
