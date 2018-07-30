from appJar import gui
from random import randint

with gui('Lesson 1', bg='black') as app:
    for x in range(10):
            app.label(str(x), 'Where to begin?', pos=[x%5, x%2],
                        fg=app.RANDOM_COLOUR(), bg=app.RANDOM_COLOUR(),
                        font={'size':randint(10,30)})
