import sys
sys.path.append("../")
from appJar import gui

def menuPress(menu):
    print(menu)

app=gui("Menu Test")
app.setGeometry(300,150)

fileMenus = ["Open", "Save", "Save as...", "-", "Export", "Print", "-", "Close"]
app.addMenuList("File", fileMenus, menuPress)

app.createMenu("Config")
app.addSubMenu("Config", "Font Size")
for i in range(5):
    app.addMenuRadioButton("Font Size", "font", "1" + str(i), menuPress)

app.addMenuSeparator("Config")

for i in range(5):
    app.addMenuCheckBox("Config", "Size 1" + str(i), menuPress)



app.go()
