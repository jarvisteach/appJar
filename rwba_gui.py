# -*- coding: utf-8 -*-
#"""rwba_gui.py: Provides a GUI class, for making simple tkinter GUIs."""
# Nearly everything I learnt came from: http://effbot.org/tkinterbook/

##########
## TO ADD: labelFrame, panedWindow
# LAST CHANGE: see changeLog.txt

from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import font
import os, sys, re, socket, hashlib
from platform import system as platform
import webbrowser

# import borrowed libraries
from rwbatools.lib.tooltip import ToolTip
from rwbatools.lib.tkinter_png import *
from rwbatools.lib import nanojpeg

# only try to import winsound if we're on windows
if platform() in [ "win32", "Windows"]:
      import winsound

#class to allow simple creation of tkinter GUIs
class gui:
      built = False
      # used to identify widgets in component configurations
      WINDOW=0
      LABEL=1
      ENTRY=2
      BUTTON=3
      CB=4
      SCALE=5
      RB=6
      LB=7
      MESSAGE=8
      SPIN=9
      OPTION=10
      TEXTAREA=11
      LINK=12
      METER=13

      # positioning
      N = N
      NE = NE
      E = E
      SE = SE
      S = S
      SW = SW
      W = W
      NW = NW
      CENTER = CENTER
      LEFT = LEFT
      RIGHT = RIGHT

      # reliefs
      SUNKEN=SUNKEN
      RAISED=RAISED
      GROOVE=GROOVE
      RIDGE=RIDGE
      FLAT=FLAT

      # music stuff
      BASIC_NOTES = {"A":440, "B":493, "C":261, "D":293, "E":329, "F":349, "G":392 }
      NOTES={'f8': 5587, 'c#6': 1108, 'f4': 349, 'c7': 2093, 'd#2': 77, 'g8': 6271,
             'd4': 293, 'd7': 2349, 'd#7': 2489, 'g#4': 415, 'e7': 2637, 'd9': 9397,
             'b8': 7902, 'a#4': 466, 'b5': 987, 'b2': 123, 'g#9': 13289, 'g9': 12543,
             'f#2': 92, 'c4': 261, 'e1': 41, 'e6': 1318, 'a#8': 7458, 'c5': 523, 'd6': 1174,
             'd3': 146, 'g7': 3135, 'd2': 73, 'd#3': 155, 'g#6': 1661, 'd#4': 311, 'a3': 219,
             'g2': 97, 'c#5': 554, 'd#9': 9956, 'a8': 7040, 'a#5': 932, 'd#5': 622, 'a1': 54,
             'g#8': 6644, 'a2': 109, 'g#5': 830, 'f3': 174, 'a6': 1760, 'e8': 5274, 'c#9': 8869,
             'f5': 698, 'b1': 61, 'c#4': 277, 'f#9': 11839, 'e5': 659, 'f9': 11175, 'f#5': 739,
             'a#1': 58, 'f#8': 5919, 'b7': 3951, 'c#8': 4434, 'g1': 48, 'c#3': 138, 'f#7': 2959,
             'c6': 1046, 'c#2': 69, 'c#7': 2217, 'c3': 130, 'e9': 10548, 'c9': 8372, 'a#6': 1864,
             'a#7': 3729, 'g#2': 103, 'f6': 1396, 'b3': 246, 'g#3': 207, 'b4': 493, 'a7': 3520,
             'd#6': 1244, 'd#8': 4978, 'f2': 87, 'd5': 587, 'f7': 2793, 'f#6': 1479, 'g6': 1567,
             'e3': 164, 'f#3': 184, 'g#1': 51, 'd8': 4698, 'f#4': 369, 'f1': 43, 'c8': 4186, 'g4': 391,
             'g3': 195, 'a4': 440, 'a#3': 233, 'd#1': 38, 'e2': 82, 'e4': 329, 'a5': 880, 'a#2': 116,
             'g5': 783, 'g#7': 3322, 'b6': 1975, 'c2': 65, 'f#1': 46}
      DURATIONS={"BREVE":2000, "SEMIBREVE":1000, "MINIM":500, "CROTCHET":250,  "QUAVER":125,"SEMIQUAVER":63, "DEMISEMIQUAVER":32, "HEMIDEMISEMIQUAVER":16}

#####################################
## CONSTRUCTOR - creates the GUI
#####################################
      def __init__(self, title="RWBA Tools", geom=None):
            # dynamically create lot of functions for configuring stuff
            self.__initArrays()
            self.__buildConfigFuncs()

            # set up some default path locations
            self.lib_file = os.path.abspath(__file__)
            self.lib_path = os.path.dirname(self.lib_file)
            self.icon_path = os.path.join(self.lib_path,"icons")
            self.sound_path = os.path.join(self.lib_path,"sounds")

            # create the main window - topLevel
            self.topLevel = Tk()
            self.topLevel.bind('<Configure>', self.__windowEvent)
            # temporarily hide it
            self.topLevel.withdraw()

            self.appWindow = Frame(self.topLevel)
            self.appWindow.pack(fill=BOTH, expand=True)

            self.setTitle(title)
            # configure geom
            self.escapeBindId = None # used to exit fullscreen
            self.setGeom(geom)

            # set the resize status - default to True
            self.setResizable(True)

            # set up fonts
            self.buttonFont = font.Font(family="Helvetica", size=12,)
            self.labelFont = font.Font(family="Helvetica", size=12)
            self.entryFont = font.Font(family="Helvetica", size=12)
            self.messageFont = font.Font(family="Helvetica", size=12)
            self.rbFont = font.Font(family="Helvetica", size=12)
            self.cbFont = font.Font(family="Helvetica", size=12)
            self.scaleFont = font.Font(family="Helvetica", size=12)
            self.statusFont = font.Font(family="Helvetica", size=12)
            self.tbFont = font.Font(family="Helvetica", size=12)
            self.spinFont = font.Font(family="Helvetica", size=12)
            self.optionFont = font.Font(family="Helvetica", size=12)
            self.lbFont = font.Font(family="Helvetica", size=12)
            self.taFont = font.Font(family="Helvetica", size=12)
            self.meterFont = font.Font(family="Helvetica", size=12, weight='bold')
            self.linkFont = font.Font(family="Helvetica", size=12, weight='bold', underline=1)

            # set up colours
            self.bgColour = self.topLevel.cget("bg")
            self.buttonBgColour = self.topLevel.cget("bg")
            self.labelBgColour = self.topLevel.cget("bg")

            self.padx = self.pady = 1
            self.expand = "ALL"
            self.sticky = True

            # create a menu bar - only shows if populated
            # now created in menu functions, as it generated a blank line...
            self.hasMenu = False
            self.hasStatus = False
            self.hasTb = False
            # won't pack, if don't pack it here
            self.tb = Frame(self.appWindow, bd=1, relief=RAISED)
            self.tb.pack(side=TOP, fill=X)

            # create the main frame - window
            self.window = Frame(self.appWindow)
            #self.window = Label(self.appWindow) # made as a label, so we can set an image
            self.window.configure(padx=2, pady=2, background=self.labelBgColour)
            self.window.pack(fill=BOTH, expand=True)

            # set up the bg label to store an image
            self.__configBg()
            
            # override close button
            self.__stopFunction = None
            self.topLevel.protocol("WM_DELETE_WINDOW", self.stop)

            # an array to hold any threaded events....
            self.events = []
            self.pollTime = 250
            self.built = True

      def __configBg(self):
            # set up a background image holder
            # alternative to label option above, as label doesn't update widgets properly
            self.bgLabel = Label(self.window)
            self.bgLabel.config(anchor=CENTER, font=self.labelFont, background=self.labelBgColour)
            self.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
            self.window.image = None

#####################################
## set the arrays we use to store everything
#####################################
      def __initArrays(self):
            # set up a row counter - used to auto add rows
            # breaks once user sets own row
            self.emptyRow = 0
            self.colCount = 1

            #set up a minimum label width for label combos
            self.labWidth=1

            # set up flash variable
            self.doFlash = False

            # collections of widgets, widget name is key
            self.n_frames=[] # un-named, so no direct access
            self.n_labels = {}
            self.n_buttons = {}
            self.n_entries={}
            self.n_messages={}
            self.n_scales={}
            self.n_cbs={}
            self.n_rbs={}
            self.n_lbs={}
            self.n_tbButts={}
            self.n_spins={}
            self.n_options={}
            self.n_frameLabs={}
            self.n_textAreas={}
            self.n_links={}
            self.n_meters={}
            self.n_toplevels={}
            self.n_flashLabs = []

            # variables associated with widgets
            self.n_entryVars={}
            self.n_optionVars={}
            self.n_boxVars={}
            self.n_rbVars={}
            self.n_rbVals={}
            self.n_images={}        # image label widgets
            self.n_imageCache={}    # image file objects
            self.n_taHashes={}      # for monitoring textAreas

#####################################
## Event Loop - must always be called at end
#####################################
      def go(self):
            # pack it all in & make sure it's drawn
            self.appWindow.pack(fill=BOTH)
            self.topLevel.update_idletasks()

            # set a minimum size
            self.topLevel.minsize(self.topLevel.winfo_width(), self.topLevel.winfo_height())

            # put it in the middle
            x = (self.topLevel.winfo_screenwidth() - self.topLevel.winfo_reqwidth()) / 2
            y = (self.topLevel.winfo_screenheight() - self.topLevel.winfo_reqheight()) / 2
            self.topLevel.geometry("+%d+%d" % (x, y))

            # bring to front
            self.topLevel.deiconify()
            self.__bringToFront()

            # start the call back & flash loops
            self.__poll()
            self.__flash()

            # start the main loop
            self.topLevel.mainloop()

      def setStopFunction(self, function):
            self.__stopFunction = function

      def stop(self):
            if self.__stopFunction is None or self.__stopFunction():
                  # stop any sounds, ignore error when not on Windows
                  try: self.stopSound()
                  except: pass
                  self.topLevel.destroy()

#####################################
## Functions for configuring polling events
#####################################
      #events will fire in order of being added, after sleeping for time
      def setPollTime(self, time):
            self.pollTime = time

      # register events to be called by the sleep timer
      def registerEvent(self, func):
            self.events.append(func)

      # internal function, called by 'after' function, after sleeping
      def __poll(self):
            # run any registered actions
            for e in self.events:
                  # execute the event
                  e()
            self.topLevel.after(self.pollTime, self.__poll)

      # not used now, but called every time window is resized
      # may be used in the future...
      def __windowEvent(self, event):
            new_width = self.topLevel.winfo_width()
            new_height = self.topLevel.winfo_height()

      # will call the specified function when enter key is pressed
      def enableEnter(self, func):
            # for now discard the Event...
            myF = self.__makeFunc(func, "<Enter>", True)
            self.topLevel.bind('<Return>', myF)

