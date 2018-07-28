import sys
sys.path.append("../../")

from appJar import gui

pos = {'a':0, 'b':0, 'c':0}

def press():
    text = app.popUp("New Task", "Enter the new task", "string")
    if text is not None:
        with app.frame("a"):
            app.label(text, bg=app.getRandomColour(), font=20, submit=labelA)

def buttonA(title): move(title, 'button', "b",  buttonB)
def buttonB(title): move(title, 'button', "c",  buttonC)
def labelA(title):  move(title, 'label',  "b",  labelB)
def labelB(title):  move(title, 'label',  "c",  labelC)
def buttonC(title): move(title, 'button', None, None)
def labelC(title):  move(title, 'label',  None, None)

def move(title, kind, parent, func):
    if parent is None:
        if kind == 'button': app.removeButton(title, collapse=True)
        elif kind == 'label': app.removeLabel(title, collapse=True)
    else:
        with app.frame(parent):
            if kind == 'button':
                app.moveButton(title, row=pos[parent], column=0, sticky='NEW')
                app.button(title, submit=func)
            elif kind == 'label':
                app.moveLabel(title, row=pos[parent], column=0, sticky='NEW')
                app.label(title, submit=func)
        pos[parent] = pos[parent] + 1

with gui("Grid", bg='grey', sticky='new', stretch='column') as app:
    app.label("TO DO", row=0,column=0, font=20, bg='white', width=12)
    app.label("IN PROGRESS", row=0,column=1, font=20, bg='white', width=12)
    app.label("DONE", row=0,column=2, font=20, bg='white', width=12)

    app.config(sticky='new', stretch='both')

    with app.frame("a", 1, 0, stretch=None, sticky='new'):
        for i in range(0, 5):
            app.label(str(i), bg=app.getRandomColour(), font=20, submit=labelA)
            app.button(str(i), buttonA, bg=app.getRandomColour(), font=20)

    with app.frame("b",1,1, sticky='new'): pass
    with app.frame("c",1,2, sticky='new'): pass

    app.buttons(["NEW"], press, colspan=3, sticky='s', stretch='column')
