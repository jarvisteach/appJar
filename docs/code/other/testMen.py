from tkinter import *
import os

def ShowHelp(e=None):
      print("help")

def showHelpDialog(e=None):
      print("help")

class App(Frame):

      def __init__(self, parent):
            Frame.__init__(self, parent)
            parent.title("Menu Tester")

            # create menu bar object
            menubar = Menu(parent)
            # create two mewnus
            menu_file = Menu(menubar)
            menu_edit = Menu(menubar)
            # make them each cascade
            menubar.add_cascade(menu=menu_file, label='File')
            menubar.add_cascade(menu=menu_edit, label='Edit')

            # add three options
            menu_file.add_command(label='New', command=ShowHelp)
            menu_file.add_command(label='Open...', command=ShowHelp)
            menu_file.add_command(label='Close', command=ShowHelp)
            # add a seperator
            menu_file.add_separator()
            # add checkboxes
            check = StringVar()
            menu_file.add_checkbutton(label='Check', variable=check, onvalue=1, offvalue=0)
            radio = StringVar()
            menu_file.add_radiobutton(label='One', variable=radio, value=1)
            menu_file.add_radiobutton(label='Two', variable=radio, value=2)

            appmenu = Menu(menubar, name='apple')
            menubar.add_cascade(menu=appmenu)
            appmenu.add_command(label='About My Application')
            appmenu.add_separator()
            def showMyPreferencesDialog():
                print("pref")

            root.createcommand('tk::mac::ShowPreferences', showMyPreferencesDialog)

            # the MAC specifi HELP Menu
            helpmenu = Menu(menubar, name='help')
            menubar.add_cascade(menu=helpmenu, label='Help')
            menubar.add_command(label='This one', command=ShowHelp)

            root.createcommand('tk::mac::ShowHelp', showHelpDialog)

            windowmenu = Menu(menubar, name='window')
            menubar.add_cascade(menu=windowmenu, label='Window')


            # start the menu bar
            root.config(menu=menubar)
            os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python3" to true' ''')


root=Tk()
root.geometry("300x250+300+300")
app=App(root)
root.mainloop()
