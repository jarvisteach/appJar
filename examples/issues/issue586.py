import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.bg='yellow'
    app.label('test', bg='pink')

    with app.toggleFrame('a', colspan=3, bg='green', stretch='column'):
        app.addLabel('a', 'a')

    with app.scrollPane("Test"):#, sticky='news', stretch='both'):
        app.label('short', bg='purple')
        with app.toggleFrame('demo'):
            for i in range(20):
                app.addLabel(str(i), str(i))
        app.label('loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong', bg='orange')