#####################################
## FUNCTIONS for configuring GUI settings
#####################################
      # called to update screen geometry
      def setGeom(self, geom):
            self.mainGeom = geom
            if self.mainGeom == "fullscreen":
                  self.topLevel.attributes('-fullscreen', True)
                  self.escapeBindId = self.topLevel.bind('<Escape>', self.exitFullscreen, "+")
            else:
                  self.exitFullscreen()
                  if self.mainGeom is not None: self.topLevel.geometry(self.mainGeom)

      # called to make sure this window is on top
      def __bringToFront(self):
            if platform() == "Darwin":
                  os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
            else:
                  self.topLevel.lift()

      # function to turn off fullscreen mode
      def exitFullscreen(self, event=None):
            self.topLevel.attributes('-fullscreen', False)
            if self.escapeBindId is not None: self.topLevel.unbind('<Escape>', self.escapeBindId)

      def setPadX(self, x=0):
            self.padx = x

      def setPadY(self, y=0):
            self.pady = y

      def getFonts(self): return list ( font.families() ). sort()

      def increaseButtonFont(self): self.setButtonFont(self.buttonFont['size'] + 1 )
      def decreaseButtonFont(self): self.setButtonFont(self.buttonFont['size'] - 1 )

      def setButtonFont(self, size, font=None):
            if font == None: font = self.buttonFont['family']
            self.buttonFont.configure (family=font, size=size)

      def increaseLabelFont(self): self.setLabelFont(self.labelFont['size'] + 1 )
      def decreaseLabelFont(self): self.setLabelFont(self.labelFont['size'] -1 )

      def setLabelFont(self, size, font=None):
            if font == None: font = self.labelFont['family']
            self.labelFont.configure (family=font, size=size)
            self.entryFont.configure (family=font, size=size)
            self.rbFont.configure (family=font, size=size)
            self.cbFont.configure (family=font, size=size)
            self.scaleFont.configure (family=font, size=size)
            self.messageFont.configure (family=font, size=size)
            self.spinFont.configure (family=font, size=size)
            self.optionFont.configure (family=font, size=size)
            self.lbFont.configure (family=font, size=size)
            self.taFont.configure (family=font, size=size)
            self.linkFont.configure (family=font, size=size)
            self.meterFont.configure (family=font, size=size)

      def increaseFont(self):
           self.increaseLabelFont()
           self.increaseButtonFont()

      def decreaseFont(self):
           self.decreaseLabelFont()
           self.decreaseButtonFont()

      def setFont(self, size, font=None):
           self.setLabelFont(size, font)
           self.setButtonFont(size, font)

      def setBg(self, colour=None):
            if colour is None: colour = self.labelBgColour
            self.labelBgColour=colour
            self.topLevel.configure(background=self.labelBgColour)
            self.appWindow.configure(background=self.labelBgColour)
            self.window.configure(background=self.labelBgColour)
            self.bgLabel.configure(background=self.labelBgColour)

            for na in self.n_labels:
                  self.n_labels[na].configure(background=self.labelBgColour)
            for na in self.n_messages:
                  self.n_messages[na].configure(background=self.labelBgColour)

            if platform() == "Darwin":
                  for na in self.n_entries:
                        self.n_entries[na].configure(highlightbackground=self.labelBgColour)
                  for na in self.n_buttons:
                        self.n_buttons[na].configure(highlightbackground=self.labelBgColour)
                  for na in self.n_spins:
                        self.n_spins[na].configure(highlightbackground=self.labelBgColour)
                  for na in self.n_options:
                        self.n_options[na].configure(background=self.labelBgColour, highlightbackground=self.labelBgColour)

            for na in self.n_scales:
                  self.n_scales[na].configure(background=self.labelBgColour)
            for na in self.n_cbs:
                  self.n_cbs[na].configure(background=self.labelBgColour, activebackground=self.labelBgColour)
            for gr in self.n_rbs:
                  for na in self.n_rbs[gr]:
                      na.configure(background=self.labelBgColour, activebackground=self.labelBgColour)
            for na in self.n_frames:
                  na.configure(background=self.labelBgColour)
            for na in self.n_links:
                  self.n_links[na].configure(background=self.labelBgColour)
            #for na in self.n_options:
            #      self.n_options[na].configure(background=self.labelBgColour)
            #for na in self.n_spins:
            #      self.n_spins[na].configure(background=self.labelBgColour)

      def setResizable(self, canResize=True):
            self.resizable = canResize
            if self.resizable: self.topLevel.resizable(True, True)
            else: self.topLevel.resizable(False, False)

      def getResizable(self):
            return self.resizable

      # function to set the window's title
      def setTitle(self, title):
            self.topLevel.title(title)

      # set an icon
      def setIcon(self, image):
            if image.endswith('.ico'):
                  self.topLevel.wm_iconbitmap(image)
            else:
                  self.icon = self.__getImage(image)
                  self.topLevel.iconphoto(True, self.icon)

      # make the window transparent (between 0 & 1)
      def setTransparency(self, percentage):
            self.topLevel.attributes("-alpha", percentage)

##############################
## funcitons to deal with tabbing and right clicking
##############################
      def __focusNextWindow(self,event):
            event.widget.tk_focusNext().focus_set()
            nowFocus = self.topLevel.focus_get()
            if isinstance(nowFocus, Entry): nowFocus.select_range(0,END)
            return("break")

      def __focusLastWindow(self,event):
            event.widget.tk_focusPrev().focus_set()
            nowFocus = self.topLevel.focus_get()
            if isinstance(nowFocus, Entry): nowFocus.select_range(0,END)
            return("break")

      def __rightClick(self,event):
            def rClick_Copy(event, apnd=0):
                  #event.widget.event_generate('<Control-c>')
                  try:
                        text = event.widget.selection_get()
                        self.topLevel.clipboard_clear()
                        #text = event.widget.get("sel.first", "sel.last")
                        self.topLevel.clipboard_append(text)
                  except TclError: pass

            def rClick_Cut(event):
                  #event.widget.event_generate('<Control-x>')
                  try:
                        text = event.widget.selection_get()
                        self.topLevel.clipboard_clear()
                        self.topLevel.clipboard_append(text)
                        event.widget.delete("sel.first", "sel.last")
                  except TclError: pass

            def rClick_Paste(event):
                  #event.widget.event_generate('<Control-v>')
                  text = self.topLevel.selection_get(selection='CLIPBOARD')
                  event.widget.insert('insert', text)

            event.widget.focus()

            nclst=[
                  (' Cut', lambda e=event: rClick_Cut(event)),
                  (' Copy', lambda e=event: rClick_Copy(event)),
                  (' Paste', lambda e=event: rClick_Paste(event)),
                  ]

            rmenu = Menu(None, tearoff=0, takefocus=0)
            for (txt, cmd) in nclst:
                  rmenu.add_command(label=txt, command=cmd)

            rmenu.tk_popup(event.x_root+40, event.y_root+10,entry="0")
            event.widget.selection_clear()
            return("break")

#####################################
## FUNCTION to configure widgets
#####################################
      def __getItems(self, kind):
            if kind == self.LABEL: return self.n_labels
            elif kind == self.MESSAGE: return self.n_messages
            elif kind == self.BUTTON: return self.n_buttons
            elif kind == self.ENTRY: return self.n_entries
            elif kind == self.CB: return self.n_cbs
            elif kind == self.SCALE: return self.n_scales
            elif kind == self.RB: return self.n_rbs
            elif kind == self.LB: return self.n_lbs
            elif kind == self.SPIN: return self.n_spins
            elif kind == self.OPTION: return self.n_options
            elif kind == self.TEXTAREA: return self.n_textAreas
            elif kind == self.LINK: return self.n_links
            elif kind == self.METER: return self.n_meters
            else: raise Exception ("Unknown widget type: " + str(kind))

      def configureAllWidgets(self, kind, option, value):
            items = list(self.__getItems(kind))
            self.configureWidgets(kind, items, option, value)

      def configureWidgets(self, kind, names, option, value ):
            if not isinstance(names, list): self.configureWidget(kind, names, option, value)
            else:
                  for widg in names:
                        self.configureWidget(kind, widg, option, value)

      def configureWidget(self, kind, name, option, value, key=None):
            items = self.__getItems(kind)
            self.__verifyItem(items, name)

            if kind == self.RB:
                  items = items[name]
            else:
                  items = [items[name]]
            for item in items:
                  if option == 'background': item.configure( background=value )
                  elif option == 'foreground': item.configure( foreground=value )
                  elif option == 'disabledforeground': item.configure( disabledforeground=value )
                  elif option == 'width': item.configure( width=value )
                  elif option == 'height': item.configure( height=value )
                  elif option == 'state': item.configure( state=value )
                  elif option == 'relief': item.configure( relief=value )
                  elif option == 'align':
                        if kind==self.ENTRY:
                              if value == W or value == LEFT: value = LEFT
                              elif value == E or value == RIGHT: value = RIGHT
                              item.configure( justify=value )
                        else:
                              item.configure( anchor=value )
                  elif option == 'anchor': item.configure( anchor=value )
                  elif option == 'cursor': item.configure( cursor=value )
                  elif option == 'tooltip': self.__addTooltip(item, value)
                  elif option == "focus": item.focus_set()
                  elif option == 'command':
                        # this will discard the scale value, as default function can't handle it
                        if kind==self.SCALE: 
                              item.configure( command=self.__makeFunc(value,name, True) )
                        elif kind==self.OPTION:
                              # need to trace the variable??
                              item.var.trace('w',  self.__makeFunc(value,name, True))
                        elif kind==self.ENTRY:
                              if key is None: key =name 
                              item.bind('<Return>', self.__makeFunc(value, key, True))
                        elif kind==self.BUTTON:
                              item.configure(command=self.__makeFunc(value, name))
                              item.bind('<Return>', self.__makeFunc(value, name, True))
                        else:
                              item.configure( command=self.__makeFunc(value,name) )
                  elif option == 'sticky':
                        info = {}
                        # need to reposition the widget in its grid
                        if self.__widgetHasContainer(kind, item):
                              # pack uses LEFT & RIGHT & BOTH
                              info["side"] = value
                              if value.lower() == "both":
                                    info["expand"] = 1
                                    info["side"] = "right"
                              else: info["expand"] = 0
                        else:
                              # grid uses E+W
                              if value.lower() == "left": side = W
                              elif value.lower() == "right": side = E
                              elif value.lower() == "both": side = W+E
                              else: side = value.upper()
                              info["sticky"] = side
                        self.__repackWidget(item, info)

      def __buildConfigFuncs(self):
            # make a list of function names & params
            widgets = { self.LABEL:"Label", self.MESSAGE:"Message", self.BUTTON:"Button",
                        self.ENTRY:"Entry", self.CB:"Cb", self.SCALE:"Scale", self.RB:"Rb",
                        self.LB:"Lb", self.SPIN:"SpinBox", self.OPTION:"OptionBox", self.TEXTAREA:"TextArea",
                        self.LINK:"Link", self.METER:"Meter" }
            # loop through array, and create the function
            for k, v in widgets.items():
                  exec("def set"+v+"Bg(self, name, val): self.configureWidgets("+str(k)+", name, 'background', val)")
                  exec("gui.set"+v+"Bg=set" +v+ "Bg")
                  exec("def set"+v+"Fg(self, name, val): self.configureWidgets("+str(k)+", name, 'foreground', val)")
                  exec("gui.set"+v+"Fg=set" +v+ "Fg")
                  exec("def set"+v+"DisabledFg(self, name, val): self.configureWidgets("+str(k)+", name, 'disabledforeground', val)")
                  exec("gui.set"+v+"DisabledFg=set" +v+ "DisabledFg")
                  exec("def set"+v+"Width(self, name, val): self.configureWidgets("+str(k)+", name, 'width', val)")
                  exec("gui.set"+v+"Width=set" +v+ "Width")
                  exec("def set"+v+"Height(self, name, val): self.configureWidgets("+str(k)+", name, 'height', val)")
                  exec("gui.set"+v+"Height=set" +v+ "Height")
                  exec("def set"+v+"State(self, name, val): self.configureWidgets("+str(k)+", name, 'state', val)")
                  exec("gui.set"+v+"State=set" +v+ "State")

                  # might not all be necessary, could make exclusion list
                  exec("def set"+v+"Relief(self, name, val): self.configureWidget("+str(k)+", name, 'relief', val)")
                  exec("gui.set"+v+"Relief=set" +v+ "Relief")
                  exec("def set"+v+"Align(self, name, val): self.configureWidget("+str(k)+", name, 'align', val)")
                  exec("gui.set"+v+"Align=set" +v+ "Align")
                  exec("def set"+v+"Anchor(self, name, val): self.configureWidget("+str(k)+", name, 'anchor', val)")
                  exec("gui.set"+v+"Anchor=set" +v+ "Anchor")
                  exec("def set"+v+"Tooltip(self, name, val): self.configureWidget("+str(k)+", name, 'tooltip', val)")
                  exec("gui.set"+v+"Tooltip=set" +v+ "Tooltip")
                  exec("def set"+v+"Function(self, name, val, key=None): self.configureWidget("+str(k)+", name, 'command', val, key)")
                  exec("gui.set"+v+"Function=set" +v+ "Function")
