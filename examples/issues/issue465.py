import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.addLabelScale("scale")
    app.setScaleRange("scale",0,10,1)
    app.disableScale("scale")
    app.scale('scale2', 1, range=[0,10], label=True)
    app.scale('scale3', 5, range=[0,10], label="fred")
    app.scale('scale4', 5, range=[0,10], label=False, direction='vertical', show=True)
