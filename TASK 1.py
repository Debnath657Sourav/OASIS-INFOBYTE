weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print("\nYour BMI is:", round(bmi, 2))

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal Weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("Category:", category)
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

# Optional Graph Library
try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False


# ---------------- BMI Calculation ---------------- #

def calculate_bmi():

    try:
        name = name_entry.get()

        if name == "":
            messagebox.showerror("Error", "Enter Name")
            return

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI = {bmi:.2f}\nCategory = {category}"
        )

        save_data(name, weight, height, bmi, category)

    except:
        messagebox.showerror(
            "Error",
            "Enter valid inputs"
        )


# ---------------- Save Data ---------------- #

def save_data(name, weight, height, bmi, category):

    file_exists = os.path.isfile("bmi_data.csv")

    with open("bmi_data.csv", "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Name",
                "Weight",
                "Height",
                "BMI",
                "Category"
            ])

        writer.writerow([
            datetime.now().strftime("%d-%m-%Y"),
            name,
            weight,
            height,
            round(bmi, 2),
            category
        ])


# ---------------- View History ---------------- #

def view_history():

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")

    tree = ttk.Treeview(
        history_window,
        columns=(
            "Date",
            "Name",
            "Weight",
            "Height",
            "BMI",
            "Category"
        ),
        show="headings"
    )

    for col in tree["columns"]:
        tree.heading(col, text=col)

    tree.pack(fill="both", expand=True)

    if os.path.exists("bmi_data.csv"):

        with open("bmi_data.csv", "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:
                tree.insert("", tk.END, values=row)


# ---------------- Statistics ---------------- #

def show_statistics():

    if not os.path.exists("bmi_data.csv"):
        messagebox.showinfo(
            "Info",
            "No data available"
        )
        return

    bmi_values = []

    with open("bmi_data.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:
            bmi_values.append(float(row[4]))

    average = sum(bmi_values) / len(bmi_values)

    messagebox.showinfo(
        "Statistics",
        f"Total Records: {len(bmi_values)}\nAverage BMI: {average:.2f}"
    )


# ---------------- Graph ---------------- #

def show_graph():

    if not MATPLOTLIB_AVAILABLE:
        messagebox.showerror(
            "Error",
            "Matplotlib not installed.\nRun:\npip install matplotlib"
        )
        return

    if not os.path.exists("bmi_data.csv"):
        return

    names = []
    bmi_values = []

    with open("bmi_data.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:
            names.append(row[1])
            bmi_values.append(float(row[4]))

    plt.figure(figsize=(8, 5))
    plt.plot(names, bmi_values, marker='o')
    plt.title("BMI Trend Analysis")
    plt.xlabel("Users")
    plt.ylabel("BMI")
    plt.grid(True)
    plt.show()


# ---------------- GUI ---------------- #

root = tk.Tk()

root.title("Advanced BMI Calculator")
root.geometry("500x500")

title = tk.Label(
    root,
    text="Advanced BMI Calculator",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)

tk.Label(root, text="Name").pack()

name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Weight (kg)").pack()

weight_entry = tk.Entry(root, width=30)
weight_entry.pack()

tk.Label(root, text="Height (m)").pack()

height_entry = tk.Entry(root, width=30)
height_entry.pack()

tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="lightgreen"
).pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)

result_label.pack(pady=10)

tk.Button(
    root,
    text="View History",
    command=view_history
).pack(pady=5)

tk.Button(
    root,
    text="Statistics",
    command=show_statistics
).pack(pady=5)

tk.Button(
    root,
    text="BMI Trend Graph",
    command=show_graph
).pack(pady=5)

root.mainloop()
