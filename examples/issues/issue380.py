import sys
sys.path.append("../../")

from appJar import gui

def press():
    pass

tabs = ['a', 'b', 'c', 'd', 'e']
icons = ['open', 'save', 'web', 'search', 'wizard']

with gui() as app:
    app.toolbar(['save', 'web'], press, findIcon=True, pinned=True)
#    app.addMenuItem('MENU', 'Save', press)
#    app.setMenuIcon('MENU', 'Save', 'save')
    app.menu('MENU', 'Save', press, icon='save')
    app.label('hello world')

#    app.addIconButton('save', None, 'save')
    app.button('save', None, icon='save')

#    app.addIcon('save', 'save')
    app.image('save', 'save', kind='icon')

    with app.tabbedFrame('tf'):
        for t in range(len(tabs)):
            with app.tab(tabs[t], icon=icons[t]):
                for i in range(5):
                    app.label(tabs[t]+str(i))
        with app.tab('c', image='lb3.gif'):
            pass

    with app.tab('tf', 'b', icon='wizard'):
        pass

#    for i in range(len(icons)):
#        app.setTabIcon('tf', tabs[i], icons[i])
