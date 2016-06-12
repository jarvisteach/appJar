from appJar import gui
def press(btn): print(btn)
app=gui()
app.addGrid("grid", [[1,2,3], [3,4,5,6,7,8], [2,4,6,8]], action=press, addRow=True)
app.go()
