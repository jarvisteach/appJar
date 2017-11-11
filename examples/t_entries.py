import sys
sys.path.append("../")
from appJar import gui

def changer(btn):
    print(btn, app.entry(btn), "changed")

def submit(btn):
    print(btn, app.entry(btn), "submitted")

def validater(btn):
    if btn == "A": app.setEntryValid("v1")
    elif btn == "B": app.setEntryInvalid("v1")
    elif btn == "C": app.setEntryWaitingValidation("v1")

app=gui()
app.addButtons(["A", "B", "C", "D", "E"], validater, colspan=2)
#app.setBg("green")
app.setLabelFont(20)

app.addEntry("e1")
app.addValidationEntry("v1")
app.addFileEntry("f1")
app.addDirectoryEntry("d1")
app.addNumericEntry("n1")
app.addAutoEntry("a1", ["a", "b", "bb", "bbb"])
app.addSecretEntry("s1")

app.separator(colspan=2)

app.addLabelEntry("le1")
app.setEntryDefault("le1", "aaa")
app.setEntryDefault("le1", "bbb")
app.addLabelFileEntry("lf1")
app.addLabelDirectoryEntry("ld1")
app.addLabelNumericEntry("ln1")
app.addLabelAutoEntry("la1", ["a", "b", "bb", "bbb"])
app.addLabelSecretEntry("ls1")
app.addLabelValidationEntry("lv1")

app.entry("sv1", row=1, column=1, type="validation", default="validation", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("se1", row=2, column=1, default="standard", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("sf1", row=3, column=1, type="file", default="file", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("sd1", row=4, column=1, type="directory", default="directory", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("sn1", row=5, column=1, type="numeric", default="numeric", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("sa1", ["a", "b", "bb", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb:bbb"], row=6, column=1, type="auto", submit=submit, change=changer, limit=5, case="upper", rows=3, default="big auto")
app.entry("ss1", row=7, column=1, secret=True, default="secret", submit=submit, change=changer, limit=5, case="upper", rows=3)

app.entry("lse1", row=9, column=1,label=True, default="standerder")
app.entry("lsf1", row=10, column=1, type="file",label=True, default="filer")
app.entry("lsd1", row=11, column=1, type="directory",label=True, default="directoryer")
app.entry("lsn1", row=12, column=1, type="numeric",label=True, default="numericer")
app.entry("lsa1", ["a", "b", "bb", "bbb"], row=13, column=1, type="auto",label=True, default="autoer")
app.entry("lss1", row=14, column=1, secret=True,label=True, default="secreter")
app.entry("lsv1", row=15, column=1, type="validation",label=True, default="validationer")
app.grip()

app.go()

