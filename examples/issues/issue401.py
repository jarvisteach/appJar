import sys
sys.path.append("../../")
from appJar import gui

class appJarExplorer:
    def __init__(self, topLevel):
        self._topLevel = topLevel

    def buildTag(self, tag, data, details):
        xml = "<" + tag + ">" + "<text>" + data + "</text>" + details + "</" + tag + ">\n"
        return xml

    def getClass(self, widg):
        wClass = widg.winfo_class()
        if wClass == "Tk": wClass = "appJar"
        elif wClass == "Toplevel": wClass = "SubWindow"
        return wClass

    def getText(self, widg):
        try:
            text = widg.cget('text')
            if text == "": text = "-EMPTY-"
        except: text = "-NONE-"
        text = text.replace("&", "&amp;")
        return text

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
        explorer = appJarExplorer(app.topLevel)
        with app.subWindow("appJar Explorer", size="300x450", sticky='news') as sw:
            sw.configure(padx=5, pady=5)
            with app.labelFrame("Explorer Tree", sticky='news'):
                app.configure(sticky="news")
                app.addTree("b", explorer.getXml(), row=1, column=1, rowspan=6)
        app.generateTree("b")
    app.showSubWindow("appJar Explorer")

with gui("appJar Explorer") as app:
    app.label("Title Label", colspan=2)
    app.label("DETAILS", "")
    app.entry("DETAILS2")
    app.check("check")
    app.radio("radio", "r1")
    app.button("DETAILS", makeExplorer)

    with app.subWindow("sub"):
        app.label("in sub")

    app.addGoogleMap("g")
