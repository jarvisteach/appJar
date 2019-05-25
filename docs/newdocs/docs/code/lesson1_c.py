from appJar import gui
from random import randint

with gui('Lesson 1', bg='yellow', fg='blue') as app:
    for x in range(10):
            app.label(str(x), 'Where to begin?',
                        fg=app.RANDOM_COLOUR(), bg=app.RANDOM_COLOUR(),
                        font={'size':randint(10,30)})
