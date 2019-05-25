import sys
sys.path.append("../../")
from xml.dom.minidom import parseString

from appJar import gui
xml= """<people cont='europe'>
        <person><name a='1' b='2' lowercase='false'>Fred</name><age>45</age><gender>Male</gender></person>
        <person><favourites f='5'><a>Cheese</a><b>Ham</b></favourites><name>Tina</name><age>37</age><gender>Female</gender></person>
        <person><name>CLive</name><age>28</age><gender>Male</gender></person>
        <person><name>Betty</name><age>51</age><gender>Female</gender></person>
        </people>"""

def press():
    print(xml)
    print(data.toxml())

def add():
    element = data.createElement('name2')
    data.documentElement.appendChild(element)
    element.appendChild(data.createTextNode("meee"))
    app.addChild("t2", element)

def _addr():
    node = data.createElement("human")
    data.documentElement.appendChild(node)

    name = data.createElement('name')
    age = data.createElement('age')
    gen = data.createElement('gender')

    name.appendChild(data.createTextNode("meee"))
    age.appendChild(data.createTextNode("44"))
    gen.appendChild(data.createTextNode("other"))

    node.appendChild(name)
    node.appendChild(age)
    node.appendChild(gen)

def dbl(t, a):
    add()

def clear():
    app.clearTree("t2")

with gui() as app:
    app.label('hello world')

#    app.tree("t1", xml, fg="white", bg="blue", fgH="blue", bgH="white")
    data = parseString(xml)
    app.tree("t2", data, menu=False, attributes=True, fg="yellow", bg="red", bgH="yellow", fgH="red")#, dbl=dbl)

    app.button("SHOW", press)
    app.button("ADD", add)
    app.button("CLEAR", clear)
