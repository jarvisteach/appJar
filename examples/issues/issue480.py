import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')
    app.text("ta", focus=True)
    #app.addTextArea("ta")#.focus_set()
    #app.setTextAreaFocus("ta")
