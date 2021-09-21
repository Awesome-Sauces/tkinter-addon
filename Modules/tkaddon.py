from tkinter import *
# Tk Addons Parent Class
class tka_parent():
    # Error Class
    class tkaError(Exception):
        def __init__(self, msg):
            super().__init__(msg)
    def __init__(self, placement="NULL"):
        self.placement = placement
        self.row = 0
        self.column = 0
    def convert(self):
        self.row = int(self.placement[5:6])
        self.column = int(self.placement[7:8])
        return self.row, self.column

# All functions
class tka(tka_parent):
    # entry volume
    def entry(placement, tab):
        if placement[0:4] == "grid":
            grid_location = tka(placement)
            row, column = grid_location.convert()
            entry = Entry(tab)
            entry.grid(row=column, column=row)
            return entry
        elif placement[0:4] == "pack":
            entry = Entry(tab)
            entry.pack()
            return entry
        else:
            raise tka_parent.tkaError("Error!")
    # button volume
<<<<<<< Updated upstream
    def button(placement, tab, text, command="Insert Function Name Here"):
=======
    def button(placement, tab, text, command="Insert Function Name Here!"):
>>>>>>> Stashed changes
        if placement[0:4] == "grid":
            grid_location = tka(placement)
            row, column = grid_location.convert()
            button = Button(tab, text=text, command=command)
            button.grid(row=row, column=column)
            return button
        elif placement[0:4] == "pack":
            button = Button(tab, text=text, command=command)
            button.pack()
            return button
        else:
            raise tka_parent.tkaError("Error!")
    # label volume
    def label(placement, tab, text):
        if placement[0:4] == "grid":
            grid_location = tka(placement)
            row, column = grid_location.convert()
            label = Label(tab, text=text)
            label.grid(row=row, column=column)
            return label
        elif placement[0:4] == "pack":
            label = Label(tab, text=text)
            label.pack()
            return label
        else:
            raise tka_parent.tkaError("Error!")
