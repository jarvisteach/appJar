import sys
sys.path.append("../../")

def press(btn=None):
    print(btn)

from appJar import gui

with gui() as app:
    app.addGrid("tbl",[["H1","H2","H3"],["1","2","3"]],action=press,addRow=press)
    app.setGridWidth("tbl",800)
    app.setGridHeight("tbl",800)
