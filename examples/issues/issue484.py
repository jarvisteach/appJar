import sys
sys.path.append("../../")

from appJar import gui

tabs=['NW', 'NE', 'SW', 'SE']

with gui('TABS', '400x400') as app:
    with app.tabbedFrame('tabs'):
        for tab in tabs:
            with app.tab(tab, stretch='both'):
                app.config(sticky='news', stretch='both', bg=app.RANDOM_COLOUR())
                with app.frame(tab):
    #                app.setSticky(tab)
                    app.setStretch('both')
                    for l in range(1,5):
                        app.label(tab+'demo'*l, bg=app.RANDOM_COLOUR(), fg=app.RANDOM_COLOUR(), stretch='none', sticky=tab)
