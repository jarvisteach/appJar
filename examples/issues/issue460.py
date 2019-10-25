import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(btn)

with gui() as app:
    app.label('hello world')
    app.addButton('but', press)
    app.addNamedButton('but', 'but2',  press)
    app.addButtons([['a', 'b', 'c', 'd'],['e', 'f', 'g', 'h']], press)
    app.buttons([['1', '2', '3', '4'],['5', '6', '7', '8']], press)
    app.addButtons([['a', 'b', 'c', 'd'],['e', 'f', 'g', 'h']], press, titles=[['a1', 'b1', 'c1', 'd1'],['e1', 'f1', 'g1', 'h1']])
    app.addNamedButtons([['a', 'b', 'c', 'd'],['e', 'f', 'g', 'h']], [['na1', 'nb1', 'nc1', 'nd1'],['ne1', 'nf1', 'ng1', 'nh1']], press)
    app.buttons([['a', 'b', 'c', 'd'],['e', 'f', 'g', 'h']], press, labels=[['a2', 'b2', 'c2', 'd2'],['e2', 'f2', 'g2', 'h2']])
