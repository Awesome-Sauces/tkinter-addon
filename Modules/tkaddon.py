from tkinter import *

def HelloWrld():
    print('Hello World')

class TkAddonGrid():
    def button(tab=1, text='TkAddons!', command=HelloWrld, row=0, column=0, varname='varname'):
        class TkAddonButtonERROR(Exception):
            def __init__(self, msg):
                super().__init__(msg)
        
        
        class TkAddonButton:
            def __init__(self,  tab='e', text='1', command='TkAddonGrid.HelloWrld', row=0, column=0, varname='varname'):
                self.__tab = tab
                self.__text = text
                self.__command = command
                self.__row = row
                self.__column = column
                self.__varname = varname
                
            def ButtonExceptions(self):
                tab_str = str(self.__tab)
                res = any(chr.isdigit() for chr in tab_str)
                if type(self.__tab) == int:
                    raise TkAddonButtonERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert Integer')
                elif str(res) == 'True':
                    raise TkAddonButtonERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert digit in string')
                elif type(self.__text) == int:
                    raise TkAddonButtonERROR('TextValue: ' + str(self.__text) + ' <---' + ' Can\'t insert Integer')
                elif type(self.__command) == int:
                    raise TkAddonButtonERROR('CommandValue: ' + str(self.__command) + ' <---' + ' Can\'t insert Integer')
                elif type(self.__row) == str:
                    raise TkAddonButtonERROR('RowValue: ' + str(self.__row) + ' <---' + ' Can\'t insert String')
                elif type(self.__column) == str:
                    raise TkAddonButtonERROR('ColumnValue: ' + str(self.__column) + ' <---' + ' Can\'t insert String')
                elif type(self.__varname) == int:
                   raise TkAddonButtonERROR('EntryNameValue: ' + str(self.__column) + ' <---' + ' Can\'t insert String')
                else:
                    TkAddonGrid.button_place(self.__tab, self.__text, self.__command, self.__row, self.__column, self.__varname)
        call_button = TkAddonButton(tab, text, command, row, column)
        call_button.ButtonExceptions()
    def button_place(tab, text, command, row, column, varname):
        varname = Button(tab, text=text, command=command)
        varname.grid(row=row, column=column)




    def label(tab='tab', text='TkAddons!', row=0, column=0, varname='varname'):
        class TkAddonLabelERROR(Exception):
            def __init__(self, msg):
                super().__init__(msg)
        
        
        class TkAddonLabel:
            def __init__(self,  tab='tab', text='TkAddons!', row=0, column=0, varname='varname'):
                self.__tab = tab
                self.__text = text
                self.__row = row
                self.__column = column
                self.__varname = varname
                
            def LabelExceptions(self):
                tab_str = str(self.__tab)
                res = any(chr.isdigit() for chr in tab_str)
                if type(self.__tab) == int:
                    raise TkAddonLabelERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert Integer')
                elif str(res) == 'True':
                    raise TkAddonLabelERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert digit in string')
                elif type(self.__text) == int:
                    raise TkAddonLabelERROR('TextValue: ' + str(self.__text) + ' <---' + ' Can\'t insert Integer')
                elif type(self.__row) == str:
                    raise TkAddonLabelERROR('RowValue: ' + str(self.__row) + ' <---' + ' Can\'t insert String')
                elif type(self.__column) == str:
                    raise TkAddonLabelERROR('ColumnValue: ' + str(self.__column) + ' <---' + ' Can\'t insert String')
                elif type(self.__varname) == int:
                   raise TkAddonLabelERROR('EntryNameValue: ' + str(self.__column) + ' <---' + ' Can\'t insert String')
                else:
                    TkAddonGrid.label_place(self.__tab, self.__text, self.__row, self.__column, self.__varname)
        call_label = TkAddonLabel(tab, text, row, column)
        call_label.LabelExceptions()
    def label_place(tab, text, row, column, varname):
        varname = Label(tab, text=text)
        varname.grid(row=row, column=column)
    
    def entry(tab='tab', text='NONE', row=0, column=0, varname='varname'):
        class TkAddonEntryERROR(Exception):
            def __init__(self, msg):
                super().__init__(msg)
        
        
        class TkAddonEntry:
            def __init__(self,  tab='tab', text='TkAddons!', row=0, column=0, varname='varname'):
                self.__tab = tab
                self.__text = text
                self.__row = row
                self.__column = column
                self.__varname = varname
                
            def EntryExceptions(self):
                tab_str = str(self.__tab)
                res = any(chr.isdigit() for chr in tab_str)
                if type(self.__tab) == int:
                    raise TkAddonEntryERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert Integer')
                elif str(res) == 'True':
                    raise TkAddonEntryERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert digit in string')
                elif type(self.__text) == int:
                    raise TkAddonEntryERROR('TextValue: ' + str(self.__text) + ' <---' + ' Can\'t insert Integer')
                elif type(self.__row) == str:
                    raise TkAddonEntryERROR('RowValue: ' + str(self.__row) + ' <---' + ' Can\'t insert String')
                elif type(self.__column) == str:
                    raise TkAddonEntryERROR('ColumnValue: ' + str(self.__column) + ' <---' + ' Can\'t insert String')
                elif type(self.__varname) == int:
                   raise TkAddonEntryERROR('EntryNameValue: ' + str(self.__column) + ' <---' + ' Can\'t insert String')
                else:
                    TkAddonGrid.entry_place(self.__tab, self.__text, self.__row, self.__column, self.__varname)
        call_entry = TkAddonEntry(tab, text, row, column)
        call_entry.EntryExceptions()
    def entry_place(tab, text, row, column, varname):
        NONE = 'NONE'
        varname = Entry(tab, text=text)
        varname.grid(row=row, column=column)
        if text == NONE:
            return
        else:
            varname.insert(0, text)
