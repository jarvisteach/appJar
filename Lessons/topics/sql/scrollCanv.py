import tkinter as tk

class Example(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")

        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")

        self.hsb = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.hsb.set)
        self.hsb.pack(side="bottom", fill="x")

        self.canvas.pack(side="left", fill="both", expand=True)

        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")
        self.frame.bind("<Configure>", self.OnFrameConfigure)

        self.populate()

    def populate(self):
        data = []
        for looper in range(20):
            data.append([])
            data[looper] = []
            for loop in range(10):
                data[looper].append(looper*loop)

        # loop through each row
        for rowNum in range(len(data)):
            # then the cells in that row
            for cellNum in range(5):
                # get a name and val ("" if no val)
                name = "c" + str(rowNum) + "-" + str(cellNum)
                if cellNum >= len(data[rowNum]) : val = ""
                else: val = data[rowNum][cellNum]

                lab = tk.Label(self.frame)
                if rowNum == 0:
                    lab.configure( relief=tk.RIDGE,text=val )
                else:
                    lab.configure( relief=tk.RIDGE,text=val)
                    lab.bind("<Enter>", lambda e: e.widget.config(background='red'))
                    lab.bind("<Leave>", lambda e: e.widget.config(background='white'))

                lab.grid ( row=rowNum, column=cellNum, sticky=tk.N+tk.E+tk.S+tk.W )
                tk.Grid.columnconfigure(self.frame, cellNum, weight=1)
            tk.Grid.rowconfigure(self.frame, rowNum, weight=1)


    def OnFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
