import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    app.removeAllWidgets()

    app.widget_defaults(sticky='ew', stretch='none')
    # Add widgets - error label (top) & button (bottom).
    app.addLabel('text2', "new one", 0, 0)
    app.setLabelAlign('text2', 'left')
    app.addButton("PRESSER", app.stop, 2, 0)
    # Text area.
    app.addScrolledTextArea('textarea2', 1, 0, 2)
#    app.addMenuEdit(inMenuBar=False)

app = gui()

# Initialise parent.
app.setTitle('Test')
app.addScrolledTextArea('textarea', 1, 0, 2)
app.setTextArea('textarea', "{}".format('test'))
app.addMenuEdit(inMenuBar=True)
app.addButton("PRESS", press)
app.go()
