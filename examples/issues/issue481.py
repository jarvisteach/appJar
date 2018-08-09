import sys, imp
sys.path.append("../../")

from appJar import gui 
import myStyle as style
#style = imp.load_source('style', 'style.css')


with gui('appJar font problem', **style.body) as app:
    app.label("l1", "Label 1")
    app.label("l2", "Label 2")
    app.label("l3", "Label 3", **style.t1)
    app.label("l4", "Label 4", **style.t2)
    app.label("l5", "Label 5", **style.t3)
    app.label("l6", "Label 6", **style.t4)
    app.label("l7", "Label 7")
