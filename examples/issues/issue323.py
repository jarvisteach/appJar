import sys
sys.path.append("../../")

def press(btn):
    print(btn)

from appJar import gui

with gui() as app:
    app.scale("a", 0, pos=(0,0), show=True, interval=50, range=(-100, 0), change=press, highlightthickness=0, over=press)
    app.scale("b", 0, pos=(0,1), show=True, interval=50, range=(0, 100), change=press, highlightthickness=0, over=press)
