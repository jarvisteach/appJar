      n_grids = {}

            # temp hack for grid...
            self.gdFont = font.Font(family="Helvetica", size=12)
            self.ghFont = font.Font(family="Helvetica", size=14, weight="bold")
            self.ghBg= "gray"
            self.gdBg= self.topLevel.cget("bg")
            self.gdHBg= "red"
            self.gdSBg= "blue"
            self.ghHBg= self.topLevel.cget("bg")
            self.gdC= self.topLevel.cget("bg")
            self.gdHighlight = "red"

      def setLabelFont(self, size, font=None):
            self.lbFont.configure (family=font, size=size)
            self.taFont.configure (family=font, size=size)
            self.gdFont.configure (family=font, size=size)
            self.ghFont.configure (family=font, size=size+2, weight="bold")

      def setBg(self, colour=None):
            for na in self.n_grids:
                  self.n_grids[na].configure(background=self.labelBgColour)

#####################################
## FUNCTION for simple grids
#####################################
      # first row is used as a header
      def addGrid(self, title, data, row=None, column=0, colspan=0, action=None, addRow=False):
            self.__verifyItem(self.n_grids, title, True)
            frame = self.__makeGrid(title, data, action, addRow)
            self.__positionWidget(frame, row, column, colspan, N+E+S+W)

      def updateGrid(self, title, data, addRow=None):
            frame = self.__verifyItem(self.n_grids, title)
            params = frame.grid_info()
            action = frame.action
            if addRow is None: addRow = frame.addRow
            entries = frame.entries
            for e in frame.entries:
                  del self.n_entries[e.myTitle]

            del ( self.n_grids[title] )
            frame.grid_forget()
            frame.destroy()

            self.addGrid(title, data, int(params["row"]), int(params["column"]), int(params["columnspan"]), action, addRow)

      def __refreshGrids(self, event):
            '''Reset the scroll region to encompass the inner frame'''
            for name in self.n_grids:
                can = self.n_grids[name].c1
                can.configure(scrollregion=can.bbox("all"))
                #can.itemconfig(_id, height=frame.c1.height, width=frame.c1.width)

      def __gridCellEnter(self, event):
            cell = event.widget
            cell.config(background=self.gdHBg)

      def __gridCellLeave(self, event):
            cell = event.widget
            if cell.selected: cell.config(background=self.gdSBg)
            else: cell.config(background=self.gdBg)

      def __gridCellClick(self, event):
            cell = event.widget
            if cell.selected:
                cell.selected = False
                cell.config(background=self.gdBg)
            else:
                cell.selected = True
                cell.config(background=self.gdSBg)

      def __scrollGrid(self, event, title):
            if platform() in [ "win32", "Windows"]:
                  self.n_grids[title].c1.yview_scroll(-1*(event.delta/120), "units")
            else:
                  #self.n_grids[title].c1.yview_scroll(event.delta, "units")
                  pass
      def setGridGeom(self, title, width=200, height=200):
            grid = self.__verifyItem(self.n_grids, title)
            grid.configure(width=width, height=height)

      def getGridEntries(self, title):
            return [e.var.get() for e in self.__verifyItem(self.n_grids, title).entries ]

      def setGridBackground(self, title, colour=None):
            grid = self.__verifyItem(self.n_grids, title)
            if colour == None: colour = self.gdC
            self.gdC = colour
            grid.c1.configure(background=self.gdC, highlightcolor=self.gdC, highlightbackground=self.gdC)

      def __makeGrid(self, title, data, action=None, addRow=False):

            # note - if use grid layout, can use AutoScrollBar
            # However, couldn't get canvas to expand in frame using grid
            frame = Frame(self.window)
            frame.configure( background=self.labelBgColour )
            self.n_grids[title] = frame
            frame.action = action
            frame.addRow = addRow
            frame.entries = []      # store them in the frame object for access, later

            frame.c1 = Canvas(frame, borderwidth=0, highlightthickness=2)
            frame.c1.bind_all("<MouseWheel>", lambda event, arg=title: self.__scrollGrid(event, arg))
            self.setGridBackground(title)

            vsb = Scrollbar(frame, orient="vertical", command=frame.c1.yview)
            frame.c1.configure(yscrollcommand=vsb.set)
            vsb.pack(side="right", fill="y")
            #vsb.grid(row=0, column=1, sticky=N+S)

            hsb = Scrollbar(frame, orient="horizontal", command=frame.c1.xview)
            frame.c1.configure(xscrollcommand=hsb.set)
            hsb.pack(side="bottom", fill="x")
            #hsb.grid(row=1, column=0, sticky=E+W)

            frame.c1.pack(side="left", fill="both", expand=True)
            #frame.c1.grid(row=0, column=0, sticky=N+S+E+W)

            #frame.c1.grid_rowconfigure(0, weight=1)
            #frame.c1.grid_columnconfigure(0, weight=1)

            gridFrame = Frame(frame.c1)
            gridFrame.configure( background=self.labelBgColour )
            frame.c1.create_window((4,4), window=gridFrame, anchor="nw", tags="gridFrame")
            gridFrame.bind("<Configure>", self.__refreshGrids)

            # find the longest row...
            maxSize = 0
            for rowNum in range(len(data)):
                  if len(data[rowNum]) > maxSize: maxSize = len(data[rowNum])

            # loop through each row
            for rowNum in range(len(data)):
                  vals = []
                  # then the cells in that row
                  for cellNum in range(maxSize):
                        # get a name and val ("" if no val)
                        name = "c" + str(rowNum) + "-" + str(cellNum)
                        if cellNum >= len(data[rowNum]) : val = ""
                        else: val = data[rowNum][cellNum]
                        vals.append(val)

                        lab = Label(gridFrame)
                        lab.selected = False
                        if rowNum == 0: lab.configure( relief=RIDGE,text=val, font=self.ghFont, background=self.ghBg )
                        else:
                              lab.configure( relief=RIDGE,text=val, font=self.gdFont, background=self.gdBg )
                              lab.bind("<Enter>", self.__gridCellEnter)
                              lab.bind("<Leave>", self.__gridCellLeave)
                              lab.bind("<Button-1>", self.__gridCellClick)

                        lab.grid ( row=rowNum, column=cellNum, sticky=N+E+S+W )
                        Grid.columnconfigure(gridFrame, cellNum, weight=1)
                  Grid.rowconfigure(gridFrame, rowNum, weight=1)

                  # add some buttons for each row
                  if action is not None:
                        widg = Label(gridFrame)
                        widg.configure( relief=RIDGE )
                        if rowNum == 0:
                              widg.configure( text="Action", font=self.ghFont, background=self.ghBg )
                        else:
                              but = Button(widg)
                              but.configure( text="Press", command=self.__makeFunc(action, vals),font=self.buttonFont, background=self.buttonBgColour )
                              but.grid ( row=0,column=0, sticky=N+E+S+W )
                        widg.grid ( row=rowNum, column=cellNum+1, sticky=N+E+S+W )
            # add a row of entry boxes...
            if addRow==True:
                  for cellNum in range(maxSize):
                        name = "GR"+data[0][cellNum]
                        #widg = Label(gridFrame)
                        #widg.configure( relief=RIDGE )
                        #entry = self.__buildEntry(name, widg)
                        widg = self.__buildEntry(name, gridFrame)
                        frame.entries.append(widg)
                        #entry.grid ( row=0,column=0, sticky=N+E+S+W )
                        widg.grid ( row=len(data), column=cellNum, sticky=N+E+S+W )
                  widg = Label(gridFrame)
                  widg.configure( relief=RIDGE )
                  but = Button(widg)
                  but.configure( text="Press", command=self.__makeFunc(action, "newRow"),font=self.buttonFont, background=self.buttonBgColour )
                  but.grid ( row=0,column=0, sticky=N+E+S+W )
                  widg.grid ( row=len(data), column=maxSize, sticky=N+E+S+W )

            return frame
