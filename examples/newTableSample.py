# https://mail.python.org/pipermail/tkinter-discuss/2009-September/002069.html
import sys
sys.path.append("../")
from Tkinter import *
from tkFont import Font
from appJar import gui

class Spreadsheet(Frame):

    def __init__(self, parent, font=None, **keywords):
        Frame.__init__(self, parent)
        self.columns=[]

        # Setup font information
        if font:
            self.txtFont=font
        else:
            self.txtFont=Font(family="Arial", size=14)

        self.defaultRowHeight=self.txtFont['size']+7
        self.headerFont=self.txtFont.copy()
        self.headerFont.configure(weight='bold')

        self.spreadsheet=Canvas(self, bg='white', bd=0, highlightthickness=0, **keywords)
        self.header=Canvas(self, height=self.defaultRowHeight+2, bd=0, highlightthickness=0, bg='white')
        self.header.pack(side=TOP, expand=FALSE, fill=X, pady=0)

        self.scrollY = Scrollbar(self, orient=VERTICAL, command=self.spreadsheet.yview )
        self.scrollX = Scrollbar(self, orient=HORIZONTAL, command=self.xview )
        self.spreadsheet["xscrollcommand"] = self.scrollX.set
        self.spreadsheet["yscrollcommand"] = self.scrollY.set
        self.scrollY.pack(side="right", fill="y")
        self.scrollX.pack(side="bottom", fill="x")
        self.spreadsheet.pack(fill="both", expand=True, side="left")

        # Set up the mousewheel to scroll
        self.spreadsheet.focus_set()
        self.spreadsheet.bind("<MouseWheel>", self.mouseScroll)

        # Store current cursor (the one to restore to after a change)
        self.defaultCursor=self.cget("cursor")
        self.bind("<Configure>", self.catchResize)

    def catchResize(self, event):
        try:
            self.after_cancel(self.config_id)
        except: pass
        self.config_id = self.after(500, self.optimiseColumns)


    def xview(self, *args):
        self.header.xview(*args)
        self.spreadsheet.xview(*args)

    def initialise(self):
        self.spreadsheet.delete(ALL)
        # Any window items still bound, destroy
        for c in self.spreadsheet.children.values(): c.destroy()

        self.columns=[]
        self.rows=[]
        self.startCol=0
        self.startRow=0
        self.totalHeight=0

    def mouseScroll(self, event):
        if event.delta >0:
            self.spreadsheet.yview("scroll", "-1", "units")
        else:
            self.spreadsheet.yview("scroll", "1", "units")

    def setupColumns(self, columns):

        self.columns=[]

        for i in range(0, len(columns)):
            column=columns[i]
            name=column[0]
            width=column[1]
            if len(column)>2:
                align=column[2]
            else:
                align=CENTER
            self.columns.append([name,width,align])

    def addColumn(self, label, width=50, align=LEFT, bg='white', fg='black'):
        col=dict()
        col['label']=label
        col['width']=width
        col['align']=align
        col['bg']=bg
        col['fg']=fg
        self.columns.append(col)

    def addRow(self, pos, row):
        if len(row) != len(self.columns):
            raise Exception('Invalid row data, must be ' + str(len(self.columns)) + ' items long.')
        row=Row(row)
        row.height=self.getRowHeight(row)

        row.widgets=[]
        col=0
        for item in row:
            colDat=self.columns[col]
            if isinstance(item, Widget):
                row.widgets.append(item)
                item.internal=False
            elif isinstance(item, bool):
                item = Checkbutton(ssw.spreadsheet)
                row.widgets.append(item)
                item.internal=False
            elif isinstance(item, list):
#                item = OptionMenu(ssw.spreadsheet)
#                row.widgets.append(item)
#                item.internal=False
                pass

            else:
                e = Label(self.spreadsheet, bg=colDat['bg'], fg=colDat['fg'], font=self.txtFont, justify=colDat['align'], text=item, borderwidth=2, relief=SUNKEN)
                e.internal=True
