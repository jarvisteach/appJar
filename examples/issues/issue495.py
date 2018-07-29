import sys
sys.path.append("../../")

from appJar import gui
data = [["Name", "Age", "Gender"], ["Fred", 45, "Male"],
        ["Tina", 37, "Female"], ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]]

def func(a):
    print(a)
    print(app.getTableLastChange('g1'))

with gui() as app:
    app.table("g1", data, showMenu=True, edit=func)
