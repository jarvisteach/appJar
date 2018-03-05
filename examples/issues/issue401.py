import sys
sys.path.append("../../")
from appJar import gui

class appJarExplorer:
    def __init__(self, topLevel):
        self._topLevel = topLevel

    def buildTag(self, tag, details, _id):
        xml = "<" + tag + " id='" + _id + "'>"
#        xml += details
        xml += "</" + tag + ">\n"
        return xml

    def getClass(self, widg):
        kind = type(widg).__name__
        if kind == "instance": kind = widg.winfo_class()
        if kind == "Tk": kind = "appJar"
        return kind

    def getDetails(self, widg):
        try:
            text = widg.cget('text').replace("&", "&amp;")
            if text == "": text = "-EMPTY-"
            text = "<text>" + text + "</text>"
        except: text=""
        try:
            grid = "<grid>"+widg.grid_info()['row']+"x"+widg.grid_info()['column']+"</grid>"
        except: grid = ""
        coordinates = "<coordinates>"+str(widg.winfo_rootx())+","+str(widg.winfo_rooty())+"</coordinates>"
        size = "<size>"+str(widg.winfo_reqwidth())+"x"+str(widg.winfo_reqheight())+"</size>"
        return text+coordinates+size + grid

    def getChildren(self, widg):
        children =  widg.winfo_children()
        kind = self.getClass(widg)
        details = self.getDetails(widg)

        if len(children) == 0:
            return self.buildTag(kind, details, str(widg))
        else:
            text = "<" + kind + " id='" + str(widg) + "'>"
#            text += details
            for w in widg.winfo_children():
                text += self.getChildren(w)
            text += "</" + kind + ">\n"
            return text

    def getXml(self):
        xml = "<?xml version='1.0' encoding='iso-8859-1'?>"
        xml += self.getChildren(self._topLevel)
        return xml

def widgProps(widg):
    props = {}
    try: props['text'] = widg.cget('text')
    except: props['text'] = ""
    try: props['grid'] = widg.grid_info()['row']+"x"+widg.grid_info()['column']
    except: props['grid'] = ""
    props['coordinates'] = str(widg.winfo_rootx())+","+str(widg.winfo_rooty())
    props['size'] = str(widg.winfo_reqwidth())+"x"+str(widg.winfo_reqheight())
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
                app.entry("Text", props['text'])
                app.entry("Grid", props['grid'])
                app.entry("Coordinates", props['coordinates'])
                app.entry("Size", props['size'])
                app.entry("Kind", props['kind'])
        else:
            pass

    def press():
        if _currentId is not None:
            widg = app.topLevel.nametowidget(_currentId)
            widg.config(text=app.entry('Text'))
        

    global _explorerMade
    if not _explorerMade:
        _explorerMade = True
        xml = appJarExplorer(app.topLevel).getXml()
        with app.subWindow("appJar Explorer", size="600x450", sticky='news') as sw:
            sw.configure(padx=5, pady=5)
            with app.panedFrame("LEFT"):
                app.configure(sticky="news")
                app.addTree("b", xml, row=1, column=1, rowspan=6)
                app.setTreeDoubleClickFunction("b", updateConfigPane)
                app.setTreeEditable("b", False)
                with app.panedFrame("RIGHT", sticky="new"):
                    app.config(sticky='new', stretch='column')
                    app.bg="blue"
                    app.fg="white"
                    app.label("Configure Widget", colspan=2)
                    app.label("Kind:")
                    app.entry("Kind", pos=('p', 1))
                    app.label("Text:")
                    app.entry("Text", pos=('p', 1))
                    app.label("Grid:")
                    app.entry("Grid", pos=('p', 1))
                    app.label("Coords:")
                    app.entry("Coordinates", pos=('p', 1))
                    app.label("Size:")
                    app.entry("Size", pos=('p', 1))
                    app.button("Update", press, colspan=2)
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
        with app.tab("b"):
            app.addGoogleMap("g")

    with app.subWindow("sub"):
        app.label("in sub")

    app.addStatusbar()
