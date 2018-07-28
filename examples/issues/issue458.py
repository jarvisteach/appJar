import sys
sys.path.append("../../")

from appJar import gui

def split(text):
    newText = ""
    pos = 0
    for t in text:
        if pos == 20:
            pos == 0
            newText += "\\n"
        newText += t
    return newText

with gui() as app:
    app.label('hello world')
    app.addTable("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["TinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinTinaaaaaaaaaaaaaaaaaaaaaaaaaaaaaTina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]], wrap=100)
