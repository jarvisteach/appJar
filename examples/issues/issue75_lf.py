import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(btn)
    if btn == 'ADD':
        with app.labelFrame('tabs'):
            app.addLabel('Hello World b')
    elif btn == 'DELETE':
        with app.labelFrame('tabs'):
            app.removeAllWidgets(current=True)
        app.removeLabelFrame('tabs')

with gui() as app:
    press('ADD')

    app.buttons(['ADD', 'DELETE'], press)
