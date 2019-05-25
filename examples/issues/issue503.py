import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')
    app.button('Accessibility', app.showAccess, icon='ACCESS')

