import sys
sys.path.append("../../")

from appJar import gui

def press():
    print("UNBINDING")
    app.enterKey=None
    app.language = "french"
    print("NEW LANG:", app.language)

with gui("KWARGS TEST", bg="green") as app:
    with app.tabbedFrame("nb1", bg="blue"):
        with app.tab("LabelFrame", bg="yellow"):
            with app.labelFrame("LabelFrame", bg="green", fg="blue"):
                app.label("YELLOW NOTE")
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
        with app.tab("NoteBook", bg="yellow"):
            with app.notebook("nb1"):
                with app.note("note1", bg="green"):
                    app.label("N_GREEN NOTE")
                with app.note("note2", bg="pink"):
                    app.label("N_PINK NOTE2")
                with app.note("note3", bg="blue"):
                    app.label("N_BLUE NOTE3")

    app.enterKey=press
    print(app.language)
