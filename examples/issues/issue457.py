import sys
sys.path.append("../../")
from xml.dom.minidom import parseString

from appJar import gui
xmlText = """<people cont='europe'>
        <person><name a='1' b='2' lowercase='false'>Fred</name><age>45</age><gender>Male</gender></person>
        <person><favourites f='5'><a>Cheese</a><b>Ham</b></favourites><name>Tina</name><age>37</age><gender>Female</gender></person>
        <person><name>CLive</name><age>28</age><gender>Male</gender></person>
        <person><name>Betty</name><age>51</age><gender>Female</gender></person>
        </people>"""

def _getNewNode():
    newNode = app.makeXmlNode("t2", 'person', "Hi", {'attribute4':'44'}, comment="hi")
    newNode.appendChild(app.makeXmlNode("t2", 'name', 'new name', {'a':'44', 'b':'b', 'c':'c'}, "another c"))
    newNode.appendChild(app.makeXmlNode("t2", 'age', '44'))
    newNode.appendChild(app.makeXmlNode("t2", 'gender', 'female'))
    newNode.appendChild(app.getTreeXmlObject("t2").createComment("help"))

    return newNode

def xml(): print("ORIG: " + xmlText + "\n" + "OBJ: " + app.getTreeXmlObject("t2").toxml())
def show(): print(app.getTreeSelectedXML("t2"))
def addChild(): app.addTreeNode("t2", _getNewNode())
def addBefore(): app.addTreeNodeBefore("t2", _getNewNode())
def addAfter(): app.addTreeNodeAfter("t2", _getNewNode())
def duplicate(): app.duplicateTreeNode("t2")
def delete(): app.deleteTreeNode("t2")
def replace(): app.replaceTreeNode("t2", _getNewNode())

def dbl(title, attribute):
    print(title, attribute)
    addChild()

with gui() as app:
    app.tree("t2", xmlText , menu=True, attributes=True, fg="white", bg="blue", fgH="blue", bgH="white", dbl=dbl)
#    app.tree("t2", parseString(xmlText), menu=True, attributes=True, fg="yellow", bg="red", bgH="yellow", fgH="red", dbl=dbl)
    app.buttons(["XML", "SHOW", "CHILD", "BEFORE", "AFTER", "DUPLICATE", "DELETE", "REPLACE"],
                [xml, show, addChild, addBefore, addAfter, duplicate, delete, replace])
