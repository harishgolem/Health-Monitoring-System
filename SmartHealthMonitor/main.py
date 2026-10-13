import tkinter as tk
from tkinter import ttk
import random, datetime

def update_readings():
    pulse = random.randint(65, 95)
    spo2 = random.randint(95, 100)
    temp = round(random.uniform(36.2, 37.2), 1)
    pulse_var.set(f"{pulse} bpm")
    spo2_var.set(f"{spo2}%")
    temp_var.set(f"{temp} °C")
    time_var.set("Updated: " + datetime.datetime.now().strftime("%H:%M:%S"))
    status_var.set("SIMULATED readings only. Not measured from a person.")
    canvas.delete("all")
    canvas.create_text(18, 18, anchor="nw", text="Demo pulse trend (simulated)", font=("Segoe UI", 11, "bold"), fill="#111827")
    vals = [random.randint(65, 95) for _ in range(24)]
    w = max(canvas.winfo_width(), 500)
    h = max(canvas.winfo_height(), 130)
    coords = []
    for i, val in enumerate(vals):
        x = 20 + i*(w-40)/(len(vals)-1)
        y = h-20-(val-55)/50*(h-60)
        coords.extend([x, y])
    canvas.create_line(*coords, fill="#0f766e", width=2, smooth=True)
    for i in range(0, len(coords), 2):
        canvas.create_oval(coords[i]-2, coords[i+1]-2, coords[i]+2, coords[i+1]+2, fill="#0f766e", outline="")

root = tk.Tk()
root.title("Smart Health Monitor — Sensor Dashboard Demo")
root.geometry("820x560")
root.minsize(650, 450)
ttk.Label(root, text="Smart Health Monitor", font=("Segoe UI", 22, "bold")).pack(pady=(16, 2))
ttk.Label(root, text="A dashboard concept for physiological measurements").pack()
ttk.Label(root, text="DEMO ONLY: All readings are randomly simulated; no sensor is connected and these values are not health advice.",
          foreground="#b91c1c", wraplength=760).pack(pady=10)
cards = ttk.Frame(root)
cards.pack(fill="x", padx=18, pady=8)
pulse_var, spo2_var, temp_var = tk.StringVar(value="—"), tk.StringVar(value="—"), tk.StringVar(value="—")
for col, (label, var) in enumerate([("Pulse", pulse_var), ("SpO₂", spo2_var), ("Temperature", temp_var)]):
    frame = ttk.LabelFrame(cards, text=label, padding=16)
    frame.grid(row=0, column=col, sticky="nsew", padx=5)
    ttk.Label(frame, textvariable=var, font=("Segoe UI", 17, "bold")).pack()
    cards.columnconfigure(col, weight=1)
canvas = tk.Canvas(root, bg="white", height=190, highlightthickness=1, highlightbackground="#d1d5db")
canvas.pack(fill="both", expand=True, padx=18, pady=8)
time_var = tk.StringVar(value="")
status_var = tk.StringVar(value="Click Refresh demo readings.")
ttk.Label(root, textvariable=time_var).pack()
ttk.Label(root, textvariable=status_var, foreground="#b91c1c", wraplength=760).pack(pady=4)
ttk.Button(root, text="Refresh demo readings", command=update_readings).pack(pady=(4, 16))
root.mainloop()
