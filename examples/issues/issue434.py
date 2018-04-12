import sys
sys.path.append("../../")

from appJar import gui

def process():
    c = app.entry("command")
    if c.lower().strip().startswith("bg"):
        col = c.split("=")[1].strip()
        app.bg = col
        app.text('text', "BG set to: " + col + "\n", bg=col)


with gui("Translator", "600x400", bg="black") as app:
    app.text("text", border=1, relief='sunken', state='disabled')
    app.entry("command", submit=process, focus=True)
