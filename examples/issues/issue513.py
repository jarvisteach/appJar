import sys
sys.path.append("../../")

from appJar import gui

def create_page(pos):
    with app.page(sticky='news', stretch='both'):
        app.label(pos, bg=app.RANDOM_COLOUR())

with gui(font=20) as app:
    with app.pagedWindow('title'):
        for i in range(10):
            create_page(i)
