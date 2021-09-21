from tkinter import *
from tkaddon import *
root = Tk()

def Hello():
    print("Hello World")

#tka_entry = tka.entry("grid", root)
#tka_entry.insert(0, "WHAT")
#print(tka_entry.get())
tka_button = tka.button("pack 0 1", root, "Hello", Hello)
root.mainloop()



