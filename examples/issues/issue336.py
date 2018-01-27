import sys
sys.path.append("../../")
from appJar import gui

with gui() as app:
    """Device info and settings window."""
    tab = 'maintab'
    status = 'Status'
    settings = 'Settings'

    # Reset to defaults & start new frame.
    app.removeAllWidgets()
    with app.tabbedFrame(tab):
        # Status tab.
        with app.tab(status):
            app.addLabel('test', 'testing!')
