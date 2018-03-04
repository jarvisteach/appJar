import sys
sys.path.append("../../")
from appJar import gui

class appJarExplorer:
    def __init__(self, topLevel):
        self._topLevel = topLevel

    def buildTag(self, tag, data, details):
        xml = "<" + tag + ">"
        if data is not None:
            xml += "<text>" + data + "</text>"
        xml += details
        xml += "</" + tag + ">\n"
        return xml

    def getClass(self, widg):
        wClass = widg.winfo_class()
        wType = type(widg).__name__
        if wType != 'instance': wClass = wType
        if wClass == "Tk": wClass = "appJar"
        return wClass

    def getText(self, widg):
        try:
            text = widg.cget('text').replace("&", "&amp;")
            if text == "": text = "-EMPTY-"
            return text
        except: return None

    def getDetails(self, widg):
        try:
            grid = "<grid>"+widg.grid_info()['row']+"x"+widg.grid_info()['column']+"</grid>"
        except: grid = ""
        coordinates = "<coordinates>"+str(widg.winfo_rootx())+","+str(widg.winfo_rooty())+"</coordinates>"
        size = "<size>"+str(widg.winfo_reqwidth())+"x"+str(widg.winfo_reqheight())+"</size>"
        return coordinates+size + grid

    def getChildren(self, widg):
        children =  widg.winfo_children()
        wClass = self.getClass(widg)
        text = self.getText(widg)
        details = self.getDetails(widg)

        if len(children) == 0:
            return self.buildTag(wClass, text, details)
        else:
            text = "<" + wClass + ">"
            text += details
            for w in widg.winfo_children():
                text += self.getChildren(w)
            text += "</" + wClass + ">\n"
            return text

    def getXml(self):
        xml = "<?xml version='1.0' encoding='iso-8859-1'?>"
        xml += self.getChildren(self._topLevel)
        return xml

_explorerMade = False
def makeExplorer():
    global _explorerMade
    if not _explorerMade:
        _explorerMade = True
        xml = appJarExplorer(app.topLevel).getXml()
        with app.subWindow("appJar Explorer", size="300x450", sticky='news') as sw:
            sw.configure(padx=5, pady=5)
            with app.labelFrame("Explorer Tree", sticky='news'):
                app.configure(sticky="news")
                app.addTree("b", xml, row=1, column=1, rowspan=6)
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