# deprecated, but left in for backwards compatability
                  exec("def set"+v+"Command(self, name, val, key=None): self.configureWidget("+str(k)+", name, 'command', val, key)")
                  exec("gui.set"+v+"Command=set" +v+ "Command")
                  # http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/cursors.html
                  exec("def set"+v+"Cursor(self, name, val): self.configureWidget("+str(k)+", name, 'cursor', val)")
                  exec("gui.set"+v+"Cursor=set" +v+ "Cursor")
                  exec("def set"+v+"Focus(self, name): self.configureWidget("+str(k)+", name, 'focus', None)")
                  exec("gui.set"+v+"Focus=set" +v+ "Focus")

                  # change the stickyness
                  exec("def set"+v+"Sticky(self, name, pos): self.configureWidget("+str(k)+", name, 'sticky', pos)")
                  exec("gui.set"+v+"Sticky=set" +v+ "Sticky")

                  # functions to manage widgets
                  exec("def show"+v+"(self, name): self.showWidget("+str(k)+", name)")
                  exec("gui.show"+v+"=show" +v )
                  exec("def hide"+v+"(self, name): self.hideWidget("+str(k)+", name)")
                  exec("gui.hide"+v+"=hide" +v )
                  exec("def remove"+v+"(self, name): self.removeWidget("+str(k)+", name)")
                  exec("gui.remove"+v+"=remove" +v )

                  # convenience functions for enable/disable
                  # might not all be necessary, could make exclusion list
                  exec("def enable"+v+"(self, name): self.configureWidget("+str(k)+", name, 'state', 'normal')")
                  exec("gui.enable"+v+"=enable"+v)
                  exec("def disable"+v+"(self, name): self.configureWidget("+str(k)+", name, 'state', 'disabled')")
                  exec("gui.disable"+v+"=disable"+v)

                  # group functions
                  exec("def set"+v+"Widths(self, names, val): self.configureWidgets("+str(k)+", names, 'width', val)")
                  exec("gui.set"+v+"Widths=set" +v+ "Widths")
                  exec("def setAll"+v+"Widths(self, val): self.configureAllWidgets("+str(k)+", 'width', val)")
                  exec("gui.setAll"+v+"Widths=setAll" +v+ "Widths")

                  exec("def set"+v+"Heights(self, names, val): self.configureWidgets("+str(k)+", names, 'height', val)")
                  exec("gui.set"+v+"Heights=set" +v+ "Heights")
                  exec("def setAll"+v+"Heights(self, val): self.configureAllWidgets("+str(k)+", 'height', val)")
                  exec("gui.setAll"+v+"Heights=setAll" +v+ "Heights")

#####################################
## FUNCTION to hide/show/remove widgets
#####################################
      def __widgetHasContainer(self, kind, item):
            if kind == self.SCALE and item.inContainer: return True
            elif kind == self.ENTRY and item.inContainer: return True
            elif kind == self.SPIN and item.inContainer: return True
            elif kind == self.OPTION and item.inContainer: return True
            elif kind == self.LABEL and item.inContainer: return True
            else: return False

      def hideWidget(self, kind, name):
            # get the dictionary of items, and find the item in it
            items = self.__getItems(kind) 
            item = self.__verifyItem(items, name)

            if self.__widgetHasContainer(kind, item):
                  widget = item.master
                  self.n_frameLabs[name].hidden = True
            else:
                  if kind == self.RB:
                        for rb in item:
                              if rb.text == name:
                                    widget = rb
                  widget = item

            if "in" in widget.grid_info():
                  widget.grid_remove()
#                  self.__updateLabelFrames(name)

      def showWidget(self, kind, name):
            # get the dictionary of items, and find the item in it
            items = self.__getItems(kind)
            item = self.__verifyItem(items, name)

            if self.__widgetHasContainer(kind, item):
                  widget = item.master
                  self.n_frameLabs[name].hidden = False
            else: widget = item

            # only show the widget, if it's not already showing
            if "in" not in widget.grid_info():
                  widget.grid()
#                  self.__updateLabelFrames(name)

      def removeWidget(self, kind, name):
            # get the dictionary of items, and find the item in it
            items = self.__getItems(kind)
            item = self.__verifyItem(items, name)

            # if it's a flasher, remove it
            if item in self.n_flashLabs:
                self.n_flashLabs.remove(item)
                if len(self.n_flashLabs) == 0: self.doFlash = False
            
            if self.__widgetHasContainer(kind, item):
                  # destroy the parent
                  parent = item.master
                  parent.grid_forget()
                  parent.destroy()
                  # remove frame, label & widget from lists
                  self.n_labels.pop(name)
                  self.n_frameLabs.pop(name)
                  self.n_frames.remove(parent)
            else:
                  item.grid_forget()
                  item.destroy()

            # finally remove it from the dictionary
            items.pop(name)
            
      def removeAllWidgets(self):
            for child in self.window.winfo_children():
                  child.destroy()
            self.__configBg()
            self.__initArrays()

#####################################
## FUNCTION for managing commands
#####################################
      def __makeFunc(self, funcName, param, discard=False):
            if discard: return lambda *args: funcName(param)
            else: return lambda: funcName(param)

      def __checkFunc(self, names, funcs):
            singleFunc = None
            if callable(funcs) : singleFunc = funcs
            elif len(names) != len(funcs): raise Exception("List sizes don't match")
            return singleFunc

#####################################
## FUNCTION to position a widget
#####################################
      # checks if the item already exists
      def __verifyItem(self, items, item, newItem=False):
            if not newItem and item not in items: raise ItemLookupError("Invalid key: "+ item + " does not exist")
            elif not newItem and item in items: return items[item]
            elif newItem and item in items: raise ItemLookupError("Duplicate key: '"+item+"' already exists")

      def getRow(self):
            return self.emptyRow

      def getNextRow(self):
            temp = self.emptyRow
            self.emptyRow += 1
            return temp

      def __repackWidget(self, widget, params):
            if widget.winfo_manager() == "grid":
                  ginfo = widget.grid_info()
                  ginfo.update(params)
                  #widget.grid(pinfo)
            elif widget.winfo_manager() == "pack":
                  pinfo = widget.pack_info()
                  pinfo.update(params)
                  #widget.pack(pinfo)
            else:
                  raise Exception("Unknown geometry manager: " + widget.winfo_manager())

      # two important thigs here:
      # grid - sticky: position of widget in its space (side or fill)
      # row/columns configure - weight: how to grow with GUI
      def __positionWidget(self, widget, row, column=0, colspan=0, sticky=W+E):
            if row is None: row=self.getNextRow()
            else: self.emptyRow = row + 1
            if column >= self.colCount: self.colCount = column + 1
            #if column == 0 and colspan == 0 and self.colCount > 1:
                  #colspan = self.colCount

            # build a dictionary for the named params
            params = {"row":row, "column":column, "ipadx":self.padx, "ipady":self.pady}
            if not self.sticky: pass#params["sticky"] = "W"
            elif self.sticky and sticky is not None: params["sticky"] = sticky
            if colspan != 0 : params["columnspan"] = colspan
            
            # expand that dictionary out as we pass it as a value
            widget.grid (**params)

            # configure the row/column to expand equally
            if self.expand in ["ALL", "COLUMN"]: Grid.columnconfigure(self.window, column, weight=1)
            else: Grid.columnconfigure(self.window, column, weight=0)
            if self.expand in ["ALL", "ROW"]: Grid.rowconfigure(self.window, row, weight=1)
            else: Grid.rowconfigure(self.window, row, weight=0)

      def setSticky(self, on=True):
            self.sticky = on

      # this tells widgets what to do when GUI is resized
      def setExpand(self, exp):
            if exp.lower() == "none": self.expand = "NONE"
            elif exp.lower() == "row": self.expand = "ROW"
            elif exp.lower() == "column": self.expand = "COLUMN"
            else: self.expand = "ALL"

