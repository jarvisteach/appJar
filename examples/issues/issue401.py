import sys
sys.path.append("../../")
from appJar import gui

class appJarExplorer:
    def __init__(self, topLevel):
        self._topLevel = topLevel

    def buildTag(self, tag, _id):
        xml = "\t<" + tag + " id='" + _id + "'></" + tag + ">\n"
        return xml

    def getClass(self, widg):
        kind = type(widg).__name__
        if kind == "instance": kind = widg.winfo_class()
        if kind == "Tk": kind = "appJar"
        return kind

    def getChildren(self, widg):
        children =  widg.winfo_children()
        kind = self.getClass(widg)

        if kind.lower() == 'menu':
            print(widg)
            menus = widg.index('end')
            if menus is not None:
                for item in range(menus+1):
                    print('\t\t', widg.entrycget(item, 'label'))

        try: name = widg.cget('text')
        except: name = ''

        if len(name) > 0: kind += '-' + name.replace(' ', '_')

        if len(children) == 0:
            return self.buildTag(kind, str(widg))
        else:
            text = "<" + kind + " id='" + str(widg) + "'>\n"
            for w in widg.winfo_children():
                text += self.getChildren(w)
            text += "</" + kind + ">\n"
            return text

    def getXml(self):
        xml = "<?xml version='1.0' encoding='iso-8859-1'?>\n"
        xml += self.getChildren(self._topLevel)
        print(xml)
        return xml

def widgProps(widg):
    props = {}
    try: props['text'] = widg.cget('text')
    except: props['text'] = ""
    try:
        props['row'] = widg.grid_info()['row']
        props['column'] = widg.grid_info()['column']
    except: props['row'] = props['column'] = ""
    props['x'] = str(widg.winfo_rootx())
    props['y'] = str(widg.winfo_rooty())
    props['width'] = str(widg.winfo_reqwidth())
    props['height'] = str(widg.winfo_reqheight())
    props['kind'] = type(widg).__name__
    if props['kind'] == 'instance': props['kind'] = widg.winfo_class()
    if props['kind'] == "Tk": props['kind'] = "appJar"
    return props


_explorerMade = False
_currentId = None
def makeExplorer():
    def updateConfigPane(tree, val):
        if val is not None:
            widg = app.topLevel.nametowidget(val)
            props = widgProps(widg)
            vals = app.getTreeSelected(tree)
            if vals is not None and vals[1] == val:
                global _currentId
                _currentId = val
                app.entry("text", props['text'])
                app.entry("row", props['row'])
                app.entry("column", props['column'])
                app.entry("x", props['x'])
                app.entry("y", props['y'])
                app.entry("width", props['width'])
                app.entry("height", props['height'])
                app.entry("kind", props['kind'])
        else:
            pass

    def press():
        if _currentId is not None:
            print(app.getAllEntries())
            widg = app.topLevel.nametowidget(_currentId)
            widg.config(text=app.entry('text'))
            widg.grid(row=int(app.entry("row")), column=int(app.entry("column")))
        

    global _explorerMade
    if not _explorerMade:
        _explorerMade = True
        xml = appJarExplorer(app.topLevel).getXml()
        with app.subWindow("appJar Explorer", size="600x450", sticky='news') as sw:
            app.bg = "#3b3f40"
            sw.configure(padx=5, pady=5)
            with app.panedFrame("LEFT"):
                app.configure(sticky="news")
                app.addTree("b", xml, row=1, column=1, rowspan=6)
                app.setTreeClickFunction("b", updateConfigPane)
                app.setTreeEditable("b", False)
                app.setTreeBg('b', "#3b3f40")
                app.setTreeFg('b', "#adadad")
                with app.panedFrame("RIGHT", sticky="new"):
                    app.config(sticky='new', stretch='column', bg="#3b3f40", fg="#adadad", font={'size':16})
                    app.label("Configure Widget", colspan=2, fg='#ca753d', font={'size':20, 'weight':'bold'})
                    app.label("Kind:", anchor='w')
                    app.entry("kind", pos=('p', 1))
                    app.label("Text:", anchor='w')
                    app.entry("text", pos=('p', 1))
                    app.label("Row:", anchor='w')
                    app.entry("row", pos=('p', 1))
                    app.label("Column:", anchor='w')
                    app.entry("column", pos=('p', 1))
                    app.label("X:", anchor='w')
                    app.entry("x", pos=('p', 1))
                    app.label("Y:", anchor='w')
                    app.entry("y", pos=('p', 1))
                    app.label("Width:", anchor='w')
                    app.entry("width", pos=('p', 1))
                    app.label("Height:", anchor='w')
                    app.entry("height", pos=('p', 1))
                    app.button("Update", press, column=1)
        app.generateTree("b")
    app.showSubWindow("appJar Explorer")

with gui("appJar Explorer") as app:
    with app.tabbedFrame("tf"):
        with app.tab("a"):
            app.label("Title Label", colspan=2)
            app.label("DETAILS", "")
            app.entry("DETAILS2")
            app.check("check")
            app.radio("radio", "r1")
            app.button("DETAILS", makeExplorer)
#        with app.tab("b"):
#            app.addGoogleMap("g")

    with app.subWindow("sub"):
        app.label("in sub")

    app.addToolbarButton('SAVE', makeExplorer, True)
    app.addStatusbar()
    for x in range(5):
        app.addMenuItem('MY MEN', str(x))
