import sys
sys.path.append("../../")

from appJar import gui

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

    app.label("Details Here", row=0, column=1)