#####################################
## FUNCTION to manage topLevels
#####################################

      def __getattr__(self,name):
            def handlerFunction(*args,**kwargs):
                  print("Unknown function:", name,args,kwargs)
            return handlerFunction

      def __setattr__(self, name, value):
            if self.built == True and not hasattr(self, name): # would this create a new attribute?
                  raise AttributeError("Creating new attributes is not allowed!")
            super(gui, self).__setattr__(name, value)

      def addTopLevel(self, name, title=None):
            self.__verifyItem(self.n_toplevels, name, True)
            if title == None: title = name
            top = GuiChild()
            top.title(title)
            top.win = self
            self.n_toplevels[name] = top

#####################################
## FUNCTION to add labels before a widget
#####################################
      # this will build a frame, with a label on the left hand side
      def __getLabelFrame(self, title):
            self.__verifyItem(self.n_labels, title, True)

            # first, make a frame
            frame = Frame(self.window)
            frame.configure( background=self.labelBgColour )
            self.n_frames.append(frame)

            # if this is a big label, update the others to match...
            if len(title) > self.labWidth:
                  self.labWidth = len(title)
                  #loop through other labels and resize
                  for na in self.n_frameLabs:
#                        self.n_frameLabs[na].configure(width=self.labWidth)
                        pass

            # next make the label
            lab = Label(frame)
            lab.hidden = False
            lab.inContainer = True
            lab.configure( anchor=W,text=title, justify=LEFT, font=self.labelFont, background=self.labelBgColour )
#            lab.configure( width=self.labWidth)
            self.n_labels[title]=lab
            self.n_frameLabs[title]=lab

            # now put the label in the frame
            lab.pack(side=LEFT, fill=Y)
            #lab.grid ( row=0, column=0, sticky=W )
            #Grid.columnconfigure(frame, 0, weight=1)
            #Grid.rowconfigure(frame, 0, weight=1)

            return frame

      # this is where we add the widget to the frame built above
      def __packLabelFrame(self, frame, widget):
            widget.pack(side=LEFT, fill=BOTH, expand=True)
            widget.inContainer = True
            #widget.grid ( row=0, column=1, sticky=W+E )
            #Grid.columnconfigure(frame, 1, weight=1)
            #Grid.rowconfigure(frame, 0, weight=1)

      # function to resize labels, if they are hidden or shown
      def __updateLabelFrames(self, title):
            if len(title) >= self.labWidth:
                  self.labWidth = 0
                  #loop through other labels and resize
                  for na in self.n_frameLabs:
                        size = len ( self.n_frameLabs[na].cget("text") )
                        if not self.n_frameLabs[na].hidden and size > self.labWidth: self.labWidth = size
                  for na in self.n_frameLabs:
                        self.n_frameLabs[na].configure(width=self.labWidth)
            
#####################################
## FUNCTION for check boxes
#####################################
      def addCheckBox(self, title, row=None, column=0, colspan=0):
            self.__verifyItem(self.n_cbs, title, True)
            var=IntVar(self.topLevel)
            cb = Checkbutton(self.window)
            cb.configure(text=title, variable=var, font=self.cbFont, background=self.labelBgColour, activebackground=self.labelBgColour)
            self.n_cbs[title]=cb
            self.n_boxVars[title]=var
            self.__positionWidget(cb, row, column, colspan, None)

      def getCheckBox(self, title):
            bVar = self.__verifyItem(self.n_boxVars, title)
            if bVar.get() == 1: return True
            else: return False

      def setCheckBox(self, title, ticked=True):
            cb = self.__verifyItem(self.n_cbs, title)
            if ticked: cb.select()
            else: cb.deselect()

#####################################
## FUNCTION for scales
#####################################
      def addScale(self, title, row=None, column=0, colspan=0 ):
            self.__verifyItem(self.n_scales, title, True)
            frame = self.__getLabelFrame(title)

            scale = Scale(frame)
            scale.configure(orient=HORIZONTAL, showvalue=False, highlightthickness=0)
            self.n_scales[title] = scale
            self.__packLabelFrame(frame, scale)
            self.__positionWidget(frame, row, column, colspan)

      def getScale(self, title):
            sc = self.__verifyItem(self.n_scales, title)
            return sc.get()

      def setScale(self, title, pos):
            sc = self.__verifyItem(self.n_scales, title)
            sc.set(pos)

      # this will make the scale show its value
      def showScaleValue(self, title, show=True):
            sc = self.__verifyItem(self.n_scales, title)
            sc.configure(showvalue=show)

      # change the orientation (Hor or Vert)
      def orientScaleHor(self, title, hor=True):
            sc = self.__verifyItem(self.n_scales, title)
            if hor: sc.configure(orient=HORIZONTAL)
            else: sc.configure(orient=VERTICAL)

      def setScaleRange(self, title, start, end, curr=0):
            sc = self.__verifyItem(self.n_scales, title)
            sc.configure(from_=start, to=end)
            self.setScale(title, curr)

#####################################
## FUNCTION for optionMenus
#####################################
      def __buildOptionBox(self, frame, title, options):
            self.__verifyItem(self.n_options, title, True)

            # deal with a dict_keys object - messy!!!!
            if not isinstance(options, list): options = list(options)

            var=StringVar(self.topLevel)
            if len(options) > 0: var.set(options[0])
            self.n_optionVars[title]=var

            if len(options) > 0: option = OptionMenu(frame,var,*options)
            else: option = OptionMenu(frame,var,[])
            option.inContainer = False
            option.configure(justify=LEFT, font=self.optionFont, background=self.labelBgColour, highlightthickness=0)
            # compare on windows & mac
            #option.configure(justify=LEFT, font=self.optionFont, background=self.labelBgColour, highlightthickness=12, bd=0, highlightbackground=self.labelBgColour)

            option.var = var
            self.n_options[title]=option

            if platform() == "Darwin":
                  option.configure(highlightbackground=self.labelBgColour)

            option.bind("<Tab>", self.__focusNextWindow)
            option.bind("<Shift-Tab>", self.__focusLastWindow)

            return option

      def addOptionBox(self, title, options, row=None, column=0, colspan=0):
            option = self.__buildOptionBox(self.window, title, options)
            self.__positionWidget(option, row, column, colspan)

      def addLabelOptionBox(self, title, options, row=None, column=0, colspan=0):
            frame = self.__getLabelFrame(title)
            option = self.__buildOptionBox(frame, title, options)
            self.__packLabelFrame(frame, option)
            self.__positionWidget(frame, row, column, colspan)

      def getOptionBox(self, title):
            self.__verifyItem(self.n_optionVars, title)
            return self.n_optionVars[title].get()

      def changeOptionBox(self, title, options, index=None):
            self.__verifyItem(self.n_optionVars, title)
            box = self.n_options[title]
            var = self.n_optionVars[title]
            box['menu'].delete(0, 'end')

            for option in options:
                  box['menu'].add_command(label=option, command=tkinter._setit(var, option))

            try: index = options.index(index)
            except: index = 0
            if len(options) > 0: var.set(options[0])

      # select the option at the specified position
      def setOptionBox(self, title, pos):
            self.__verifyItem(self.n_optionVars, title)
            box = self.n_options[title]
            box['menu'].invoke(pos)

#####################################
## FUNCTION to add spin boxes
#####################################
      def __buildSpinBox(self, frame, title, fromVal, toVal=None):
            self.__verifyItem(self.n_spins, title, True)
            spin = Spinbox(frame)
            spin.inContainer = False
            spin.configure(font=self.entryFont, highlightbackground=self.labelBgColour, highlightthickness=0)

            if platform() == "Darwin":
                  spin.configure(highlightbackground=self.labelBgColour)

            spin.bind("<Tab>", self.__focusNextWindow)
            spin.bind("<Shift-Tab>", self.__focusLastWindow)

            if toVal is None: spin.config(values=fromVal)
            else: spin.config(from_=fromVal, to=toVal)

            self.n_spins[title] = spin
            return  spin

      def __addSpinBox(self, title, fromVal, toVal=None, row=None, column=0, colspan=0):
            spin = self.__buildSpinBox(self.window, title, fromVal, toVal)
            self.__positionWidget(spin, row, column, colspan)

      def addSpinBox(self, title, vals, row=None, column=0, colspan=0):
            self.__addSpinBox(title, vals, None, row, column, colspan)
            
      def addSpinBoxRange(self, title, fromVal, toVal, row=None, column=0, colspan=0):
            self.__addSpinBox(title, fromVal, toVal, row, column, colspan)

      def addLabelSpinBox(self, title, fromVal, toVal=None, row=None, column=0, colspan=0):
            frame = self.__getLabelFrame(title)
            spin = self.__buildSpinBox(frame, title, fromVal, toVal)
            self.__packLabelFrame(frame, spin)
            self.__positionWidget(frame, row, column, colspan)

      def getSpinBox(self, title):
            spin = self.__verifyItem(self.n_spins, title)
            return spin.get()

      # not finished
      def setSpinBox(self, title, pos):
            spin = self.__verifyItem(self.n_spins, title)
            var = StringVar(self.topLevel)
            var.set("4")
            spin.config(textvariable=var)

