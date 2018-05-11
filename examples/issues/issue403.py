import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')
    app.tree("t1",
        """<people>
        <person><name>Fred</name><age>45</age><gender>Male</gender></person>
        <person><name>Tina</name><age>37</age><gender>Female</gender></person>
        <person><name>CLive</name><age>28</age><gender>Male</gender></person>
        <person><name>Betty</name><age>51</age><gender>Female</gender></person>
        </people>""")
