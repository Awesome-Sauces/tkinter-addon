from tkinter import *

class CantTakeInteger(ValueError):
    pass

class CantTakeString(ValueError):
    pass

class TkAddonGrid():
    def button(tab='%s', text='Button', command='gPack', row=0, column=0, varname='varname'):
        if type(varname) == int:
            raise CantTakeInteger
        else:
            if type(row) == str:
                raise CantTakeVariable
            else:
                if type(column) == str:
                    raise CantTakeVariable
                else:
                    varname = Button(tab, text=text)
                    varname.grid(row=row, column=column)

    def label(tab='%s', text='Label', row=0, column=0, varname='varname'):
        if type(varname) == int:
            raise CantTakeInteger
        else:
            if type(row) == str:
                raise CantTakeVariable
            else:
                if type(column) == str:
                    raise CantTakeString
                else:
                    varname = Label(tab, text=text)
                    varname.grid(row=row, column=column)
    
    def entry(tab='%s', text='Entry', row=0, column=0, varname='varname'):
        if type(varname) == int:
            raise CantTakeInteger
        else:
            if type(row) == str:
                raise CantTakeVariable
            else:
                if type(column) == str:
                    raise CantTakeString
                else:
                    NONE = 'NONE'
                    varname = Entry(tab, text=text)
                    varname.grid(row=row, column=column)
                    if text == NONE:
                        print('hello world')
                    else:
                        varname.insert(0, text)
                    
#----------------------------------------------------------------------------------------------------------#   
# TkAddonPack
class TkAddonPack():
    def button(tab='%s', text='Button', command='cPack' , varname='varname'):
        if type(varname) == int:
            raise CantTakeInteger
        else:
            varname = Button(tab, text=text)
            varname.pack()
        
    def label(tab='%s', text='Button', varname='varname'):
        if type(varname) == int:
            raise CantTakeInteger
        else:
            varname = Label(tab, text=text)
            varname.pack()
    
    def entry(tab='%s', text='Button', varname='varname'):
        if type(varname) == int:
            raise CantTakeInteger
        else:
            varname = Entry(tab, text=text)
            varname.pack()
            varname.insert(0, text)
