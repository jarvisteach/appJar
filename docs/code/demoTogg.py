from tkinter import *
from platform import system as platform
# http://stackoverflow.com/questions/13141259/expandable-and-contracting-frame-in-tkinter

class ToggledFrame(Frame):
    def __init__(self, parent, text="", *args, **options):
        Frame.__init__(self, parent, *args, **options)
        self.config(relief="raised", borderwidth=1, height=20)

        self.showing=False
        self.colour=None

        self.titleFrame = Frame(self)
        self.titleFrame.pack(fill="x", expand=1)

        self.titleLabel = Label(self.titleFrame, text=text)
        self.titleLabel.pack(side="left", fill="x", expand=1)

        self.toggleButton = Button(self.titleFrame, width=2, text='+', command=self.toggle)
        self.toggleButton.pack(side="left")

        self.sub_frame = Frame(self, relief="sunken", borderwidth=1)

    def setColour(self, colour):
        self.colour = colour
        self.titleFrame.config(bg=colour)
        self.titleLabel.config(bg=colour, foreground="white")
        if platform() == "Darwin": self.toggleButton.config(highlightbackground=colour)

    def toggle(self):
        if not self.showing:
            self.sub_frame.pack(fill="x", expand=1)
            self.toggleButton.configure(text='-')
        else:
            self.sub_frame.forget()
            self.toggleButton.configure(text='+')
        self.showing = not self.showing

    def getContainer(self):
        return self.sub_frame

class ToggleContainer(Frame):
    def __init__(self, parent, text="", *args, **options):
        Frame.__init__(self, parent, *args, **options)
        self.parent=parent
        self.config(relief="sunken", borderwidth=1, bg="skyblue")
        self.bg = True
        self.currentFrame = None

    def addToggleFrame(self, name):
        t = ToggledFrame(self, text=name)
        t.pack(fill="x", pady=5, padx=5, anchor="n")
        if self.bg: t.setColour("blue")
        self.bg = not self.bg
        self.currentFrame = t

    def packWidg(self, widg):
        widg.pack()
        x=widg.winfo_reqwidth()
        if x > self.winfo_reqwidth():
            print("update", x)
            self.currentFrame.pack_propagate(0)
            self.currentFrame.config(width=x)


    def addLab(self, text):
        lab = Label(self.currentFrame.getContainer(), text=text)
        self.packWidg(lab)

if __name__ == "__main__":
    root = Tk()

    tc = ToggleContainer(root)
    tc.pack()

    tc.addToggleFrame("Rotate")
    tc.addLab('Rotation [deg]:')
#    Label(tc.currentFrame.getContainer(), text='Rotation [deg]:').pack(side="left", fill="x", expand=1)
    entry = Entry(tc.currentFrame.getContainer())
    tc.packWidg(entry)

    tc.addToggleFrame("Toggle")
    for i in range(10): tc.addLab('Test' + str(i))

    tc.addToggleFrame("Fooo")
    for i in range(10): tc.addLab('Bar' + str(i))

    root.mainloop()
