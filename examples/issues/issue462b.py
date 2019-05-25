import sys
sys.path.append("../../")

from appJar import gui

def reload():
    showInfo({'Score':50, 'Name':'Omega', 'Occupation':'Nothing'})

def showInfo(data):
    with app.labelFrame('Info'):
        app.emptyCurrentContainer()
        for name, value in data.items():
            app.entry(name, value, label=True)

with gui('Show Dict') as app:
    showInfo({'Score':100, 'Name':'Vida', 'Occupation':'Other'})
    app.button('RELOAD', reload)