#                if colDat['align']==RIGHT: e.xview(END)

                row.widgets.append(e)
            col += 1

        if pos==END:
            self.rows.append(row)
        else:
            self.rows.insert(pos, row)

    def getRowHeight(self, row):
        maxh=0
        for item in row:
            maxh=max(maxh, self.valHeight(item))
        return maxh


    def optimiseColumns(self, fixedWidth=True):
        if not self.columns: return

        # 1. Find the current total
        totWidth=0
        for column in self.columns:
            totWidth+=column['width']

        # Minimise columns which can be
        newWidth=0
        for col in range(0, len(self.columns)):
            maxwidth=self.neededWidth(col)
            colObj=self.columns[col]
            if maxwidth<colObj['width']:
                colObj['width']=maxwidth
            newWidth+=colObj['width']

        # Now, if some columns need more space, and it is available, give it to them
        swidth=self.spreadsheet.winfo_width()
        if swidth<2:
            swidth=self.spreadsheet.winfo_reqwidth()

        if swidth>newWidth:
            # we have free space

            expand=[]
            for col in range(0, len(self.columns)):
                coldat=self.columns[col]
                reqwidth=self.neededWidth(col)
                if reqwidth>coldat['width']:
                    expand.append((coldat, reqwidth-coldat['width']))

            # Now, we assign each col an equal share of the free space,
            # up to their max requirement
            free=swidth-newWidth
            expand.sort(cmp=lambda a, b: cmp(a[1], b[1]))
            while expand:
                if free<1: break
                col,req=expand.pop()
                req=min(free, req)
                col['width']+=req
                free=free-req

        self.show()

    def neededWidth(self, col):
        maxwidth=self.headerFont.measure(self.columns[col]['label'])
        for row in self.rows:
            wdth=self.valWidth(row[col])
            maxwidth=max(wdth, maxwidth)
        return maxwidth+6


    def valWidth(self, val):
        if isinstance(val, basestring):
            return self.txtFont.measure(val)
        try:
            return val.winfo_reqwidth()
        except: pass


    def valHeight(self, val):
        if isinstance(val, basestring):
            return self.defaultRowHeight
        try:
            return val.winfo_reqheight()
        except: pass


    ##########################################
    # REDRAWING

    # REDRAW after change of screensize
    # Called after screen resize or the first time

    def show(self):
        self.spreadsheet.delete(ALL)
        self.redrawHeader()
        self.redrawSheet()

    def redrawHeader(self):
        self.header.delete(ALL)
        x=5
        height=self.defaultRowHeight+2
        self.header.create_line(x, 2, x, height)
        count=0
        for col in self.columns:
            width=col['width']
            self.header.create_rectangle(x+1, 3, x+width-1, height-1, fill="#c1c2ef", outline="#c1c2ef")
            self.header.create_line(x, 2, x+width, 2)
            self.header.create_line(x, height, x+width, height)
            self.header.create_line(x+width, 2, x+width, height, tags=('colend', str(count)))

            self.header.create_text(x+width/2, 1, text=col['label'], anchor=N, font=self.headerFont, tags=('title', str(count)))
            # for the endline use a rect of width 3, but the border same as background
            # Basically, this gives us a widget of 3 pix width for detecting enter/leave events
            self.header.create_rectangle(x+width-1, 2, x+width+1, height, fill='black', outline="#c1c2ef", tags=('colend', str(count)))
            x+=width
            count+=1

        self.header["scrollregion"]=(0,0, x+self.scrollY.winfo_reqwidth(), height)

        # Make sure all controls are on top
        self.header.tag_raise('colend')
        self.header.tag_bind("colend", "<Enter>", self.enterColEnd)
        self.header.tag_bind("colend", "<Leave>", self.leaveColEnd)
        self.header.tag_bind("colend", "<Button-1>", self.startDrag)
        self.header.tag_bind("title", "<ButtonRelease>", self.orderByColumn)

    def redrawSheet(self):
        if not self.rows: return
        # now show the data
        y=0
        for row in self.rows:
            height=row.height
            x=5
            col=-1
            for value in row.widgets:
                col+=1
                width=self.columns[col]['width']
                self.drawCell(x, y, width, height, value, self.columns[col])
                x+=width
            y+=height

        self.spreadsheet["scrollregion"]=(0,0, x, y)

    def orderByColumn(self, event):
        wgt=self.header.find_withtag('current')
        colID=int(self.header.gettags(wgt)[1])
        self.sortOnColumn(colID)

    def enterColEnd(self, event):
        self.header.configure(cursor='sb_h_double_arrow')

    def leaveColEnd(self, event):
        self.header.configure(cursor=self.defaultCursor)

    def startDrag(self, event):
        self.wgt1=self.header.find_withtag('current')
        self.currCol=self.columns[int(self.header.gettags(self.wgt1)[1])]
        self.startX=self.header.bbox(self.wgt1)[0]
        self.header.bind('<B1-Motion>', self.moveBorder)
        self.header.bind('<ButtonRelease>', self.stopMoveBorder)

    def moveBorder(self, event):
        self.header.tag_raise(self.wgt1)
        wgt_x=self.header.bbox(self.wgt1)[0]
        diff=event.x-wgt_x
        self.header.move(self.wgt1, diff, 0)

    def stopMoveBorder(self, event):
        self.header.unbind('<B1-Motion>')
        self.header.unbind('<ButtonRelease>')
        self.grab_release()
        wgt_x=self.header.bbox(self.wgt1)[0]
        change=wgt_x-self.startX
        self.currCol['width']+=change
        self.show()

    def drawCell(self, x, y, width, height, value, col):
        if value.internal:
            self.spreadsheet.create_window(x, y,  window=value, height=height, width=width, anchor=NW)
        else:
            wheight=min(height-2,value.winfo_reqheight())
            self.spreadsheet.create_window(x+width/2, y+height/2, window=value, height=wheight, anchor=CENTER)

    def sortOnColumn(self, colID):
        self.rows.sort(cmp=lambda a, b, c=colID: cmp(a[c], b[c]))
        self.show()


class Row(list):

    def __init__(self, vals):
        if isinstance(vals, tuple): vals=list(vals)
        list.__init__(self, vals)
        self.height=0



if __name__ == '__main__':
    app = gui()
    ssw = Spreadsheet(app.getContainer(), width=900)
    app.sticky='news'
    app.addWidget('ssw', ssw)
    ssw.initialise()
    ssw.addColumn('', 110)
    ssw.addColumn('Subject', 300, bg='light blue')
    ssw.addColumn('Sender', 200, align=CENTER)
    ssw.addColumn('Date', 200, align=RIGHT)
    ssw.addColumn('Date2', 200, align=RIGHT)
    ssw.addColumn('Date3', 200, align=RIGHT)
    ssw.addColumn('But', 200, align=RIGHT)

    # if embedded widgets do not have ssw.spreadsheet as parent, they will overlap the border
    for i in range(0,50):
        but=Button(ssw.spreadsheet, text="View", font="Arial 8")
        rad = Radiobutton(ssw.spreadsheet)
        ent = Entry(ssw.spreadsheet)
        check = Checkbutton(ssw.spreadsheet)
        ssw.addRow(700, (but, 'Important Message: %d' % i, 'John Doe', '10/10/%04d' % (1900-i), [1,2,3], ent, True))


    ssw.optimiseColumns()
    ssw.show()
    app.go()
