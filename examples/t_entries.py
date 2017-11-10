import sys
sys.path.append("../")
from appJar import gui

def changer(btn):
    print(btn, app.entry(btn), "changed")

def submit(btn):
    print(btn, app.entry(btn), "submitted")

app=gui()
app.setFont(20)

app.addEntry("e1")
app.addValidationEntry("v1")
app.addFileEntry("f1")
app.addDirectoryEntry("d1")
app.addNumericEntry("n1")
app.addAutoEntry("a1", ["a", "b", "bb", "bbb"])
app.addSecretEntry("s1")

app.addLabelEntry("le1")
app.setEntryDefault("le1", "aaa")
app.setEntryDefault("le1", "bbb")
app.addLabelValidationEntry("lv1")
app.addLabelFileEntry("lf1")
app.addLabelDirectoryEntry("ld1")
app.addLabelNumericEntry("ln1")
app.addLabelAutoEntry("la1", ["a", "b", "bb", "bbb"])
app.addLabelSecretEntry("ls1")

app.entry("se1", row=0, column=1, default="standard", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("sv1", row=1, column=1, type="validation", default="validation", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("sf1", row=2, column=1, type="file", default="file", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("sd1", row=3, column=1, type="directory", default="directory", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("sn1", row=4, column=1, type="numeric", default="numeric", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("sa1", ["a", "b", "bb", "bbb"], row=5, column=1, type="auto", default="auto", submit=submit, change=changer, limit=5, case="upper", rows=3)
app.entry("ss1", row=6, column=1, secret=True, default="secret", submit=submit, change=changer, limit=5, case="upper", rows=3)

app.entry("lse1", row=7, column=1,label=True)
app.entry("lsv1", row=8, column=1, type="validation",label=True)
app.entry("lsf1", row=8, column=1, type="file",label=True)
app.entry("lsd1", row=9, column=1, type="directory",label=True)
app.entry("lsn1", row=10, column=1, type="numeric",label=True)
app.entry("lsa1", ["a", "b", "bb", "bbb"], row=11, column=1, type="auto",label=True)
app.entry("lss1", row=12, column=1, secret=True,label=True)

app.go()

