import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world', tip="help me")
    app.addLabel("l1", "text")
    app.setLabelTooltip("l1", "more help")
