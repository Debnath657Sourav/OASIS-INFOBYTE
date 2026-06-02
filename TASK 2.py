import random
import string

print("===== Password Generator =====")

# Password length
length = int(input("Enter password length: "))

# Character preferences
use_lower = input("Include lowercase letters? (y/n): ").lower()
use_upper = input("Include uppercase letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

# Build character pool
characters = ""

if use_lower == "y":
    characters += string.ascii_lowercase

if use_upper == "y":
    characters += string.ascii_uppercase

if use_numbers == "y":
    characters += string.digits

if use_symbols == "y":
    characters += string.punctuation

# Check if at least one character type is selected
if not characters:
    print("Error: You must select at least one character type.")
else:
    password = "".join(random.choice(characters) for _ in range(length))

    print("\nGenerated Password:")
    print(password)
import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate Password
def generate_password():

    length = length_var.get()

    chars = ""

    if lower_var.get():
        chars += string.ascii_lowercase

    if upper_var.get():
        chars += string.ascii_uppercase

    if number_var.get():
        chars += string.digits

    if symbol_var.get():
        chars += string.punctuation

    if chars == "":
        messagebox.showerror(
            "Error",
            "Select at least one character type!"
        )
        return

    password = ''.join(
        random.choice(chars)
        for _ in range(length)
    )

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check_strength(password)


# Password Strength Checker
def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Strength: Weak")
    elif score <= 4:
        strength_label.config(text="Strength: Medium")
    else:
        strength_label.config(text="Strength: Strong")


# Copy Password
def copy_password():

    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)

        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )


# Security Rule Check
def validate_password():

    password = password_entry.get()

    issues = []

    if len(password) < 8:
        issues.append("Minimum 8 characters")

    if not any(c.isupper() for c in password):
        issues.append("Add uppercase letter")

    if not any(c.islower() for c in password):
        issues.append("Add lowercase letter")

    if not any(c.isdigit() for c in password):
        issues.append("Add number")

    if not any(c in string.punctuation for c in password):
        issues.append("Add symbol")

    if issues:
        messagebox.showwarning(
            "Security Check",
            "\n".join(issues)
        )
    else:
        messagebox.showinfo(
            "Security Check",
            "Password meets all security rules!"
        )


# GUI Window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x450")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Advanced Password Generator",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# Length Selection
tk.Label(
    root,
    text="Password Length"
).pack()

length_var = tk.IntVar(value=12)

length_spin = tk.Spinbox(
    root,
    from_=4,
    to=50,
    textvariable=length_var,
    width=10
)
length_spin.pack(pady=5)

# Character Options
lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Include Lowercase",
    variable=lower_var
).pack()

tk.Checkbutton(
    root,
    text="Include Uppercase",
    variable=upper_var
).pack()

tk.Checkbutton(
    root,
    text="Include Numbers",
    variable=number_var
).pack()

tk.Checkbutton(
    root,
    text="Include Symbols",
    variable=symbol_var
).pack()

# Generate Button
tk.Button(
    root,
    text="Generate Password",
    command=generate_password
).pack(pady=10)

# Password Display
password_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)
password_entry.pack(pady=5)

# Strength Label
strength_label = tk.Label(
    root,
    text="Strength: Not Generated",
    font=("Arial", 11)
)
strength_label.pack(pady=5)

# Copy Button
tk.Button(
    root,
    text="Copy to Clipboard",
    command=copy_password
).pack(pady=5)

# Security Check Button
tk.Button(
    root,
    text="Validate Password",
    command=validate_password
).pack(pady=5)

root.mainloop()
