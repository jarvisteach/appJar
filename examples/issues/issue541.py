import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.addLabel("l1", "text")
    app.setLabelTooltip("l1", "text")
