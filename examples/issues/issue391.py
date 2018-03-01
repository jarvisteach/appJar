import sys
sys.path.append("../../")
from appJar import gui
from time import gmtime, strftime

def show():
    time = strftime("%H:%M:%S", gmtime())
    app.label("time here", time, sticky='nw', stretch='none')
    app.status(time, field=2, bg='green')
    app.after(50, show)

with gui("timer", "200x200", font={'size':20}) as app:
    app.status(fields=3)
    with app.labelFrame("TIMER"):
        app.label("time here")
    show()
