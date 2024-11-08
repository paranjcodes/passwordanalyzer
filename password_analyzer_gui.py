import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    strength_score = 0
    criteria = []

    if len(password) >= 12:
        strength_score += 1
        criteria.append("✔️ Sufficient length (>=12 characters)")
    else:
        criteria.append("❌ Too short")

    if re.search(r'[a-z]', password):
        strength_score += 1
        criteria.append("✔️ Lowercase letters")
    else:
        criteria.append("❌ No lowercase")

    if re.search(r'[A-Z]', password):
        strength_score += 1
        criteria.append("✔️ Uppercase letters")
    else:
        criteria.append("❌ No uppercase")

    if re.search(r'\d', password):
        strength_score += 1
        criteria.append("✔️ Digits")
    else:
        criteria.append("❌ No digits")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
        criteria.append("✔️ Special characters")
    else:
        criteria.append("❌ No special chars")

    if strength_score == 5:
        return "Very Strong", criteria
    elif strength_score >= 3:
        return "Moderate", criteria
    else:
        return "Weak", criteria

def analyze_password():
    password = entry.get()
    strength, criteria = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")
    analysis_list.delete(0, tk.END)
    for crit in criteria:
        analysis_list.insert(tk.END, crit)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Analyzer")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Enter Password:").grid(row=0, column=0)
entry = tk.Entry(frame, show='*', width=30)
entry.grid(row=0, column=1)

analyze_btn = tk.Button(frame, text="Analyze", command=analyze_password)
analyze_btn.grid(row=1, columnspan=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=2, columnspan=2)

analysis_list = tk.Listbox(frame, width=50)
analysis_list.grid(row=3, columnspan=2, pady=10)

root.mainloop()

