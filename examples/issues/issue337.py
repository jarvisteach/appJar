import sys
sys.path.append("../../")

text = """
asdfasdf
asdf
asdf
asfd
as
fas
fa
sf
asdf
asdf
as
dfa
sdf
asdf
asd
fas
df
asdf
asdf
sa
fa
d
asdf
asdf
"""
from appJar import gui

app=gui("lots of text")
app.startScrollPane("scroller")
app.addLabel("title", text)
app.stopScrollPane()
app.go()
