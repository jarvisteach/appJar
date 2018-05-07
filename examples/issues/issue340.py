import sys
sys.path.append("../../")

from appJar import gui

def press():
    print("UNBINDING")
    app.enterKey=None
    app.language = "french"
    print("NEW LANG:", app.language)
    app.logFile = None
    print(app.logFile.endswith("a.txt"))

def logger(level):
    lev = app.radio("logger")
    print("BEFORE", app.logLevel, " -> ", lev)
    app.logLevel = app.radio("logger")
    print("AFTER", app.logLevel)

def setts(btn):
    if btn == 'SIZE':
        if app.entry('y') is None:
            app.size=str(app.entry('x'))+'x'+str(app.entry('x'))
        else:
            app.size=(app.entry('x'), app.entry('y'))
    elif btn == 'LOCATION':
        app.location=(app.entry('x'), app.entry('y'))
    elif btn == 'FSIZE':
        app.size="fullscreen"
    elif btn == 'FULL':
        app.fullscreen = True
    elif btn == 'NOFULL':
        app.fullscreen = False
    elif btn == "RESIZE":
        app.resizable = app.check("RESIZE")
    elif btn == 'GET':
        app.label("t",
            "SIZE: " + str(app.size) + "\n" +
            "LOC: " + str(app.location) + "\n" +
            "FULL: " + str(app.fullscreen) + '\n' +
            "RES: " + str(app.resizable) 
        )
    elif btn == "fonts":
        app.label("fonts",
            "FG: " + str(app.fg) + "\n" +
            "BG: " + str(app.bg) + "\n" +
            "FONT: " + str(app.font) + "\n" +
            "BUTFONT: " + str(app.buttonFont) + "\n" + 
            "LABFONT: " + str(app.labelFont) + "\n"
        )

with gui("KWARGS TEST", bg="green") as app:
    with app.tabbedFrame("nb1", bg="blue"):

        with app.tab("fonts"):
            app.buttonFont = {'family':'arial', 'size':20}
            app.button("fonts", setts)
            app.label("fonts")

        with app.tab("settings", bg="green", fg="red"):
            app.entry("x", label=True, kind='numeric')
            app.entry("y", label=True, kind='numeric', pos=(0,1))
            app.check("RESIZE", label=True, change=setts)
            app.buttons(["SIZE", "FSIZE", "LOCATION", "FULL", "NOFULL"], setts, colspan=2)
            app.button('GET', setts, colspan=2)
            app.label('t', colspan=2, font={'size':20})

        with app.tab("LabelFrame", bg="yellow"):
            with app.labelFrame("LabelFrame", bg="green", fg="blue"):
                app.label("NEW ONES")
                app.radio("logger", "error", change=logger)
                app.radio("logger", "warning", change=logger)
                app.radio("logger", "debug", change=logger)
                app.radio("logger", "info", change=logger)
                app.radio("logger", "trace", change=logger)
            with app.labelFrame("LabelFrame", bg="green", fg="blue", row='p', column=1):
                app.label("OLD ONES")
                app.addRadioButton("logger2", "error")
                app.addRadioButton("logger2", "warning")
                app.addRadioButton("logger2", "debug")
                app.addRadioButton("logger2", "info")
                app.addRadioButton("logger2", "trace")
                app.setRadioButtonChangeFunction('logger2', logger)
                app.setRadioButtonChangeFunction('logger2', logger)

        with app.tab("ToggleFrame", bg="black", fg="white"):
            with app.toggleFrame("ToggleFrame", bg="pink", fg="red"):
                app.label("BLACK NOTE")
        with app.tab("PanedFrame", bg="orange"):
            app.label("ORANGE NOTE")
            with app.panedFrame("PanedFrame2", bg="orange", fg="white"):
                app.label("ORANGE NOTE2")
                with app.panedFrame("PanedFrame3", bg="green", fg="blue"):
                    app.label("ORANGE NOTE3")
        with app.tab("PagedWindow", bg="purple"):
            with app.pagedWindow("PagedWindow", bg="red", fg="yellow"):
                with app.page(bg="white", fg="pink"):
                    app.label("PINK ON WHITE")
                with app.page(bg="black", fg="red"):
                    app.label("RED ON BLACK")
                with app.page():
                    app.label("PURPLE3 NOTE")
        with app.tab("Frame", bg="red"):
            with app.frame("Frame", bg="purple", fg="white"):
                app.label("RED NOTE")
        with app.tab("ScrollPane", bg="grey"):
            with app.scrollPane("ScrollPane", sticky="SE", bg="pink"):
                app.label("GREY NOTE", bg="orange")
#        with app.tab("NoteBook", bg="yellow"):
#            with app.notebook("nb1"):
#                with app.note("note1", bg="green"):
#                    app.label("N_GREEN NOTE")
#                with app.note("note2", bg="pink"):
#                    app.label("N_PINK NOTE2")
#                with app.note("note3", bg="blue"):
#                    app.label("N_BLUE NOTE3")

    app.enterKey=press
    print(app.language)
