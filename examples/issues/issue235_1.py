import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(btn)

with gui("Simple Demo") as app:
    app.label("title", "hello world", bg="green", fg="blue", column=0, row=0)
    app.label("title2", "hello world", bg="red", fg="white", column=1, row=0)
    app.label("title3", "hello world", bg="orange", fg="black", column=0, row=1)
    app.label("title4", "hello world", bg="pink", fg="yellow", column=1, row=1)