#----------------------------------------------------------------------------------------------------------#   
# TkAddonPack
class TkAddonPack():
    def button(tab=1, text='TkAddons!', command=HelloWrld, varname='varname'):
        class TkAddonButtonERROR(Exception):
            def __init__(self, msg):
                super().__init__(msg)
        
        
        class TkAddonButton:
            def __init__(self,  tab='e', text='1', command='TkAddonGrid.HelloWrld', varname='varname'):
                self.__tab = tab
                self.__text = text
                self.__command = command
                self.__varname = varname
                
            def ButtonExceptions(self):
                tab_str = str(self.__tab)
                res = any(chr.isdigit() for chr in tab_str)
                if type(self.__tab) == int:
                    raise TkAddonButtonERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert Integer')
                elif str(res) == 'True':
                    raise TkAddonButtonERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert digit in string')
                elif type(self.__text) == int:
                    raise TkAddonButtonERROR('TextValue: ' + str(self.__text) + ' <---' + ' Can\'t insert Integer')
                elif type(self.__command) == int:
                    raise TkAddonButtonERROR('CommandValue: ' + str(self.__command) + ' <---' + ' Can\'t insert Integer')
                elif type(self.__varname) == int:
                   raise TkAddonButtonERROR('EntryNameValue: ' + str(self.__column) + ' <---' + ' Can\'t insert String')
                else:
                    TkAddonPack.button_place(self.__tab, self.__text, self.__command, self.__varname)
        call_button = TkAddonButton(tab, text, command)
        call_button.ButtonExceptions()
    def button_place(tab, text, command, varname):
        varname = Button(tab, text=text, command=command)
        varname.pack()




    def label(tab='tab', text='TkAddons!', varname='varname'):
        class TkAddonLabelERROR(Exception):
            def __init__(self, msg):
                super().__init__(msg)
        
        
        class TkAddonLabel:
            def __init__(self,  tab='tab', text='TkAddons!', varname='varname'):
                self.__tab = tab
                self.__text = text
                self.__varname = varname
                
            def LabelExceptions(self):
                tab_str = str(self.__tab)
                res = any(chr.isdigit() for chr in tab_str)
                if type(self.__tab) == int:
                    raise TkAddonLabelERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert Integer')
                elif str(res) == 'True':
                    raise TkAddonLabelERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert digit in string')
                elif type(self.__text) == int:
                    raise TkAddonLabelERROR('TextValue: ' + str(self.__text) + ' <---' + ' Can\'t insert Integer')
                elif type(self.__varname) == int:
                   raise TkAddonLabelERROR('EntryNameValue: ' + str(self.__column) + ' <---' + ' Can\'t insert String')
                else:
                    TkAddonPack.label_place(self.__tab, self.__text, self.__varname)
        call_label = TkAddonLabel(tab, text)
        call_label.LabelExceptions()
    def label_place(tab, text, varname):
        varname = Label(tab, text=text)
        varname.pack()
    
    def entry(tab='tab', text='NONE', varname='varname'):
        class TkAddonEntryERROR(Exception):
            def __init__(self, msg):
                super().__init__(msg)
        
        
        class TkAddonEntry:
            def __init__(self,  tab='tab', text='TkAddons!', varname='varname'):
                self.__tab = tab
                self.__text = text
                self.__varname = varname
                
            def EntryExceptions(self):
                tab_str = str(self.__tab)
                res = any(chr.isdigit() for chr in tab_str)
                if type(self.__tab) == int:
                    raise TkAddonEntryERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert Integer')
                elif str(res) == 'True':
                    raise TkAddonEntryERROR('WindowValue: ' + str(self.__tab) + ' <---' + ' Can\'t insert digit in string')
                elif type(self.__text) == int:
                    raise TkAddonEntryERROR('TextValue: ' + str(self.__text) + ' <---' + ' Can\'t insert Integer')
                elif type(self.__varname) == int:
                   raise TkAddonEntryERROR('EntryNameValue: ' + str(self.__column) + ' <---' + ' Can\'t insert String')
                else:
                    TkAddonPack.entry_place(self.__tab, self.__text, self.__varname)
        call_entry = TkAddonEntry(tab, text)
        call_entry.EntryExceptions()
    def entry_place(tab, text, varname):
        NONE = 'NONE'
        varname = Entry(tab, text=text)
        varname.pack()
        if text == NONE:
            return
        else:
            varname.insert(0, text)


        