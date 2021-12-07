from tkinter import *
from tkinter import ttk

# ------------Day 1--------------------#
# create a normal calculator
root = Tk()
# root.minsize(width=300, height=300)
# root.geometry("300x300+700+200")
root.resizable(False, False)
root.title("Basic calculator.")
my_tabs = ttk.Notebook(root)
total = 0
number = "0"
frame_1 = Frame(root).grid(column=0, row=0, columnspan=3)

entry = Entry(frame_1, width=45, cursor="arrow", justify="left", exportselection=False, borderwidth=5)
entry.grid(column=0, row=0, columnspan=3, pady=10, padx=5)
entry.insert(0, "0")


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




def total_addition():
    global total
    add_numbers()
    entry.delete(0, END)
    entry.insert(0, str(total))


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
# ----------Later
# window = Tk()
# window.title("E-mail Automation V1.0")
# # ----Adjust where your window will appear.
# window.geometry('600x500+600+200')
# window.minsize(width=700, height=500)
# # ----------Do not let user to resize the window.
# window.resizable(False, False)
# # ------------Create the tabs from Network class from ttk module.
# my_notebook = ttk.Notebook(window)
# my_notebook.grid(column=0, row=0, columnspan=3)
#
#
# # -----------My question is do I can mix between pack and grid? The answer was just one layout system.
#
# def return_tab():
#     my_notebook.select(0)
#
#
# def select():
#     my_notebook.select(1)
#     window.after(1000, return_tab)
#
#
# my_frame1 = Frame(my_notebook, width=700, height=500, bg="blue")
# my_frame2 = Frame(my_notebook, width=700, height=500, bg="red")
#
# my_notebook.add(my_frame1, text="My blue tab")
# my_notebook.add(my_frame2, text="My red tab")
#
# blue_button = Button(my_frame1, text="Click me", command=select).grid(column=0, row=2)
#
# red_button = Button(my_frame2, text="Click me").grid(column=1, row=3)
#
# window.mainloop()
