from tkinter import *
# Error Class
class tkaError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
# All functions
class tka():
    # entry volume
    def entry(placement, tab, row=0, column=0):
        if placement[0:4] == "grid":
            row = int(placement[5:6])
            column = int(placement[7:8])
            entry = Entry(tab)
            entry.grid(row=column, column=row)
            return entry
        elif placement == "pack":
            entry = Entry(tab)
            entry.pack()
            return entry
    # button volume
    def button(placement, tab, textit):
        if placement[0:4] == "grid":
            row = int(placement[5:6])
            column = int(placement[7:8])
            button = Button(tab, text=textit)
            button.grid(row=row, column=column)
            return button
        elif placement[0:4] == "pack":
            button = Button(tab, text="test")
            button.pack()
            return button
    # label volume
    def label(placement, tab, row=0, column=0):
        if placement[0:4] == "grid":
            row = int(placement[5:6])
            column = int(placement[7:8])
            label = Label(tab)
            label.grid(row=row, column=column)
            return label
        elif placement == "pack":
            label = Label(tab)
            label.pack()
            return label