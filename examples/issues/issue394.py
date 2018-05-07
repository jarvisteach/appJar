import sys
sys.path.append("../../")
from appJar import gui

def select_all(e):
    try: e.widget.tag_add("sel","1.0","end")
    except:
        try: e.widget.select_range(0, 'end') 
        except: gui.trace('Unable to select all')
    print(app.topLevel.clipboard_get())

with gui("timer", font={'size':20}) as app:
    app.textArea("text").config(relief='groove', bd=3)
    app.entry("entry")
    app.option("opt", [1,2,3,4])
    app.spin("sp", [1,2,3,4])
