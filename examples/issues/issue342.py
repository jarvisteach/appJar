import sys
sys.path.append("../../")
from appJar import gui

pages = ["Page 1", "Page 2", "Page 3", "Page 4", "Page 5", "Page 6"]
bgs = [ "red", "yellow", "green", "purple", "pink", "skyblue"]

def updateButtons():
    currentPage = app.listBox("list")[0]
    if currentPage == pages[0]:
        app.disableButton("Previous")
    elif currentPage == pages[-1]:
        app.disableButton("Next")
    else:
        app.enableButton("Previous")
        app.enableButton("Next")

def change(listName):
    app.getFrameWidget(app.listBox("list")[0]).lift()
    updateButtons()

def press(btn):
    pos = pages.index(app.listBox("list")[0])

    if btn == "Previous": pos -= 1
    elif btn == "Next": pos += 1

    if pos < 0 or pos == len(pages):
        app.bell()
        return
    else:
        app.selectListItemAtPos("list", pos, True)

with gui("SideMenu", resizable=True, icon="favicon.ico",
            bg="lightslategrey", fg="black", stretch="both", location=(450,100),
            size=(600,400), sticky="news", labelFont=20, buttonFont=15, transparency=98) as app:

    with app.labelFrame("Setup", sticky="nws", stretch="none", padding=[10,10]):
        app.listBox("list", pages, row=0, column=0, change=change, rows=len(pages), focus=True,
                    width=12, border=0, selectbackground="blue", selectforeground="white", background="lightslategrey", fg="black")
        app.configure(sticky="news", stretch = "both")
        for pos, page in enumerate(pages):
            with app.frame(page, 0, 1, inPadding=(17,17), bg=bgs[pos], sticky="new"):
                app.label("l" + page, page, bg="white")

    app.configure(sticky="se", stretch="column")
    app.addButtons(["Previous", "Next"], press)
    app.selectListItemAtPos("list", 0, callFunction=True)
