import sys
sys.path.append("../../")
from appJar import gui

redWords = ("string", "integer", "boolean", "real")
greenWords = ("print", "input")

def enb(btn):
    if btn == "DISABLE": app.disableTextArea("ta")
    else: app.enableTextArea("ta")

def tagSelected(tag):
    tag=tag.lower().strip()
    if tag == "bold": app.textAreaToggleFontSelected("ta", "BOLD")
    if tag == "underline": app.textAreaToggleFontSelected("ta", "UNDERLINE")
    if tag == "italic": app.textAreaToggleFontSelected("ta", "ITALIC")
    if tag == "boldItalic": app.textAreaToggleFontSelected("ta", "BOLD_ITALIC")
    else:
        op = app.radio('operation')
        if op == 'add': app.textAreaToggleTagSelected("ta", tag)
        elif op == 'remove': app.textAreaUntagSelected("ta", tag)
        elif op == 'delete': app.textAreaDeleteTag("ta", tag)

def highlightSyntax(param):
    for w in redWords:
        app.textAreaTagPattern("ta", "red", w)

    for w in greenWords:
        app.textAreaTagPattern("ta", "green", w)

    app.textAreaTagRange("ta", "red", 1.0, 1.4)

def search():
    print(app.searchTextArea("ta", app.entry("search")))

def show():
    print(app.getTextAreaTags("ta"))

def fontSize():
    size = app.spin("SIZE")
    print(size)
    app.setTextAreaFont("ta", size=size)

with gui("Text Editor", "300x400") as app:
    app.addMenuEdit(inMenuBar=True)

    app.setSize(400,400)
    app.addToolbar(["BOLD", "ITALIC", "UNDERLINE"], tagSelected)

    app.text("ta", focus=True, change=highlightSyntax)
    app.textAreaCreateTag("ta", "red", background="red", foreground="white")
    app.textAreaCreateTag("ta", "green", background="green", foreground="white")

    with app.frame("f1"):
        app.radio('operation', 'add', 0, 0)
        app.radio('operation', 'remove', 0, 1)
        app.radio('operation', 'delete', 0, 2)
    app.buttons(['bold', 'underline', 'italic', 'boldItalic'], tagSelected)
    app.spin("SIZE", value=8, endValue=45, change=fontSize)

    with app.frame("f2", sticky="ew"):
        app.entry("search", pos=(0, 0))
        app.button("SEARCH", search, 0, 1)
    app.button("SHOW", show)
    app.buttons(["DISABLE", "ENABLE"], enb)
