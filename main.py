from tkinter import *
from tkinter import ttk

# create a Basic calculator
root = Tk()
root.resizable(False, False)
root.title("Basic calculator.")
# -----------------Global variable---------#
total = 0
number = "0"

# ---------------- Add a frame layer ------------#
frame_1 = Frame(root).grid(column=0, row=0, columnspan=3)

# -------------Create an entry field

entry = Entry(frame_1, width=45, borderwidth=5)
entry.grid(column=0, row=0, columnspan=3, pady=10, padx=5)
entry.insert(0, "0")


# ----------- When numbers button clicked
def number_clicked(num):
    global number
    entry.delete(0, END)
    if number == "0":
        entry.delete(0, END)
        number = str(num)
        entry.insert(0, number)
    else:
        number += str(num)
        entry.insert(0, number)


# ----------- Here the addition operator
def add_numbers():
    global total, number
    try:
        if number == "0":
            entry.insert(0, number)
    except ValueError:
        entry.insert(0, "0")
    else:
        add_to = int(number)
        total += add_to
        number = "0"
        entry.delete(0, END)
        entry.insert(0, "0")


# ------------ Here return the total from your addition .
def total_addition():
    global total
    add_numbers()
    entry.delete(0, END)
    entry.insert(0, str(total))

# ------------Clear the calculator
def clear_entry():
    global total, number
    total = 0
    number = "0"
    entry.delete(0, END)
    entry.insert(0, number)


# my_tabs.add(root, text="tab one")

number_1_b = Button(frame_1, text="1", width=10, height=2, command=lambda: number_clicked(1))
number_1_b.grid(column=0, row=1, pady=3)

number_2_b = Button(frame_1, text="2", width=10, height=2, command=lambda: number_clicked(2))
number_2_b.grid(column=1, row=1, pady=3)

number_3_b = Button(frame_1, text="3", width=10, height=2, command=lambda: number_clicked(3))
number_3_b.grid(column=2, row=1, pady=3)

number_4_b = Button(frame_1, text="4", width=10, height=2, command=lambda: number_clicked(4))
number_4_b.grid(column=0, row=2, pady=3)

number_5_b = Button(frame_1, text="5", width=10, height=2, command=lambda: number_clicked(5))
number_5_b.grid(column=1, row=2, pady=3)

number_6_b = Button(frame_1, text="6", width=10, height=2, command=lambda: number_clicked(6))
number_6_b.grid(column=2, row=2, pady=3)

number_7_b = Button(frame_1, text="7", width=10, height=2, command=lambda: number_clicked(7))
number_7_b.grid(column=0, row=3, pady=3)

number_8_b = Button(frame_1, text="8", width=10, height=2, command=lambda: number_clicked(8))
number_8_b.grid(column=1, row=3, pady=3)

number_9_b = Button(frame_1, text="9", width=10, height=2, command=lambda: number_clicked(9))
number_9_b.grid(column=2, row=3, pady=3)

number_0_b = Button(frame_1, text="0", width=10, height=2, command=lambda: number_clicked(0))
number_0_b.grid(column=1, row=4, pady=3)

add_button_b = Button(frame_1, text="+", width=10, height=2, command=add_numbers)
add_button_b.grid(column=0, row=4, pady=3)

clear_b = Button(frame_1, text="Clear", width=10, height=2, command=clear_entry)
clear_b.grid(column=2, row=4, pady=3)

equal_button_b = Button(frame_1, text="=", width=38, height=2, command=total_addition)
equal_button_b.grid(column=0, row=5, columnspan=3, pady=3)

root.mainloop()