#####################################
## FUNCTION to add images
#####################################
      # must be GIF or PNG
      def addImage(self, name, imageFile, row=None, column=0, colspan=0):
            #image = re.escape(image)
            self.__verifyItem(self.n_images, name, True)
            img = self.__getImage(imageFile)

            label = Label(self.window)
            label.config(anchor=CENTER, font=self.labelFont, background=self.labelBgColour)
            label.config(image=img)
            label.image = img # keep a reference!

            if img is not None:
                  h = img.height()
                  w = img.width()
                  label.config(height=h, width=w)
            
            self.n_images[name] = label
            self.__positionWidget(label, row, column, colspan)

      def setImageSize(self, name, width, height):
            img = self.__verifyItem(self.n_images, name)
            img.config(height=height, width=width)

      def rotateImage(self, name, image):
            img = self.__verifyItem(self.n_images, name)

      #if +ve then grow, else shrink...
      def zoomImage(self, name, x, y=''):
            img = self.__verifyItem(self.n_images, name)
            if x <= 0: self.shrinkImage(name, x*-1, y*-1)
            else: self.growImage(name, x, y)

      #get every nth pixel (must be an integer)
      # 0 will return an empty image, 1 will return the image, 2 will be 1/2 the size ...
      def shrinkImage(self, name, x, y=''):
            img = self.__verifyItem(self.n_images, name)
            image = img.image.subsample(x,y)

            img.config(image=image)
            img.config(anchor=CENTER, font=self.labelFont, background=self.labelBgColour)
            img.modImage = image # keep a reference!
            img.config(width=image.width(), height=image.height()) 

      #get every nth pixel (must be an integer)
      # 0 won't work, 1 will return the original size
      def growImage(self, name, x,y=''):
            label = self.__verifyItem(self.n_images, name)
            image = label.image.zoom(x,y)

            label.config(image=image)
            label.config(anchor=CENTER, font=self.labelFont, background=self.labelBgColour)
            label.modImage = image # keep a reference!
            label.config(width=image.width(), height=image.height()) 

      # replace the current image, with a new one
      def setImage(self, name, image):
            label = self.__verifyItem(self.n_images, name)
            image = self.__getImage(image)
            
            label.config(image=image)
            label.config(anchor=CENTER, font=self.labelFont, background=self.labelBgColour)
            label.image = image # keep a reference!

            h = image.height()
            w = image.width()
            #label.config(height=h, width=w)
            self.topLevel.update_idletasks()

      # function to remove image objects form cache
      def clearImageCache(self):
            self.n_imageCache = {}

      # internal function to check/build image object
      def __getImage(self, image):
            if image is None: return None
            if os.path.isfile(image):
                  if os.access(image, os.R_OK):
                        if image in self.n_imageCache and self.n_imageCache[image] is not None:
                              pass
                        elif image.endswith('.gif'):
                              self.n_imageCache[image]=PhotoImage(file=image)
                        elif image.endswith('.png'):
                              png = PngImageTk(image)
                              png.convert()
                              self.n_imageCache[image]=png.image
                        elif image.endswith('.ppm') or image.endswith('.pgm'):
                              self.n_imageCache[image]=PhotoImage(file=image)
                        elif image.endswith('jpg'):
                              self.n_imageCache[image]=self.convertJpgToBmp(image)
                        else:
                              raise Exception("Invalid image type: "+ image) from None
                  else:
                        raise Exception("Can't read image: "+ image) from None
            else:
                  raise Exception("Image "+image+" does not exist") from None
            return self.n_imageCache[image]

      def convertJpgToBmp(self, image):
            # read the image into an array of bytes
            with open(image, 'rb') as inFile:
                  import array
                  buf = array.array("B",inFile.read())

            # init the translator, and decode the array of bytes
            nanojpeg.njInit()
            nanojpeg.njDecode(buf, len(buf))

            # determine a file name & type
            if nanojpeg.njIsColor():
                  fileName = image.split('.jpg', 1)[0] + '.ppm'
                  param = 6
            else:
                  fileName = image.split('.jpg', 1)[0] + '.pgm'
                  fileName = "test3.pgm"
                  param = 5

            # create a string, starting with the header
            val = "P%d\n%d %d\n255\n" % (param, nanojpeg.njGetWidth(), nanojpeg.njGetHeight())
            # append the bytes, converted to chars
            val += ''.join(map(chr,nanojpeg.njGetImage()))

            # release any stuff
            nanojpeg.njDone()

            photo = PhotoImage(data=val)
            return photo

            # write the chars to a new file, if python3 we need to encode them first
#            with open(fileName, "wb") as outFile:
#                  if sys.version_info[0] == 2: outFile.write(val)
#                  else: outFile.write(val.encode('ISO-8859-1'))
#
#            return fileName
            
      # function to set a background image
      # make sure this is done before everything else, otherwise it will cover other widgets
      def setBgImage(self, image):
            image = self.__getImage(image)
            #self.window.config(image=image) # window as a label doesn't work...
            self.bgLabel.config(image=image)
            self.window.image = image # keep a reference!

      def removeBgImage(self):
            self.bgLabel.config(image=None)
            #self.window.config(image=None) # window as a label doesn't work...
            self.window.image = None # remove the reference

      def resizeBgImage(self):
            if self.window.image == None: return
            else:
                  pass

#####################################
## FUNCTION to play sounds
#####################################
      # internal function to manage sound availability
      def __soundWrap(self, sound, isFile=False, repeat=False):
            if platform() in ["win32", "Windows"]:
                  if isFile:
                        if False== os.path.isfile(sound): raise Exception("Can't find sound: "+ sound)
                        if not sound.endswith('.wav'): raise Exception("Invalid sound format: "+ sound)
                        kind = winsound.SND_FILENAME | winsound.SND_ASYNC
                  else:
                        if sound is None:
                              kind = winsound.SND_FILENAME
                        else:
                              kind = winsound.SND_ALIAS | winsound.SND_ASYNC

                  if repeat: kind = kind | winsound.SND_LOOP

                  winsound.PlaySound(sound, kind)
            else:
                  # sound not available at this time
                  raise Exception("Sound not supported on this platform: " + platform() )

      def playSound(self, sound):
            self.__soundWrap(sound, True)

      def stopSound(self):
            self.__soundWrap(None)

      def loopSound(self, sound):
            self.__soundWrap(sound, True, True)

      def soundError(self):
            self.__soundWrap("SystemHand")
      def soundWarning(self):
            self.__soundWrap("SystemAsterisk")

      def playNote(self, note, duration=200):
            if platform() in ["win32", "Windows"]:
                  try:
                        if isinstance(note, str): freq=self.NOTES[note]
                        else: freq=note
                  except KeyError:
                        raise Exception("Error: cannot play note - "+ note)
                  try:
                        if isinstance(duration, str): length=self.DURATIONS[duration]
                        else: length=duration
                  except KeyError:
                        raise Exception("Error: cannot play duration - " + duration)

                  try:
                        winsound.Beep(freq, length)
                  except RuntimeError:
                        raise Exception("Sound not available on this platform: " + platform() )
            else:
                  # sound not available at this time
                  raise Exception("Sound not supported on this platform: " + platform() )
      
#####################################
## FUNCTION for radio buttons
#####################################
      def addRadioButton(self, title, name, row=None, column=0, colspan=0 ):
            var = None
            newRb = False
            if (title in self.n_rbVars):
                  var = self.n_rbVars[title]
                  vals = self.n_rbVals[title]
                  if name in vals: raise Exception("Invalid radio button: "+ name+ " already exists" )
                  else: vals.append(name)
            else:
                  var = StringVar(self.topLevel)
                  vals = [name]
                  self.n_rbVars[title]=var
                  self.n_rbVals[title]=vals
                  newRb = True
            rb = Radiobutton(self.window)
            rb.configure(text=name, variable=var, value=name, background=self.labelBgColour, activebackground=self.labelBgColour, font=self.rbFont, indicatoron=1)
            if (title in self.n_rbs): self.n_rbs[title].append(rb)
            else: self.n_rbs[title]=[rb]
            #rb.bind("<Tab>", self.__focusNextWindow)
            #rb.bind("<Shift-Tab>", self.__focusLastWindow)
            if newRb: rb.select()

            self.__positionWidget(rb, row, column, colspan, None)

      def getRadioButton(self, title):
            var = self.__verifyItem(self.n_rbVars, title)
            return var.get()

      def setRadioButton(self, title, value):
            vals = self.__verifyItem(self.n_rbVals, title)
            if value not in vals: raise Exception("Invalid radio button: '"+ value+ "' doesn't exist" )
            var = self.n_rbVars[title]
            var.set(value)

      def setRadioTick(self, title, tick=True):
            radios = self.__verifyItem(self.n_rbs, title)
            for rb in radios:
                  if tick: rb.configure(indicatoron=1)
                  else: rb.configure(indicatoron=0)
                  
#####################################
## FUNCTION for list box
#####################################
      def addListBox(self, name, values=None, row=None, column=0, colspan=0):
            self.__verifyItem(self.n_lbs, name, True)
            frame = Frame(self.window)
            vscrollbar = AutoScrollbar(frame)
            hscrollbar = AutoScrollbar(frame, orient=HORIZONTAL)

            lb = Listbox(frame, yscrollcommand = vscrollbar.set, xscrollcommand=hscrollbar.set )

            vscrollbar.grid(row=0, column=1, sticky=N+S)
            hscrollbar.grid(row=1, column=0, sticky=E+W)

            lb.grid(row=0, column=0, sticky=N+S+E+W)

            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)

            vscrollbar.config( command = lb.yview )
            hscrollbar.config( command = lb.xview )

            lb.configure( font=self.lbFont )
            self.n_lbs[name] = lb

            if values is not None:
                  for name in values:
                        lb.insert(END, name)

            self.__positionWidget(frame, row, column, colspan)

      def setListSingle(self, title, single=True):
            lb = self.__verifyItem(self.n_lbs, title)
            if single: lb.configure(selectmode=BROWSE)
            else: lb.configure(selectmode=EXTENDED)

      def addListItem(self, title, item):
            lb = self.__verifyItem(self.n_lbs, title)
            lb.insert(END, item)

            items = lb.curselection()
            if len(items) > 0: lb.selection_clear(items)

            lb.see(END)
            lb.activate(lb.size()-1)
            lb.selection_set(lb.size()-1)

      def getListItems(self, title):
            lb = self.__verifyItem(self.n_lbs, title)
            items = lb.curselection()
            values = []
            for loop in range(len(items)):
                values.append ( lb.get(items[loop]) )
            return values

      def clearListBox(self, title):
            lb = self.__verifyItem(self.n_lbs, title)
            lb.delete(0, END) # clear

