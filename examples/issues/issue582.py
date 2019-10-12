import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')
    app.addSpinBox('s1', [0, 1, 2, 3, 4, 5, 6], 0, 0)
    app.addLabelSpinBox('s2', [0, 1, 2, 3, 4, 5, 6], 1, 0)
    app.addSpinBoxRange('s3', 0, 6, 2, 0)
    app.addLabelSpinBoxRange('s4', 0, 6, 3, 0)

    app.addSpinBox('rs1', [0, 1, 2, 3, 4, 5, 6], 0, 1, reverse=False)
    app.addLabelSpinBox('rs2', [0, 1, 2, 3, 4, 5, 6], 1, 1, reverse=False)
    app.addSpinBoxRange('rs3', 0, 6, 2, 1, reverse=False)
    app.addLabelSpinBoxRange('rs4', 0, 6, 3, 1, reverse=False)

    app.spin('qs1', [0, 1, 2, 3, 4, 5, 6], 4, 0)
    app.spin('qs2', [0, 1, 2, 3, 4, 5, 6], 5, 0, label=True)
    app.spin('qs3', 0, endValue=6, row=6, col=0)
    app.spin('qs4', 0, endValue=6, row=7, col=0, label=True)

    app.spin('ts1', [0, 1, 2, 3, 4, 5, 6], 4, 1, reverse=False)
    app.spin('ts2', [0, 1, 2, 3, 4, 5, 6], 5, 1, label=True, reverse=False)
    app.spin('ts3', 0, endValue=6, row=6, col=1, reverse=False)
    app.spin('ts4', 0, endValue=6, row=7, col=1, label=True, reverse=False)
