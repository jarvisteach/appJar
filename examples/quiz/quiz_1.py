import sys
sys.path.append("../../")
from appJar import gui

def launcher(btn):
    print(btn)

with gui("Quiz Demo") as app:
    app.buttons(["Quiz", "Scores"], launcher)
