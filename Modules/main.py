from tkinter import *
from tkaddon import *
root = Tk()
def HelloWorld():
    print("Hello World!")
tka_buttonA = tka.button(placement="grid 0 1", tab=root, text="Hello", command=HelloWorld)
tka_buttonB = tka.button(placement="grid 0 2", tab=root, text="Hello", command=HelloWorld)
tka_buttonC = tka.button(placement="grid 2 0", tab=root, text="Hello", command=HelloWorld)
root.mainloop()





