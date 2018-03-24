import sys
sys.path.append("../../")

from appJar import gui

def tickOptionBox_has_changed(widgetFullName):
    print("DEBUG: widgetFullName=" + str(widgetFullName))
    optionBoxContent=app.getOptionBox(myTitle)
    print("DEBUG:optionBox content=" + str(optionBoxContent))
            
app = gui()
# feedback objects
myTitle="test"
options=["val1", "val2", "val3"]
optionsTicked=[False, False, False]
ent=app.addTickOptionBox(myTitle, options, row=1, column=1, colspan=1 )
ent=app.addOptionBox('aaa', options, row=2, column=1, colspan=1 )
app.setOptionBoxSticky(myTitle, "both")
for idx in range(len(optionsTicked)):
    print("idx=" + str(idx))
    app.setOptionBox(myTitle, options[idx], value=False, callFunction=False, override=True)#optionsTicked[idx]
for idx in range(len(optionsTicked)):
    print("idx=" + str(idx))
    app.setOptionBox(myTitle, options[idx], value=False, callFunction=False, override=True)#optionsTicked[idx]
#ent.customFieldWhoAmI = guiObjName
app.setOptionBoxChangeFunction(myTitle, tickOptionBox_has_changed)
app.setOptionBoxChangeFunction('aaa', tickOptionBox_has_changed)
optionBoxContent=app.getOptionBox(myTitle)
print("DEBUG:optionBox content from main=" + str(optionBoxContent))
app.go()