#####################################
## FUNCTION for buttons
#####################################
      def __buildButton(self, title, func, frame, name = None):
            if name is None: name = title
            self.__verifyItem(self.n_buttons, name, True)
            but = Button(frame)

            but.configure( text=title, font=self.buttonFont, background=self.buttonBgColour )

            if func is not None:
                  command = self.__makeFunc(func, title)
                  bindCommand = self.__makeFunc(func, title, True)

                  but.configure( command=command )
                  but.bind('<Return>', bindCommand)
            
            if platform() == "Darwin":
                but.configure(highlightbackground=self.labelBgColour)
            #but.bind("<Tab>", self.__focusNextWindow)
            #but.bind("<Shift-Tab>", self.__focusLastWindow)
            self.n_buttons[name]=but

            return but

      def addNamedButton(self, name, title, func, row=None, column=0, colspan=0):
            but = self.__buildButton(title, func, self.window, name)
            self.__positionWidget(but, row, column, colspan, None)

      def addButton(self, title, func, row=None, column=0, colspan=0):
            but = self.__buildButton(title, func, self.window)
            self.__positionWidget(but, row, column, colspan, None)

      def setButton(self, name, text):
            but = self.__verifyItem(self.n_buttons, name)
            but.configure(text=text)

      def setButtonImage(self, name, imgFile):
            but = self.__verifyItem(self.n_buttons, name)
            image = self.__getImage( imgFile )
            but.configure(image=image)
            but.image = image

      # adds a set of buttons, in the row, spannning specified columns
      # pass in a list of names & a list of functions (or a single function to use for all)
      def addButtons(self, names, funcs, row=None, column=0, colspan=0):

            if not isinstance(names, list):
                  raise Exception("Invalid button: " + names + ". It must be a list of buttons.")
        
            singleFunc = self.__checkFunc(names, funcs)
            
            frame = Frame(self.window)
            frame.configure( background=self.labelBgColour )

            # make them into a 2D array, if not already
            if not isinstance(names[0], list):
                  names = [names]
                  # won't be used if single func
                  funcs = [funcs]

            for bRow in range(len(names)):
                  for i in range(len(names[bRow])):
                        t = names[bRow][i]
                        if singleFunc is None: singleFunc = funcs[bRow][i]
                        but = self.__buildButton(t, singleFunc, frame)

                        but.grid ( row=bRow, column=i )
                        Grid.columnconfigure(frame, i, weight=1)
                        Grid.rowconfigure(frame, bRow, weight=1)
                  
            self.__positionWidget(frame, row, column, colspan)
            self.n_frames.append(frame)

#####################################
## FUNCTIONS for links
#####################################
      def __buildLink(self, title):
            link = Link(self.window)
            link.configure(text=title, font=self.linkFont, background=self.labelBgColour)
            self.n_links[title]=link
            return link

      # launches a browser to the specified page
      def addWebLink(self, title, page, row=None, column=0, colspan=0):
            link = self.__buildLink(title)
            link.registerWebpage(page)
            self.__positionWidget(link, row, column, colspan)

      # executes the specified function
      def addLink(self, title, func, row=None, column=0, colspan=0):
            link = self.__buildLink(title)
            myF = self.__makeFunc(func, title, True)
            link.registerCallback(myF)
            self.__positionWidget(link, row, column, colspan)

#####################################
## FUNCTIONS for labels
#####################################
      def __flash(self):
            if self.doFlash:
                  for lab in self.n_flashLabs:
                        bg = lab.cget("background")
                        fg = lab.cget("foreground")
                        lab.configure(background=fg, foreground=bg)
            self.topLevel.after(250, self.__flash)

      def addFlashLabel(self, title, text=None, row=None, column=0, colspan=0):
            self.addLabel(title, text, row, column, colspan)
            self.n_flashLabs.append(self.n_labels[title])
            self.doFlash = True

      def addLabel(self, title, text=None, row=None, column=0, colspan=0):
            self.__verifyItem(self.n_labels, title, True)
            lab = Label(self.window)
            lab.inContainer=False
            if text is not None: lab.configure ( text=text )
            lab.configure( justify=LEFT, font=self.labelFont, background=self.labelBgColour )
            self.n_labels[title]=lab

            self.__positionWidget(lab, row, column, colspan)

      def addEmptyLabel(self, title, row=None, column=0, colspan=0):
            self.addLabel(title, None, row, column, colspan)     

      # adds a set of labels, in the row, spannning specified columns
      def addLabels(self, names, row=None, colspan=0):
            frame = Frame(self.window)
            frame.configure( background=self.labelBgColour )
            for i in range(len(names)):
                  self.__verifyItem(self.n_labels, names[i], True)
                  lab = Label(frame)
                  lab.configure( text=names[i], font=self.labelFont, justify=LEFT, background=self.labelBgColour )
                  lab.inContainer=False
                  
                  self.n_labels[names[i]]=lab
                  lab.grid ( row=0, column=i )
                  Grid.columnconfigure(frame, i, weight=1)
                  Grid.rowconfigure(frame, 0, weight=1)
                  
            self.__positionWidget(frame, row, 0, colspan)
            self.n_frames.append(frame)

      def setLabel(self, name, text):
            lab = self.__verifyItem(self.n_labels, name)
            lab.configure(text=text)

      def getLabel(self, name):
            lab = self.__verifyItem(self.n_labels, name)
            return lab.cget("text")

      def clearLabel(self, name):
            self.setLabel(name, "")

#####################################
## FUNCTIONS to add Text Area
#####################################
      def __buildTextArea(self, title, frame, scrollable=False):
            self.__verifyItem(self.n_textAreas, title, True)
            if scrollable: text = scrolledtext.ScrolledText(frame)
            else: text = Text(frame)
            text.configure(font=self.taFont)

            if platform() == "Darwin":
                text.configure(highlightbackground=self.labelBgColour)
            text.bind("<Tab>", self.__focusNextWindow)
            text.bind("<Shift-Tab>", self.__focusLastWindow)

            text.bind('<Button-2>',self.__rightClick)
            text.bind('<Button-3>',self.__rightClick)
                  
            self.n_textAreas[title]=text
            self.logTextArea(title)
            return text

      def addTextArea(self, title, row=None, column=0, colspan=0):
            text = self.__buildTextArea(title, self.window)
            self.__positionWidget(text, row, column, colspan, NESW)

      def addScrolledTextArea(self, title, row=None, column=0, colspan=0):
            text = self.__buildTextArea(title, self.window, True)
            self.__positionWidget(text, row, column, colspan, N+E+S+W)

      def getTextArea(self, title):
            self.__verifyItem(self.n_textAreas, title)
            text = self.n_textAreas[title].get('1.0', END+'-1c')
            return text

      def setTextArea(self, title, text):
            self.__verifyItem(self.n_textAreas, title)
            self.n_textAreas[title].insert('1.0',text)

      def clearTextArea(self, title):
            self.__verifyItem(self.n_textAreas, title)
            self.n_textAreas[title].delete('1.0',END)

      def logTextArea(self, title):
            newHash = self.__getTextAreaHash(title)
            self.n_taHashes[title] = newHash

      def textAreaChanged(self, title):
            newHash = self.__getTextAreaHash(title)
            return newHash != self.n_taHashes[title]

      def __getTextAreaHash(self, title):
            self.__verifyItem(self.n_textAreas, title)
            text = self.getTextArea(title)
            md5 = hashlib.md5(str.encode(text)).digest()
            return md5

#####################################
## FUNCTIONS to add Message Box
#####################################
      def addMessage(self, title, text, row=None, column=0, colspan=0):
            if (title in self.n_messages): raise Exception("Invalid name:", title, "already exists")
            mess = Message(self.window) 
            mess.configure(font=self.messageFont)
            mess.configure( justify=LEFT, background=self.labelBgColour )
            if text is not None: mess.configure(text=text)
            if platform() == "Darwin":
                mess.configure(highlightbackground=self.labelBgColour)
            self.n_messages[title]=mess

            self.__positionWidget(mess, row, column, colspan)
#            mess.bind("<Configure>", lambda e: mess.configure(width=e.width-10))

      def addEmptyMessage(self, title, row=None, column=0, colspan=0):
            self.addMessage(title, None, row, column, colspan)
            
      def setMessage(self, title, text):
            if (title not in self.n_messages): raise Exception("Invalid message:", title)
            self.n_messages[title].configure(text=text)

      def clearMessage(self, title ):
            if (title not in self.n_messages): raise Exception("Invalid message:", title)
            self.n_messages[title].configure(text="")

#####################################
## FUNCTIONS for entry boxes
#####################################
      def __buildEntry(self, title, frame, secret=False):
            self.__verifyItem(self.n_entries, title, True)
            var=StringVar(self.topLevel)
            ent = Entry(frame)
            ent.var = var
            ent.inContainer = False
            ent.myTitle=title
            ent.configure(textvariable=var, font=self.entryFont)
            if secret: ent.configure(show="*")            
            if platform() == "Darwin":
                ent.configure(highlightbackground=self.labelBgColour)
            ent.bind("<Tab>", self.__focusNextWindow)
            ent.bind("<Shift-Tab>", self.__focusLastWindow)

            ent.bind('<Button-2>',self.__rightClick)
            ent.bind('<Button-3>',self.__rightClick)
            self.n_entries[title]=ent
            self.n_entryVars[title]=var
            return ent

      def addEntry(self, title, row=None, column=0, colspan=0, secret=False):
            ent = self.__buildEntry(title, self.window, secret)
            self.__positionWidget(ent, row, column, colspan)

      def addSecretEntry(self, title, row=None, column=0, colspan=0):
            self.addEntry(title, row, column, colspan, True)

      def addLabelEntry(self, title, row=None, column=0, colspan=0, secret=False):
            frame = self.__getLabelFrame(title)
            ent = self.__buildEntry(title, frame, secret)
            self.__packLabelFrame(frame, ent)
            self.__positionWidget(frame, row, column, colspan)
            
      def addSecretLabelEntry(self, title, row=None, column=0, colspan=0):
            self.addLabelEntry(title, row, column, colspan, True)

      def getEntry(self, name):
            self.__verifyItem(self.n_entryVars, name)
            return self.n_entryVars[name].get()

      def setEntry(self, name, text):
            self.__verifyItem(self.n_entryVars, name)
            self.n_entryVars[name].set(text)

      def clearEntry(self, name):
            self.__verifyItem(self.n_entryVars, name)
            self.n_entryVars[name].set("")
            self.setFocus(name)

      def clearAllEntries(self):
            for entry in self.n_entryVars:
                  self.n_entryVars[entry].set("")

      def setFocus(self, name):
            self.__verifyItem(self.n_entries, name)
            self.n_entries[name].focus_set()

#####################################
## FUNCTIONS for progress bars (meters)
#####################################
      def addMeter(self, name, row=None, column=0, colspan=0):
            self.__verifyItem(self.n_meters, name, True)
            meter = Meter(self.window, font=self.meterFont)
            self.n_meters[name] = meter
            self.__positionWidget(meter, row, column, colspan)

      def setMeter(self, name, value=0.0, text=None):
            item = self.__verifyItem(self.n_meters, name)
            item.set(value, text) 

      def getMeter(self, name):
            item = self.__verifyItem(self.n_meters, name)
            return item.get()
      
