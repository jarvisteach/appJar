import sys
sys.path.append("../../")
from appJar import gui

def details():
    xml = getChildren(app.topLevel)
    print(xml)
    app.addTree("b", xml, row=1, column=1, rowspan=3)
    app.reloadTree("b")

def buildTag(tag, data):
    tag = "<" + tag + ">" + data + "</" + tag + ">\n"
    return tag

def getClass(widg):
    wClass = widg.winfo_class()
    if wClass == "Tk": wClass = "appJar"
    elif wClass == "Toplevel": wClass = "SubWindow"
    return wClass

def getText(widg):
    try:
        text = widg.cget('text')
        if text == "": text = "-EMPTY-"
    except: text = "-NONE-"
    return text

def getChildren(widg):
    children =  widg.winfo_children()
    wClass = getClass(widg)
    text = getText(widg)
    xml = buildTag(wClass, text)

    if len(children) == 0:
        return xml
    else:
        text = "<" + wClass + ">"
        for w in widg.winfo_children():
            text += getChildren(w)
        text += "</" + wClass + ">\n"
        return text

with gui("appJar Explorer") as app:
    app.label("Title Label", colspan=2)
    app.label("DETAILS", "")
    app.entry("DETAILS2")
    app.check("check")
    app.radio("radio", "r1")
    app.button("DETAILS", details)

    with app.subWindow("sub"):
        app.label("in sub")

    app.topLevel.after_idle(details)

