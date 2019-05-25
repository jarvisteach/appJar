from appJar import gui

with gui('Lesson 1', geom='400x200', bg='yellow', fg='blue') as app:
    app.label('Where to begin?', bg='orange', font={'size':20})
