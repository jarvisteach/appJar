import sys
sys.path.append("../../")

""" Click labels to remove their frame
    Press a button to put them back
    Each widget is added to a stack
"""

from appJar import gui
p = ["Top Left", "Top Right", "Bottom Left", "Bottom Right"]
remove_stack = []

def place(btn):
    """ get item from stack, and put it in the right place """
    if len(remove_stack) == 0: app.bell()
    else:
        f = remove_stack.pop()
        if btn == p[0]: f.grid(row=0, column=0, sticky='NEWS')
        elif btn == p[1]: f.grid(row=0, column=1, sticky='NEWS')
        elif btn == p[2]: f.grid(row=1, column=0, sticky='NEWS')
        elif btn == p[3]: f.grid(row=1, column=1, sticky='NEWS')

def remove(label):
    """ remove the item from the grid, add it to the stack """
    f = app.getFrameWidget(label)
    remove_stack.append(f)
    f.grid_forget()

with gui("Grid", "600x600") as app:
    with app.frame(p[0],0,0): app.label(p[0], bg='red', font=20, submit=remove)
    with app.frame(p[1],0,1): app.label(p[1], bg='yellow', font=20, submit=remove)
    with app.frame(p[2],1,0): app.label(p[2], bg='green', font=20, submit=remove)
    with app.frame(p[3],1,1): app.label(p[3], bg='blue', font=20, submit=remove)
    app.buttons([p[0],p[1],p[2],p[3]], place, colspan=2, fill=True, sticky="esw", stretch="column")