#####################################
## FUNCTIONS for tool bar
#####################################
      # adds a list of buttons along the top - like a tool bar...
      def addToolbar(self, names, funcs):
            if not self.hasTb: self.hasTb = True

            image = None
            singleFunc = self.__checkFunc(names, funcs)
            if not isinstance(names, list): names = [names]

            for i in range(len(names)):
                  t = names[i]
                  if (t in self.n_tbButts): raise Exception("Invalid toolbar name: "+ t+ " already exists")
            
                  imgFile = os.path.join(self.icon_path,"default",t.lower() + ".png")
                  try: image = self.__getImage( imgFile )
                  except Exception as e: image = None

                  but = Button(self.tb)
                  self.n_tbButts[t] = but

                  if singleFunc is not None:
                        u = self.__makeFunc(singleFunc, t)
                  else:
                        u = self.__makeFunc(funcs[i], t)

                  but.configure( text=t, command=u, relief=FLAT, font=self.tbFont )
                  if image is not None:
                        but.image = image
                        but.configure(image=image)
                  but.pack (side=LEFT, padx=2, pady=2)
                  self.__addTooltip(but, t)

      def setToolbarImage(self, name, imgFile):
            if (name not in self.n_tbButts): raise Exception("Unknown toolbar name: " + name)
            image = self.__getImage( imgFile )
            self.n_tbButts[name].configure(image=image)
            self.n_tbButts[name].image = image

#####################################
## FUNCTIONS for menu bar
#####################################
      def addMenuList(self, menuName, names, funcs, tearable=False):

            # deal with a dict_keys object - messy!!!!
            if not isinstance(names, list): names = list(names)

            # create a menu bar - only shows if populated
            if not self.hasMenu:
                  self.hasMenu = True
                  self.menuBar = Menu(self.appWindow)
                  self.topLevel.config(menu=self.menuBar)

            singleFunc = self.__checkFunc(names, funcs)
            menu = Menu(self.menuBar, tearoff=tearable)

            for i in range(len(names)):
                  t = names[i]
                  if t == "-": menu.add_separator()
                  else:
                        if singleFunc is not None:
                                u = self.__makeFunc(singleFunc, t)
                        else:
                                u = self.__makeFunc(funcs[i], t)

                        menu.add_command(label=t, command=u )

            self.menuBar.add_cascade(label=menuName,menu=menu)

      # add a single entry for a menu
      def addMenu(self, name, func):
            # create a menu bar - only shows if populated
            if not self.hasMenu:
                  self.hasMenu = True
                  self.menuBar = Menu(self.topLevel)
                  self.topLevel.config(menu=self.menuBar)

            u = self.__makeFunc(func, name, True)
            self.menuBar.add_command(label=name, command=u)

#####################################
## FUNCTIONS for status bar
#####################################
      def setStatusBg(self, colour=None):
            if colour is not None: self.status.configure(background=colour)

      def setStatusFg(self, colour=None):
            if colour is not None: self.status.configure(foreground=colour)

      def addStatus(self, header=""):
            self.hasStatus = True
            self.header=header
            self.status = Label(self.appWindow)
            self.status.configure( bd=1, relief=SUNKEN, anchor=W, font=self.statusFont)
            self.__addTooltip(self.status, "Status bar")
            self.status.pack(side=BOTTOM, fill=X, anchor=S)

      def setStatus(self, text):
            if self.hasStatus: self.status.configure(text=self.__getFormatStatus(text))

      def clearStatus(self):
            if self.hasStatus: self.status.configure(text=self.__getFormatStatus(""))
            
      # formats the string shown in the status bar
      def __getFormatStatus(self, text):
            text = str(text)
            if len(text) == 0: return ""
            elif len (self.header) == 0:
                  return text
            else:
                  return self.header + ": " + text
#####################################
## TOOLTIPS
#####################################
      def __addTooltip(self, item, text):
            tip = ToolTip(item, delay=500, follow_mouse=1, text=text)

#####################################
## FUNCTIONS to show pop-up dialogs
#####################################
      def infoBox(self, title, message):
            messagebox.showinfo(title, message)

      def errorBox(self, title, message):
            messagebox.showerror(title, message)

      def warningBox(self, title, message):
            messagebox.showwarning(title, message)

      def yesNoBox(self, title, message):
            return messagebox.askyesno(title, message)

      def questionBox(self, title, message):
            return messagebox.askquestion(title, message)

      def okBox(self, title, message):
            return messagebox.askokcancel(title, message)

      def retryBox(self, title, message):
            return messagebox.askretrycancel(title, message)

      def openBox(self, title=None, fileName=None, dirName=None, fileExt=".txt", fileTypes=None, asFile=True):
            if fileTypes is None: fileTypes = [('all files', '.*'), ('text files', '.txt')]
            # define options for opening
            options = {}
            options['defaultextension'] = fileExt
            options['filetypes'] = fileTypes
            options['initialdir'] = dirName
            options['initialfile'] = fileName
            options['title'] = title

            if asFile: return filedialog.askopenfile(mode="r", **options)
            # will return "" if cancelled
            else:return filedialog.askopenfilename(**options)

      def saveBox(self, title=None, fileName=None, dirName=None, fileExt=".txt", fileTypes=None, asFile=True):
            if fileTypes is None: fileTypes = [('all files', '.*'), ('text files', '.txt')]
            # define options for opening
            options = {}
            options['defaultextension'] = fileExt
            options['filetypes'] = fileTypes
            options['initialdir'] = dirName
            options['initialfile'] = fileName
            options['title'] = title

            if asFile: return filedialog.asksaveasfile(mode='w', **options)
            # will return "" if cancelled
            else: return filedialog.asksaveasfilename(**options)

      def directoryBox(self, title=None, dirName=None):
            options = {}
            options['initialdir'] = dirName
            options['title'] = title
            options['mustexist'] = False
            file =  filedialog.askdirectory(**options)
            if file == "": return None
            else: return file

      def colourBox(self, colour='#ff0000'):
            col = colorchooser.askcolor(colour)
            if col[1] is None: return None
            else: return col[1]

      def textBox(self, title, question):
            return TextDialog(self.topLevel, title, question).result

      def numBox(self, title, question):
            return NumDialog(self.topLevel, title, question).result

#####################################
## ProgressBar Class
## from: http://tkinter.unpythonic.net/wiki/ProgressMeter
#####################################
class Meter(Frame):
      def __init__(self, master, width=700, height=20, bg='white', fillcolor='orchid1', value=0.0, text=None, font=None, textcolor='black', *args, **kw):
            Frame.__init__(self, master, bg=bg, width=width, height=height, *args, **kw)
            self._value = value
            self.config(relief='ridge', bd=3)

#            self._canv = Canvas(self, bg=self['bg'], height=self['height'], highlightthickness=0, relief='flat', bd=0)
            self._canv = Canvas(self, bg=self['bg'], width=self['width'], height=self['height'], highlightthickness=0, relief='flat', bd=0)
            self._canv.pack(fill='both', expand=1)
            self._rect = self._canv.create_rectangle(0, 0, 0, self._canv.winfo_reqheight(), fill=fillcolor, width=0)
            self._text = self._canv.create_text(self._canv.winfo_reqwidth()/2, self._canv.winfo_reqheight()/2, text='', fill=textcolor)
            if font: self._canv.itemconfigure(self._text, font=font)

            self.set(value, text)
            self.bind('<Configure>', self._update_coords)

      def _update_coords(self, event):
            '''Updates the position of the text and rectangle inside the canvas when the size of the widget gets changed.'''
            # looks like we have to call update_idletasks() twice to make sure
            # to get the results we expect
            self._canv.update_idletasks()
            self._canv.coords(self._text, self._canv.winfo_width()/2, self._canv.winfo_height()/2)
            self._canv.coords(self._rect, 0, 0, self._canv.winfo_width()*self._value, self._canv.winfo_height())
            self._canv.update_idletasks()

      def get(self): return self._value, self._canv.itemcget(self._text, 'text')

      def set(self, value=0.0, text=None):
            #make the value failsafe:
            if value < 0.0: value = 0.0
            elif value > 1.0: value = 1.0
            self._value = value

            #if no text is specified use the default percentage string:
            if text == None: text = str(int(round(100 * value))) + ' %'

            self._canv.coords(self._rect, 0, 0, self._canv.winfo_width()*value, self._canv.winfo_height())
            self._canv.itemconfigure(self._text, text=text)
            self._canv.update_idletasks()

#####################################
## Hyperlink Class
#####################################
class Link(Label):
      def __init__(self, *args, **kwargs):
            Label.__init__(self, *args, **kwargs)
            self.configure(fg="blue")
            self.page=""

            if platform() == "Darwin":
                  self.configure(cursor="pointinghand")
            elif platform() in [ "win32", "Windows"]:
                  self.configure(cursor="hand2")

      def registerCallback(self, callback):
            self.bind("<Button-1>", callback)

      def launchBrowser(self, event):
            webbrowser.open_new(r""+self.page)
            #webbrowser.open_new_tab(self.page)

      def registerWebpage(self, page):
            if not page.startswith("http"):
                  raise InvalidURLError("Invalid URL: " + page + " (it should begin as http://)")

            self.page = page
            self.bind("<Button-1>", self.launchBrowser)

#####################################
## errors
#####################################
class ItemLookupError(LookupError):
      '''raise this when there's a lookup error for my app'''
      pass

class InvalidURLError(ValueError):
      '''raise this when there's a lookup error for my app'''
      pass

#####################################
## scrollable frame...
#####################################
class AutoScrollbar(Scrollbar):
      # a scrollbar that hides itself if it's not needed.  only
      # works if you use the grid geometry manager.
      def set(self, lo, hi):
            if float(lo) <= 0.0 and float(hi) >= 1.0:
                  # grid_remove is currently missing from Tkinter!
                  self.tk.call("grid", "remove", self)
            else:
                  self.grid()
            Scrollbar.set(self, lo, hi)
      def pack(self, **kw):
            raise Exception("cannot use pack with this widget")
      def place(self, **kw):
            raise Exception("cannot use place with this widget")

