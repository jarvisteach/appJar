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
    app.link("GOOGLE", "aaa")


from appJar import gui

with gui("Button tester") as app:
    app.button("PARAM", param)
    app.button("NO PARAM", noParam)
    app.link("GOOGLE", "http://www.google.com")
    app.link("PARAM", param)
    app.link("NO PARAM", noParam)
