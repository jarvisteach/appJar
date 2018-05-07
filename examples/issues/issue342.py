import sys
sys.path.append("../../")
from appJar import gui

pages = ["Page 1", "Page 2", "Page 3", "Page 4", "Page 5", "Page 6", "Page 7", "Page 8"]
showButtons = True
BG = "lightslategrey"
OPS = None
KEYS = ["<Leave>", "<Enter>", "<Up>", "<Down>", "<Double-Button-1>", "<ButtonPress-1>", "<ButtonRelease-1>", "<B1-Motion>", "<Home>", "<End>", "<space>", "<Prior>", "<Next>"]


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
    pos = pages.index(app.listBox("list")[0])
    app.selectFrame("frames", pos)
    if showButtons: updateButtons()

def press(btn):
    pos = pages.index(app.listBox("list")[0])

    if btn == "Previous": pos -= 1
    elif btn == "Next": pos += 1

    if pos < 0 or pos == len(pages): app.bell()
    else: app.selectListItemAtPos("list", pos, True)

def disableInteraction(lb, disable=True):
    global OPS
    if disable and OPS is None:
        OPS = {}
        def no_op(event): return "break"
        for k in KEYS:
            OPS[k] = lb.bind(k, no_op)
    elif not disable and OPS is not None:
        for k in OPS:
            lb.unbind(k, OPS[k])
        OPS = None

def push(btn):
    if btn == "ENABLE": disableInteraction(lb, False)
    else: disableInteraction(lb)

with gui("SideMenu", resizable=True, guiPadding=(5,5), bg=BG, stretch="both", location=(450,100),
        size=(600,400), sticky="news", inputFont=20, labelFont=20, buttonFont=15, transparency=98) as app:

    with app.labelFrame("Setup"):
        # hack to have grey border
        app.config(sticky="new", stretch="column")
        with app.frame("top", 0, 0, 4, 1, bg=BG) as f:
            f.config(height=8)
            app.containerStack[-1]['widgets'] = True
        app.config(sticky="nsw", stretch="row")
        with app.frame("left", 1, 0, 1, 1, bg=BG) as f:
            f.config(width=8)
            app.containerStack[-1]['widgets'] = True
        
        app.config(sticky="nsw", stretch = "none")
        lb = app.listBox("list", pages, row=1, column=1, change=change, rows=len(pages), activestyle="none",
                    borderwidth=0, selectborderwidth=0, highlightthickness=0, width=12, border=0, background=BG)
        disableInteraction(lb)

        app.config(sticky="news", stretch = "both")
        with app.frameStack("frames", 1, 2):
            for pos, page in enumerate(pages):
                bg=app.RANDOM_COLOUR(), 
                fg=app.RANDOM_COLOUR(), 
                with app.frame(bg=bg):
                    lb.itemconfig(pos, {'selectbackground':bg, 'selectforeground':fg})
                    with app.labelFrame(page, inPadding=(17,17), bg=bg, sticky="new", fg=fg) as f:
                        f.config(foreground=fg)
                        app.label("l" + page, page)

        app.config(sticky="nes", stretch="row")
        with app.frame("right", 1, 3, 1, 1, bg=BG) as f:
            f.config(width=8)
            app.containerStack[-1]['widgets'] = True

        app.config(sticky="esw", stretch="none")
        with app.frame("bottom", 2, 0, 4, 1, bg=BG) as f:
            f.config(height=8)
            app.containerStack[-1]['widgets'] = True

    if showButtons:
        app.buttons(["Previous", "Next"], press, sticky="se", stretch="column")

    app.selectListItemAtPos("list", 0, callFunction=True)
    app.buttons(["DISABLE", "ENABLE"], push)
