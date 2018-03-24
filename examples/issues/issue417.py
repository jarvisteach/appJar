import sys
sys.path.append("../../")

from appJar import gui

app = gui('app.py','fullscreen')

def btn(b):
    app.showSubWindow('sub')

app.addLabel('lbl1','MainWindow Fullscreen')
app.addButton('open subwindow',btn)

app.startSubWindow('sub')
app.setFullscreen()
app.addLabel('lbl2','Subwindow Non Fullscreen')
app.stopSubWindow()

app.go()
