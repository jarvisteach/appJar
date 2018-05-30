import sys
sys.path.append("../../")
from xml.dom.minidom import parseString

from appJar import gui
xml= """<people>
        <person><name>Fred</name><age>45</age><gender>Male</gender></person>
        <person><name>Tina</name><age>37</age><gender>Female</gender></person>
        <person><name>CLive</name><age>28</age><gender>Male</gender></person>
        <person><name>Betty</name><age>51</age><gender>Female</gender></person>
        </people>"""

def press():
    print(xml)
    print(data.toxml())

def add():

    element = data.createElement('name2')
    element.appendChild(data.createTextNode("meee"))
    node.appendChild(element)

    app.generateTree("t2")

with gui() as app:
    app.label('hello world')
    app.tree("t1", xml, fg="white", bg="blue", fgH="blue", bgH="white")

    data = parseString(xml)

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

    app.tree("t2", data, fg="yellow", bg="red", bgH="yellow", fgH="red")

    app.button("SHOW", press)
    app.button("ADD", add)
