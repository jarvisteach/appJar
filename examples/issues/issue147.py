import sys
sys.path.append("../../")

from appJar import gui

def press():
    print(app.getFocus())

with gui() as app:
    app.addToolbar(['a', 'b', 'c'], press)
    app.label('hello world')
    app.button('PRESS', press)
    app.entry('ent')
    app.registerEvent(press)
    app.link('press', press)
    app.text('tarea')
    app.radio('radio_group', 'radio_name')
    app.scale('scaler')
    app.listbox('lbox', ['a', 'b', 'c'])
    app.spinbox('sbox', ['a', 'b', 'c'])
    app.optionbox('obox', ['a', 'b', 'c'])
#            z.update(self.widgetManager.group(self.Widgets.Toolbar))
    
    with app.subWindow('sub'):
        with app.labelFrame('lf'):
            app.check('chk')

    app.showSubWindow('sub')
