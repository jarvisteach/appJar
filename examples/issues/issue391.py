import sys
sys.path.append("../../")
from appJar import gui
from time import gmtime, strftime

def show():
    app.label("time here", strftime("%H:%M:%S", gmtime()), sticky='nw', stretch='none')
    app.after(50, show)

with gui("timer", "200x200", font={'size':20}) as app:
    with app.labelFrame("TIMER"):
        app.label("time here")
    show()
