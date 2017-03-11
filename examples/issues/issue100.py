import sys
sys.path.append("../../")
from appJar import gui

def m_in(btn): app.setLabel("status", "IN")
def m_out(btn): app.setLabel("status", "OUT")
def ent(btn): app.setLabel("status", "ENTER")
def f_out(btn): app.setLabel("status", "F_OUT")

app = gui()
app.addLabel("status", "Status here")
app.addEntry("mouser")
app.addEntry("mouser2")
app.setEntryOverFunction("mouser", [m_in, m_out])
app.setEntryFunction("mouser", ent)
app.getEntryWidget("mouser").bind("<FocusOut>", f_out, add="+")
app.go()
