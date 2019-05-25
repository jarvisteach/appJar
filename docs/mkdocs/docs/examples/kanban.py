import sys
sys.path.append("../../../../")
from appJar import gui 
from random import choice

ttl = ('Backlog', 'In Progress', 'Done')

def genNewLbl():
    with app.frame(ttl[0]):
            text = ''.join(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for c in range(8))
            app.label(text, bg=app.getRandomColour(), submit=move1)

def move1(lblName): move(lblName, ttl[1])
def move2(lblName): move(lblName, ttl[2])
def trash(lblName): app.removeLabel(lblName)

def move(lblName, frmName):
    # move the label to the new frame
    with app.frame(frmName): app.moveLabel(lblName)

    if frmName == ttl[1]: app.label(lblName, submit=move2)
    else: app.label(lblName, submit=trash)

with gui("Kanban Demo", "450x200", bg='grey', font=20, sticky='new') as app:
    for pos in range(len(ttl)):
        app.label(ttl[pos], pos=(0, pos), bg='white', width=12, stretch='column')
        app.stretch = 'both'
        with app.frame(ttl[pos], row=1, column=pos, sticky='new'): pass

    app.button("NEW LABEL", genNewLbl, colspan=3, sticky='s', stretch='column', font=16)
