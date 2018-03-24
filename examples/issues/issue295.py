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

with gui() as app:
    app.bg='blue'
    app.label('hello world', bg='pink')
    app.entry('vals', kind='validation', bg='orange')
    app.entry('vals', bg='orange')
    app.buttons(['YES', 'NO', 'REQUIRED'], validate)
