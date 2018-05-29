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
    app.tree("t1",xml)
    data = parseString(xml)

    node = data.createElement("person")

    element = data.createElement('name')
    element.appendChild(data.createTextNode("meee"))
    node.appendChild(element)

    element = data.createElement('age')
    element.appendChild(data.createTextNode("44"))
    node.appendChild(element)

    element = data.createElement('gender')
    element.appendChild(data.createTextNode("other"))
    node.appendChild(element)

    data.documentElement.appendChild(node)
    app.addTreeObject("t2", data)

    app.button("SHOW", press)
    app.button("ADD", add)
