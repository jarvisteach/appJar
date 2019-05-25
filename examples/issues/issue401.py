import sys
sys.path.append("../../")
from appJar import gui

class appJarExplorer:
    def __init__(self, app):
        self._app = app
        self._currentId = None

        # generate the subWindow
        # note tree BG & sub PADDING not right..
        with self._app.subWindow("appJar Explorer", size="600x450", sticky='news', bg='#3b3f40', fg='#adadad',  padx=5, pady=5) as sw:
            sw.configure(padx=5, pady=5)
            with self._app.frame("LEFT", 0, 0, sticky='news'):
                self._app.tree("b", self.getXml(), row=1, column=1, rowspan=6, click=self.updateConfigPane, editable=False, bg="#3b3f40", fg="#adadad")
            with self._app.frame("RIGHT", 0, 1, sticky='news', stretch='column'):
                app.font={'size':16}
                with self._app.labelFrame("Configure Widget", sticky='new', stretch='column', labelFg='#ca753d'):
                    self._app.label('EMPTY')
                self._app.button("Update", self.updatePressed, pos=(1,0))
        self._app.generateTree("b")

    def showExplorer(self):
        """ make the subwindow visible """
        self._app.showSubWindow("appJar Explorer")

    def buildTag(self, tag, _id=None):
        """ make a tag from the data """
        if _id is None: xml = "\t<" + tag + "></" + tag + ">\n"
        else: xml = "\t<" + tag + " id='" + _id + "'></" + tag + ">\n"
        return xml

    def getChildren(self, widg, label=None):
        """ recursive function to get all children as XML """
        children =  widg.winfo_children()

        # determine what *kind* the widget is
        kind = type(widg).__name__
        if kind == "instance": kind = widg.winfo_class()
        if kind == "Tk": kind = "appJar"

        try:
            if label is None:
                name = widg.cget('text').replace(' ', '_')
            else:
                name = label.replace(' ', '_')
        except:
            name = ''

        if len(name) > 0: name = kind + '-' + name
        else: name = kind

        if kind.lower() == 'menu':
            if str(widg).endswith('apple'): name = "AppleMenu"
            elif str(widg).endswith('help'): name = "AppleHelp"
            elif str(widg).endswith('window'): name = "AppleWindow"
            menus = widg.index('end')
            if menus is not None:
                text = "<" + name + " id='" + str(widg) + "'>\n"
                count = 0
                # add any menu items
                for pos in range(menus+1):
                    if widg.type(pos) == 'separator':
                        text += self.buildTag("Separator")
                    elif widg.type(pos) == 'checkbutton':
                        text += self.buildTag("CheckBox")
                    elif widg.type(pos) == 'radiobutton':
                        text += self.buildTag("RadioButton")
                    elif widg.type(pos) == 'cascade':
                        w = widg.winfo_children()[count]
                        label = widg.entrycget(pos, 'label')
                        text += self.getChildren(w, label)
                        count += 1
                    else:
                        text += self.buildTag(name + '_' + widg.entrycget(pos, 'label').replace(' ', '_'))
                text += "</" + name + ">"
                return text
            else:
                return self.buildTag(name, str(widg))

        if len(children) == 0:
            return self.buildTag(name, str(widg))
        else:
            text = "<" + name + " id='" + str(widg) + "'>\n"
            for w in widg.winfo_children():
                text += self.getChildren(w)
            text += "</" + name + ">\n"
            return text

    def getXml(self):
        # converts the GUI into XML
        xml = "<?xml version='1.0' encoding='iso-8859-1'?>\n"
        xml += self.getChildren(self._app.topLevel)
        return xml

    def widgProps(self, widg):
        """ get a customised dictionary of properties for the widget """
        props = {}
        try: props['text'] = widg.cget('text')
        except: props['text'] = ""
        try:
            props['row'] = widg.grid_info()['row']
            props['column'] = widg.grid_info()['column']
        except:
            props['row'] = props['column'] = ""
        props['x'] = str(widg.winfo_rootx())
        props['y'] = str(widg.winfo_rooty())
        props['width'] = str(widg.winfo_reqwidth())
        props['height'] = str(widg.winfo_reqheight())
        props['kind'] = type(widg).__name__
        if props['kind'] == 'instance': props['kind'] = widg.winfo_class()
        if props['kind'] == "Tk": props['kind'] = "appJar"
        return props

    def updatePressed(self):
        """ get data in entries & apply to current widget """
        if self._currentId is not None:
            vals = self._app.getAllEntries()
            newVals = {}
            for k in vals.keys():
                if k.startswith('APP_EXP_'):
                    newVals[k[8:]] = vals[k]
            widg = self._app.topLevel.nametowidget(self._currentId)
            print(newVals)
            widg.config(newVals)
            try: widg.grid(row=int(self._app.entry("row")), column=int(self._app.entry("column")))
            except ValueError: print("Invalid position")

    def updateConfigPane(self, tree, val):
        """ update the RIGHT (config) pane """
        if val is not None:
            # get the widget object using the val code
            widg = self._app.topLevel.nametowidget(val)
            # get a customised set of properties
            props = self.widgProps(widg)
            vals = self._app.getTreeSelected(tree)
            if vals is not None and vals[1] == val:
                self._currentId = val
                self._app.removeLabelFrame("Configure Widget")
                with self._app.frame("RIGHT"):
                    with self._app.labelFrame("Configure Widget", row=0, sticky='ew', stretch='column', font={'size':16}, fg="#adadad") as lf:
                        lf.config(fg='#ca753d')
                        for k in props.keys():
                            self._app.label(k.capitalize() + ":", anchor='e')
                            self._app.entry('APP_EXP_'+k , props[k], pos=('p', 1))

# function to create the explorer SubWindow
explorer = None
def makeExplorer():
    # this makes the new SubWindow
    global explorer
    if explorer is None:
        explorer = appJarExplorer(app)
    explorer.showExplorer()

# make a dummy GUI
with gui("appJar Explorer") as app:
    with app.tabbedFrame("tf"):
        app.setTabbedFrameActiveBg("tf", 'pink')
        with app.tab("a"):
            app.label("Title Label", colspan=2)
            app.label("DETAILS", "")
            app.entry("DETAILS2")
            app.entry("files", kind='file', label=True)
            app.buttons(['a', 'b'], None)
            app.check("check")
            app.radio("radio", "r1")
            # pressing the button creates the explorer
            app.button("DETAILS", makeExplorer)
        for t in ['b', 'c', 'd', 'e', 'f']:
            with app.tab(t):
                app.label(t)
        app.setTabBg('tf', 'c', 'green')

    with app.subWindow("sub"):
        app.label("in sub")

    app.addToolbarButton('SAVE', makeExplorer, True)
    app.addStatusbar()
    app.addMenuCheckBox('MY MEN', 'checker')
    app.addMenuRadioButton('MY MEN', 'radio', 'radio')
    for x in range(5):
        app.addMenuItem('MY MEN', str(x))
        app.addMenuSeparator('MY MEN')
    app.addSubMenu("MY MEN", "SUB")
    app.addMenuItem('SUB', "subber")
    app.addSubMenu("SUB", "SUB_SUB")
    app.addMenuItem('SUB_SUB', "super_sub")
    app.addMenuItem('MAC_APP', "map_app")
    app.addMenuPreferences(makeExplorer)
    app.addMenuHelp(makeExplorer)
    app.addMenuItem('MAC_HELP', "more help")
    app.addMenuWindow()
