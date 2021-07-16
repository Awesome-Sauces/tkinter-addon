from tkinter import *
from PIL import ImageTk,Image
global TkAddonImage
TkAddonImage = 'IMAGE.TKADDON'



def button(varname, tab, text, row=0, column=0):
    varname = Button(tab, text=text)
    varname.grid(row=row, column=column)
    
def entry(varname, tab, text, row=0, column=0):
    varname = Entry(tab, text=text)
    varname.grid(row=row, column=column)
    varname.insert(0, text)
    
def label(varname, tab, text, row=0, column=0):
    varname = Label(tab, text=text)
    varname.grid(row=row, column=column)
    
def image(varname, tab, filename, row=0, column=0):
    TkAddonImage = ImageTk.PhotoImage(Image.open(filename))
    varname = Label(tab, image=TkAddonImage)
    varname.grid(row=row, column=column)
    print()