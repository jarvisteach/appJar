import sys
sys.path.append("../")

def param(a):
    print("Param:", a)
    print(app.button("PARAM", fg="red"))
    print(app.button("NO PARAM"))
    print(app.link("GOOGLE", fg="red"))
    print(app.link("PARAM"))
    print(app.link("NO PARAM"))

def noParam():
    print("no param")
    app.button("NEW ONE", param)

def setTheme():
    app.ttkTheme = app.popUp("theme", "theme", kind="text")

def showThemes(): app.popUp("Themes", str(app.getTtkThemes(True)))
def showTheme(): app.popUp("Current Theme", app.ttkTheme)


from appJar import gui

with gui("Button tester", useTtk=True) as app:
    app.button("PARAM", param)
    app.button("NO PARAM", noParam)
    app.link("GOOGLE", "http://www.google.com")
    app.link("PARAM", param)
    app.link("NO PARAM", noParam)
    app.button("SET THEME", setTheme)
    app.button("THEMES", showThemes)
    app.button("SHOW", showTheme)