#################################
## Additional Dialog Classes
#################################
# the main daialog class to be extended
class Dialog(Toplevel):
    def __init__(self, parent, title = None):
        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title: self.title(title)
        self.parent = parent
        self.result = None

        # create a frame to hold the contents
        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        # create the buttons
        self.buttonbox()

        self.grab_set()
        if not self.initial_focus: self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.initial_focus.focus_set()
        self.wait_window(self)

    # override to create the contents of the dialog
    # should return the widget to give focus to
    def body(self, master):
        pass

    # add standard buttons
    # override if you don't want the standard buttons
    def buttonbox(self):
        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    # called when ok button pressed
    def ok(self, event=None):
        # only continue of validate() returns True
        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        # call the validate function before calling the cancel function
        self.apply()
        self.cancel()

    # called when cancel button pressed
    def cancel(self, event=None):
        self.parent.focus_set() # give focus back to the parent
        self.destroy()

    # override this to cancel closing the form
    def validate(self):
        return True

    # override this to do something before closing 
    def apply(self):
        pass

# a base class for a simple data capture dialog
class SimpleEntryDialog(Dialog):
    def __init__(self, parent, title, question):
        self.error = False
        self.question = question
        super(SimpleEntryDialog, self).__init__(parent, title)

    def clearError(self, e):
        if self.error:
            self.error = False
            self.l1.configure(text="")

    def setError(self, message):
        self.error = True
        self.l1.configure(text=message)

    # a label for the question, an entry for the answer
    # a label for an error message
    def body(self, master):
        Label(master, text=self.question).grid(row=0)
        self.e1 = Entry(master)
        self.l1 = Label(master, fg="red")
        self.e1.grid(row=1)
        self.l1.grid(row=2)
        self.e1.bind("<Key>", self.clearError)
        return self.e1

# captures a string - must not be empty
class TextDialog(SimpleEntryDialog):
    def __init__(self, parent, title, question):
        super(TextDialog, self).__init__(parent, title, question)

    def validate(self):
        res = self.e1.get()
        if len(res.strip()) == 0:
            self.setError("Invalid text.")
            return False
        else:
            self.result = res
            return True

# capture a number - must be a valid float
class NumDialog(SimpleEntryDialog):
    def __init__(self, parent, title, question):
        super(NumDialog, self).__init__(parent, title, question)

    def validate(self):
        res = self.e1.get()
        try:
            self.result = float(res) if '.' in res else int(res)
            return True
        except ValueError:
            self.setError("Invalid number.")
            return False


#####################################
## Toplevel Stuff
#####################################
class GuiChild(Toplevel):
      def __init__(self):
            Toplevel.__init__(self)

      def __getattr__(self,name):
            def handlerFunction(*args,**kwargs):
                  print("Unknown function:", name,args,kwargs)
            return handlerFunction

#####################################
## MAIN - for testing
#####################################
if __name__ == "__main__":
      progress = 0
      main = True
      meter = True
      def tb_press(name):
            global main, meter
            win.setStatus("TB Press:"+name)
            try:
                  if name == "Save": win.setStatus(win.saveBox())
                  elif name == "Open": win.setStatus(win.openBox())
                  elif name == "Dir": win.setStatus(win.directoryBox())
                  elif name == "Close": win.stop()
                  elif name == "Colour":
                        col = win.colourBox()
                        if col is not None:
                            win.setStatus(col)
                            win.setBg(col)
                  elif name == "Resizable": win.setResizable(not win.getResizable())
                  elif name == "RBCheck":
                        win.setStatus(win.getRadioButton("Test") + str(win.getCheckBox("Click Me")))
                  elif name == "SetRB":
                        win.setStatus(win.getEntry("RB"))
                        win.setRadioButton("Test", win.getEntry("RB"))
                  elif name == "IncreaseB": win.increaseButtonFont()
                  elif name == "DecreaseB": win.decreaseButtonFont()
                  elif name == "IncreaseL": win.increaseLabelFont()
                  elif name == "DecreaseL": win.decreaseLabelFont()
                  elif name == "GetList": win.infoBox("List", win.getListItems("Bits"))
                  elif name == "H-Widget":
                        name = win.textBox("Hide Widget", "Enter widget name:")
                        win.hideWidget(getWidget(), name)
                  elif name == "S-Widget":
                        name = win.textBox("Show Widget", "Enter widget name:")
                        win.showWidget(getWidget(), name)
                  elif name == "R-Widget":
                        name = win.textBox("Remove Widget", "Enter widget name:")
                        win.removeWidget(getWidget(), name)
                  elif name == "Sticky":
                        name = win.textBox("Sticky Widget", "Enter widget name:")
                        pos = win.getOptionBox("Option")
                        win.configureWidget(getWidget(), name, 'sticky', pos)
                        #win.setEntrySticky(name, pos)
                  elif name == "FullScreen": win.setGeom("fullscreen")
                  elif name == "Submit":
                        if win.retryBox("Submit", "Are you sure?"):
                              win.setStatus ( str(win.getScale("Scale")) )
                        win.removeAllWidgets()
                  elif name == "Clear":
                        if win.yesNoBox("Clear", "Are you sure?"):
                              win.setCheckBox("Click Me", False)
                              win.clearAllEntries()
                              win.setFocus("Name")
                        win.removeScale("Scale")
                  elif name == "Scale":
                        win.setStatus("Scale: " + str(win.getScale("Scale")))
                        win.setTransparency(win.getScale("Scale")/100)
                  elif name == "Test":
                        win.setStatus("RB: " + win.getRadioButton("Test"))
                  elif name == "spins1":
                        win.setStatus("SPIN: " + win.getSpinBox("spins1"))
                  elif name == "Click Me":
                        win.setStatus("CLICK"+ str(win.getCheckBox("Click Me")))
                  elif name == "stop-start":
                        meter = not meter
                        
            except Exception as e:
                  win.errorBox("Exception", e)

      def getWidget():
            kind = win.getOptionBox("Widgets")
            if kind == "WINDOW": return 0
            elif kind == "LABEL": return 1
            elif kind == "ENTRY": return 2
            elif kind == "BUTTON": return 3
            elif kind == "CB": return 4
            elif kind == "SCALE": return 5
            elif kind == "RB": return 6
            elif kind == "LB": return 7
            elif kind == "MESSAGE": return 8
            elif kind == "SPIN": return 9
            elif kind == "OPTION": return 10
            elif kind == "TEXTAREA": return 11
            elif kind == "LINK": return 12
            elif kind == "METER": return 13
            else: return 0

      def widgetChanged():
            print("HERE")

      
      def meter():
            global progress
            if meter:
                  progress += .1
                  win.setMeter("Meter", progress)
                  print("ping: ", progress)
                  if progress >1: progress = 0

      print ( "Making GUI" )
      win = gui("Details")
      win.setExpand("all")
      #win.setSticky(False)
#      win.addEntry("Empty")
#      win.addLabelEntry("Name")
#      win.setLabelBg("Name", "red")
#      win.setLabelFg("Name", "yellow")
      #win.setLabelWidth("Name", "40")
      #win.setLabelHeight("Name", "20")
#      win.disableEntry("Name")
#      win.setFocus("Name")
#      win.addLabelEntry("Age")
#      win.addLabelEntry("Gender")
#      win.addButtons(["Submit","Clear", "Resizable"], tb_press)
#      win.setButtonBg("Resizable", "red")
#      win.setButtonFg("Resizable", "yellow")
#      win.setButtonWidth("Resizable", "40")
#      win.setButtonHeight("Resizable", "30")
#      win.setButtonState("Resizable", "disabled")
      win.addButtons(["IncreaseB", "DecreaseB"], tb_press)
      win.addButtons(["IncreaseL", "DecreaseL"], tb_press)
      win.addLabels(["a", "b", "c", "d", "e"])
      win.addCheckBox("Click Me")
      win.setCbCommand("Click Me", tb_press)
      win.addButton("RBCheck", tb_press)
      win.addScale("Scale")
      win.orientScaleHor("Scale", True)
      win.setScaleCommand("Scale", tb_press)
      win.setScaleRange("Scale",0, 100, 100)
      #win.addImage("8ball.gif", win.getNextRow(), 0, 2)
      win.addRadioButton("Test", "Oneeeeeeeeeeeeeeeeeeeee")
      win.addRadioButton("Test", "Two")
      win.addRadioButton("Test", "Three")
      #win.addRadioButton("Test", "Four")
      win.setRbAlign("Test", win.SE)
      win.setRbCommand("Test", tb_press)
      win.addEntry("RB")
      win.setEntryFg("RB", "yellow")
      win.setEntryBg("RB", "blue")
      win.addButtons(["SetRB", "GetList"], tb_press)
      #win.addListBox("Bits", [1,2,3,4,5])
      #win.setListSingle("Bits", False)
      #win.setLbBg("Bits", "green")
      #win.setLbFg("Bits", "pink")
      #win.setLbState("Bits", "disabled")
      win.addOptionBox("opt",[7,2,3,4,5])
      win.setOptionBoxCommand("opt", tb_press)
      win.addLabelOptionBox("Option",["left", "right", "both"])
      win.addLabelOptionBox("opt2",["a","b","c"])
      win.addSpinBoxRange("spins1", 1, 10)
      win.addLabelSpinBox("spins2", 1, 10)
      win.addLabelSpinBox("superSpinsAre", 1, 10)
      win.setSpinBoxCommand("spins1", tb_press)
      win.setSpinBox("superSpinsAre", 4)
      win.addLabelOptionBox("Widgets",[ "WINDOW", "LABEL", "ENTRY", "BUTTON", "CB", "SCALE", "RB", "LB", "MESSAGE", "SPIN", "OPTION", "TEXTAREA", "LINK", "METER"]) 
      win.addMeter("Meter")
      win.setPollTime(2000)
      win.registerEvent(meter)
      win.addWebLink("link", "http://www.google.com")
      win.addLink("stop-start", tb_press)
      win.addEmptyMessage("fred2")
      win.addEmptyLabel("fff")
      win.setLabelBg("fff", "pink")
      win.setMessageBg("fred2", "yellow")
      #win.addMessage("fred", "Help somebody zsdf asdf asdf asdgfasdgasdfg asdgfasdfasdf asdfasdf . asdfasdf ")
      #win.setMessageBg("fred", "Green")
      #win.setMessageWidth("fred", 100)

      win.addToolbar(["H-Widget", "S-Widget", "R-Widget", "Sticky", "Download", "Open", "Close", "Colour", "FullScreen"], tb_press)
      win.addStatus("Status")
      win.setStatusBg("green")
      win.setStatusFg("orange")
      win.addMenuList("Fonts", ["IncreaseB", "DecreaseB", "IncreaseL", "DecreaseL"], tb_press)
      win.addMenu("Close", tb_press)
      win.addMenu("ThisOne", tb_press)
      #win.setIcon("/Users/jarvismail/Downloads/PYLIB/icons/default/left.png")
      win.go()
      print ("Done making GUI" )
