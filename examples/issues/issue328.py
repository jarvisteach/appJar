import sys
sys.path.append("../../")
from appJar import gui

currFont = currBg = currFg = None

def open():
    global currFont, currBg, currFg
    # get current settings
    currFont = app._labelFont.actual()
    currBg = app.bgLabel.cget("bg")
    currFg = app.containerStack[0]["fg"]
    reset()
    app.showSubWindow("Accessibility")

def reset():
    app.listbox("Family", currFont["family"])
    app.option("Size:", str(currFont["size"]))

    if currFont["weight"] == "normal": app.check("Bold", False)
    else: app.check("Bold", True)

    if currFont["slant"] == "roman": app.radio("slant", "Normal")
    else: app.radio("slant", "Italic")

    app.check("Overstrike", currFont["overstrike"])
    app.check("Underline", currFont["underline"])

    app.label("fg", bg=currFg)
    app.label("bg", bg=currBg)
 
def close(): app.hideSubWindow("Accessibility")
def changeFg(): app.label("fg", bg=app.colourBox(app.getLabelBg("fg")))
def changeBg(): app.label("bg", bg=app.colourBox(app.getLabelBg("bg")))

def settings():
    font = {"underline":app.check("Underline"), "overstrike":app.check("Overstrike")}

    font["weight"] = "bold" if app.check("Bold") is True else "normal"
    font["slant"] = "roman" if app.radio("slant") == "Normal" else "italic"
    if len(app.listbox("Family")) > 0: font["family"] = app.listbox("Family")[0]
    if app.option("Size:") is not None: font["size"] = app.option("Size:")

    app.font = font
    app.bg = app.getLabelBg("bg")
    app.fg = app.getLabelBg("fg")

with gui("COLOUR TEST", "400x400") as app:
    app.label("Some text")
    app.button("Accessibility", open, icon="ACCESS", tip="Click here for accessibility options")

    with app.subWindow("Accessibility", sticky = "news", location=(200,200)) as sw:
        sw.config(padx=5, pady=1)
        with app.labelFrame("Font", sticky="news") as lf:
            lf.config(padx=10, pady=10)
            app.listbox("Family", app.fonts, rows=6, tip="Choose a font", colspan=2)
            app.option("Size:", [7, 8, 9, 10, 12, 13, 14, 16, 18, 20, 22, 25, 29, 34, 40], label=True, tip="Choose a font size")
            app.check("Bold", pos=('p',1), tip="Check this to make all font bold")
            app.radio("slant", "Normal", tip="No italics")
            app.radio("slant", "Italic", pos=('p',1), tip="Set font italic")
            app.check("Underline", tip="Underline all text")
            app.check("Overstrike", pos=('p',1), tip="Strike out all text")
            app.label("Foreground:", sticky="ew", anchor="w")
            app.label("fg", "", pos=('p',1), sticky="ew", submit=changeFg, relief="ridge", tip="Click here to set the foreground colour")
            app.label("Background:", sticky="ew", anchor="w")
            app.label("bg", "", pos=('p',1), sticky="ew", submit=changeBg, relief="ridge", tip="Click here to set the background colour")
        app.buttons(["OK", "Cancel", "Reset"], [settings, close, reset], sticky="se")
