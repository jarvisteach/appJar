import sys
sys.path.append("../../")
from appJar import gui

def details():
    app.label("DETAILS", app.getTreeSelected("t1"))
    app.label("DETAILS2", app.getTreeSelectedXML("t1"))

with gui("appJar Explorer") as app:
    app.addTree("t1",
        """<topLevel>
            <tabbedFrame>
                <tab>
                    <labelFrame><label><title>aaa</title><text>bbb</text></label></labelFrame>
                    <frame>
                        <check a='fff'><title>aaa</title></check>
                        <check><title>aaa</title></check>
                        <check><title>aaa</title></check>
                    </frame>
                </tab>
                <tab>
                    <labelFrame><label><title>aaa</title><text>bbb</text></label></labelFrame>
                </tab>
                <tab>
                    <labelFrame><label><title>aaa</title><text>bbb</text></label></labelFrame>
                </tab>
            </tabbedFrame>
        </topLevel>""")

    with app.frame("DETAILS", row=0, column=1):
        app.label("DETAILS")
        app.label("DETAILS2")
    app.button("DETAILS", details, colspan=2)
