import sys
sys.path.append("../../")

from appJar import gui


def validate(btn):
    if btn == 'YES':
        app.setValidationEntry('vals', state='valid')
    elif btn == 'NO':
        app.setValidationEntry('vals', state='invalid')
    elif btn == 'REQUIRED':
        app.setValidationEntry('vals', state='wait')

def cols(btn):
    if btn == 'a': app.bg="green"
    elif btn == 'b': app.entry('vals', bg="pink")
    elif btn == 'c': app.entry('vals2', bg="green")
    elif btn == 'd': app.label('vals2', bg="white")
    elif btn == 'e': app.entry('vals', labBg="purple")

with gui() as app:
    app.bg='blue'
    app.label('hello world', bg='pink')
    app.entry('vals', kind='validation', bg='orange', labBg='white')
    app.entry('vals2', label=True, bg='yellow')
    #app.entry('vals', bg='orange')
    app.buttons(['YES', 'NO', 'REQUIRED'], validate)
    app.buttons(['a', 'b', 'c', 'd', 'e'], cols)
