import sys
sys.path.append("../../")

from appJar import gui

app = gui()
tree = """
<test>
    <test1 />
</test>
"""
app.addTree(
    'Android Manifest Tree',
    tree,
    rowspan = 1
)
app.go()
