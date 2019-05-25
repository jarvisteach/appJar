import sys
sys.path.append("../../")

from appJar import gui

def draw(name):
    s = win.getTurtleScreen("Circle")
    t = win.getTurtle("Circle")
    win.hideLabel('Lbb1','Please try again')# tring to remove or at lease clear it but it's keeping flasing
    t.reset()
    t.penup()
    t.goto(-150,-120)
    t.pendown()

    try:
        Lnum = int(win.getEntry('length'))
    except ValueError:
        win.showLabel('Lbb1')
            
    t.fd(Lnum)
    t.left(90)
    t.fd(Lnum)
    t.left(90)
    t.fd(Lnum)
    t.left(90)
    t.fd(Lnum)

win = gui('Circle area calculator')
win.addLabelEntry('length')
win.addTurtle('Circle')
win.addButton('Draw', draw)
win.addFlashLabel('Lbb1','Please try again')# adding flashing label
win.hideLabel('Lbb1')
win.go()
