import sys
sys.path.append("../")

from appJar import gui

with gui("FRAME DEMO", "250x150", bg='yellow') as app:

    with app.frame("LEFT", row=0, column=0, bg='blue', sticky='NEW', stretch='COLUMN'):
        app.label("Label on the left 1", bg='red')
        app.label("Label on the left 2", bg='orange')
        app.label("Label on the left 3", bg='yellow')

    with app.frame("RIGHT", row=0, column=1, bg='green', fg='white'):
        for x in range(5):
            app.radio("RADIO", "Choice " + str(x))
