import sys
sys.path.append("../")
from appJar import gui

def changer(btn):
    print(btn, app.entry(btn), "changed")

def submit(btn):
    print(btn, app.entry(btn), "submitted")

def validater(btn):
    if btn == "A":
        app.setEntryBg("e1", "red")
        app.setEntryBg("le1", "red")
        app.setEntryBg("ld1", "red")
        app.setEntryBg("lv1", "red")
        app.setLabelBg("le1", "red")
        app.setEntryValid("v1")
        app.setEntryValid("lv1")
        app.setEntryValid("lsv1")
        app.setLabelBg("lsv1", "red")
        app.setEntryValid("sv1")
    elif btn == "B":
        app.setEntryBg("e1", "green")
        app.setEntryBg("le1", "green")
        app.setEntryBg("ld1", "green")
        app.setEntryBg("lv1", "green")
        app.setEntryInvalid("v1")
        app.setEntryInvalid("lv1")
        app.setEntryInvalid("lsv1")
        app.setEntryInvalid("sv1")
    elif btn == "C":
        app.setEntryBg("e1", "orange")
        app.setEntryBg("le1", "orange")
        app.setEntryBg("ld1", "orange")
        app.setEntryBg("lv1", "orange")
        app.setEntryWaitingValidation("v1")
        app.setEntryWaitingValidation("lv1")
        app.setEntryWaitingValidation("lsv1")
        app.setEntryWaitingValidation("sv1")
    elif btn == "D":
        app.hideEntry("e1")
        app.hideEntry("le1")
        app.hideEntry("d1")
        app.hideEntry("ld1")
        app.hideEntry("v1")
        app.hideEntry("lv1")
    elif btn == "E":
        app.showEntry("e1")
        app.showEntry("le1")
        app.showEntry("d1")
        app.showEntry("ld1")
        app.showEntry("v1")
        app.showEntry("lv1")
    elif btn == "F":
        app.removeEntry("e1")
        app.removeEntry("f1")
        app.removeEntry("le1")
        app.removeEntry("d1")
        app.removeEntry("ld1")
        app.removeEntry("v1")
        app.removeEntry("lv1")
    elif btn == "G":
        app.debug("Adding entry: e1")
        app.addEntry("e1", row=1)
        app.debug("Adding val entry: v1")
        app.addValidationEntry("v1",row=2)
        app.debug("Adding file entry: f1")
        app.addFileEntry("f1", row=3)
        app.debug("Adding dir entry: d1")
        app.addDirectoryEntry("d1", row=4)
        app.debug("Adding lab entry: l1")
        app.addLabelEntry("le1", row=9)
        app.debug("Adding lab dir entry: ld1")
        app.addLabelDirectoryEntry("ld1", row=11)
        app.debug("Adding lab val entry: lv1")
        app.addLabelValidationEntry("lv1", row=15)
    elif btn == "0":
        app.addLabelEntry("long", row=16)

with gui(bg="green") as app:
    app.addButtons(["0", "A", "B", "C", "D", "E", "F", "G"], validater, colspan=2)
    app.setLabelFont(size=20)

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

    app.entry("sv1", row=1, column=1, kind="validation", default="validation", submit=submit, change=changer, limit=5, case="upper", rows=3)
    app.entry("se1", row=2, column=1, default="standard", submit=submit, change=changer, limit=5, case="upper", rows=3)
    app.entry("sf1", row=3, column=1, kind="file", default="file", submit=submit, change=changer, limit=5, case="upper", rows=3)
    app.entry("sd1", row=4, column=1, kind="directory", default="directory", submit=submit, change=changer, limit=5, case="upper", rows=3)
    app.entry("sn1", row=5, column=1, kind="numeric", default="numeric", submit=submit, change=changer, limit=5, case="upper", rows=3)
    app.entry("sa1", ["a", "b", "bb", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb:bbb"], row=6, column=1, kind="auto", submit=submit, change=changer, limit=5, case="upper", rows=3, default="big auto")
    app.entry("ss1", row=7, column=1, secret=True, default="secret", submit=submit, change=changer, limit=5, case="upper", rows=3)

    app.entry("lse1", row=9, column=1,label=True, default="standerder")
    app.entry("lsf1", row=10, column=1, kind="file",label=True, default="filer")
    app.entry("lsd1", row=11, column=1, kind="directory",label=True, default="directoryer")
    app.entry("lsn1", row=12, column=1, kind="numeric",label=True, default="numericer")
    app.entry("lsa1", ["a", "b", "bb", "bbb"], row=13, column=1, kind="auto",label=True, default="autoer")
    app.entry("lss1", row=14, column=1, secret=True,label=True, default="secreter")
    app.entry("lsv1", row=15, column=1, kind="validation",label=True, default="validationer")
    app.grip()
    app.bg = "blue"
    app.bg = "yellow"
