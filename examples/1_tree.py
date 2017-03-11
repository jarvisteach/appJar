import sys
sys.path.append("../")
from appJar import gui
def press(btn): print(btn)
def press2(btn): print("EDIT", btn)
app=gui()
data="<people><person><name>Richard</name><age>21</age></person><person><name>kh</name><age>44</age></person></people>"
app.addTree("tree", data)
app.setTreeDoubleClickFunction("tree", press)
app.setTreeEditFunction("tree", press2)
app.go()
