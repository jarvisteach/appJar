import sys
sys.path.append("../../")

from appJar import gui

bPos = cPos = 0

def press():
    with app.frame("A"):
        text = app.popUp("New Task", "Enter the new task", "string")
        if text is not None:
            app.label(text, bg=app.getRandomColour(), font=20, submit=removeA)

def clone(widget, newParent):
    clone = widget.__class__(newParent)
    for key in widget.configure():
        clone.configure({key: widget.cget(key)})

    origProps = widget.__dict__
    for x in origProps:
        if x not in ['_w', '_tclCommands', '_name', 'master', 'tk']:
            setattr(clone, x, origProps[x])

    return clone

def removeA(label):
    global bPos
    remove(label, "B", bPos, removeB)
    bPos += 1

def removeB(label):
    global cPos
    remove(label, "C", cPos, removeC)
    cPos += 1

def removeC(label):
    remove(label, None, None, None)

def remove(label, parent, row, func):
    l = app.getLabelWidget(label)
    info = l.grid_info()
    l.master.grid_rowconfigure(info["row"], minsize=0, weight=0)

    if parent is None:
        app.removeLabel(label)
    else:
        app.hideLabel(label)
        newL = clone(l, app.getFrameWidget(parent))                 # create the clone
        app.widgetManager.update(app.Widgets.Label, label, newL)    # update widget store

        app.label(label, submit=func)                               # replace function
        newL.grid(row=row, column=0, sticky='NEW')
        newL.master.grid_columnconfigure(0, weight=1)

with gui("Grid", bg='grey', sticky='new', stretch='column') as app:
    app.label("TO DO", row=0,column=0, font=20, bg='grey', width=12)
    app.label("IN PROGRESS", row=0,column=1, font=20, bg='grey', width=12)
    app.label("DONE", row=0,column=2, font=20, bg='grey', width=12)

    app.config(sticky='new', stretch='both')

    with app.frame("A",1,0, stretch=None, sticky='new'):
        for i in range(10):
            app.label(str(i), bg=app.getRandomColour(), font=20, submit=removeA)

    with app.frame("B",1,1, sticky='new'): pass
    with app.frame("C",1,2, sticky='new'): pass

    app.buttons(["NEW"], press, colspan=3, sticky='s', stretch='column')
