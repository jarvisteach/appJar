from appJar import gui
from random import randint

def press():
    app.label(str(randint(0, 9)), bg=app.RANDOM_COLOUR(), fg=app.RANDOM_COLOUR())

with gui('Lesson 1', bg='black') as app:
    for x in range(10):
            app.label(str(x), 'Where to begin?', pos=[x%5, x%2],
                    fg=app.RANDOM_COLOUR(), bg=app.RANDOM_COLOUR(),
                    font={'size':randint(10,30)})

    app.button("PRESS ME", press, colspan=2)
