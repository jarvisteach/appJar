import sys
sys.path.append("../../")

from appJar import gui

with gui("AutoEntry", "400x400") as app:
    app.addAutoEntry("e", ["a", "aa", "aab", "cc", "d", "e", "f", "g"])
    app.appendAutoEntry("e", ["zzz"])
    app.removeAutoEntry("e", "ccc")
    app.changeAutoEntry("e", ["zzz"])
    app.setAutoEntryNumRows("e", 3)
