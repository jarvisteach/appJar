import sys
sys.path.append("../../")
from appJar import gui

def close(): app.hideSubWindow("Accessibility")
def changeFg(): app.label("fg", bg=app.colourBox(app.getLabelWidget("fg").cget("bg")))
def changeBg(): app.label("bg", bg=app.colourBox(app.getLabelWidget("bg").cget("bg")))

def settings():
    font = {"underline":app.check("Underline"), "overstrike":app.check("Overstrike")}

    font["weight"] = "bold" if app.check("Bold") is True else "normal"
    font["slant"] = "roman" if app.radio("slant") == "Normal" else "italic"
    if len(app.listbox("Family")) > 0: font["family"] = app.listbox("Family")[0]
    if app.option("Size:") is not None: font["size"] = app.option("Size:")

    app.font = font
    app.bg = app.getLabelWidget("bg").cget("bg")
    app.fg = app.getLabelWidget("fg").cget("bg")

with gui("COLOUR TEST", "400x400") as app:
    app.label("Some text")
    app.button("Accessibility", app.showSubWindow, icon="ACCESS", tip="Click here for accessibility options")

    with app.subWindow("Accessibility", sticky = "news", location=(200,200)) as sw:
        sw.config(padx=5, pady=1)
        with app.labelFrame("Font", sticky="news") as lf:
            lf.config(padx=10, pady=10)
            app.listbox("Family", app.fonts, colspan=2, rows=6)
            app.option("Size:", [7, 8, 9, 10, 12, 13, 14, 16, 18, 20, 22, 25, 29, 34, 40], label=True, pos=(1,0), selected="12")
            app.check("Bold", pos=(1,1))
            app.radio("slant", "Normal", pos=(2,0))
            app.radio("slant", "Italic", pos=(2,1))
            app.check("Underline", pos=(3,0))
            app.check("Overstrike", pos=(3,1))
            app.label("Foreground:", pos=(4,0), sticky="ew", anchor="w")
            app.label("fg", "", pos=(4,1), bg="black", sticky="ew", submit=changeFg, relief="ridge")
            app.label("Background:", pos=(5,0), sticky="ew", anchor="w")
            app.label("bg", "", pos=(5,1), bg="grey", sticky="ew", submit=changeBg, relief="ridge")
        app.buttons(["Update", "Close"], [settings, close], sticky="se")
