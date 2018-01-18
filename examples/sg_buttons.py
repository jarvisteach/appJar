import sys
sys.path.append("../")

def param(a):
    print("Param:", a)
    print(app.button("PARAM", fg="red"))
    print(app.button("NO PARAM"))

def noParam():
    print("no param")
    app.button("NEW ONE", param)


from appJar import gui

with gui("Button tester") as app:
    app.button("PARAM", param)
    app.button("NO PARAM", noParam)
