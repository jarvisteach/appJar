import sys
sys.path.append("../../")

from appJar import gui

def process():
    c = app.entry("command")
    if c.lower().strip().startswith("bg"):
        col = c.split("=")[1].strip()
        app.bg = col
        app.label('text', value="BG set to: " + col + "\n", bg=col)
        app.openScrollPane("pane")
        app.setBg(col)
        app.stopScrollPane()

with gui("Translator", "600x400", bg="black") as app:
    with app.scrollPane("pane", sticky='news', stretch='both'):
        app.config(sticky='news', stretch='both')
        app.label("text", "help.....", border=1, relief='sunken', sticky='news')
    app.entry("command", submit=process, focus=True, stretch='column', sticky='esw')
    app.openScrollPane("pane")
    for i in range(50):
        app.label(str(i))
    app.stopScrollPane()
