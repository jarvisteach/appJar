import sys
sys.path.append("../../")

from appJar import gui

bPos = 0
cPos = 0

def press(btn):
    if btn == "NEW":
        with app.frame("A"):
            l = app.popUp("New Task", "Enter the new task", "string")
            if l is not None:
                app.label(l, bg=app.getRandomColour(), font=20, submit=removeA, width=8, height=2)

def clone(widget, newParent):
    clone = widget.__class__(newParent)
    for key in widget.configure():
        clone.configure({key: widget.cget(key)})
    return clone

def removeA(label):
    global bPos
    remove(label, "B", bPos, removeB)
    bPos += 1

def removeB(label):
    global cPos
    remove(label, "C", cPos, None)
    cPos += 1

def remove(label, parent, row, func):
    """ remove the item from the grid, add it to the stack """
    l = app.getLabelWidget(label)
    info = l.grid_info()
    l.master.grid_rowconfigure(info["row"], minsize=0, weight=0)
    l.grid_forget()
    newL = clone(l, app.getFrameWidget(parent))
    app.widgetManager.update(app.Widgets.Label, label, newL)

    app.label(label, submit=func)
    newL.grid(row=row, column=0, sticky='N')
    newL.master.grid_rowconfigure(row, weight=0)

with gui("Grid", bg='grey') as app:
#    app.config(stretch='row', sticky='n')
#
#    app.label("TO DO", row=0,column=0, font=20, bg='grey', width=12)
#    app.label("IN PROGRESS", row=0,column=1, font=20, bg='grey', width=12)
#    app.label("DONE", row=0,column=2, font=20, bg='grey', width=12)

    app.config(stretch='column', sticky='ns')
    with app.frame("A",1,0):
        app.config(sticky='n', stretch='column')
        for i in range(10):
            app.label(str(i), bg=app.getRandomColour(), font=20, submit=removeA, width=8, height=2)

    app.config(stretch='both', sticky='news')
    with app.frame("B",1,1):
        app.config(sticky='n', stretch='column')

    app.config(stretch='both', sticky='news')
    with app.frame("C",1,2):
        app.config(sticky='n', stretch='column')

    app.config(stretch='column', sticky='s')
    app.buttons(["NEW"], press, colspan=3)
