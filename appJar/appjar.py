# -*- coding: utf-8 -*-
"""appJar.py: Provides a GUI class, for making simple tkinter GUIs."""
# Nearly everything I learnt came from: http://effbot.org/tkinterbook/
# with help from: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
# with snippets from stackexchange.com

# make print backwards compatible
from __future__ import print_function

try:
    # for Python2
    from Tkinter import *
    import tkMessageBox as messagebox
    from tkColorChooser import askcolor
    import tkFileDialog as filedialog
    import ScrolledText as scrolledtext
    import tkFont as font
    PYTHON2 = True
    PY_NAME = "Python"
except ImportError:
    # for Python3
    from tkinter import *
    from tkinter import messagebox
    from tkinter.colorchooser import askcolor
    from tkinter import filedialog
    from tkinter import scrolledtext
    from tkinter import font
    PYTHON2 = False
    PY_NAME = "python3"

import os
import sys
import re
import hashlib
import imghdr
import time

import __main__ as theMain
from platform import system as platform

# Links
import webbrowser

# ajTree
try:
    from idlelib.TreeWidget import TreeItem, TreeNode, ZoomHeight
except:
    try:
        from idlelib.tree import TreeItem, TreeNode
        from idlelib.zoomheight import ZoomHeight
    except:
        raise Exception("Unsupported python build, unable to access idlelib")

from xml.dom.minidom import parseString
# DatePicker
import calendar
import datetime

#######################
# import borrowed libraries - not compulsory
#######################
try:
    from appJar.lib.tooltip import ToolTip
    TOOLTIP_AVAILABLE = True
except:
    TOOLTIP_AVAILABLE = False

try:
    from appJar.lib.tkinter_png import *
    TKINTERPNG_AVAILABLE = True
except:
    TKINTERPNG_AVAILABLE = False
try:
    from appJar.lib import nanojpeg
    NANOJPEG_AVAILABLE = True
except:
    NANOJPEG_AVAILABLE = False

# only try to import winsound if we're on windows
if platform() in ["win32", "Windows"]:
    import winsound

# details
__author__ = "Richard Jarvis"
__copyright__ = "Copyright 2016, Richard Jarvis"
__credits__ = ["Graham Turner", "Sarah Murch"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Richard Jarvis"
__email__ = "info@appJar.info"
__status__ = "Development"

# class to allow simple creation of tkinter GUIs


class gui(object):
    """
        Class to represent the GUI
        - Create one of these
        - add some widgets
        - call the go() function
    """

    @staticmethod
    def CLEAN_CONFIG_DICTIONARY(**kw):
        """
            Used by all Classes to tidy up dictionaries passed into config functions
            Allows us to more quickly process the dictionaries when overriding config
        """
        try:
            kw['bg'] = kw.pop('background')
        except:
            pass
        try:
            kw['fg'] = kw.pop('foreground')
        except:
            pass
        kw = dict((k.lower().strip(), v) for k, v in kw.items())
        return kw

    # globals for supported platforms
    WINDOWS = 1
    MAC = 2
    LINUX = 3

    @staticmethod
    def GET_PLATFORM():
        # get the platform
        if platform() in ["win32", "Windows"]:
            return gui.WINDOWS
        elif platform() == "Darwin":
            return gui.MAC
        elif platform() == "Linux":
            return gui.LINUX
        else:
            raise Exception("Unsupported platform: " + platform())

    @staticmethod
    def CENTER(win):
        """
        centers a tkinter window
        http://stackoverflow.com/questions/3352918/
        :param win: the root or Toplevel window to center
        """
        win.attributes('-alpha', 0.0)  # hide the window
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        y = y - 150
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()
        win.attributes('-alpha', 1.0)

    built = False

    # used to identify widgets in component configurations
    WINDOW = 0
    LABEL = 1
    ENTRY = 2
    BUTTON = 3
    CHECKBOX = 4
    SCALE = 5
    RADIOBUTTON = 6
    LISTBOX = 7
    MESSAGE = 8
    SPIN = 9
    OPTION = 10
    TEXTAREA = 11
    LINK = 12
    METER = 13
    IMAGE = 14
    PIECHART = 15
    PROPERTIES = 16
    GRID = 17

    RB = 60
    CB = 40
    LB = 70

    LABELFRAME = 30
    FRAME = 36
    TABBEDFRAME = 31
    PANEDFRAME = 32
    SCROLLPANE = 33
    PAGEDWINDOW = 34
    TOGGLEFRAME = 35

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
    SUNKEN = SUNKEN
    RAISED = RAISED
    GROOVE = GROOVE
    RIDGE = RIDGE
    FLAT = FLAT

    # containers
    C_ROOT = 'rootPage'
    C_LABELFRAME = 'labelFrame'
    C_FRAME = 'frame'
    C_TOGGLEFRAME = 'toggleFrame'

    # 2 containers for pagedWindow
    C_PAGEDWINDOW = 'pagedWindow'
    C_PAGE = 'page'
    # 2 containers for tabbedFrame
    C_TABBEDFRAME = 'tabbedFrame'
    C_TAB = 'tab'
    # 2 containers for panedFrame
    C_PANEDFRAME = 'panedFrame'
    C_PANE = 'pane'

    C_SUBWINDOW = 'subWindow'
    C_SCROLLPANE = 'scrollPane'

    # names for each of the widgets defined above
    # used for defining functions
    WIDGETS = {
        LABEL: "Label",
        MESSAGE: "Message",
        BUTTON: "Button",
        ENTRY: "Entry",
        CB: "Cb",
        SCALE: "Scale",
        RB: "Rb",
        GRID: "Grid",
        LB: "Lb",
        SPIN: "SpinBox",
        OPTION: "OptionBox",
        TEXTAREA: "TextArea",
        LINK: "Link",
        METER: "Meter",
        IMAGE: "Image",
        RADIOBUTTON: "RadioButton",
        CHECKBOX: "CheckBox",
        LISTBOX: "ListBox",
        PIECHART: "PieChart",
        PROPERTIES: "Properties",
        FRAME: "Frame",
        LABELFRAME: "LabelFrame",
        PANEDFRAME: "PanedFrame",
        TOGGLEFRAME: "ToggleFrame",
        TABBEDFRAME: "TabbedFrame"}

    # music stuff
    BASIC_NOTES = {
        "A": 440,
        "B": 493,
        "C": 261,
        "D": 293,
        "E": 329,
        "F": 349,
        "G": 392}
    NOTES = {
        'f8': 5587,
        'c#6': 1108,
        'f4': 349,
        'c7': 2093,
        'd#2': 77,
        'g8': 6271,
        'd4': 293,
        'd7': 2349,
        'd#7': 2489,
        'g#4': 415,
        'e7': 2637,
        'd9': 9397,
        'b8': 7902,
        'a#4': 466,
        'b5': 987,
        'b2': 123,
        'g#9': 13289,
        'g9': 12543,
        'f#2': 92,
        'c4': 261,
        'e1': 41,
        'e6': 1318,
        'a#8': 7458,
        'c5': 523,
        'd6': 1174,
        'd3': 146,
        'g7': 3135,
        'd2': 73,
        'd#3': 155,
        'g#6': 1661,
        'd#4': 311,
        'a3': 219,
        'g2': 97,
        'c#5': 554,
        'd#9': 9956,
        'a8': 7040,
        'a#5': 932,
        'd#5': 622,
        'a1': 54,
        'g#8': 6644,
        'a2': 109,
        'g#5': 830,
        'f3': 174,
        'a6': 1760,
        'e8': 5274,
        'c#9': 8869,
        'f5': 698,
        'b1': 61,
        'c#4': 277,
        'f#9': 11839,
        'e5': 659,
        'f9': 11175,
        'f#5': 739,
        'a#1': 58,
        'f#8': 5919,
        'b7': 3951,
        'c#8': 4434,
        'g1': 48,
        'c#3': 138,
        'f#7': 2959,
        'c6': 1046,
        'c#2': 69,
        'c#7': 2217,
        'c3': 130,
        'e9': 10548,
        'c9': 8372,
        'a#6': 1864,
        'a#7': 3729,
        'g#2': 103,
        'f6': 1396,
        'b3': 246,
        'g#3': 207,
        'b4': 493,
        'a7': 3520,
        'd#6': 1244,
        'd#8': 4978,
        'f2': 87,
        'd5': 587,
        'f7': 2793,
        'f#6': 1479,
        'g6': 1567,
        'e3': 164,
        'f#3': 184,
        'g#1': 51,
        'd8': 4698,
        'f#4': 369,
        'f1': 43,
        'c8': 4186,
        'g4': 391,
        'g3': 195,
        'a4': 440,
        'a#3': 233,
        'd#1': 38,
        'e2': 82,
        'e4': 329,
        'a5': 880,
        'a#2': 116,
        'g5': 783,
        'g#7': 3322,
        'b6': 1975,
        'c2': 65,
        'f#1': 46}

    DURATIONS = {
        "BREVE": 2000,
        "SEMIBREVE": 1000,
        "MINIM": 500,
        "CROTCHET": 250,
        "QUAVER": 125,
        "SEMIQUAVER": 63,
        "DEMISEMIQUAVER": 32,
        "HEMIDEMISEMIQUAVER": 16}

#####################################
# CONSTRUCTOR - creates the GUI
#####################################
    def __init__(self, title=None, geom=None, warn=True, debug=False):
        # first out, verify the platform
        self.platform = gui.GET_PLATFORM()

        self.WARN = warn
        self.DEBUG = debug

        # a stack to hold containers as being built
        # done here, as initArrays is called elsewhere - to reset the gubbins
        self.containerStack = []

        # first up, set up all the data stores
        self.__initArrays()

        # dynamically create lots of functions for configuring stuff
        self.__buildConfigFuncs()

        # language parser
        self.config = None

        # set up some default path locations
        self.lib_file = os.path.abspath(__file__)
        self.exe_file = os.path.basename(theMain.__file__)
        self.exe_loc = os.path.dirname(theMain.__file__)
        # location of appJar
        self.lib_path = os.path.dirname(self.lib_file)
        self.resource_path = os.path.join(self.lib_path, "resources")
        self.icon_path = os.path.join(self.resource_path, "icons")
        self.sound_path = os.path.join(self.resource_path, "sounds")
        self.appJarIcon = os.path.join(self.icon_path, "favicon.ico")

        # user configurable
        self.userImages = self.exe_loc
        self.userSounds = self.exe_loc

        # create the main window - topLevel
        self.topLevel = Tk()
        self.topLevel.bind('<Configure>', self.__windowEvent)
        # override close button
        self.topLevel.protocol("WM_DELETE_WINDOW", self.stop)
        # temporarily hide it
        self.topLevel.withdraw()
        self.locationSet = False

        # create a frame to store all the widgets
        self.appWindow = Frame(self.topLevel)
        self.appWindow.pack(fill=BOTH, expand=True)

        # set the windows title
        if title is None:
            title = self.exe_file
        self.setTitle(title)

        # configure the geometry of the window
        self.topLevel.escapeBindId = None  # used to exit fullscreen
        self.topLevel.stopFunction = None  # used to exit fullscreen
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
        self.tbFont = font.Font(family="Helvetica", size=12)
        self.scaleFont = font.Font(family="Helvetica", size=12)
        self.statusFont = font.Font(family="Helvetica", size=12)
        self.spinFont = font.Font(family="Helvetica", size=12)
        self.optionFont = font.Font(family="Helvetica", size=12)
        self.lbFont = font.Font(family="Helvetica", size=12)
        self.taFont = font.Font(family="Helvetica", size=12)
        self.meterFont = font.Font(family="Helvetica", size=12, weight='bold')
        self.linkFont = font.Font(
            family="Helvetica",
            size=12,
            weight='bold',
            underline=1)
        self.labelFrameFont = font.Font(family="Helvetica", size=12)
        self.frameFont = font.Font(family="Helvetica", size=12)
        self.toggleFrameFont = font.Font(family="Helvetica", size=12)
        self.tabbedFrameFont = font.Font(family="Helvetica", size=12)
        self.panedFrameFont = font.Font(family="Helvetica", size=12)
        self.scrollPaneFont = font.Font(family="Helvetica", size=12)
        self.propertiesFont = font.Font(family="Helvetica", size=12)
        self.gridFont = font.Font(family="Helvetica", size=12)

#        self.fgColour = self.topLevel.cget("foreground")
#        self.buttonFgColour = self.topLevel.cget("foreground")
#        self.labelFgColour = self.topLevel.cget("foreground")

        # create a menu bar - only shows if populated
        # now created in menu functions, as it generated a blank line...
        self.hasMenu = False
        self.hasStatus = False
        self.hasTb = False
        self.copyAndPaste = CopyAndPaste(self.topLevel)

        # won't pack, if don't pack it here
        self.tb = Frame(self.appWindow, bd=1, relief=RAISED)
        self.tb.pack(side=TOP, fill=X)

        # create the main container for this GUI
        container = Frame(self.appWindow)
        # container = Label(self.appWindow) # made as a label, so we can set an
        # image
        container.config(padx=2, pady=2, background=self.topLevel.cget("bg"))
        container.pack(fill=BOTH, expand=True)
        self.__addContainer(self.C_ROOT, container, 0, 1)

        # set up the main container to be able to host an image
        self.__configBg(container)

        # an array to hold any threaded events....
        self.events = []
        self.pollTime = 250
        self.built = True
        if self.platform == self.WINDOWS:
            try:
                self.topLevel.wm_iconbitmap(self.appJarIcon)
            except: # file not found
                self.debug("Error setting Windows default icon")

    def __configBg(self, container):
        # set up a background image holder
        # alternative to label option above, as label doesn't update widgets
        # properly
        self.bgLabel = Label(container)
        self.bgLabel.config(
            anchor=CENTER,
            font=self.labelFont,
            background=self.__getContainerBg())
        self.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        container.image = None

#####################################
# set the arrays we use to store everything
#####################################
    def __initArrays(self):
        # set up a row counter - used to auto add rows
        # breaks once user sets own row

        # set up a minimum label width for label combos
        self.labWidth = 1

        # validate function callbacks - used by numeric texts
        # created first time a widget is used
        self.validateNumeric = None
        self.validateSpinBox = None

        # set up flash variable
        self.doFlash = False

        # used to hide/show title bar
        self.hasTitleBar = True
        # records if we're in fullscreen - stops hideTitle from breaking
        self.isFullscreen = False

        # splash screen?
        self.splashConfig = None

        # collections of widgets, widget name is key
        self.n_frames = []  # un-named, so no direct access
        self.n_labels = {}
        self.n_buttons = {}
        self.n_entries = {}
        self.n_messages = {}
        self.n_scales = {}
        self.n_cbs = {}
        self.n_rbs = {}
        self.n_lbs = {}
        self.n_tbButts = {}
        self.n_spins = {}
        self.n_props = {}
        self.n_options = {}
        self.n_frameLabs = {}
        self.n_textAreas = {}
        self.n_links = {}
        self.n_meters = {}
        self.n_subWindows = {}
        self.n_labelFrames = {}
        self.n_ajFrame = {}
        self.n_tabbedFrames = {}
        self.n_panedFrames = {}
        self.n_panes = {}
        self.n_pagedWindows = {}
        self.n_toggleFrames = {}
        self.n_scrollPanes = {}
        self.n_trees = {}
        self.n_flashLabs = []
        self.n_pieCharts = {}
        self.n_separators = []

        # variables associated with widgets
        self.n_entryVars = {}
        self.n_optionVars = {}
        self.n_boxVars = {}
        self.n_rbVars = {}
        self.n_rbVals = {}
        self.n_images = {}        # image label widgets
        self.n_imageCache = {}    # image file objects
        self.n_imageAnimationIds = {} # stores after ids
        self.n_taHashes = {}      # for monitoring textAreas

        # for simple grids
        self.n_grids = {}

        # menu stuff
        self.n_menus = {}
        self.n_menuVars = {}
        self.n_accelerators = []

    def setLanguage(self, language):
        try:
            from configparser import ConfigParser
        except:
            self.warn("Internationalisation not supported")
            self.config = None
            return
        self.config = ConfigParser()
        self.changeLanguage(language)

    # function to update languages
    def changeLanguage(self, language):
        if self.config is None:
            self.warn("Internationalisation not supported")
            return

        language = language.upper()
        import codecs
        if not PYTHON2:
            try:
                with codecs.open(language + ".ini", "r", "utf8") as langFile:
                    self.config.read_file(langFile)
            except FileNotFoundError:
                self.warn("Invalid language: " + language)
                return
        else:
            try:
                with codecs.open(language + ".ini", "r", "utf8") as langFile:
                    self.config.read_file(langFile)
            except IOError:
                self.warn("Invalid language: " + language)
                return

        self.debug("Switching to: " + language)
        # loop through each section, get the relative set of widgets
        # change the text
        for section in self.config.sections():
            section = section.upper()
            # skip the config section (for now)
            if section == "CONFIG":
                continue

            self.debug("\t" + section)

            # convert the section title to its code
            try:
                kind = vars(gui)[section]
                texts = self.config[section]
            except KeyError:
                self.warn("Invalid config section: " + section)
                continue

            # use the code to get the widget list
            widgets = self.__getItems(kind)

            if kind in [self.SCALE]:
                self.warn("No text is displayed in " + section + ". Maybe it has a Label?")
                continue
            elif kind in [self.TEXTAREA, self.METER]:
                self.warn("No text is displayed in " + section)
                continue
            elif kind in [self.PROPERTIES]:
                self.warn(section + " - list-style widgets are currently not supported")
            elif kind in [self.LISTBOX]:
                for k in widgets.keys():
                    lb = widgets[k]
                    # convert data to a list
                    data = texts.get(k, lb.DEFAULT_TEXT).strip().split("\n")
                    # tidy up the list
                    data = [item.strip() for item in data if len(item.strip()) > 0]
                    self.updateListItems(k, data)
            elif kind in [self.SPIN]:
                for k in widgets.keys():
                    sb = widgets[k]
                    # convert data to a list
                    data = texts.get(k, sb.DEFAULT_TEXT).strip().split("\n")
                    # tidy up the list
                    data = [item.strip() for item in data if len(item.strip()) > 0]
                    self.changeSpinBox(k, data)
            elif kind in [self.OPTION]:
                for k in widgets.keys():
                    ob = widgets[k]
                    # convert data to a list
                    data = texts.get(k, ob.DEFAULT_TEXT).strip().split("\n")
                    # tidy up the list
                    data = [item.strip() for item in data if len(item.strip()) > 0]
                    self.changeOptionBox(k, data)
            elif kind in [self.RADIOBUTTON]:
                for (key, val) in self.config.items(section):
                    keys = key.split("-")

                    try:
                        rbs = self.n_rbs[keys[0]]
                    except KeyError:
                        self.warn("Invalid RADIOBUTTON key: " + keys[0])
                        continue
                    for rb in rbs:
                        if rb.DEFAULT_TEXT == keys[1]:
                            rb["text"] = val
                            break
            elif kind in [self.PIECHART, self.GRID]:
                self.warn(section + " - widgets not yet implemented")
                continue
            elif kind == self.ENTRY:
                for k in widgets.keys():
                    ent = widgets[k]
                    self.updateDefaultText(k, texts.get(k, ent.DEFAULT_TEXT))
                    self.debug("\t\t" + k + "=" + ent.default)
            elif kind in [self.LABEL, self.BUTTON, self.CHECKBOX, self.MESSAGE, self.LINK]:
                # relabel each widget
                for k in widgets.keys():
                    widg = widgets[k]
                    self.debug("\t\t" + k + "---->" +  texts.get(k, widg.DEFAULT_TEXT))
                    widg.config(text = texts.get(k, widg.DEFAULT_TEXT))
                    self.debug("\t\t" + k + "=" + widg.cget("text"))
            else:
                self.warn("Unsupported widget: " + section)
                continue
                

    # function to generate warning messages
    def warn(self, message):
        if self.WARN:
            print("Warning -", message)

    # function to turn off warning messages
    def disableWarnings(self):
        self.WARN = False


    def enableWarnings(self):
        self.WARN = True


    # function to generate warning messages
    def debug(self, message):
        if self.DEBUG:
            print("Debug -", message)

    # function to turn on debug messages
    def enableDebug(self):
        self.DEBUG = True


    def disableDebug(self):
        self.DEBUG = False

    # function to turn on the splash screen
    def showSplash(self, text="appJar", fill="red", stripe="black", fg="white", font=44):
            self.splashConfig= {'text':text, 'fill':fill, 'stripe':stripe, 'fg':fg, 'font':font}

#####################################
# Event Loop - must always be called at end
#####################################
    def go(self, language=None):
        """ Most important function! Start the GUI """

        if self.splashConfig is not None:
            splash = SplashScreen(
                            self.topLevel,
                            self.splashConfig['text'],
                            self.splashConfig['fill'],
                            self.splashConfig['stripe'],
                            self.splashConfig['fg'],
                            self.splashConfig['font']
                            )
            self.topLevel.withdraw()
            self.__bringToFront(splash)

        # if language is populated, we are in internationalisation mode
        # call the setLanguage function - to re-badge all the widgets
        if language is not None:
            self.setLanguage(language)

        # check the containers have all been stopped
        if len(self.containerStack) > 1:
            self.warn("You didn't stop all containers")
            for i in range(len(self.containerStack) - 1, 0, -1):
                kind = self.containerStack[i]['type']
                if kind not in [self.C_PANE]:
                    self.warn("STOP: " + kind)

        if len(self.n_trees) > 0:
            for k in self.n_trees:
                self.n_trees[k].update()
                self.n_trees[k].expand()

        # create appJar menu, if no menuBar created
        if not self.hasMenu:
            self.addAppJarMenu()
        if self.platform == self.WINDOWS:
            self.menuBar.add_cascade(menu=self.n_menus["WIN_SYS"])
        self.topLevel.config(menu=self.menuBar)

        # pack it all in & make sure it's drawn
        self.appWindow.pack(fill=BOTH)
        self.topLevel.update_idletasks()

        # check geom is set and set a minimum size, also positions the window
        # if necessary
        self.__dimensionWindow()

        if self.splashConfig is not None:
            time.sleep(3)
            splash.destroy()

        # bring to front
        self.__bringToFront()
        self.topLevel.deiconify()

        # required to make the gui reopen after minimising
        if self.GET_PLATFORM() == self.MAC:
            self.topLevel.createcommand(
                'tk::mac::ReopenApplication',
                self.topLevel.deiconify)

        # start the call back & flash loops
        self.__poll()
        self.__flash()

        # start the main loop
        try:
            self.topLevel.mainloop()
        except(KeyboardInterrupt, SystemExit):
            self.stop()

    def setStopFunction(self, function):
        """ set a function to call when the GUI is quit. Must return True or False """
        tl = self.__getTopLevel()
        tl.stopFunction = function
        # link to exit item in topMenu
        # only if in root
        if self.containerStack[-1]['type'] != self.C_SUBWINDOW:
            tl.createcommand('exit', self.stop)

    def stop(self, event=None):
        """ Closes the GUI. If a stop function is set, will only close the GUI if True """
        theFunc = self.__getTopLevel().stopFunction
        if theFunc is None or theFunc():
            # stop the after loops
            self.topLevel.after_cancel(self.pollId)
            self.topLevel.after_cancel(self.flashId)
            self.topLevel.after_cancel(self.preloadAnimatedImageId)

            # stop any animations
            for key in self.n_imageAnimationIds:
                self.topLevel.after_cancel(self.n_imageAnimationIds[key])

            # stop any sounds, ignore error when not on Windows
            try:
                self.stopSound()
            except:
                pass
            self.topLevel.quit()
            self.topLevel.destroy()

#####################################
# Functions for configuring polling events
#####################################
    # events will fire in order of being added, after sleeping for time
    def setPollTime(self, time):
        """ Set a frequency for executing queued functions """
        self.pollTime = time

    # register events to be called by the sleep timer
    def registerEvent(self, func):
        """ Queue a function, to be executed every poll time """
        self.events.append(func)

    # internal function, called by 'after' function, after sleeping
    def __poll(self):
        # run any registered actions
        for e in self.events:
            # execute the event
            e()
        self.pollId = self.topLevel.after(self.pollTime, self.__poll)

    # not used now, but called every time window is resized
    # may be used in the future...
    def __windowEvent(self, event):
        new_width = self.topLevel.winfo_width()
        new_height = self.topLevel.winfo_height()
        self.debug("Window resized: " + str(new_width) + "x" + str(new_height))

    # will call the specified function when enter key is pressed
    def enableEnter(self, func):
        """ Binds <Return> to the specified function - all widgets """
        self.bindKey("<Return>", func)

    def disableEnter(self):
        """ unbinds <enter> from all widgets """
        self.unbindKey("<Return>")

    def bindKey(self, key, func):
        """ bind the specified key, to the specified function, for all widgets """
        # for now discard the Event...
        myF = self.MAKE_FUNC(func, key, True)
        self.__getTopLevel().bind(key, myF)

    def unbindKey(self, key):
        """ unbinds the specified key from whatever functions it os bound to """
        self.__getTopLevel().unbind(key)

    # helper - will see if the mouse is in the specified widget
    def __isMouseInWidget(self, w):
        l_x = w.winfo_rootx()
        l_y = w.winfo_rooty()

        if l_x <= w.winfo_pointerx() <= l_x + \
                w.winfo_width() and l_y <= w.winfo_pointery() <= l_y + w.winfo_height():
            return True
        else:
            return False

    # function to give a clicked widget the keyboard focus
    def __grabFocus(self, e): e.widget.focus_set()

#####################################
# FUNCTIONS for configuring GUI settings
#####################################
    # set a minimum size
    def __dimensionWindow(self):
        self.topLevel.update_idletasks()
        if self.__getTopLevel().geom != "fullscreen":
            # ISSUES HERE:
            # on MAC & LINUX, w_width/w_height always 1
            # on WIN, w_height is bigger then r_height - leaving empty space

            # get the apps requested width & height
            r_width = self.__getTopLevel().winfo_reqwidth()
            r_height = self.__getTopLevel().winfo_reqheight()

            # get the current width & height
            w_width = self.__getTopLevel().winfo_width()
            w_height = self.__getTopLevel().winfo_height()

            # get the window's width & height
            m_width = self.topLevel.winfo_screenwidth()
            m_height = self.topLevel.winfo_screenheight()

            # determine best geom for OS
            if self.platform in [self.MAC, self.LINUX]:
                b_width = r_width
                b_height = r_height
            elif self.platform == self.WINDOWS:
                b_height = min(r_height, w_height)
                b_width = min(r_width, w_width)
                h_height = max(r_height, w_height)
                h_width = max(r_width, w_width)

            # if a geom has not ben set
            if self.__getTopLevel().geom is None:
                width = b_width
                height = b_height
                # store it in the app's geom
                self.__getTopLevel().geom = str(width) + "x" + str(height)
            else:
                # now split the app's geom
                width = int(self.__getTopLevel().geom.lower().split("x")[0])
                height = int(self.__getTopLevel().geom.lower().split("x")[1])
                # warn the user that their geom is not big enough
                if width < b_width or height < b_height:
                    self.warn(
                        "Specified dimensions (" +
                        self.__getTopLevel().geom +
                        "), less than requested dimensions (" +
                        str(b_width) +
                        "x" +
                        str(b_height) +
                        ")")

            # and set it as the minimum size
            self.__getTopLevel().minsize(width, height)

            # if the window hasn't been positioned by the user, put it in the
            # middle
            if not self.locationSet:
                if self.platform == self.WINDOWS:
                    x = (m_width - h_width) / 2
                    y = (m_height - h_height) / 2
                elif self.platform in [self.MAC, self.LINUX]:
                    x = (m_width - width) / 2
                    y = (m_height - height) / 2

                self.setLocation(x, y)

    # called to update screen geometry
    def setGeometry(self, geom, height=None):
        self.setGeom(geom, height)

    def setGeom(self, geom, height=None):
        if height is not None:
            geom = str(geom) + "x" + str(height)
        container = self.__getTopLevel()
        container.geom = geom
        if container.geom == "fullscreen":
            self.setFullscreen()
        else:
            self.exitFullscreen()
            if container.geom is not None:
                container.geometry(container.geom)

    # called to set screen position
    def setLocation(self, x, y):
        # get the window's width & height
        m_width = self.topLevel.winfo_screenwidth()
        m_height = self.topLevel.winfo_screenheight()

        if x < 0 or x > m_width or y < 0 or y > m_height:
            self.warn(
                "Invalid location: " +
                str(x) +
                ", " +
                str(y) +
                " - ignoring")
            return

        if self.containerStack[-1]['type'] != self.C_SUBWINDOW:
            self.locationSet = True

        self.__getTopLevel().geometry("+%d+%d" % (x, y))

    # called to make sure this window is on top
    def __bringToFront(self, win=None):
        if win is None: win = self.topLevel
        if self.platform == self.MAC:
            import subprocess
            tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
            script = tmpl.format(os.getpid())
            output = subprocess.check_call(
                ['/usr/bin/osascript', '-e', script])
            win.after(
                0, lambda: win.attributes(
                    "-topmost", False))
#            val=os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "''' + PY_NAME + '''" to true' ''')
            win.lift()
        elif self.platform == self.WINDOWS:
            win.lift()
        elif self.platform == self.LINUX:
            win.lift()

    def setFullscreen(self, container=None):
        if not self.isFullscreen:
            self.isFullscreen = True
            if container is None:
                container = self.__getTopLevel()
            container.attributes('-fullscreen', True)
            container.escapeBindId = container.bind(
                '<Escape>', self.MAKE_FUNC(
                    self.exitFullscreen, container, True), "+")

    # function to turn off fullscreen mode
    def exitFullscreen(self, container=None):
        if self.isFullscreen:
            self.isFullscreen = False
            if container is None:
                container = self.__getTopLevel()
            container.attributes('-fullscreen', False)
            if container.escapeBindId is not None:
                container.unbind('<Escape>', container.escapeBindId)
            myWarn = self.__pauseWarn()
            self.__doTitleBar()
            self.__resumeWarn(myWarn)
            return True
        else:
            return False

    def __pauseWarn(self):
        myWarn = self.WARN
        self.WARN = False
        return myWarn

    def __resumeWarn(self, myWarn):
        self.WARN = myWarn

    # set the current container's external grid padding
    def setPadX(self, x=0): self.containerStack[-1]['padx'] = x

    def setPadY(self, y=0): self.containerStack[-1]['pady'] = y

    # sets the padding around the border of the root container
    def setPadding(self, x, y=None):
        if y is None:
            if isinstance(x, list):
                self.containerStack[-1]['padx'] = x[0]
                self.containerStack[-1]['pady'] = x[1]
        else:
            self.containerStack[-1]['padx'] = x
            self.containerStack[-1]['pady'] = y

    def setGuiPadding(self, x, y=None):
        if y is None:
            if isinstance(x, list):
                self.containerStack[0]['container'].config(padx=x[0], pady=x[1])
        else:
            self.containerStack[0]['container'].config(padx=x, pady=y)

    # sets the current containers internal padding
    def setIPadX(self, x=0): self.setInPadX(x)

    def setIPadY(self, y=0): self.setInPadY(y)

    def setIPadding(self, x, y=None): self.setInPadding(x, y)

    def setInPadX(self, x=0): self.containerStack[-1]['ipadx'] = x

    def setInPadY(self, y=0): self.containerStack[-1]['ipady'] = y

    def setInPadding(self, x, y=None):
        if y is None:
            if isinstance(x, list):
                self.containerStack[-1]['ipadx'] = x[0]
                self.containerStack[-1]['ipady'] = x[1]
        else:
            self.containerStack[-1]['ipadx'] = x
            self.containerStack[-1]['ipady'] = y


    # set an override sticky for this container
    def setSticky(self, sticky):
        self.containerStack[-1]['sticky'] = sticky

    # this tells widgets what to do when GUI is resized
    def setStretch(self, exp): self.setExpand(exp)

    def setExpand(self, exp):
        if exp.lower() == "none":
            self.containerStack[-1]['expand'] = "NONE"
        elif exp.lower() == "row":
            self.containerStack[-1]['expand'] = "ROW"
        elif exp.lower() == "column":
            self.containerStack[-1]['expand'] = "COLUMN"
        else:
            self.containerStack[-1]['expand'] = "ALL"

    def getFonts(self): return list(font.families()).sort()

    def increaseButtonFont(self): self.setButtonFont(
        self.buttonFont['size'] + 1)

    def decreaseButtonFont(self): self.setButtonFont(
        self.buttonFont['size'] - 1)

    def setButtonFont(self, size, font=None):
        if font is None:
            font = self.buttonFont['family']
        self.buttonFont.config(family=font, size=size)

    def increaseLabelFont(self): self.setLabelFont(self.labelFont['size'] + 1)

    def decreaseLabelFont(self): self.setLabelFont(self.labelFont['size'] - 1)

    def setLabelFont(self, size, font=None):
        if font is None:
            font = self.labelFont['family']
        self.labelFont.config(family=font, size=size)
        self.entryFont.config(family=font, size=size)
        self.rbFont.config(family=font, size=size)
        self.cbFont.config(family=font, size=size)
        self.scaleFont.config(family=font, size=size)
        self.messageFont.config(family=font, size=size)
        self.spinFont.config(family=font, size=size)
        self.optionFont.config(family=font, size=size)
        self.lbFont.config(family=font, size=size)
        self.taFont.config(family=font, size=size)
        self.linkFont.config(family=font, size=size)
        self.meterFont.config(family=font, size=size)
        self.propertiesFont.config(family=font, size=size)
        self.labelFrameFont.config(family=font, size=size)
        self.frameFont.config(family=font, size=size)
        self.toggleFrameFont.config(family=font, size=size)
        self.tabbedFrameFont.config(family=font, size=size)
        self.panedFrameFont.config(family=font, size=size)
        self.scrollPaneFont.config(family=font, size=size)
        self.gridFont.config(family=font, size=size)

        # need tbetter way to register font change events on grids
        for grid in self.n_grids:
            self.n_grids[grid].config(font=self.gridFont)

    def increaseFont(self):
        self.increaseLabelFont()
        self.increaseButtonFont()

    def decreaseFont(self):
        self.decreaseLabelFont()
        self.decreaseButtonFont()

    def setFont(self, size, font=None):
        self.setLabelFont(size, font)
        self.setButtonFont(size, font)

    # need to set a default colour for container
    # then populate that field
    # then use & update that field accordingly
    # all widgets will then need to use it
    # and here we update all....
    def setFg(self, colour):
        self.SET_WIDGET_FG(self.containerStack[-1]['container'], colour, True)

    # self.topLevel = Tk()
    # self.appWindow = Frame, fills all of self.topLevel
    # self.tb = Frame, at top of appWindow
    # self.container = Frame, at bottom of appWindow => C_ROOT container
    # self.bglabel = Label, filling all of container
    def setBg(self, colour):
        if self.containerStack[-1]['type'] == self.C_ROOT:
            self.appWindow.config(background=colour)
            self.bgLabel.config(background=colour)

        self.containerStack[-1]['container'].config(background=colour)

        for child in self.containerStack[-1]['container'].winfo_children():
            if not self.__isWidgetContainer(child):
                gui.SET_WIDGET_BG(child, colour)

    def __isWidgetContainer(self, widget):
        try:
            if widget.isContainer:
                return True
        except:
            pass
        return False

    def setResizable(self, canResize=True):
        self.__getTopLevel().isResizable = canResize
        if self.__getTopLevel().isResizable:
            self.__getTopLevel().resizable(True, True)
        else:
            self.__getTopLevel().resizable(False, False)

    def getResizable(self):
        return self.__getTopLevel().isResizable

    def __doTitleBar(self):
        if self.platform == self.MAC:
            self.warn(
                "Title bar hiding doesn't work on MAC - app may become unresponsive.")
        elif self.platform == self.LINUX:
            self.warn(
                "Title bar hiding doesn't work on LINUX - app may become unresponsive.")
        self.__getTopLevel().overrideredirect(not self.hasTitleBar)

    def hideTitleBar(self):
        self.hasTitleBar = False
        self.__doTitleBar()

    def showTitleBar(self):
        self.hasTitleBar = True
        self.__doTitleBar()

    # function to set the window's title
    def setTitle(self, title):
        self.__getTopLevel().title(title)

    # set an icon
    def setIcon(self, image):
        container = self.__getTopLevel()
        if image.endswith('.ico'):
            container.wm_iconbitmap(image)
        else:
            icon = self.__getImage(image)
            container.iconphoto(True, icon)

    def __getTopLevel(self):
        if len(
                self.containerStack) > 1 and self.containerStack[-1]['type'] == self.C_SUBWINDOW:
            return self.containerStack[-1]['container']
        else:
            return self.topLevel

    # make the window transparent (between 0 & 1)
    def setTransparency(self, percentage):
        if self.platform == self.LINUX:
            self.warn("Transparency not supported on LINUX")
        else:
            if percentage > 1:
                percentage = percentage / 100
            self.__getTopLevel().attributes("-alpha", percentage)

##############################
# functions to deal with tabbing and right clicking
##############################
    def __focusNextWindow(self, event):
        event.widget.tk_focusNext().focus_set()
        nowFocus = self.topLevel.focus_get()
        if isinstance(nowFocus, Entry):
            nowFocus.select_range(0, END)
        return("break")

    def __focusLastWindow(self, event):
        event.widget.tk_focusPrev().focus_set()
        nowFocus = self.topLevel.focus_get()
        if isinstance(nowFocus, Entry):
            nowFocus.select_range(0, END)
        return("break")

    # creates relevant bindings on the widget
    def __addRightClickMenu(self, widget):
        widget.bind("<FocusIn>", self.__checkCopyAndPaste, add="+")
        widget.bind("<FocusOut>", self.__checkCopyAndPaste, add="+")

        if widget.var is None:  # TEXT:
            widget.bind('<KeyRelease>', self.__checkCopyAndPaste)
            widget.bind('<<Paste>>', self.__checkCopyAndPaste)

        else:
            widget.var.trace(
                "w",
                lambda name,
                index,
                mode,
                e=None,
                w=widget: self.__checkCopyAndPaste(
                    e,
                    w))  # ENTRY/OPTION

        if self.platform in [self.WINDOWS, self.LINUX]:
            widget.bind('<Button-3>', self.__rightClick)
        else:
            widget.bind('<Button-2>', self.__rightClick)

    def __rightClick(self, event, menu="EDIT"):
        event.widget.focus()
        if menu == "EDIT":
            if self.__checkCopyAndPaste(event):
                self.n_menus[menu].tk_popup(
                    event.x_root - 10, event.y_root - 10)
        else:
            self.n_menus[menu].tk_popup(event.x_root - 10, event.y_root - 10)
        return "break"

#####################################
# FUNCTION to configure widgets
#####################################
    def __getItems(self, kind):
        if kind == self.LABEL:
            return self.n_labels
        elif kind == self.MESSAGE:
            return self.n_messages
        elif kind == self.BUTTON:
            return self.n_buttons
        elif kind == self.ENTRY:
            return self.n_entries
        elif kind == self.SCALE:
            return self.n_scales
        elif kind in [self.CB, self.CHECKBOX]:
            return self.n_cbs
        elif kind in [self.RB, self.RADIOBUTTON]:
            return self.n_rbs
        elif kind in [self.LB, self.LISTBOX]:
            return self.n_lbs
        elif kind == self.SPIN:
            return self.n_spins
        elif kind == self.OPTION:
            return self.n_options
        elif kind == self.TEXTAREA:
            return self.n_textAreas
        elif kind == self.LINK:
            return self.n_links
        elif kind == self.METER:
            return self.n_meters
        elif kind == self.IMAGE:
            return self.n_images
        elif kind == self.PIECHART:
            return self.n_pieCharts
        elif kind == self.PROPERTIES:
            return self.n_props
        elif kind == self.GRID:
            return self.n_grids
        elif kind == self.LABELFRAME:
            return self.n_labelFrames
        elif kind == self.FRAME:
            return self.n_ajFrame
        elif kind == self.TABBEDFRAME:
            return self.n_tabbedFrames
        elif kind == self.PANEDFRAME:
            return self.n_panedFrames
        elif kind == self.PANE:
            return self.n_panes
        elif kind == self.SCROLLPANE:
            return self.n_scrollPanes
        elif kind == self.PAGEDWINDOW:
            return self.n_pagedWindows
        elif kind == self.TOGGLEFRAME:
            return self.n_toggleFrames
        else:
            raise Exception("Unknown widget type: " + str(kind))

    def configureAllWidgets(self, kind, option, value):
        items = list(self.__getItems(kind))
        self.configureWidgets(kind, items, option, value)

    def configureWidgets(self, kind, names, option, value):
        if not isinstance(names, list):
            self.configureWidget(kind, names, option, value)
        else:
            for widg in names:
                # incase 2D array, eg. buttons
                if isinstance(widg, list):
                    for widg2 in widg:
                        self.configureWidget(kind, widg2, option, value)
                else:
                    self.configureWidget(kind, widg, option, value)

    def getWidget(self, kind, name):
        # get the list of items for this type, and validate the widget is in
        # the list
        items = self.__getItems(kind)
        return self.__verifyItem(items, name, False)

    def configureWidget(
            self,
            kind,
            name,
            option,
            value,
            key=None,
            deprecated=False):
        # warn about deprecated functions
        if deprecated:
            self.warn(
                "Deprecated config function (" +
                option +
                ") used for: " +
                self.WIDGETS[kind] +
                "->" +
                name +
                " use " +
                deprecated +
                " instead")
        if kind in [self.RB, self.LB, self.CB]:
            self.warn(
                "Deprecated config function (" +
                option +
                ") used for: " +
                self.WIDGETS[kind] +
                "->" +
                name +
                " use " +
                self.WIDGETS[
                    kind /
                    10] +
                " instead")
        # get the list of items for this type, and validate the widgetis in the
        # list
        items = self.__getItems(kind)
        self.__verifyItem(items, name)

        if kind in [self.RB, self.RADIOBUTTON]:
            items = items[name]
        else:
            items = [items[name]]

        # loop through each item, and try to reconfigure it
        # this will often fail - widgets have varied config options
        for item in items:
            try:
                if option == 'background':
                    if kind == self.METER:
                        item.config(backfill=value)
                    else:
                        gui.SET_WIDGET_BG(item, value, True)
                elif option == 'foreground':
                    if kind == self.ENTRY:
                        if item.showingDefault:
                            item.oldFg = value
                        else:
                            item.config(foreground=value)
                            item.oldFg = value
                    else:
                        item.config(foreground=value)
                elif option == 'disabledforeground':
                    item.config(disabledforeground=value)
                elif option == 'disabledbackground':
                    item.config(disabledbackground=value)
                elif option == 'activeforeground':
                    item.config(activeforeground=value)
                elif option == 'activebackground':
                    item.config(activebackground=value)
                elif option == 'inactiveforeground':
                    if kind == self.TABBEDFRAME:
                        item.config(inactiveforeground=value)
                    else:
                        self.warn("Error configuring " + name +
                                  ": can't set inactiveforeground")
                elif option == 'inactivebackground':
                    if kind == self.TABBEDFRAME:
                        item.config(inactivebackground=value)
                    else:
                        self.warn("Error configuring " + name +
                                  ": can't set inactivebackground")
                elif option == 'width':
                    item.config(width=value)
                elif option == 'height':
                    item.config(height=value)
                elif option == 'state':
                    item.config(state=value)
                elif option == 'relief':
                    item.config(relief=value)
                elif option == 'align':
                    if kind == self.ENTRY:
                        if value == W or value == LEFT:
                            value = LEFT
                        elif value == E or value == RIGHT:
                            value = RIGHT
                        item.config(justify=value)
                    else:
                        if value == LEFT:
                            value = "w"
                        elif value == RIGHT:
                            value = "e"
                        item.config(anchor=value)
                elif option == 'anchor':
                    item.config(anchor=value)
                elif option == 'cursor':
                    item.config(cursor=value)
                elif option == 'tooltip':
                    self.__addTooltip(item, value)
                elif option == "focus":
                    item.focus_set()
                elif option == 'over':
                    if not isinstance(value, list):
                        value = [value]
                    if len(value) == 1:
                        value.append(None)
                    if len(value) != 2:
                        raise Exception(
                            "Invalid arguments, set<widget>OverFunction requires 1 ot 2 functions to be passed in.")
                    if kind == self.LABEL:
                        if value[0] is not None:
                            item.bind(
                                "<Enter>", self.MAKE_FUNC(
                                    value[0], name, True), add="+")
                        if value[1] is not None:
                            item.bind(
                                "<Leave>", self.MAKE_FUNC(
                                    value[1], name, True), add="+")
                        #item.bind("<B1-Motion>",self.MAKE_FUNC(value[0], name, True), add="+")
                elif option == 'drag':
                    if not isinstance(value, list):
                        value = [value]
                    if len(value) == 1:
                        value.append(None)
                    if len(value) != 2:
                        raise Exception(
                            "Invalid arguments, set<widget>DragFunction requires 1 ot 2 functions to be passed in.")
                    if kind == self.LABEL:
                        item.config(cursor="fleur")

                        def getLabel(f):
                            # loop through all labels
                            for key, value in self.n_labels.items():
                                if self.__isMouseInWidget(value):
                                    f(key)
                                    return

                        if value[0] is not None:
                            item.bind(
                                "<ButtonPress-1>",
                                self.MAKE_FUNC(
                                    value[0],
                                    name,
                                    True),
                                add="+")
                        if value[1] is not None:
                            item.bind(
                                "<ButtonRelease-1>",
                                self.MAKE_FUNC(
                                    getLabel,
                                    value[1],
                                    True),
                                add="+")
                elif option == 'command':
                    # this will discard the scale value, as default function
                    # can't handle it
                    if kind == self.SCALE:
                        item.config(command=self.MAKE_FUNC(value, name, True))
                    elif kind == self.OPTION:
                        # need to trace the variable??
                        item.var.trace('w', self.MAKE_FUNC(value, name, True))
                    elif kind == self.ENTRY:
                        if key is None:
                            key = name
                        item.bind('<Return>', self.MAKE_FUNC(value, key, True))
                    elif kind == self.BUTTON:
                        item.config(command=self.MAKE_FUNC(value, name))
                        item.bind(
                            '<Return>', self.MAKE_FUNC(
                                value, name, True))
                    # make labels clickable, add a cursor, and change the look
                    elif kind == self.LABEL or kind == self.IMAGE:
                        if self.platform == self.MAC:
                            item.config(cursor="pointinghand")
                        elif self.platform in [self.WINDOWS, self.LINUX]:
                            item.config(cursor="hand2")

                        item.bind(
                            "<Button-1>",
                            self.MAKE_FUNC(
                                value,
                                name,
                                True),
                            add="+")
                        # these look good, but break when dialogs take focus
                        #up = item.cget("relief").lower()
                        # down="sunken"
                        # make it look like it's pressed
                        #item.bind("<Button-1>",lambda e: item.config(relief=down), add="+")
                        #item.bind("<ButtonRelease-1>",lambda e: item.config(relief=up))
                    elif kind == self.LISTBOX:
                        item.bind('<<ListboxSelect>>', self.MAKE_FUNC(value, name, True))
                    else:
                        item.config(command=self.MAKE_FUNC(value, name))
                elif option == 'sticky':
                    info = {}
                    # need to reposition the widget in its grid
                    if self.__widgetHasContainer(kind, item):
                        # pack uses LEFT & RIGHT & BOTH
                        info["side"] = value
                        if value.lower() == "both":
                            info["expand"] = 1
                            info["side"] = "right"
                        else:
                            info["expand"] = 0
                    else:
                        # grid uses E+W
                        if value.lower() == "left":
                            side = W
                        elif value.lower() == "right":
                            side = E
                        elif value.lower() == "both":
                            side = W + E
                        else:
                            side = value.upper()
                        info["sticky"] = side
                    self.__repackWidget(item, info)
                elif option == 'padding':
                    if value[1] is None:
                        item.config(padx=value[0][0], pady=value[0][1])
                    else:
                        item.config(padx=value[0], pady=value[1])
                elif option == 'ipadding':
                    if value[1] is None:
                        item.config(ipadx=value[0][0], ipady=value[0][1])
                    else:
                        item.config(ipadx=value[0], ipady=value[1])
                elif option == 'rightClick':
                    if self.platform in [self.WINDOWS, self.LINUX]:
                        item.bind(
                            '<Button-3>',
                            lambda e,
                            menu=value: self.__rightClick(
                                e,
                                menu))
                    else:
                        item.bind(
                            '<Button-2>',
                            lambda e,
                            menu=value: self.__rightClick(
                                e,
                                menu))
            except TclError as e:
                self.warn("Error configuring " + name + ": " + str(e))

    # dynamic way to create the configuration functions
    def __buildConfigFuncs(self):
        # loop through all the available widgets
        # and make all the below functons for each one
        for k, v in self.WIDGETS.items():
            exec(
                "def set" +
                v +
                "Bg(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'background', val)")
            exec("gui.set" + v + "Bg=set" + v + "Bg")
            exec(
                "def set" +
                v +
                "Fg(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'foreground', val)")
            exec("gui.set" + v + "Fg=set" + v + "Fg")

            exec(
                "def set" +
                v +
                "DisabledFg(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'disabledforeground', val)")
            exec("gui.set" + v + "DisabledFg=set" + v + "DisabledFg")
            exec(
                "def set" +
                v +
                "DisabledBg(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'disabledbackground', val)")
            exec("gui.set" + v + "DisabledBg=set" + v + "DisabledBg")

            exec(
                "def set" +
                v +
                "ActiveFg(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'activeforeground', val)")
            exec("gui.set" + v + "ActiveFg=set" + v + "ActiveFg")
            exec(
                "def set" +
                v +
                "ActiveBg(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'activebackground', val)")
            exec("gui.set" + v + "ActiveBg=set" + v + "ActiveBg")

            exec(
                "def set" +
                v +
                "InactiveFg(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'inactiveforeground', val)")
            exec("gui.set" + v + "InactiveFg=set" + v + "InactiveFg")
            exec(
                "def set" +
                v +
                "InactiveBg(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'inactivebackground', val)")
            exec("gui.set" + v + "InactiveBg=set" + v + "InactiveBg")

            exec(
                "def set" +
                v +
                "Width(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'width', val)")
            exec("gui.set" + v + "Width=set" + v + "Width")
            exec(
                "def set" +
                v +
                "Height(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'height', val)")
            exec("gui.set" + v + "Height=set" + v + "Height")
            exec(
                "def set" +
                v +
                "State(self, name, val): self.configureWidgets(" +
                str(k) +
                ", name, 'state', val)")
            exec("gui.set" + v + "State=set" + v + "State")
            exec(
                "def set" +
                v +
                "Padding(self, name, x, y=None): self.configureWidgets(" +
                str(k) +
                ", name, 'padding', [x, y])")
            exec("gui.set" + v + "Padding=set" + v + "Padding")

            exec(
                "def set" +
                v +
                "IPadding(self, name, x, y=None): self.configureWidgets(" +
                str(k) +
                ", name, 'ipadding', [x, y])")
            exec("gui.set" + v + "IPadding=set" + v + "IPadding")

            exec(
                "def set" +
                v +
                "InPadding(self, name, x, y=None): self.configureWidgets(" +
                str(k) +
                ", name, 'ipadding', [x, y])")
            exec("gui.set" + v + "InPadding=set" + v + "InPadding")

            # might not all be necessary, could make exclusion list
            exec(
                "def set" +
                v +
                "Relief(self, name, val): self.configureWidget(" +
                str(k) +
                ", name, 'relief', val)")
            exec("gui.set" + v + "Relief=set" + v + "Relief")
            exec(
                "def set" +
                v +
                "Align(self, name, val): self.configureWidget(" +
                str(k) +
                ", name, 'align', val)")
            exec("gui.set" + v + "Align=set" + v + "Align")
            exec(
                "def set" +
                v +
                "Anchor(self, name, val): self.configureWidget(" +
                str(k) +
                ", name, 'anchor', val)")
            exec("gui.set" + v + "Anchor=set" + v + "Anchor")
            exec(
                "def set" +
                v +
                "Tooltip(self, name, val): self.configureWidget(" +
                str(k) +
                ", name, 'tooltip', val)")
            exec("gui.set" + v + "Tooltip=set" + v + "Tooltip")
            exec(
                "def set" +
                v +
                "Function(self, name, val, key=None): self.configureWidget(" +
                str(k) +
                ", name, 'command', val, key)")
            exec("gui.set" + v + "Function=set" + v + "Function")
            exec(
                "def set" +
                v +
                "DragFunction(self, name, val): self.configureWidget(" +
                str(k) +
                ", name, 'drag', val)")
            exec("gui.set" + v + "DragFunction=set" + v + "DragFunction")
            exec(
                "def set" +
                v +
                "OverFunction(self, name, val): self.configureWidget(" +
                str(k) +
                ", name, 'over', val)")
            exec("gui.set" + v + "OverFunction=set" + v + "OverFunction")
# deprecated, but left in for backwards compatability
            exec(
                "def set" +
                v +
                "Command(self, name, val, key=None): self.configureWidget(" +
                str(k) +
                ", name, 'command', val, key, deprecated='Function')")
            exec("gui.set" + v + "Command=set" + v + "Command")
            exec(
                "def set" +
                v +
                "Func(self, name, val, key=None): self.configureWidget(" +
                str(k) +
                ", name, 'command', val, key, deprecated='Function')")
            exec("gui.set" + v + "Func=set" + v + "Func")
# end deprecated
            # http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/cursors.html
            exec(
                "def set" +
                v +
                "Cursor(self, name, val): self.configureWidget(" +
                str(k) +
                ", name, 'cursor', val)")
            exec("gui.set" + v + "Cursor=set" + v + "Cursor")
            exec(
                "def set" +
                v +
                "Focus(self, name): self.configureWidget(" +
                str(k) +
                ", name, 'focus', None)")
            exec("gui.set" + v + "Focus=set" + v + "Focus")

            # change the stickyness
            exec(
                "def set" +
                v +
                "Sticky(self, name, pos): self.configureWidget(" +
                str(k) +
                ", name, 'sticky', pos)")
            exec("gui.set" + v + "Sticky=set" + v + "Sticky")

            # add right click
            exec(
                "def set" +
                v +
                "RightClick(self, name, menu): self.configureWidget(" +
                str(k) +
                ", name, 'rightClick', menu)")
            exec("gui.set" + v + "RightClick=set" + v + "RightClick")

            # functions to manage widgets
            exec(
                "def show" +
                v +
                "(self, name): self.showWidget(" +
                str(k) +
                ", name)")
            exec("gui.show" + v + "=show" + v)
            exec(
                "def hide" +
                v +
                "(self, name): self.hideWidget(" +
                str(k) +
                ", name)")
            exec("gui.hide" + v + "=hide" + v)
            exec(
                "def remove" +
                v +
                "(self, name): self.removeWidget(" +
                str(k) +
                ", name)")
            exec("gui.remove" + v + "=remove" + v)

            # convenience functions for enable/disable
            # might not all be necessary, could make exclusion list
            exec(
                "def enable" +
                v +
                "(self, name): self.configureWidget(" +
                str(k) +
                ", name, 'state', 'normal')")
            exec("gui.enable" + v + "=enable" + v)
            exec(
                "def disable" +
                v +
                "(self, name): self.configureWidget(" +
                str(k) +
                ", name, 'state', 'disabled')")
            exec("gui.disable" + v + "=disable" + v)

            # group functions
            exec(
                "def set" +
                v +
                "Widths(self, names, val): self.configureWidgets(" +
                str(k) +
                ", names, 'width', val)")
            exec("gui.set" + v + "Widths=set" + v + "Widths")
            exec(
                "def setAll" +
                v +
                "Widths(self, val): self.configureAllWidgets(" +
                str(k) +
                ", 'width', val)")
            exec("gui.setAll" + v + "Widths=setAll" + v + "Widths")

            exec(
                "def set" +
                v +
                "Heights(self, names, val): self.configureWidgets(" +
                str(k) +
                ", names, 'height', val)")
            exec("gui.set" + v + "Heights=set" + v + "Heights")
            exec(
                "def setAll" +
                v +
                "Heights(self, val): self.configureAllWidgets(" +
                str(k) +
                ", 'height', val)")
            exec("gui.setAll" + v + "Heights=setAll" + v + "Heights")

            exec(
                "def get" +
                v +
                "Widget(self, name): return self.getWidget(" +
                str(k) +
                ", name)")
            exec("gui.get" + v + "Widget=get" + v + "Widget")

#####################################
#  FUNCTION to hide/show/remove widgets
#####################################
    def __widgetHasContainer(self, kind, item):
        if kind in [
                self.SCALE,
                self.ENTRY,
                self.SPIN,
                self.OPTION,
                self.LABEL] and item.inContainer:
            return True
        else:
            return False

    def hideWidget(self, kind, name):
        # get the dictionary of items, and find the item in it
        items = self.__getItems(kind)
        item = self.__verifyItem(items, name)

        if self.__widgetHasContainer(kind, item):
            widget = item.master
            self.n_frameLabs[name].hidden = True
        else:
            if kind in [self.RB, self.RADIOBUTTON]:
                for rb in item:
                    if rb.text == name:
                        widget = rb
            widget = item

        if "in" in widget.grid_info():
            widget.grid_remove()
#                  self.__updateLabelBoxes(name)

    def showWidget(self, kind, name):
        # get the dictionary of items, and find the item in it
        items = self.__getItems(kind)
        item = self.__verifyItem(items, name)

        if self.__widgetHasContainer(kind, item):
            widget = item.master
            self.n_frameLabs[name].hidden = False
        else:
            widget = item

        # only show the widget, if it's not already showing
        if "in" not in widget.grid_info():
            widget.grid()
#                  self.__updateLabelBoxes(name)

    def removeWidget(self, kind, name):
        # get the dictionary of items, and find the item in it
        items = self.__getItems(kind)
        item = self.__verifyItem(items, name)

        # if it's a flasher, remove it
        if item in self.n_flashLabs:
            self.n_flashLabs.remove(item)
            if len(self.n_flashLabs) == 0:
                self.doFlash = False

        # animated images...

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
        for child in self.containerStack[0]['container'].winfo_children():
            child.destroy()
        self.__configBg(self.containerStack[0]['container'])
        self.__initArrays()
        self.setGeom(None)

#####################################
# FUNCTION for managing commands
#####################################
    # funcion to wrap up lambda
    # if the thing calling this generates parameters - then set discard=True
    @staticmethod
    def MAKE_FUNC(funcName, param, discard=False):
        if discard:
            return lambda *args: funcName(param)
        else:
            return lambda: funcName(param)

    def __checkFunc(self, names, funcs):
        singleFunc = None
        if funcs is None:
            return None
        elif callable(funcs):
            singleFunc = funcs
        elif len(names) != len(funcs):
            raise Exception("List sizes don't match")
        return singleFunc

#####################################
# FUNCTION to position a widget
#####################################
    # checks if the item already exists
    def __verifyItem(self, items, item, newItem=False):
        if not newItem and item not in items:
            raise ItemLookupError("Invalid key: " + item + " does not exist")
        elif not newItem and item in items:
            return items[item]
        elif newItem and item in items:
            raise ItemLookupError(
                "Duplicate key: '" + item + "' already exists")

    def getRow(self):
        return self.containerStack[-1]['emptyRow']

    def gr(self): return self.getRow()

    def __repackWidget(self, widget, params):
        if widget.winfo_manager() == "grid":
            ginfo = widget.grid_info()
            ginfo.update(params)
            widget.grid(ginfo)
        elif widget.winfo_manager() == "pack":
            pinfo = widget.pack_info()
            pinfo.update(params)
            widget.pack(pinfo)
        else:
            raise Exception(
                "Unknown geometry manager: " +
                widget.winfo_manager())

    # convenience function to set RCS, referencing the current container's
    # settings
    def __getRCS(self, row, column, colspan, rowspan):
        if row is None:
            row = self.containerStack[-1]['emptyRow']
        self.containerStack[-1]['emptyRow'] = row + 1

        if column >= self.containerStack[-1]['colCount']:
            self.containerStack[-1]['colCount'] = column + 1
        # if column == 0 and colspan == 0 and self.containerStack[-1]['colCount'] > 1:
        #      colspan = self.containerStack[-1]['colCount']

        return row, column, colspan, rowspan

    def SET_WIDGET_FG(self, widget, fg, external=False):

        widgType = widget.__class__.__name__
        isDarwin = gui.GET_PLATFORM() == gui.MAC

        if self.__isWidgetContainer(widget):
            self.containerStack[-1]['fg'] = fg
        elif widgType == "Link" and not external:
            pass
        else:
            try:
                widget.config(foreground=fg)
            except:
                pass  # can't set an FG colour on this widget

    @staticmethod
    def TINT(widget, colour):
        col = []
        for a, b in enumerate(widget.winfo_rgb(colour)):
            t = int(min(max(0, b / 256 + (255 - b / 256) * .3), 255))
            t = str(hex(t))[2:]
            if len(t) == 1:
                t = '0' + t
            elif len(t) == 0:
                t = '00'
            col.append(t)
        return "#" + "".join(col)

    # convenience method to set a widget's bg
    @staticmethod
    def SET_WIDGET_BG(widget, bg, external=False):
        # POTENTIAL ISSUES
        # spinBox - highlightBackground
        # cbs/rbs - activebackground
        # grids - background

        if bg is None:
            return  # ignore empty colours

        # , "Scale"]#, "Button", "OptionMenu"]
        darwinBorders = [
            "Text",
            "ScrolledText",
            "Entry",
            "AutoCompleteEntry",
            "Button"]
        linuxBorders = darwinBorders + ["Radiobutton", "Checkbutton"]
        noBg = [
            "Button",
            "Spinbox",
            "ListBox",
            "SplitMeter",
            "DualMeter",
            "Meter",
            "ToggleFrame",
            "OptionMenu"]  # , "Scale"]

        widgType = widget.__class__.__name__
        isDarwin = gui.GET_PLATFORM() == gui.MAC
        isLinux = gui.GET_PLATFORM() == gui.LINUX

        # always remove the border from scales
        if widgType == "Scale":
            widget.config(highlightbackground=bg)

        # tint the background colour when active...
        if widgType in ["Button", "OptionMenu", "Scale"]:
            widget.config(activebackground=gui.TINT(widget, bg))

        # Mac specific colours
        if widgType in darwinBorders:
            if isDarwin:
                widget.config(highlightbackground=bg)
#               if widgType == "OptionMenu": widget.config(background=bg)
            if external or widgType == "Scale":
                widget.config(bg=bg)

        # Linux specific colours
        if widgType in linuxBorders:
            if isLinux:
                widget.config(highlightbackground=bg)
            if external:
                widget.config(bg=bg)

        # widget with label, in frame
        elif widgType == "LabelBox":
            widget.theLabel.config(bg=bg)
            gui.SET_WIDGET_BG(widget.theWidget, bg)

        # group of buttons or labels
        elif widgType == "WidgetBox":
            widget.config(bg=bg)
            for widg in widget.theWidgets:
                gui.SET_WIDGET_BG(widg, bg)

        elif widgType in ["LabelFrame", "PanedFrame", "Pane", "ajFrame"]:
            widget.config(bg=bg)
            for child in widget.winfo_children():
                gui.SET_WIDGET_BG(child, bg)

        # any other widgets
        elif external:
            if gui.GET_PLATFORM() == gui.MAC:
                if widgType not in ["OptionMenu"]:
                    widget.config(bg=bg)
            else:
                widget.config(bg=bg)
        elif widgType not in noBg:
            widget.config(bg=bg)

    def __getContainerBg(self):
        return self.__getContainer()["bg"]

    def __getContainerFg(self):
        try:
            return self.__getContainer()["fg"]
        except:
            return "black"

    # two important things here:
    # grid - sticky: position of widget in its space (side or fill)
    # row/columns configure - weight: how to grow with GUI
    def __positionWidget(
            self,
            widget,
            row,
            column=0,
            colspan=0,
            rowspan=0,
            sticky=W + E):
        # allow item to be added to container
        container = self.__getContainer()
        gui.SET_WIDGET_BG(widget, self.__getContainerBg())
        self.SET_WIDGET_FG(widget, self.__getContainerFg())

        # alpha paned window placement
        if self.containerStack[-1]['type'] == self.C_PANEDFRAME:
            container.add(widget)
            self.containerStack[-1]['widgets'] = True
            return

        # else, add to grid
        row, column, colspan, rowspan = self.__getRCS(
            row, column, colspan, rowspan)

        # build a dictionary for the named params
        iX = self.containerStack[-1]['ipadx']
        iY = self.containerStack[-1]['ipady']
        cX = self.containerStack[-1]['padx']
        cY = self.containerStack[-1]['pady']
        params = {
            "row": row,
            "column": column,
            "ipadx": iX,
            "ipady": iY,
            "padx": cX,
            "pady": cY}

        # if we have a column span, apply it
        if colspan != 0:
            params["columnspan"] = colspan
        # if we have a rowspan, apply it
        if rowspan != 0:
            params["rowspan"] = rowspan

        # 1) if param has sticky, use that
        # 2) if container has sticky - override
        # 3) else, none
        if self.containerStack[-1]["sticky"] is not None:
            params["sticky"] = self.containerStack[-1]["sticky"]
        elif sticky is not None:
            params["sticky"] = sticky
        else:
            pass

        # make colspanned widgets expand to fill height of cell
        if rowspan != 0:
            if "sticky" in params:
                if "n" not in params["sticky"]:
                    params["sticky"] += "n"
                if "s" not in params["sticky"]:
                    params["sticky"] += "s"
            else:
                params["sticky"] = "ns"

        # expand that dictionary out as we pass it as a value
        widget.grid(**params)
        self.containerStack[-1]['widgets'] = True
        # if we're in a PANEDFRAME - we need to set parent...
        if self.containerStack[-1]['type'] == self.C_PANE:
            self.containerStack[-2]['widgets'] = True

        # configure the row/column to expand equally
        if self.containerStack[-1]['expand'] in ["ALL", "COLUMN"]:
            Grid.columnconfigure(container, column, weight=1)
        else:
            Grid.columnconfigure(container, column, weight=0)
        if self.containerStack[-1]['expand'] in ["ALL", "ROW"]:
            Grid.rowconfigure(container, row, weight=1)
        else:
            Grid.rowconfigure(container, row, weight=0)

#        self.containerStack[-1]['container'].columnconfigure(0, weight=1)
#        self.containerStack[-1]['container'].rowconfigure(0, weight=1)

#####################################
# FUNCTION to manage containers
#####################################
    # adds the container to the container stack - makes this the current
    # working container
    def __addContainer(self, cType, container, row, col, sticky=None):
        self.containerStack.append({'type': cType,
                                    'container': container,
                                    'emptyRow': row,
                                    'colCount': col,
                                    'sticky': sticky,
                                    'padx': 0,
                                    'pady': 0,
                                    'ipadx': 0,
                                    'ipady': 0,
                                    'expand': "ALL",
                                    'widgets': False,
                                    "fg": "black"})

    # returns the current working container
    def __getContainer(self):
        container = self.containerStack[-1]['container']
        if self.containerStack[-1]['type'] == self.C_SCROLLPANE:
            return container.interior
        elif self.containerStack[-1]['type'] == self.C_PAGEDWINDOW:
            return container.getPage()
        elif self.containerStack[-1]['type'] == self.C_TOGGLEFRAME:
            return container.getContainer()
        else:
            return container

    # if possible, removes the current container
    def __removeContainer(self):
        if len(self.containerStack) == 1:
            raise Exception("Can't remove container, already in root window.")
        elif not self.containerStack[-1]['widgets']:
            raise Exception(
                "Put something in the container, before removing it.")
        else:
            return self.containerStack.pop()

    # functions to start the various containers
    def startContainer(
            self,
            fType,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            sticky=None):
        if fType == self.C_LABELFRAME:
            # first, make a LabelFrame, and position it correctly
            self.__verifyItem(self.n_labelFrames, title, True)
            container = LabelFrame(
                self.containerStack[-1]['container'], text=title)
            container.isContainer = True
            container.config(
                background=self.__getContainerBg(),
                font=self.labelFrameFont,
                relief="groove")
            self.setPadX(5)
            self.setPadY(5)
            self.__positionWidget(
                container, row, column, colspan, rowspan, "nsew")
            self.n_labelFrames[title] = container

            # now, add to top of stack
            self.__addContainer(self.C_LABELFRAME, container, 0, 1, sticky)
        elif fType == self.C_FRAME:
            # first, make a Frame, and position it correctly
            self.__verifyItem(self.n_ajFrame, title, True)
            container = ajFrame(self.containerStack[-1]['container'])
            container.isContainer = True
#            container.config(background=self.__getContainerBg(), font=self.frameFont, relief="groove")
            container.config(background=self.__getContainerBg())
            self.__positionWidget(
                container, row, column, colspan, rowspan, "nsew")
            self.n_ajFrame[title] = container

            # now, add to top of stack
            self.__addContainer(self.C_FRAME, container, 0, 1, sticky)
        elif fType == self.C_TABBEDFRAME:
            self.__verifyItem(self.n_tabbedFrames, title, True)
            tabbedFrame = TabbedFrame(
                self.containerStack[-1]['container'], bg=self.__getContainerBg())
#            tabbedFrame.isContainer = True
            self.__positionWidget(
                tabbedFrame,
                row,
                column,
                colspan,
                rowspan,
                sticky=sticky)
            self.n_tabbedFrames[title] = tabbedFrame

            # now, add to top of stack
            self.__addContainer(self.C_TABBEDFRAME, tabbedFrame, 0, 1, sticky)
        elif fType == self.C_TAB:
            # add to top of stack
            self.containerStack[-1]['widgets'] = True
            self.__addContainer(
                self.C_TAB, self.containerStack[-1]['container'].addTab(title), 0, 1, sticky)
        elif fType == self.C_PANEDFRAME:
            # if we previously put a frame for widgets
            # remove it
            if self.containerStack[-1]['type'] == self.C_PANE:
                self.stopContainer()

            # now, add the new pane
            self.__verifyItem(self.n_panedFrames, title, True)
            pane = PanedWindow(
                self.containerStack[
                    -1]['container'],
                showhandle=True,
                sashrelief="groove",
                bg=self.__getContainerBg())
            pane.isContainer = True
            self.__positionWidget(
                pane, row, column, colspan, rowspan, sticky=sticky)
            self.n_panedFrames[title] = pane

            # now, add to top of stack
            self.__addContainer(self.C_PANEDFRAME, pane, 0, 1, sticky)

            # now, add a frame to the pane
            self.startContainer(self.C_PANE, title)
        elif fType == self.C_PANE:
            # create a frame, and add it to the pane
            pane = Pane(
                self.containerStack[-1]['container'], bg=self.__getContainerBg())
            pane.isContainer = True
            self.containerStack[-1]['container'].add(pane)
            self.n_panes[title] = pane

            # now, add to top of stack
            self.__addContainer(self.C_PANE, pane, 0, 1, sticky)
        elif fType == self.C_SCROLLPANE:
            scrollPane = ScrollPane(
                self.containerStack[-1]['container'], bg=self.__getContainerBg(), width=100, height=100)
            scrollPane.isContainer = True
#                self.containerStack[-1]['container'].add(scrollPane)
            self.__positionWidget(
                scrollPane,
                row,
                column,
                colspan,
                rowspan,
                sticky=sticky)
            self.n_scrollPanes[title] = scrollPane

            # now, add to top of stack
            self.__addContainer(self.C_SCROLLPANE, scrollPane, 0, 1, sticky)
        elif fType == self.C_TOGGLEFRAME:
            toggleFrame = ToggleFrame(
                self.containerStack[-1]['container'], title=title, bg=self.__getContainerBg())
            toggleFrame.configure(font=self.toggleFrameFont)
            toggleFrame.isContainer = True
            self.__positionWidget(
                toggleFrame,
                row,
                column,
                colspan,
                rowspan,
                sticky=sticky)
            self.__addContainer(self.C_TOGGLEFRAME, toggleFrame, 0, 1, "nw")
            self.n_toggleFrames[title] = toggleFrame
        elif fType == self.C_PAGEDWINDOW:
            # create the paged window
            pagedWindow = PagedWindow(
                self.containerStack[
                    -1]['container'],
                title=title,
                bg=self.__getContainerBg(),
                width=200,
                height=400)
            # bind events
            self.topLevel.bind("<Left>", pagedWindow.showPrev)
            self.topLevel.bind("<Control-Left>", pagedWindow.showFirst)
            self.topLevel.bind("<Right>", pagedWindow.showNext)
            self.topLevel.bind("<Control-Right>", pagedWindow.showLast)
            # register it as a container
            pagedWindow.isContainer = True
            self.__positionWidget(
                pagedWindow,
                row,
                column,
                colspan,
                rowspan,
                sticky=sticky)
            self.__addContainer(self.C_PAGEDWINDOW, pagedWindow, 0, 1, "nw")
            self.n_pagedWindows[title] = pagedWindow
        elif fType == self.C_PAGE:
            page = self.containerStack[-1]['container'].addPage()
            page.isContainer = True
            self.__addContainer(self.C_PAGE, page, 0, 1, sticky)
            self.containerStack[-1]['expand'] = "None"
        else:
            raise Exception("Unknown container: " + fType)

    ####### Tabbed Frames ########

    def startTabbedFrame(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            sticky="NSEW"):
        self.startContainer(
            self.C_TABBEDFRAME,
            title,
            row,
            column,
            colspan,
            rowspan,
            sticky)

    def stopTabbedFrame(self):
        # auto close the existing TAB - keep it?
        if self.containerStack[-1]['type'] == self.C_TAB:
            self.warn("You didn't STOP the previous TAB")
            self.stopContainer()
        self.stopContainer()

    def setTabbedFrameTabExpand(self, title, expand=True):
        nb = self.__verifyItem(self.n_tabbedFrames, title)
        nb.expandTabs(expand)

    def setTabbedFrameSelectedTab(self, title, tab):
        nb = self.__verifyItem(self.n_tabbedFrames, title)
        nb.changeTab(tab)

    def setTabbedFrameDisabledTab(self, title, tab, disabled=True):
        nb = self.__verifyItem(self.n_tabbedFrames, title)
        nb.disableTab(tab, disabled)

    def setTabbedFrameDisableAllTabs(self, title, disabled=True):
        nb = self.__verifyItem(self.n_tabbedFrames, title)
        nb.disableAllTabs(disabled)

    def setTabBg(self, title, tab, colour):
        nb = self.__verifyItem(self.n_tabbedFrames, title)
        tab = nb.getTab(tab)
        gui.SET_WIDGET_BG(tab, colour)
        # tab.config(bg=colour)
        #gui.SET_WIDGET_BG(tab, colour)
        for child in tab.winfo_children():
            gui.SET_WIDGET_BG(child, colour)

    def startTab(self, title):
        # auto close the previous TAB - keep it?
        if self.containerStack[-1]['type'] == self.C_TAB:
            self.warn("You didn't STOP the previous TAB")
            self.stopContainer()
        elif self.containerStack[-1]['type'] != self.C_TABBEDFRAME:
            raise Exception(
                "Can't add a Tab to the current container: ", self.containerStack[-1]['type'])
        self.startContainer(self.C_TAB, title)

    def getTabbedFrameSelectedTab(self, title):
        nb = self.__verifyItem(self.n_tabbedFrames, title)
        return nb.getSelectedTab()

    def stopTab(self):
        if self.containerStack[-1]['type'] != self.C_TAB:
            raise Exception("Can't stop a TAB, currently in:",
                            self.containerStack[-1]['type'])
        self.stopContainer()

    ###### END Tabbed Frames ########

    #####################################
    # FUNCTION for simple grids
    #####################################
    def addGrid(
            self,
            title,
            data,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            action=None,
            addRow=False):
        self.__verifyItem(self.n_grids, title, True)
        grid = SimpleGrid(
            self.__getContainer(),
            title,
            data,
            action,
            addRow,
            buttonFont=self.buttonFont)
        grid.config(font=self.gridFont, background=self.__getContainerBg())
        self.__positionWidget(
            grid,
            row,
            column,
            colspan,
            rowspan,
            N + E + S + W)
        self.n_grids[title] = grid

    def getGridEntries(self, title):
        return self.__verifyItem(self.n_grids, title).getEntries()

    def getGridSelectedCells(self, title):
        return self.__verifyItem(self.n_grids, title).getSelectedCells()

    def addGridRow(self, title, data):
        self.__verifyItem(self.n_grids, title).addRow(data)

    ########################################

    def startPanedFrame(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            sticky="NSEW"):
        self.startContainer(
            self.C_PANEDFRAME,
            title,
            row,
            column,
            colspan,
            rowspan,
            sticky)

    def startPanedFrameVertical(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            sticky="NSEW"):
        self.startPanedFrame(title, row, column, colspan, rowspan, sticky)
        self.setPanedFrameVertical(title)

    # sticky is alignment inside frame
    # frame will be added as other widgets
    def startLabelFrame(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            sticky=W):
        self.startContainer(
            self.C_LABELFRAME,
            title,
            row,
            column,
            colspan,
            rowspan,
            sticky)

    ###### TOGGLE FRAMES #######
    def startToggleFrame(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.startContainer(
            self.C_TOGGLEFRAME,
            title,
            row,
            column,
            colspan,
            rowspan,
            sticky="new")

    def stopToggleFrame(self):
        if self.containerStack[-1]['type'] != self.C_TOGGLEFRAME:
            raise Exception("Can't stop a TOGGLEFRAME, currently in:",
                            self.containerStack[-1]['type'])
        self.containerStack[-1]['container'].stop()
        self.stopContainer()

    def toggleToggleFrame(self, title):
        toggle = self.__verifyItem(self.n_toggleFrames, title)
        toggle.toggle()

    def disableToggleFrame(self, title, disabled=True):
        toggle = self.__verifyItem(self.n_toggleFrames, title)
        toggle.disable(disabled)

    def getToggleFrameState(self, title):
        toggle = self.__verifyItem(self.n_toggleFrames, title)
        return toggle.isShowing()

    ###### PAGED WINDOWS #######
    def startPagedWindow(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.startContainer(
            self.C_PAGEDWINDOW,
            title,
            row,
            column,
            colspan,
            rowspan,
            sticky="nsew")

    def setPagedWindowPage(self, title, page):
        pager = self.__verifyItem(self.n_pagedWindows, title)
        pager.showPage(page)

    def setPagedWindowButtonsTop(self, title, top=True):
        pager = self.__verifyItem(self.n_pagedWindows, title)
        pager.setNavPositionTop(top)

    def setPagedWindowButtons(self, title, buttons):
        pager = self.__verifyItem(self.n_pagedWindows, title)
        if not isinstance(buttons, list) or len(buttons) != 2:
            raise Exception(
                "You must provide a list of two strings fot setPagedWinowButtons()")
        pager.setPrevButton(buttons[0])
        pager.setNextButton(buttons[1])

    def setPagedWindowFunction(self, title, func):
        pager = self.__verifyItem(self.n_pagedWindows, title)
        command = self.MAKE_FUNC(func, title)
        pager.registerPageChangeEvent(command)

    def getPagedWindowPageNumber(self, title):
        pager = self.__verifyItem(self.n_pagedWindows, title)
        return pager.getPageNumber()

    def showPagedWindowPageNumber(self, title, show=True):
        pager = self.__verifyItem(self.n_pagedWindows, title)
        pager.showLabel(show)

    def showPagedWindowTitle(self, title, show=True):
        pager = self.__verifyItem(self.n_pagedWindows, title)
        pager.showTitle(show)

    def setPagedWindowTitle(self, title, pageTitle):
        pager = self.__verifyItem(self.n_pagedWindows, title)
        pager.setTitle(pageTitle)

    def startPage(self, row=None, column=0, colspan=0, rowspan=0, sticky="nw"):
        if self.containerStack[-1]['type'] == self.C_PAGE:
            self.warn("You didn't STOP the previous PAGE")
            self.stopPage()
        elif self.containerStack[-1]['type'] != self.C_PAGEDWINDOW:
            raise Exception("Can't start a PAGE, currently in:",
                            self.containerStack[-1]['type'])

        self.containerStack[-1]['widgets'] = True
        self.startContainer(
            self.C_PAGE,
            None,
            row,
            column,
            colspan,
            rowspan,
            sticky="nw")

    def stopPage(self):
        if self.containerStack[-1]['type'] == self.C_PAGE:
            self.stopContainer()
        else:
            raise Exception("Can't stop PAGE, currently in:",
                            self.containerStack[-1]['type'])
        self.containerStack[-1]['container'].stopPage()

    def stopPagedWindow(self):
        if self.containerStack[-1]['type'] == self.C_PAGE:
            self.warn("You didn't STOP the previous PAGE")
            self.containerStack[-1]['container'].stopPage()
            self.stopContainer()
        if self.containerStack[-1]['type'] != self.C_PAGEDWINDOW:
            raise Exception("Can't stop a PAGEDWINDOW, currently in:",
                            self.containerStack[-1]['type'])
        self.stopContainer()

    ###### PAGED WINDOWS #######

    def startScrollPane(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            sticky="NSEW"):
        self.startContainer(
            self.C_SCROLLPANE,
            title,
            row,
            column,
            colspan,
            rowspan,
            sticky)

    # functions to stop the various containers
    def stopContainer(self): self.__removeContainer()

    def stopFrame(self):
        if self.containerStack[-1]['type'] != self.C_FRAME:
            raise Exception("Can't stop a FRAME, currently in:",
                            self.containerStack[-1]['type'])
        self.stopContainer()

    def stopLabelFrame(self):
        if self.containerStack[-1]['type'] != self.C_LABELFRAME:
            raise Exception("Can't stop a LABELFRAME, currently in:",
                            self.containerStack[-1]['type'])
        self.stopContainer()

    def stopPanedFrame(self):
        if self.containerStack[-1]['type'] == self.C_PANE:
            self.stopContainer()
        if self.containerStack[-1]['type'] != self.C_PANEDFRAME:
            raise Exception("Can't stop a PANEDFRAME, currently in:",
                            self.containerStack[-1]['type'])
        self.stopContainer()

    def stopScrollPane(self):
        if self.containerStack[-1]['type'] != self.C_SCROLLPANE:
            raise Exception("Can't stop a SCROLLPANE, currently in:",
                            self.containerStack[-1]['type'])
        self.stopContainer()

    def stopAllPanedFrames(self):
        while True:
            try:
                self.stopPanedFrame()
            except:
                break

    def startFrame(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            sticky="NSEW"):
        self.startContainer(
            self.C_FRAME,
            title,
            row,
            column,
            colspan,
            rowspan,
            sticky)

    ### SUB WINDOWS ###

    def startSubWindow(self, name, title=None, modal=False, grouped=False):
        self.__verifyItem(self.n_subWindows, name, True)
        if title is None:
            title = name
        top = SubWindow()
        top.modal = modal
        top.title(title)
        top.protocol(
            "WM_DELETE_WINDOW",
            self.MAKE_FUNC(
                self.hideSubWindow,
                name))
        top.withdraw()
        top.win = self
        if not grouped:
            top.group(self.topLevel.group())
        self.n_subWindows[name] = top

        # now, add to top of stack
        self.__addContainer(self.C_SUBWINDOW, top, 0, 1, "")

    def stopSubWindow(self):
        if self.containerStack[-1]['type'] == self.C_SUBWINDOW:
            self.stopContainer()
        else:
            raise Exception("Can't stop a SUBWINDOW, currently in:",
                            self.containerStack[-1]['type'])

    # functions to show/hide/destroy SubWindows
    def showSubWindow(self, title):
        tl = self.__verifyItem(self.n_subWindows, title)
        tl.deiconify()
        tl.config(takefocus=True)
        tl.killLab = Label(tl)

        if tl.modal:
            tl.transient(self.topLevel)
            tl.grab_set()
            tl.focus_set()
            self.topLevel.wait_window(tl.killLab)

    def setSubWindowLocation(self, title, x, y):
        tl = self.__verifyItem(self.n_subWindows, title)
        tl.geometry("+%d+%d" % (x, y))

    def hideSubWindow(self, title):
        tl = self.__verifyItem(self.n_subWindows, title)
        theFunc = tl.stopFunction
        if theFunc is None or theFunc():
            tl.withdraw()
            if tl.modal:
                tl.killLab.destroy()
                self.topLevel.grab_set()
                self.topLevel.focus_set()

    def destroySubWindow(self, title):
        tl = self.__verifyItem(self.n_subWindows, title)
        theFunc = tl.stopFunction
        if theFunc is None or theFunc():
            tl.withdraw()
            tl.killLab.destroy()
            tl.killLab = None
            self.topLevel.grab_set()
            self.topLevel.focus_set()

            tl.destroy()
            del self.n_subWindows[title]
    #### END SUB WINDOWS ####

    # make a PanedFrame align vertically
    def setPanedFrameVertical(self, window):
        pane = self.__verifyItem(self.n_panedFrames, window)
        pane.config(orient=VERTICAL)

    # function to set position of title for label frame
    def setLabelFrameAnchor(self, title, anchor):
        frame = self.__verifyItem(self.n_labelFrames, title)
        frame.config(labelanchor=anchor)

#####################################
# warn when bad functions called...
#####################################
    def __getattr__(self, name):
        def handlerFunction(*args, **kwargs):
            self.warn(
                "Unknown function:" +
                name +
                " " +
                str(args) +
                " " +
                str(kwargs))
        return handlerFunction

    def __setattr__(self, name, value):
        if self.built and not hasattr(
                self, name):  # would this create a new attribute?
            raise AttributeError("Creating new attributes is not allowed!")
        super(gui, self).__setattr__(name, value)

#####################################
# FUNCTION to add labels before a widget
#####################################
    # this will build a frame, with a label on the left hand side
    def __getLabelBox(self, title):
        self.__verifyItem(self.n_labels, title, True)

        # first, make a frame
        frame = LabelBox(self.__getContainer())
        frame.config(background=self.__getContainerBg())
        self.n_frames.append(frame)

        # if this is a big label, update the others to match...
        if len(title) > self.labWidth:
            self.labWidth = len(title)
            # loop through other labels and resize
            for na in self.n_frameLabs:
                #                        self.n_frameLabs[na].config(width=self.labWidth)
                pass

        # next make the label
        lab = Label(frame)
        frame.theLabel = lab
        lab.hidden = False
        lab.inContainer = True
        lab.config(
            anchor=W,
            text=title,
            justify=LEFT,
            font=self.labelFont,
            background=self.__getContainerBg())
#            lab.config( width=self.labWidth)
        lab.DEFAULT_TEXT = title

        self.n_labels[title] = lab
        self.n_frameLabs[title] = lab

        # now put the label in the frame
        lab.pack(side=LEFT, fill=Y)
        #lab.grid( row=0, column=0, sticky=W )
        #Grid.columnconfigure(frame, 0, weight=1)
        #Grid.rowconfigure(frame, 0, weight=1)

        return frame

    # this is where we add the widget to the frame built above
    def __packLabelBox(self, frame, widget):
        widget.pack(side=LEFT, fill=BOTH, expand=True)
        widget.inContainer = True
        frame.theWidget = widget
        #widget.grid( row=0, column=1, sticky=W+E )
        #Grid.columnconfigure(frame, 1, weight=1)
        #Grid.rowconfigure(frame, 0, weight=1)

    # function to resize labels, if they are hidden or shown
    def __updateLabelBoxes(self, title):
        if len(title) >= self.labWidth:
            self.labWidth = 0
            # loop through other labels and resize
            for na in self.n_frameLabs:
                size = len(self.n_frameLabs[na].cget("text"))
                if not self.n_frameLabs[na].hidden and size > self.labWidth:
                    self.labWidth = size
            for na in self.n_frameLabs:
                self.n_frameLabs[na].config(width=self.labWidth)

#####################################
# FUNCTION for check boxes
#####################################
    def addCheckBox(self, title, row=None, column=0, colspan=0, rowspan=0):
        self.__verifyItem(self.n_cbs, title, True)
        var = IntVar(self.topLevel)
        cb = Checkbutton(self.__getContainer())
        cb.config(
            text=title,
            variable=var,
            font=self.cbFont,
            background=self.__getContainerBg(),
            activebackground=self.__getContainerBg())
        cb.DEFAULT_TEXT = title
        cb.config(anchor=W)
        cb.bind("<Button-1>", self.__grabFocus)
        self.n_cbs[title] = cb
        self.n_boxVars[title] = var
        self.__positionWidget(cb, row, column, colspan, rowspan, EW)

    def getCheckBox(self, title):
        bVar = self.__verifyItem(self.n_boxVars, title)
        if bVar.get() == 1:
            return True
        else:
            return False

    def setCheckBox(self, title, ticked=True):
        cb = self.__verifyItem(self.n_cbs, title)
        if ticked:
            cb.select()
        else:
            cb.deselect()

#####################################
# FUNCTION for scales
#####################################

    def __buildScale(self, title, frame):
        self.__verifyItem(self.n_scales, title, True)
        scale = Scale(frame)
        scale.config(
            repeatinterval=10,
            digits=1,
            orient=HORIZONTAL,
            showvalue=False,
            highlightthickness=1)
        scale.inContainer = False
        self.n_scales[title] = scale
        scale.bind("<Button-1>", self.__grabFocus)
        return scale

    def addScale(self, title, row=None, column=0, colspan=0, rowspan=0):
        scale = self.__buildScale(title, self.__getContainer())
        self.__positionWidget(scale, row, column, colspan, rowspan)

    def addLabelScale(self, title, row=None, column=0, colspan=0, rowspan=0):
        frame = self.__getLabelBox(title)
        scale = self.__buildScale(title, frame)
        self.__packLabelBox(frame, scale)
        self.__positionWidget(frame, row, column, colspan, rowspan)

    def getScale(self, title):
        sc = self.__verifyItem(self.n_scales, title)
        return sc.get()

    def setScale(self, title, pos):
        sc = self.__verifyItem(self.n_scales, title)
        sc.set(pos)

    def setScaleWidth(self, title, width):
        sc = self.__verifyItem(self.n_scales, title)
        sc.config(width=width)

    def setScaleLength(self, title, length):
        sc = self.__verifyItem(self.n_scales, title)
        sc.config(sliderlength=length)

    # this will make the scale show interval numbers
    # set to 0 to remove
    def showScaleIntervals(self, title, intervals):
        sc = self.__verifyItem(self.n_scales, title)
        sc.config(tickinterval=intervals)

    # this will make the scale show its value
    def showScaleValue(self, title, show=True):
        sc = self.__verifyItem(self.n_scales, title)
        sc.config(showvalue=show)

    # change the orientation (Hor or Vert)
    def orientScaleHor(self, title, hor=True):
        self.warn(
            ".orientScaleHor() is deprecated. Please use .setScaleHorizontal() or .setScaleVertical()")
        sc = self.__verifyItem(self.n_scales, title)
        if hor:
            sc.config(orient=HORIZONTAL)
        else:
            sc.config(orient=VERTICAL)

    def setScaleVertical(self, title):
        sc = self.__verifyItem(self.n_scales, title)
        sc.config(orient=VERTICAL)

    def setScaleHorizontal(self, title):
        sc = self.__verifyItem(self.n_scales, title)
        sc.config(orient=HORIZONTAL)

    def setScaleRange(self, title, start, end, curr=None):
        if curr is None:
            curr = start
        sc = self.__verifyItem(self.n_scales, title)
        sc.config(from_=start, to=end)
        self.setScale(title, curr)

#####################################
# FUNCTION for optionMenus
#####################################
    def __buildOptionBox(self, frame, title, options, kind="normal"):
        self.__verifyItem(self.n_options, title, True)

        # create a string var to hold selected item
        var = StringVar(self.topLevel)
        self.n_optionVars[title] = var

        maxSize, options = self.__configOptionBoxList(title, options, kind)

        if len(options) > 0 and kind == "normal":
            option = OptionMenu(frame, var, *options)
            var.set(options[0])
            option.kind = "normal"

        elif kind == "ticks":
            # http://stackoverflow.com/questions/29019760/how-to-create-a-combobox-that-includes-checkbox-for-each-item
            option = OptionMenu(frame, variable=var, value="")
            # delete the empty value we just added
            option['menu'].delete(0, 'end')
            var.set(title)
            vals = {}
            for o in options:
                vals[o] = BooleanVar()
                option['menu'].add_checkbutton(
                    label=o, onvalue=True, offvalue=False, variable=vals[o])
            self.n_optionVars[title] = vals
            option.kind = "ticks"

        else:
            option = OptionMenu(frame, var, [])
            option.kind = "normal"

        option.config(
            justify=LEFT,
            font=self.optionFont,
            background=self.__getContainerBg(),
            highlightthickness=1,
            width=maxSize,
            takefocus=1)
        option.bind("<Button-1>", self.__grabFocus)
        # compare on windows & mac
        #option.config(highlightthickness=12, bd=0, highlightbackground=self.__getContainerBg())
        option.var = var
        option.maxSize = maxSize
        option.inContainer = False
        option.options = options

        option.DEFAULT_TEXT=""
        if options is not None:
            option.DEFAULT_TEXT='\n'.join(str(x) for x in options)

        # configure the drop-down too
        dropDown = option.nametowidget(option.menuname)
        dropDown.configure(font=self.optionFont)
#        dropDown.configure(background=self.__getContainerBg())

#        if self.platform == self.MAC:
#            option.config(highlightbackground=self.__getContainerBg())

        option.bind("<Tab>", self.__focusNextWindow)
        option.bind("<Shift-Tab>", self.__focusLastWindow)

        # add a right click menu
        self.__addRightClickMenu(option)

        self.__disableOptionBoxSeparators(option)

        # add to array list
        self.n_options[title] = option
        return option

    def addOptionBox(
            self,
            title,
            options,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        option = self.__buildOptionBox(self.__getContainer(), title, options)
        self.__positionWidget(option, row, column, colspan, rowspan)

    def addTickOptionBox(
            self,
            title,
            options,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        tick = self.__buildOptionBox(
            self.__getContainer(), title, options, "ticks")
        self.__positionWidget(tick, row, column, colspan, rowspan)

    def addLabelTickOptionBox(
            self,
            title,
            options,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        frame = self.__getLabelBox(title)
        tick = self.__buildOptionBox(frame, title, options, "ticks")
        self.__packLabelBox(frame, tick)
        self.__positionWidget(frame, row, column, colspan, rowspan)

    def addLabelOptionBox(
            self,
            title,
            options,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        frame = self.__getLabelBox(title)
        option = self.__buildOptionBox(frame, title, options)
        self.__packLabelBox(frame, option)
        self.__positionWidget(frame, row, column, colspan, rowspan)

    def getOptionBox(self, title):
        self.__verifyItem(self.n_optionVars, title)
        val = self.n_optionVars[title]

        if isinstance(val, dict):
            retVal = {}
            for k, v in val.items():
                retVal[k] = bool(v.get())
            return retVal
        else:
            val = val.get().strip()
            # set to None if it's a divider
            if val.startswith("-") or len(val) == 0:
                val = None
            return val

    def __disableOptionBoxSeparators(self, box):
        # disable any separators
        for pos, item in enumerate(box.options):
            if item.startswith("-"):
                box["menu"].entryconfigure(pos, state="disabled")

    def __configOptionBoxList(self, title, options, kind):
        # deal with a dict_keys object - messy!!!!
        if not isinstance(options, list):
            options = list(options)

        # make sure all options are strings
        options = [str(i) for i in options]

        # check for empty strings, replace first with message, remove rest
        found = False
        for pos, item in enumerate(options):
            if item == "":
                if not found:
                    options[pos] = "- options -"
                    found = True
                else:
                    del options[pos]

        # get the longest string length
        try:
            maxSize = len(str(max(options, key=len)))
        except:
            try:
                maxSize = len(str(max(options)))
            except:
                maxSize = 0

        # increase if ticks
        if kind == "ticks":
            if len(title) > maxSize:
                maxSize = len(title)

        # new bug?!? - doesn't fit anymore!
        if self.platform == self.MAC:
            maxSize += 3
        return maxSize, options

    # function to replace the current contents of an option box
    # http://www.prasannatech.net/2009/06/tkinter-optionmenu-changing-choices.html
    def changeOptionBox(self, title, options, index=None):
        # get the optionBox & associated var
        box = self.__verifyItem(self.n_options, title)
        if box.kind == "ticks":
            self.warn("Unable to change TickOptionBoxes")
            return
        var = self.n_optionVars[title]

        # tidy up list and get max size
        maxSize, options = self.__configOptionBoxList(title, options, "normal")

        # warn if new options bigger
        if maxSize > box.maxSize:
            self.warn("The new options are wider then the old ones. " +
                      str(maxSize) + ">" + str(box.maxSize))

        # delete the current options
        box['menu'].delete(0, 'end')
        #var.set(" ")

        # add the new items
        for option in options:
            box["menu"].add_command(
                label=option, command=lambda temp=option: box.setvar(
                    box.cget("textvariable"), value=temp))
        box.options = options

        # disable any separators
        self.__disableOptionBoxSeparators(box)

        var.set(options[0])
        # select the specified option
        self.setOptionBox(title, index)

    def deleteOptionBox(self, title, index):
        self.__verifyItem(self.n_optionVars, title)
        box = self.n_options[title]
        self.setOptionBox(title, index, None)

    # select the option at the specified position
    def setOptionBox(self, title, index, value=True):
        var = self.__verifyItem(self.n_optionVars, title)
        box = self.n_options[title]

        if box.kind == "ticks":
            if index in var:
                var[index].set(value)
            else:
                raise Exception("Unknown TickOptionBox: " +
                                str(index) + " in: " + title)
        else:
            count = len(box.options)
            if count > 0:
                if index is None:
                    index = 0
                if not isinstance(index, int):
                    try:
                        index = box.options.index(index)
                    except:
                        self.warn("Invalid selection option: " + str(index))
                        return

                if index < 0 or index > count - 1:
                    self.warn("Invalid selection index: " + str(index) +
                              ". Should be between 0 and " + str(count - 1) + ".")
                else:
                    # then we can delete it...
                    if value is None:
                        box['menu'].delete(index)
                        del(box.options[index])
                        self.setOptionBox(title, 0)
                    else:
                        if not box['menu'].invoke(index):
                            self.warn(
                                "Invalid selection index: " +
                                str(index) +
                                " is a disabled index.")
            else:
                var.set("")
                self.warn("No items to select from: " + title)

#####################################
# FUNCTION to manage Properties Widgets
#####################################
    def addProperties(
            self,
            title,
            values=None,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.__verifyItem(self.n_props, title, True)
        haveTitle = True
        if self.containerStack[-1]['type'] == self.C_TOGGLEFRAME:
            self.containerStack[-1]['sticky'] = "ew"
            haveTitle = False

        props = Properties(
            self.__getContainer(),
            title,
            values,
            haveTitle,
            font=self.propertiesFont,
            background=self.__getContainerBg())
        self.__positionWidget(props, row, column, colspan, rowspan)
        self.n_props[title] = props

    def getProperties(self, title):
        props = self.__verifyItem(self.n_props, title)
        return props.getProperties()

    def getProperty(self, title, prop):
        props = self.__verifyItem(self.n_props, title)
        return props.getProperty(prop)

    def setProperty(self, title, prop, value=False):
        props = self.__verifyItem(self.n_props, title)
        props.addProperty(prop, value)

    def setProperties(self, title, props):
        p = self.__verifyItem(self.n_props, title)
        p.addProperties(props)

    def deleteProperty(self, title, prop):
        props = self.__verifyItem(self.n_props, title)
        props.addProperty(prop, None)

#####################################
# FUNCTION to add spin boxes
#####################################
    def __buildSpinBox(self, frame, title, vals):
        self.__verifyItem(self.n_spins, title, True)
        if type(vals) not in [list, tuple]:
            raise Exception(
                "Can't create SpinBox " +
                title +
                ". Invalid values: " +
                str(vals))

        spin = Spinbox(frame)
        spin.inContainer = False
        spin.isRange = False
        spin.config(font=self.entryFont, highlightthickness=0)

# adds bg colour under spinners
#        if self.platform == self.MAC:
#              spin.config(highlightbackground=self.__getContainerBg())

        spin.bind("<Tab>", self.__focusNextWindow)
        spin.bind("<Shift-Tab>", self.__focusLastWindow)

        # store the vals in DEFAULT_TEXT
        spin.DEFAULT_TEXT=""
        if vals is not None:
            spin.DEFAULT_TEXT='\n'.join(str(x) for x in vals)

        # make sure it's a list
        # reverse it, so the spin box functions properly
        vals = list(vals)
        vals.reverse()
        vals = tuple(vals)
        spin.config(values=vals)

        # prevent invalid entries
        if self.validateSpinBox is None:
            self.validateSpinBox = (
                self.containerStack[0]['container'].register(
                    self.__validateSpinBox), '%P', '%W')

        spin.config(validate='all', validatecommand=self.validateSpinBox)

        self.n_spins[title] = spin
        return spin

    def __addSpinBox(
            self,
            title,
            values,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        spin = self.__buildSpinBox(self.__getContainer(), title, values)
        self.__positionWidget(spin, row, column, colspan, rowspan)
        self.setSpinBoxPos(title, 0)
        return spin

    def addSpinBox(
            self,
            title,
            values,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        return self.__addSpinBox(title, values, row, column, colspan, rowspan)

    def addLabelSpinBox(
            self,
            title,
            values,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        frame = self.__getLabelBox(title)
        spin = self.__buildSpinBox(frame, title, values)
        self.__packLabelBox(frame, spin)
        self.__positionWidget(frame, row, column, colspan, rowspan)
        self.setSpinBoxPos(title, 0)
        return spin

    def addSpinBoxRange(
            self,
            title,
            fromVal,
            toVal,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        vals = list(range(fromVal, toVal + 1))
        spin = self.__addSpinBox(title, vals, row, column, colspan, rowspan)
        spin.isRange = True

    def addLabelSpinBoxRange(
            self,
            title,
            fromVal,
            toVal,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        vals = list(range(fromVal, toVal + 1))
        spin = self.addLabelSpinBox(title, vals, row, column, colspan, rowspan)
        spin.isRange = True

    def getSpinBox(self, title):
        spin = self.__verifyItem(self.n_spins, title)
        return spin.get()

    # validates that an item in the named spinbox starts with the user_input
    def __validateSpinBox(self, user_input, widget_name):
        spin = self.containerStack[0]['container'].nametowidget(widget_name)

        vals = spin.cget("values")  # .split()
        vals = self.__getSpinBoxValsAsList(vals)
        for i in vals:
            if i.startswith(user_input):
                return True

        self.containerStack[0]['container'].bell()
        return False

    # expects a valid spin box widget, and a valid value
    def __setSpinBoxVal(self, spin, val):
        var = StringVar(self.topLevel)
        var.set(val)
        spin.config(textvariable=var)

    # is it going to be a hash or list??
    def __getSpinBoxValsAsList(self, vals):
        vals.replace("{", "")
        vals.replace("}", "")
#        if "{" in vals:
#            vals = vals[1:-1]
#            vals = vals.split("} {")
#        else:
        vals = vals.split()
        return vals

    def setSpinBox(self, title, value):
        spin = self.__verifyItem(self.n_spins, title)
        vals = spin.cget("values")  # .split()
        vals = self.__getSpinBoxValsAsList(vals)
        val = str(value)
        if val not in vals:
            raise Exception(
                "Invalid value: " +
                val +
                ". Not in SpinBox: " +
                title +
                "=" +
                str(vals))
        self.__setSpinBoxVal(spin, val)

    def setSpinBoxPos(self, title, pos):
        spin = self.__verifyItem(self.n_spins, title)
        vals = spin.cget("values")  # .split()
        vals = self.__getSpinBoxValsAsList(vals)
        pos = int(pos)
        if pos < 0 or pos >= len(vals):
            raise Exception(
                "Invalid position: " +
                str(pos) +
                ". No position in SpinBox: " +
                title +
                "=" +
                str(vals))
        pos = len(vals) - 1 - pos
        val = vals[pos]
        self.__setSpinBoxVal(spin, val)

    def changeSpinBox(self, title, vals):
        spin = self.__verifyItem(self.n_spins, title)
        if spin.isRange:
            self.warn("Can't convert " + title + " RangeSpinBox to SpinBox")
        else:
            vals = list(vals)
            vals.reverse()
            vals = tuple(vals)
            spin.config(values=vals)
            self.setSpinBoxPos(title, 0)

#####################################
# FUNCTION to add images
#####################################
    # looks up label containing image
    def __animateImage(self, title, firstTime=False):
        try:
            lab = self.__verifyItem(self.n_images, title)
        except ItemLookupError:
            # image destroyed...
            try: del self.n_imageAnimationIds[title]
            except: pass
            return
        if not lab.image.animating:
            del self.n_imageAnimationIds[title]
            return
        if firstTime and lab.image.alreadyAnimated:
            return

        lab.image.alreadyAnimated = True
        try:
            if lab.image.cached:
                pic = lab.image.pics[lab.image.anim_pos]
            else:
                pic = PhotoImage(file=lab.image.path,
                                 format="gif - {}".format(lab.image.anim_pos))
                lab.image.pics.append(pic)
            lab.image.anim_pos += 1
            lab.config(image=pic)
            anim_id = self.topLevel.after(
                lab.image.anim_speed,
                self.__animateImage,
                title)
            self.n_imageAnimationIds[title] = anim_id
        except:
            lab.image.anim_pos = 0
            lab.image.cached = True
            self.__animateImage(title)

    def __preloadAnimatedImage(self, img):
        if img.cached:
            return
        try:
            pic = PhotoImage(file=img.path,
                             format="gif - {0}".format(img.anim_pos))
            img.pics.append(pic)
            img.anim_pos += 1
            self.preloadAnimatedImageId = self.topLevel.after(
                0, self.__preloadAnimatedImage, img)
        # when all frames have been processed
        except TclError:
            img.anim_pos = 0
            img.cached = True

    def __configAnimatedImage(self, img):
        img.alreadyAnimated = False
        img.isAnimated = True
        img.pics = []
        img.cached = False
        img.anim_pos = 0
        img.anim_speed = 150
        img.animating = True

    # simple way to check if image is animated
    def __checkIsAnimated(self, name):
        if imghdr.what(name) == "gif":
            try:
                PhotoImage(file=name, format="gif - 1")
                return True
            except:
                pass
        return False

    def setAnimationSpeed(self, name, speed):
        img = self.__verifyItem(self.n_images, name).image
        img.anim_speed = speed

    def stopAnimation(self, name):
        img = self.__verifyItem(self.n_images, name).image
        img.animating = False

    def startAnimation(self, name):
        img = self.__verifyItem(self.n_images, name).image
        if not img.animating:
            img.animating = True
            anim_id = self.topLevel.after(img.anim_speed, self.__animateImage, name)
            self.n_imageAnimationIds[name] = anim_id

    def addAnimatedImage(
            self,
            name,
            imageFile,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.warn("addAnimatedImage() is now deprecated - use addImage()")
        self.addImage(name, imageFile, row, column, colspan, rowspan)

    # function to set an alternative image, when a mouse goes over
    def setImageMouseOver(self, title, overImg):
        lab = self.__verifyItem(self.n_images, title)
        leaveImg = lab.image.originalPath
        lab.bind("<Leave>", lambda e: self.setImage(title, leaveImg))
        lab.bind("<Enter>", lambda e: self.setImage(title, overImg))

    # function to set an image location
    def setImageLocation(self, location):
        if os.path.isdir(location):
            self.userImages = location
        else:
            raise Exception("Invalid image location: " + location)

    # function to remove image objects form cache
    def clearImageCache(self):
        self.n_imageCache = {}

    # internal function to check/build image object
    def __getImage(self, imagePath, cache=True):
        if imagePath is None:
            return None
        originalPath = imagePath
        if self.userImages is not None:
            imagePath = os.path.join(self.userImages, imagePath)

        if cache and imagePath in self.n_imageCache and self.n_imageCache[
                imagePath] is not None:
            photo = self.n_imageCache[imagePath]
        elif os.path.isfile(imagePath):
            if os.access(imagePath, os.R_OK):
                imgType = imghdr.what(imagePath)
                if not imagePath.lower().endswith(imgType) and not (
                        imgType == "jpeg" and imagePath.lower().endswith("jpg")):
                        # the image has been saved with the wrong extension
                    raise Exception(
                        "Invalid image extension: " +
                        imagePath +
                        " should be a ." +
                        imgType)
                elif imagePath.lower().endswith('.gif'):
                    photo = PhotoImage(file=imagePath)
                elif imagePath.lower().endswith('.ppm') or imagePath.lower().endswith('.pgm'):
                    photo = PhotoImage(file=imagePath)
                elif imagePath.lower().endswith('jpg') or imagePath.lower().endswith('jpeg'):
                    self.warn(
                        "Image processing for .JPGs is slow. .GIF is the recommended format")
                    photo = self.convertJpgToBmp(imagePath)
                elif imagePath.lower().endswith('.png'):
                    # known issue here, some PNGs lack IDAT chunks
                    # also, PNGs seem broken on python<3, maybe around the map
                    # function used to generate pixel maps
                    if not TKINTERPNG_AVAILABLE:
                        raise Exception(
                            "TKINTERPNG library not found, PNG files not supported: " + imagePath)
                    if sys.version_info >= (2, 7):
                        self.warn(
                            "Image processing for .PNGs is slow. .GIF is the recommended format")
                        png = PngImageTk(imagePath)
                        png.convert()
                        photo = png.image
                    else:
                        raise Exception(
                            "PNG images only supported in python 3: " + imagePath)
                else:
                    raise Exception("Invalid image type: " + imagePath)
            else:
                raise Exception("Can't read image: " + imagePath)
        else:
            raise Exception("Image " + imagePath + " does not exist")

        photo.path = imagePath
        photo.originalPath = originalPath

        # sort out if it's an animated images
        if self.__checkIsAnimated(imagePath):
            self.__configAnimatedImage(photo)
            self.__preloadAnimatedImage(photo)
        else:
            photo.isAnimated = False
            photo.animating = False
            if cache:
                self.n_imageCache[imagePath] = photo

        return photo

    # force replace the current image, with a new one
    def reloadImage(self, name, imageFile):
        label = self.__verifyItem(self.n_images, name)
        image = self.__getImage(imageFile, False)
        self.__populateImage(name, image)

    # replace the current image, with a new one
    def setImage(self, name, imageFile):
        label = self.__verifyItem(self.n_images, name)
        # only set the image if it's different
        if label.image.originalPath == imageFile:
            self.warn("Not updating " + str(name) + ", " + str(imageFile) + " hasn't changed." )
            return
        else:
            image = self.__getImage(imageFile)
            self.__populateImage(name, image)

    # internal function to update the image in a label
    def __populateImage(self, name, image):
        label = self.__verifyItem(self.n_images, name)

        label.image.animating = False
        label.config(image=image)
        label.config(
            anchor=CENTER,
            font=self.labelFont,
            background=self.__getContainerBg())
        label.image = image  # keep a reference!

        if image.isAnimated:
            anim_id = self.topLevel.after(
                image.anim_speed + 100,
                self.__animateImage,
                name,
                True)
            self.n_imageAnimationIds[name] = anim_id

        # removed - keep the label the same size, and crop images
        #h = image.height()
        #w = image.width()
        #label.config(height=h, width=w)
        self.topLevel.update_idletasks()

    # must be GIF or PNG
    def addImage(
            self,
            name,
            imageFile,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        #image = re.escape(image)
        self.__verifyItem(self.n_images, name, True)
        img = self.__getImage(imageFile)

        label = Label(self.__getContainer())
        label.config(
            anchor=CENTER,
            font=self.labelFont,
            background=self.__getContainerBg())
        label.config(image=img)
        label.image = img  # keep a reference!

        if img is not None:
            h = img.height()
            w = img.width()
            label.config(height=h, width=w)

        self.n_images[name] = label
        self.__positionWidget(label, row, column, colspan, rowspan)
        if img.isAnimated:
            anim_id = self.topLevel.after(
                img.anim_speed, self.__animateImage, name, True)
            self.n_imageAnimationIds[name] = anim_id

    def setImageSize(self, name, width, height):
        img = self.__verifyItem(self.n_images, name)
        img.config(height=height, width=width)

#      def rotateImage(self, name, image):
#            img = self.__verifyItem(self.n_images, name)

    # if +ve then grow, else shrink...
    def zoomImage(self, name, x, y=''):
        img = self.__verifyItem(self.n_images, name)
        if x <= 0:
            self.shrinkImage(name, x * -1, y * -1)
        else:
            self.growImage(name, x, y)

    # get every nth pixel (must be an integer)
    # 0 will return an empty image, 1 will return the image, 2 will be 1/2 the
    # size ...
    def shrinkImage(self, name, x, y=''):
        img = self.__verifyItem(self.n_images, name)
        image = img.image.subsample(x, y)

        img.config(image=image)
        img.config(
            anchor=CENTER,
            font=self.labelFont,
            background=self.__getContainerBg())
        img.modImage = image  # keep a reference!
        img.config(width=image.width(), height=image.height())

    # get every nth pixel (must be an integer)
    # 0 won't work, 1 will return the original size
    def growImage(self, name, x, y=''):
        label = self.__verifyItem(self.n_images, name)
        image = label.image.zoom(x, y)

        label.config(image=image)
        label.config(
            anchor=CENTER,
            font=self.labelFont,
            background=self.__getContainerBg())
        label.modImage = image  # keep a reference!
        label.config(width=image.width(), height=image.height())

    def convertJpgToBmp(self, image):
        if not NANOJPEG_AVAILABLE:
            raise Exception(
                "nanjpeg library not found, unable to display jpeg files: " + image)
        elif sys.version_info < (2, 7):
            raise Exception(
                "JPG images only supported in python 2.7+: " + image)
        else:
            # read the image into an array of bytes
            with open(image, 'rb') as inFile:
                import array
                buf = array.array("B", inFile.read())

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
            val = "P%d\n%d %d\n255\n" % (
                param, nanojpeg.njGetWidth(), nanojpeg.njGetHeight())
            # append the bytes, converted to chars
            val += ''.join(map(chr, nanojpeg.njGetImage()))

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
    # make sure this is done before everything else, otherwise it will cover
    # other widgets
    def setBgImage(self, image):
        image = self.__getImage(image, False)  # make sure it's not cached
        # self.containerStack[0]['container'].config(image=image) # window as a
        # label doesn't work...
        self.bgLabel.config(image=image)
        self.containerStack[0]['container'].image = image  # keep a reference!

    def removeBgImage(self):
        self.bgLabel.config(image=None)
        # self.containerStack[0]['container'].config(image=None) # window as a
        # label doesn't work...
        # remove the reference - shouldn't be cached
        self.containerStack[0]['container'].image = None

    def resizeBgImage(self):
        if self.containerStack[0]['container'].image is None:
            return
        else:
            pass

#####################################
# FUNCTION to play sounds
#####################################
    # function to set a sound location
    def setSoundLocation(self, location):
        if os.path.isdir(location):
            self.userSounds = location
        else:
            raise Exception("Invalid sound location: " + location)

    # internal function to manage sound availability
    def __soundWrap(self, sound, isFile=False, repeat=False, wait=False):
        if self.platform == self.WINDOWS:
            if self.userSounds is not None and sound is not None:
                sound = os.path.join(self.userSounds, sound)
            if isFile:
                if False == os.path.isfile(sound):
                    raise Exception("Can't find sound: " + sound)
                if not sound.lower().endswith('.wav'):
                    raise Exception("Invalid sound format: " + sound)
                kind = winsound.SND_FILENAME
                if not wait:
                    kind = kind | winsound.SND_ASYNC
            else:
                if sound is None:
                    kind = winsound.SND_FILENAME
                else:
                    kind = winsound.SND_ALIAS
                    if not wait:
                        kind = kind | winsound.SND_ASYNC

            if repeat:
                kind = kind | winsound.SND_LOOP

            winsound.PlaySound(sound, kind)
        else:
            # sound not available at this time
            raise Exception(
                "Sound not supported on this platform: " +
                platform())

    def playSound(self, sound, wait=False):
        self.__soundWrap(sound, True, False, wait)

    def stopSound(self):
        self.__soundWrap(None)

    def loopSound(self, sound):
        self.__soundWrap(sound, True, True)

    def soundError(self):
        self.__soundWrap("SystemHand")

    def soundWarning(self):
        self.__soundWrap("SystemAsterisk")

    def playNote(self, note, duration=200):
        if self.platform == self.WINDOWS:
            try:
                if isinstance(note, str):
                    freq = self.NOTES[note.lower()]
                else:
                    freq = note
            except KeyError:
                raise Exception("Error: cannot play note - " + note)
            try:
                if isinstance(duration, str):
                    length = self.DURATIONS[duration.upper()]
                else:
                    length = duration
            except KeyError:
                raise Exception("Error: cannot play duration - " + duration)

            try:
                winsound.Beep(freq, length)
            except RuntimeError:
                raise Exception(
                    "Sound not available on this platform: " +
                    platform())
        else:
            # sound not available at this time
            raise Exception(
                "Sound not supported on this platform: " +
                platform())

#####################################
# FUNCTION for radio buttons
#####################################
    def addRadioButton(
            self,
            title,
            name,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        var = None
        newRb = False
        # title - is the grouper
        # so, if we already have an entry in n_rbVars - get it
        if (title in self.n_rbVars):
            var = self.n_rbVars[title]
            # also get the list of rbVals
            vals = self.n_rbVals[title]
            # and if we already have the new item in that list - reject it
            if name in vals:
                raise Exception(
                    "Invalid radio button: " +
                    name +
                    " already exists")
            # otherwise - append it to the list of vals
            else:
                vals.append(name)
        else:
            # if this is a new grouper - set it all up
            var = StringVar(self.topLevel)
            vals = [name]
            self.n_rbVars[title] = var
            self.n_rbVals[title] = vals
            newRb = True

        # finally, create the actual RadioButton
        rb = Radiobutton(self.__getContainer())
        rb.config(
            text=name,
            variable=var,
            value=name,
            background=self.__getContainerBg(),
            activebackground=self.__getContainerBg(),
            font=self.rbFont,
            indicatoron = 1)
        rb.config(anchor = W)
        rb.bind("<Button-1>", self.__grabFocus)
        rb.DEFAULT_TEXT = name

        # either append to existing widget list
        if (title in self.n_rbs):
            self.n_rbs[title].append(rb)
        # or create a new one
        else:
            self.n_rbs[title] = [rb]
        #rb.bind("<Tab>", self.__focusNextWindow)
        #rb.bind("<Shift-Tab>", self.__focusLastWindow)

        # and select it, if it's the first item in the list
        if newRb:
            rb.select()
        self.__positionWidget(rb, row, column, colspan, rowspan, EW)

    def getRadioButton(self, title):
        var = self.__verifyItem(self.n_rbVars, title)
        return var.get()

    def setRadioButton(self, title, value):
        vals = self.__verifyItem(self.n_rbVals, title)
        if value not in vals:
            raise Exception(
                "Invalid radio button: '" +
                value +
                "' doesn't exist")
        var = self.n_rbVars[title]
        var.set(value)

    def setRadioTick(self, title, tick=True):
        radios = self.__verifyItem(self.n_rbs, title)
        for rb in radios:
            if tick:
                rb.config(indicatoron=1)
            else:
                rb.config(indicatoron=0)

#####################################
# FUNCTION for list box
#####################################
    def addListBox(
            self,
            name,
            values=None,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.__verifyItem(self.n_lbs, name, True)
        frame = ListBox(self.__getContainer())
        vscrollbar = AutoScrollbar(frame)
        hscrollbar = AutoScrollbar(frame, orient=HORIZONTAL)

        lb = Listbox(
            frame,
            yscrollcommand=vscrollbar.set,
            xscrollcommand=hscrollbar.set)

        vscrollbar.grid(row=0, column=1, sticky=N + S)
        hscrollbar.grid(row=1, column=0, sticky=E + W)

        lb.grid(row=0, column=0, sticky=N + S + E + W)

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        vscrollbar.config(command=lb.yview)
        hscrollbar.config(command=lb.xview)

        lb.config(font=self.lbFont)
        self.n_lbs[name] = lb

        lb.DEFAULT_TEXT=""
        if values is not None:
            lb.DEFAULT_TEXT='\n'.join(str(x) for x in values)
            for name in values:
                lb.insert(END, name)

        self.__positionWidget(frame, row, column, colspan, rowspan)

    # set how many rows to display
    def setListBoxRows(self, name, rows):
        lb = self.__verifyItem(self.n_lbs, name)
        lb.config(height=rows)

    # make the list single/multi select
    # default is single
    def setListBoxMulti(self, title, multi=True):
        lb = self.__verifyItem(self.n_lbs, title)
        if multi:
            lb.config(selectmode=EXTENDED)
        else:
            lb.config(selectmode=BROWSE)

    # make the list single/multi select
    # default is single
    def setListBoxSingle(self, title, single=True):
        self.setListSingle(title, single)

    def setListSingle(self, title, single=True):
        self.setListBoxMulti(title, not single)

    # select the specified item in the list
    def selectListItem(self, title, item):
        lb = self.__verifyItem(self.n_lbs, title)
        items = lb.get(0, END)
        if len(items) > 0:
            for pos in range(len(items)):
                if items[pos] == item:
                    self.selectListItemPos(title, pos)
                    break

    def selectListItemPos(self, title, pos):
        lb = self.__verifyItem(self.n_lbs, title)
        sel = lb.curselection()
        lb.selection_clear(0, END)
        # show & select this item
        if pos >= 0:
            lb.see(pos)
            lb.activate(pos)
            lb.selection_set(pos)

    # replace the list items in the list box
    def updateListItems(self, title, items):
        self.clearListBox(title)
        self.addListItems(title, items)

    # add the items to the specified list box
    def addListItems(self, title, items):
        for i in items:
            self.addListItem(title, i)

    # add the item to the end of the list box
    def addListItem(self, title, item):
        lb = self.__verifyItem(self.n_lbs, title)
        # add it at the end
        lb.insert(END, item)

        # clear any selection
        items = lb.curselection()
        if len(items) > 0:
            lb.selection_clear(items)

        # show & select the newly added item
        self.selectListItemPos(title, lb.size() - 1)

    # returns a list containing 0 or more elements
    # all that are in the selected range
    def getListItems(self, title):
        lb = self.__verifyItem(self.n_lbs, title)
        items = lb.curselection()
        values = []
        for loop in range(len(items)):
            values.append(lb.get(items[loop]))
        return values

    def getAllListItems(self, title):
        lb = self.__verifyItem(self.n_lbs, title)
        items = lb.get(0, END)
        return list(items)

    def getListItemsPos(self, title):
        lb = self.__verifyItem(self.n_lbs, title)
        items = lb.curselection()
        return items

    def removeListItemAtPos(self, title, pos):
        lb = self.__verifyItem(self.n_lbs, title)
        items = lb.get(0, END)
        if pos >= len(items):
            raise Exception("Invalid position: " + str(pos))
        lb.delete(pos)

        # show & select this item
        if pos >= lb.size():
            pos -= 1
        self.selectListItemPos(title, pos)

    # remove a specific item from the listBox
    # will only remove the first item that matches the String
    def removeListItem(self, title, item):
        lb = self.__verifyItem(self.n_lbs, title)
        items = lb.get(0, END)
        for pos, val in enumerate(items):
            if val == item:
                lb.delete(pos)
                break

        # show & select this item
        if pos >= lb.size():
            pos -= 1
        self.selectListItemPos(title, pos)

    def clearListBox(self, title):
        lb = self.__verifyItem(self.n_lbs, title)
        lb.delete(0, END)  # clear

#####################################
# FUNCTION for buttons
#####################################
    def __buildButton(self, title, func, frame, name=None):
        if name is None:
            name = title
        self.__verifyItem(self.n_buttons, title, True)
        but = Button(frame)

        but.config(text=name, font=self.buttonFont)
        but.DEFAULT_TEXT = name

        if func is not None:
            command = self.MAKE_FUNC(func, title)
            bindCommand = self.MAKE_FUNC(func, title, True)

            but.config(command=command)
            but.bind('<Return>', bindCommand)

        if self.platform in [self.MAC, self.LINUX]:
            but.config(highlightbackground=self.__getContainerBg())

        #but.bind("<Tab>", self.__focusNextWindow)
        #but.bind("<Shift-Tab>", self.__focusLastWindow)
        self.n_buttons[title] = but

        return but

    def addNamedButton(
            self,
            name,
            title,
            func,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        but = self.__buildButton(title, func, self.__getContainer(), name)
        self.__positionWidget(but, row, column, colspan, rowspan, None)

    def addButton(self, title, func, row=None, column=0, colspan=0, rowspan=0):
        but = self.__buildButton(title, func, self.__getContainer())
        self.__positionWidget(but, row, column, colspan, rowspan, None)

    def setButton(self, name, text):
        but = self.__verifyItem(self.n_buttons, name)
        but.config(text=text)

    def setButtonImage(self, name, imgFile):
        but = self.__verifyItem(self.n_buttons, name)
        image = self.__getImage(imgFile)
        # works on Mac & Windows :)
        but.config(image=image, compound=TOP, text="", justify=LEFT)
        # but.config(image=image, compound=None, text="") # works on Windows,
        # not Mac

        but.image = image

    # adds a set of buttons, in the row, spannning specified columns
    # pass in a list of names & a list of functions (or a single function to
    # use for all)
    def addButtons(
            self,
            names,
            funcs,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):

        if not isinstance(names, list):
            raise Exception(
                "Invalid button: " +
                names +
                ". It must be a list of buttons.")

        singleFunc = self.__checkFunc(names, funcs)

        frame = WidgetBox(self.__getContainer())
        frame.config(background=self.__getContainerBg())

        # make them into a 2D array, if not already
        if not isinstance(names[0], list):
            names = [names]
            # won't be used if single func
            if funcs is not None:
                funcs = [funcs]

        for bRow in range(len(names)):
            for i in range(len(names[bRow])):
                t = names[bRow][i]
                if funcs is None:
                    tempFunc = None
                elif singleFunc is None:
                    tempFunc = funcs[bRow][i]
                else:
                    tempFunc = singleFunc
                but = self.__buildButton(t, tempFunc, frame)

                but.grid(row=bRow, column=i)
                Grid.columnconfigure(frame, i, weight=1)
                Grid.rowconfigure(frame, bRow, weight=1)
                frame.theWidgets.append(but)

        self.__positionWidget(frame, row, column, colspan, rowspan)
        self.n_frames.append(frame)

#####################################
# FUNCTIONS for links
#####################################
    def __buildLink(self, title):
        link = Link(self.__getContainer())
        link.config(
            text=title,
            font=self.linkFont,
            background=self.__getContainerBg())
        self.n_links[title] = link
        return link

    # launches a browser to the specified page
    def addWebLink(
            self,
            title,
            page,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        link = self.__buildLink(title)
        link.registerWebpage(page)
        self.__positionWidget(link, row, column, colspan, rowspan)

    # executes the specified function
    def addLink(self, title, func, row=None, column=0, colspan=0, rowspan=0):
        link = self.__buildLink(title)
        myF = self.MAKE_FUNC(func, title, True)
        link.registerCallback(myF)
        self.__positionWidget(link, row, column, colspan, rowspan)

#####################################
# FUNCTIONS for grips
#####################################
    # adds a simple grip, used to drag the window around
    def addGrip(self, row=None, column=0, colspan=0, rowspan=0):
        grip = Grip(self.__getContainer())
        self.__positionWidget(grip, row, column, colspan, rowspan)
        self.__addTooltip(grip, "Drag here to move", True)

#####################################
# DatePicker Widget - using Form Container
#####################################
    def addDatePicker(self, name, row=None, column=0, colspan=0, rowspan=0):
        # initial DatePicker has these dates
        days = range(1, 32)
        self.MONTH_NAMES = calendar.month_name[1:]
        years = range(1970, 2021)

        # create a frame, and add the widgets
        self.startFrame(name, row, column, colspan, rowspan)
        self.setExpand("none")
        self.addLabel(name + "_DP_DayLabel", "Day:", 0, 0)
        self.setLabelAlign(name + "_DP_DayLabel", "w")
        self.addOptionBox(name + "_DP_DayOptionBox", days, 0, 1)
        self.addLabel(name + "_DP_MonthLabel", "Month:", 1, 0)
        self.setLabelAlign(name + "_DP_MonthLabel", "w")
        self.addOptionBox(name + "_DP_MonthOptionBox", self.MONTH_NAMES, 1, 1)
        self.addLabel(name + "_DP_YearLabel", "Year:", 2, 0)
        self.setLabelAlign(name + "_DP_YearLabel", "w")
        self.addOptionBox(name + "_DP_YearOptionBox", years, 2, 1)
        self.setOptionBoxFunction(
            name + "_DP_MonthOptionBox",
            self.__updateDatePickerDays)
        self.setOptionBoxFunction(
            name + "_DP_YearOptionBox",
            self.__updateDatePickerDays)
        self.stopFrame()

    # function to update DatePicker dropDowns
    def __updateDatePickerDays(self, title):
        if title.find("_DP_MonthOptionBox") > -1:
            title = title.split("_DP_MonthOptionBox")[0]
        elif title.find("_DP_YearOptionBox") > -1:
            title = title.split("_DP_YearOptionBox")[0]
        else:
            self.warn("Can't update days in DatePicker: " + title)
            return

        day = self.getOptionBox(title + "_DP_DayOptionBox")
        month = self.MONTH_NAMES.index(
            self.getOptionBox(
                title + "_DP_MonthOptionBox")) + 1
        year = int(self.getOptionBox(title + "_DP_YearOptionBox"))
        days = range(1, calendar.monthrange(year, month)[1] + 1)
        self.changeOptionBox(title + "_DP_DayOptionBox", days)

        # keep previous day if possible
        myWarn = self.__pauseWarn()
        self.setOptionBox(title + "_DP_DayOptionBox", day)
        self.__resumeWarn(myWarn)

    # set a date for the named DatePicker
    def setDatePickerRange(self, title, startYear, endYear=None):
        if endYear is None:
            endYear = datetime.date.today().year
        years = range(startYear, endYear + 1)
        self.changeOptionBox(title + "_DP_YearOptionBox", years)

    def setDatePicker(self, title, date=None):
        if date is None:
            date = datetime.date.today()
        self.setOptionBox(title + "_DP_YearOptionBox", str(date.year))
        self.setOptionBox(title + "_DP_MonthOptionBox", date.month - 1)
        self.setOptionBox(title + "_DP_DayOptionBox", date.day - 1)

    def getDatePicker(self, title):
        day = int(self.getOptionBox(title + "_DP_DayOptionBox"))
        month = self.MONTH_NAMES.index(
            self.getOptionBox(
                title + "_DP_MonthOptionBox")) + 1
        year = int(self.getOptionBox(title + "_DP_YearOptionBox"))
        date = datetime.date(year, month, day)
        return date

#####################################
# FUNCTIONS for labels
#####################################
    def __flash(self):
        if self.doFlash:
            for lab in self.n_flashLabs:
                bg = lab.cget("background")
                fg = lab.cget("foreground")
                lab.config(background=fg, foreground=bg)
        self.flashId = self.topLevel.after(250, self.__flash)

    def addFlashLabel(
            self,
            title,
            text=None,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.addLabel(title, text, row, column, colspan, rowspan)
        self.n_flashLabs.append(self.n_labels[title])
        self.doFlash = True

    def addLabel(
            self,
            title,
            text=None,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.__verifyItem(self.n_labels, title, True)
        container = self.__getContainer()
        lab = Label(container)

        lab.inContainer = False
        if text is not None:
            lab.config(text=text)
            lab.DEFAULT_TEXT = text
        else:
            lab.DEFAULT_TEXT = ""
        lab.config(
            justify=LEFT,
            font=self.labelFont,
            background=self.__getContainerBg())
        self.n_labels[title] = lab

        self.__positionWidget(lab, row, column, colspan, rowspan)

    def addEmptyLabel(self, title, row=None, column=0, colspan=0, rowspan=0):
        self.addLabel(title, None, row, column, colspan, rowspan)

    # adds a set of labels, in the row, spannning specified columns
    def addLabels(self, names, row=None, colspan=0, rowspan=0):
        frame = WidgetBox(self.__getContainer())
        frame.config(background=self.__getContainerBg())
        for i in range(len(names)):
            self.__verifyItem(self.n_labels, names[i], True)
            lab = Label(frame)
            lab.config(
                text=names[i],
                font=self.labelFont,
                justify=LEFT,
                background=self.__getContainerBg())
            lab.inContainer = False

            self.n_labels[names[i]] = lab
            lab.grid(row=0, column=i)
            Grid.columnconfigure(frame, i, weight=1)
            Grid.rowconfigure(frame, 0, weight=1)
            frame.theWidgets.append(lab)

        self.__positionWidget(frame, row, 0, colspan, rowspan)
        self.n_frames.append(frame)

    def setLabel(self, name, text):
        lab = self.__verifyItem(self.n_labels, name)
        lab.config(text=text)

    def getLabel(self, name):
        lab = self.__verifyItem(self.n_labels, name)
        return lab.cget("text")

    def clearLabel(self, name):
        self.setLabel(name, "")

#####################################
# FUNCTIONS to add Text Area
#####################################
    def __buildTextArea(self, title, frame, scrollable=False):
        self.__verifyItem(self.n_textAreas, title, True)
        if scrollable:
            text = scrolledtext.ScrolledText(frame)
        else:
            text = Text(frame)
        text.config(font=self.taFont, width=20, height=10, undo=True)

        if self.platform in [self.MAC, self.LINUX]:
            text.config(highlightbackground=self.__getContainerBg())

        text.bind("<Tab>", self.__focusNextWindow)
        text.bind("<Shift-Tab>", self.__focusLastWindow)

        # add a right click menu
        text.var = None
        self.__addRightClickMenu(text)

        self.n_textAreas[title] = text
        self.logTextArea(title)
        return text

    def addTextArea(self, title, row=None, column=0, colspan=0, rowspan=0):
        text = self.__buildTextArea(title, self.__getContainer())
        self.__positionWidget(
            text,
            row,
            column,
            colspan,
            rowspan,
            N + E + S + W)

    def addScrolledTextArea(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        text = self.__buildTextArea(title, self.__getContainer(), True)
        self.__positionWidget(
            text,
            row,
            column,
            colspan,
            rowspan,
            N + E + S + W)

    def getTextArea(self, title):
        self.__verifyItem(self.n_textAreas, title)
        text = self.n_textAreas[title].get('1.0', END + '-1c')
        return text

    def setTextArea(self, title, text):
        self.__verifyItem(self.n_textAreas, title)
        self.n_textAreas[title].insert('1.0', text)

    # functions to try to monitor text areas
    def clearTextArea(self, title):
        self.__verifyItem(self.n_textAreas, title)
        self.n_textAreas[title].delete('1.0', END)

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
# FUNCTIONS to add Tree Widgets
#####################################
    def addTree(self, title, data, row=None, column=0, colspan=0, rowspan=0):
        self.__verifyItem(self.n_trees, title, True)
        frame = ScrollPane(
            self.__getContainer(),
            relief=RAISED,
            borderwidth=2,
            bg="white",
            highlightthickness=0,
            takefocus=1)
        self.__positionWidget(frame, row, column, colspan, rowspan, "NSEW")

        xmlDoc = parseString(data)
        item = ajTreeData(xmlDoc.documentElement)
        node = ajTreeNode(frame.getPane(), None, item)
        self.n_trees[title] = node
        # update() & expand() called in go() function

    def setTreeEditable(self, title, value=True):
        tree = self.__verifyItem(self.n_trees, title)
        tree.item.setCanEdit(value)

    def setTreeBg(self, title, colour):
        tree = self.__verifyItem(self.n_trees, title)
        tree.setBgColour(colour)

    def setTreeFg(self, title, colour):
        tree = self.__verifyItem(self.n_trees, title)
        tree.setFgColour(colour)

    def setTreeHighlightBg(self, title, colour):
        tree = self.__verifyItem(self.n_trees, title)
        tree.setBgHColour(colour)

    def setTreeHighlightFg(self, title, colour):
        tree = self.__verifyItem(self.n_trees, title)
        tree.setFgHColour(colour)

    def setTreeDoubleClickFunction(self, title, func):
        if func is not None:
            tree = self.__verifyItem(self.n_trees, title)
            command = self.MAKE_FUNC(func, title)
            tree.item.registerDblClick(command)

    def setTreeEditFunction(self, title, func):
        if func is not None:
            tree = self.__verifyItem(self.n_trees, title)
            command = self.MAKE_FUNC(func, title)
            tree.registerEditEvent(command)

    # get whole tree as XML
    def getTreeXML(self, title):
        tree = self.__verifyItem(self.n_trees, title)
        return tree.item.node.toxml()

    # get selected node as a string
    def getTreeSelected(self, title):
        tree = self.__verifyItem(self.n_trees, title)
        return tree.getSelectedText()

    # get selected node (and children) as XML
    def getTreeSelectedXML(self, title):
        tree = self.__verifyItem(self.n_trees, title)
        item = tree.getSelected()
        if item is not None:
            return item.node.toxml()
        else:
            return None

#####################################
# FUNCTIONS to add Message Box
#####################################
    def addMessage(
            self,
            title,
            text,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):

        self.__verifyItem(self.n_messages, title, True)
        mess = Message(self.__getContainer())
        mess.config(font=self.messageFont)
        mess.config(justify=LEFT, background=self.__getContainerBg())

        if text is not None:
            mess.config(text=text)
            mess.DEFAULT_TEXT = text
        else:
            mess.DEFAULT_TEXT = ""

        if self.platform in [self.MAC, self.LINUX]:
            mess.config(highlightbackground=self.__getContainerBg())

        self.n_messages[title] = mess

        self.__positionWidget(mess, row, column, colspan, rowspan)
#            mess.bind("<Configure>", lambda e: mess.config(width=e.width-10))

    def addEmptyMessage(self, title, row=None, column=0, colspan=0, rowspan=0):
        self.addMessage(title, None, row, column, colspan, rowspan)

    def setMessage(self, title, text):
        mess = self.__verifyItem(self.n_messages, title)
        mess.config(text=text)

    def clearMessage(self, title):
        self.setMessage(title, "")

#####################################
# FUNCTIONS for entry boxes
#####################################
    def __buildEntry(self, title, frame, secret=False, words=[]):
        self.__verifyItem(self.n_entries, title, True)

        # if we are an autocompleter
        if len(words) > 0:
            ent = AutoCompleteEntry(words, frame)
            ent.config(font=self.entryFont)
        else:
            ent = Entry(frame)
            ent.var = StringVar(self.topLevel)
            ent.config(textvariable=ent.var, font=self.entryFont)

        ent.inContainer = False
        ent.showingDefault = False  # current status of entry
        ent.default = ""  # the default value to show (if set)
        ent.DEFAULT_TEXT = ""  # the default value for language support
        ent.myTitle = title  # thr title of the entry
        ent.isNumeric = False  # if the entry is numeric

        # configure it to be secret
        if secret:
            ent.config(show="*")

        if self.platform in [self.MAC, self.LINUX]:
            ent.config(highlightbackground=self.__getContainerBg())
        ent.bind("<Tab>", self.__focusNextWindow)
        ent.bind("<Shift-Tab>", self.__focusLastWindow)

        # add a right click menu
        self.__addRightClickMenu(ent)

        self.n_entries[title] = ent
        self.n_entryVars[title] = ent.var
        return ent

    def addEntry(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            secret=False):
        ent = self.__buildEntry(title, self.__getContainer(), secret)
        self.__positionWidget(ent, row, column, colspan, rowspan)

    def addAutoEntry(
            self,
            title,
            words,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        ent = self.__buildEntry(
            title,
            self.__getContainer(),
            secret=False,
            words=words)
        self.__positionWidget(ent, row, column, colspan, rowspan)

    def __validateNumericEntry(
            self,
            action,
            index,
            value_if_allowed,
            prior_value,
            text,
            validation_type,
            trigger_type,
            widget_name):
        if action == "1":
            if text in '0123456789.-+':
                try:
                    if len(value_if_allowed) == 1 and value_if_allowed in '.-':
                        return True
                    elif len(value_if_allowed) == 2 and value_if_allowed == '-.':
                        return True
                    else:
                        float(value_if_allowed)
                        return True
                except ValueError:
                    self.containerStack[0]['container'].bell()
                    return False
            else:
                self.containerStack[0]['container'].bell()
                return False
        else:
            return True

    def addNumericEntry(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            secret=False):
        ent = self.__buildEntry(title, self.__getContainer(), secret)
        self.__positionWidget(ent, row, column, colspan, rowspan)

        if self.validateNumeric is None:
            self.validateNumeric = (self.containerStack[0]['container'].register(
                self.__validateNumericEntry), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        ent.isNumeric = True
        ent.config(validate='key', validatecommand=self.validateNumeric)
        self.setEntryTooltip(title, "Numeric data only.")

    def addLabelNumericEntry(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            secret=False):
        self. addNumericLabelEntry(
            title, row, column, colspan, rowspan, secret)

    def addNumericLabelEntry(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            secret=False):
        frame = self.__getLabelBox(title)
        ent = self.__buildEntry(title, frame, secret)
        self.__packLabelBox(frame, ent)
        self.__positionWidget(frame, row, column, colspan, rowspan)

        if self.validateNumeric is None:
            self.validateNumeric = (self.containerStack[0]['container'].register(
                self.__validateNumericEntry), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        ent.isNumeric = True
        ent.config(validate='key', validatecommand=self.validateNumeric)
        self.setEntryTooltip(title, "Numeric data only.")

    def addSecretEntry(self, title, row=None, column=0, colspan=0, rowspan=0):
        self.addEntry(title, row, column, colspan, rowspan, True)

    def addLabelEntry(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            secret=False):
        frame = self.__getLabelBox(title)
        ent = self.__buildEntry(title, frame, secret)
        self.__packLabelBox(frame, ent)
        self.__positionWidget(frame, row, column, colspan, rowspan)

    def addLabelSecretEntry(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.addSecretLabelEntry(title, row, column, colspan, rowspan)

    def addSecretLabelEntry(
            self,
            title,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.addLabelEntry(title, row, column, colspan, rowspan, True)

    def getEntry(self, name):
        self.__verifyItem(self.n_entryVars, name)
        entry = self.__verifyItem(self.n_entries, name)
        if entry.showingDefault:
            if entry.isNumeric:
                return 0
            else:
                return ""
        else:
            val = self.n_entryVars[name].get()
            if entry.isNumeric:
                if len(val) == 0 or (len(val) == 1 and val in '.-') or (len(val) == 2 and val == "-."):
                    return 0
                else:
                    return float(val)
            else:
                return val

    def setEntry(self, name, text):
        self.__verifyItem(self.n_entryVars, name)
        self.__updateEntryDefault(name, mode="set")
        self.n_entryVars[name].set(text)

    def __entryIn(self, name):
        self.__updateEntryDefault(name, "in")

    def __entryOut(self, name):
        self.__updateEntryDefault(name, "out")

    def __updateEntryDefault(self, name, mode=None):
        self.__verifyItem(self.n_entryVars, name)
        entry = self.__verifyItem(self.n_entries, name)

        # ignore this if no default to apply
        if entry.default == "":
            return

        current = self.n_entryVars[name].get()

        # clear & remove default 
        if mode == "set" or (mode in [ "in", "clear"] and entry.showingDefault):
            self.n_entryVars[name].set("")
            entry.showingDefault = False
            entry.config(justify=entry.oldJustify, foreground=entry.oldFg)
        elif mode == "out" and current == "":
            self.n_entryVars[name].set(entry.default)
            entry.config(justify='center', foreground='grey')
            entry.showingDefault = True

    def updateDefaultText(self, name, text):
        self.__verifyItem(self.n_entryVars, name)
        entry = self.__verifyItem(self.n_entries, name)
        current = self.n_entryVars[name].get()

        if entry.showingDefault:
            self.n_entryVars[name].set(text)
        entry.default = text

    def setEntryDefault(self, name, text="default"):
        entry = self.__verifyItem(self.n_entries, name)
        self.__verifyItem(self.n_entryVars, name)

        # remember current settings - to return to
        entry.oldJustify = entry.cget('justify')
        entry.oldFg = entry.cget('foreground')
        entry.config(justify='center', foreground='grey')

        # show the new text
        self.n_entryVars[name].set(text)
        entry.showingDefault = True
        entry.default = text
        entry.DEFAULT_TEXT = text

        # bind commands to show/remove the default
        in_command = self.MAKE_FUNC(self.__entryIn, name, True)
        out_command = self.MAKE_FUNC(self.__entryOut, name, True)
        entry.bind("<FocusIn>", in_command, add="+")
        entry.bind("<FocusOut>", out_command, add="+")

    def clearEntry(self, name):
        self.__verifyItem(self.n_entryVars, name)
        self.n_entryVars[name].set("")
        self.__updateEntryDefault(name, mode="clear")
        self.setFocus(name)

    def clearAllEntries(self):
        for entry in self.n_entryVars:
            self.n_entryVars[entry].set("")
            self.__updateEntryDefault(entry, mode="clear")

    def setFocus(self, name):
        self.__verifyItem(self.n_entries, name)
        self.n_entries[name].focus_set()

    def __lookupValue(self, myDict, val):
        for name in myDict:
            if isinstance(myDict[name], type([])):  # array of cbs
                for rb in myDict[name]:
                    if rb == val:
                        return name
            else:
                if myDict[name] == val:
                    return name
        return None

    def __getWidgetName(self, widg):
        name = widg.__class__.__name__
        if name.lower() == "tk":
            return self.__getTopLevel().title()
        elif name == "Listbox":
            return self.__lookupValue(self.n_lbs, widg)
        elif name == "Button":
            # merge together Buttons & Toolbar Buttons
            z = self.n_buttons.copy()
            z.update(self.n_tbButts)
            return self.__lookupValue(z, widg)
        elif name == "Entry":
            return self.__lookupValue(self.n_entries, widg)
        elif name == "Scale":
            return self.__lookupValue(self.n_scales, widg)
        elif name == "Checkbutton":
            return self.__lookupValue(self.n_cbs, widg)
        elif name == "Radiobutton":
            return self.__lookupValue(self.n_rbs, widg)
        elif name == "Spinbox":
            return self.__lookupValue(self.n_spins, widg)
        elif name == "OptionMenu":
            return self.__lookupValue(self.n_options, widg)
        elif name == "Text":
            return self.__lookupValue(self.n_textAreas, widg)
        elif name == "Link":
            return self.__lookupValue(self.n_links, widg)
        else:
            raise Exception("Unknown widget type: " + name)

    def getFocus(self):
        widg = self.topLevel.focus_get()
        return self.__getWidgetName(widg)

#####################################
# FUNCTIONS for progress bars (meters)
#####################################
    def addMeter(self, name, row=None, column=0, colspan=0, rowspan=0):
        self.__addMeter(name, "METER", row, column, colspan, rowspan)

    def addSplitMeter(self, name, row=None, column=0, colspan=0, rowspan=0):
        self.__addMeter(name, "SPLIT", row, column, colspan, rowspan)

    def addDualMeter(self, name, row=None, column=0, colspan=0, rowspan=0):
        self.__addMeter(name, "DUAL", row, column, colspan, rowspan)

    def __addMeter(
            self,
            name,
            type="METER",
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.__verifyItem(self.n_meters, name, True)

        if type == "SPLIT":
            meter = SplitMeter(self.__getContainer(), font=self.meterFont)
        elif type == "DUAL":
            meter = DualMeter(self.__getContainer(), font=self.meterFont)
        else:
            meter = Meter(self.__getContainer(), font=self.meterFont)

        self.n_meters[name] = meter
        self.__positionWidget(meter, row, column, colspan, rowspan)

    def getMeter(self, name):
        item = self.__verifyItem(self.n_meters, name)
        return item.get()

    # update the value of the specified meter
    # note: expects a value between 0 (-100 for split/dual) & 100
    def setMeter(self, name, value=0.0, text=None):
        item = self.__verifyItem(self.n_meters, name)
        value = value / 100.0
        item.set(value, text)

    # a single colour for meters, a list of 2 colours for splits & duals
    def setMeterFill(self, name, colour):
        item = self.__verifyItem(self.n_meters, name)
        if item.__class__.__name__ == "Meter":
            item.configure(fill=colour)
        else:
            item.setFill(colour)

#####################################
# FUNCTIONS for seperators
#####################################
    def addSeparator(
            self,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            colour=None):
        self.warn(
            ".addSeparator() is deprecated. You should be using .addHorizontalSeparator() or .addVerticalSeparator()")
        self.addHorizontalSeparator(row, column, colspan, rowspan, colour)

    def addHorizontalSeparator(
            self,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            colour=None):
        self.__addSeparator(
            "horizontal",
            row,
            column,
            colspan,
            rowspan,
            colour)

    def addVerticalSeparator(
            self,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            colour=None):
        self.__addSeparator("vertical", row, column, colspan, rowspan, colour)

    def __addSeparator(
            self,
            orient,
            row=None,
            column=0,
            colspan=0,
            rowspan=0,
            colour=None):
        sep = Separator(self.__getContainer(), orient)
        if colour is not None:
            sep.configure(fg=colour)
        self.n_separators.append(sep)
        self.__positionWidget(sep, row, column, colspan, rowspan)

#####################################
# FUNCTIONS for pie charts
#####################################
    def addPieChart(
            self,
            name,
            fracs,
            row=None,
            column=0,
            colspan=0,
            rowspan=0):
        self.__verifyItem(self.n_pieCharts, name, True)
        pie = PieChart(self.__getContainer(), fracs, self.__getContainerBg())
        self.n_pieCharts[name] = pie
        self.__positionWidget(pie, row, column, colspan, rowspan, sticky=None)

    def setPieChart(self, title, name, value):
        pie = self.__verifyItem(self.n_pieCharts, title)
        pie.setValue(name, value)

#####################################
# FUNCTIONS for tool bar
#####################################
    # adds a list of buttons along the top - like a tool bar...
    def addToolbar(self, names, funcs, findIcon=False):
        if not self.hasTb:
            self.hasTb = True

        image = None
        singleFunc = self.__checkFunc(names, funcs)
        if not isinstance(names, list):
            names = [names]

        for i in range(len(names)):
            t = names[i]
            if (t in self.n_tbButts):
                raise Exception(
                    "Invalid toolbar button name: " +
                    t +
                    " already exists")

            if findIcon:
                # turn off warnings about PNGs
                myWarn = self.__pauseWarn()
                imgFile = os.path.join(self.icon_path, t.lower() + ".png")
                try:
                    image = self.__getImage(imgFile)
                except Exception as e:
                    image = None
                self.__resumeWarn(myWarn)

            but = Button(self.tb)
            self.n_tbButts[t] = but

            if singleFunc is not None:
                u = self.MAKE_FUNC(singleFunc, t)
            else:
                u = self.MAKE_FUNC(funcs[i], t)

            but.config(text=t, command=u, relief=FLAT, font=self.tbFont)
            if image is not None:
                but.image = image
                # works on Mac & Windows :)
                but.config(image=image, compound=TOP, text="", justify=LEFT)
            but.pack(side=LEFT, padx=2, pady=2)
            but.tt_var = self.__addTooltip(but, t.title(), True)

    def setToolbarIcon(self, name, icon):
        if (name not in self.n_tbButts):
            raise Exception("Unknown toolbar name: " + name)
        imgFile = os.path.join(self.icon_path, icon.lower() + ".png")
        myWarn = self.__pauseWarn()
        self.setToolbarImage(name, imgFile)
        self.__resumeWarn(myWarn)
        self.n_tbButts[name].tt_var.set(icon)

    def setToolbarImage(self, name, imgFile):
        if (name not in self.n_tbButts):
            raise Exception("Unknown toolbar name: " + name)
        image = self.__getImage(imgFile)
        self.n_tbButts[name].config(image=image)
        self.n_tbButts[name].image = image

    def setToolbarButtonEnabled(
        self, name): self.setToolbarButtonDisabled(
        name, False)

    def setToolbarButtonDisabled(self, name, disabled=True):
        if (name not in self.n_tbButts):
            raise Exception("Unknown toolbar name: " + name)
        if disabled:
            self.n_tbButts[name].config(state=DISABLED)
        else:
            self.n_tbButts[name].config(state=NORMAL)

    def setToolbarEnabled(self): self.setToolbarDisabled(False)

    def setToolbarDisabled(self, disabled=True):
        for but in self.n_tbButts.keys():
            if disabled:
                self.n_tbButts[but].config(state=DISABLED)
            else:
                self.n_tbButts[but].config(state=NORMAL)

    # functions to hide & show the toolbar
    def hideToolbar(self):
        if self.hasTb:
            self.tb.pack_forget()

    def showToolbar(self):
        if self.hasTb:
            self.tb.pack(before=self.containerStack[0][
                         'container'], side=TOP, fill=X)

#####################################
# FUNCTIONS for menu bar
#####################################
    def __initMenu(self):
        # create a menu bar - only shows if populated
        if not self.hasMenu:
            #            self.topLevel.option_add('*tearOff', FALSE)
            self.hasMenu = True
            self.menuBar = Menu(self.topLevel)
            if self.platform == self.MAC:
                appmenu = Menu(self.menuBar, name='apple')
                self.menuBar.add_cascade(menu=appmenu)
                self.n_menus["MAC_APP"] = appmenu
            elif self.platform == self.WINDOWS:
                # sysMenu must be added last, otherwise other menus vanish
                sysMenu = Menu(self.menuBar, name='system', tearoff=False)
                self.n_menus["WIN_SYS"] = sysMenu

    # add a parent menu, for menu items
    def createMenu(self, title, tearable=False, showInBar=True):
        self.__verifyItem(self.n_menus, title, True)
        self.__initMenu()
        if self.platform == self.MAC and tearable:
            self.warn("Tearable menus (" + title + ") not supported on MAC")
            tearable = False
        theMenu = Menu(self.menuBar, tearoff=tearable)
        if showInBar:
            self.menuBar.add_cascade(label=title, menu=theMenu)
        self.n_menus[title] = theMenu
        return theMenu

    def createRightClickMenu(self, title, showInBar=False):
        men = self.createMenu(title, False, showInBar)
        if gui.GET_PLATFORM() == gui.LINUX:
            self.addMenuSeparator(title)
        return men

    # add items to the named menu
    def addMenuItem(
            self,
            title,
            item,
            func=None,
            kind=None,
            shortcut=None,
            underline=-1,
            rb_id=None,
            createBinding=True):
        # set the initial menubar
        self.__initMenu()

        # get or create an initial menu
        if title is not None:
            try:
                theMenu = self.__verifyItem(self.n_menus, title, False)
            except:
                theMenu = self.createMenu(title)

        if underline > -1 and self.platform == self.MAC:
            self.warn("Underlining menu items not available on MAC")

        if func is not None:
            u = self.MAKE_FUNC(func, item, True)
        else:
            u = None

        a = b = None
        if shortcut is not None:
            #            MODIFIERS=["Control", "Ctrl", "Option", "Opt", "Alt", "Shift", "Command", "Cmd", "Meta"]

            # UGLY formatting of accelerator & shortcut
            a = b = shortcut.lower().replace("+", "-")

            a = a.replace("control", "ctrl")
            a = a.replace("command", "cmd")
            a = a.replace("option", "opt")

            b = b.replace("ctrl", "Control")
            b = b.replace("control", "Control")
            b = b.replace("cmd", "Command")
            b = b.replace("command", "Command")
            b = b.replace("option", "Option")
            b = b.replace("opt", "Option")
            b = b.replace("alt", "Alt")
            b = b.replace("shift", "Shift")
            b = b.replace("meta", "Meta")

            if gui.GET_PLATFORM() != gui.MAC:
                a = a.replace("cmd", "ctrl")
                b = b.replace("Command", "Control")

            b = "<" + b + ">"
            a = a.title()

            self.__verifyItem(self.n_accelerators, a, True)
            self.n_accelerators.append(a)
            if u is not None and createBinding:
                self.topLevel.bind_all(b, u)

        if item == "-" or kind == "separator":
            theMenu.add_separator()
        elif kind == "topLevel" or title is None:
            if self.platform == self.MAC:
                self.warn(
                    "Unable to make topLevel menus (" + item + ") on Mac")
            else:
                self.menuBar.add_command(
                    label=item, command=u, accelerator=a, underline=underline)
        elif kind == "rb":
            varName = title + "rb" + item
            newRb = False
            if (varName in self.n_menuVars):
                var = self.n_menuVars[varName]
            else:
                newRb = True
                var = StringVar(self.topLevel)
                self.n_menuVars[varName] = var
            theMenu.add_radiobutton(
                label=rb_id,
                command=u,
                variable=var,
                value=rb_id,
                accelerator=a,
                underline=underline)
            if newRb:
                self.setMenuRadioButton(title, item, rb_id)
        elif kind == "cb":
            varName = title + "cb" + item
            self.__verifyItem(self.n_menuVars, varName, True)
            var = StringVar(self.topLevel)
            self.n_menuVars[varName] = var
            theMenu.add_checkbutton(
                label=item,
                command=u,
                variable=var,
                onvalue=1,
                offvalue=0,
                accelerator=a,
                underline=underline)
        elif kind == "sub":
            self.__verifyItem(self.n_menus, item, True)
            subMenu = Menu(theMenu, tearoff=False)
            self.n_menus[item] = subMenu
            theMenu.add_cascade(menu=subMenu, label=item)
        else:
            theMenu.add_command(
                label=item,
                command=u,
                accelerator=a,
                underline=underline)

    #################
    # wrappers for other menu types

    def addMenuList(self, menuName, names, funcs):
        # deal with a dict_keys object - messy!!!!
        if not isinstance(names, list):
            names = list(names)

        # append some Nones, if it's a list and contains separators
        if funcs is not None:
            if not callable(funcs):
                seps = names.count("-")
                for i in range(seps):
                    funcs.append(None)
            singleFunc = self.__checkFunc(names, funcs)

        # add menu items
        for t in names:
            if funcs is None:
                u = None
            elif singleFunc is not None:
                u = singleFunc
            else:
                u = funcs.pop(0)

            self.addMenuItem(menuName, t, u)

    def __checkCopyAndPaste(self, event, widget=None):
        if self.copyAndPaste.inUse:
            if event is None or not (
                    event.type == "10" and self.GET_PLATFORM() == self.LINUX):
                self.disableMenu("EDIT", 10)

            if event is not None:
                widget = event.widget

            # 9 = ENTER/10 = LEAVE/4=RCLICK/3=PRESS/2=PASTE
            if event is None or event.type in ["9", "3", "4", "2"]:
                self.copyAndPaste.setUp(widget)
                if self.copyAndPaste.canCopy:
                    self.enableMenuItem("EDIT", "Copy")
                if self.copyAndPaste.canCut:
                    self.enableMenuItem("EDIT", "Cut")
                if self.copyAndPaste.canPaste:
                    self.enableMenuItem("EDIT", "Paste")
                    self.enableMenuItem("EDIT", "Clear Clipboard")
                if self.copyAndPaste.canSelect:
                    self.enableMenuItem("EDIT", "Select All")
                    self.enableMenuItem("EDIT", "Clear All")
                if self.copyAndPaste.canUndo:
                    self.enableMenuItem("EDIT", "Undo")
                if self.copyAndPaste.canRedo:
                    self.enableMenuItem("EDIT", "Redo")
            return True
        else:
            return False

    def __copyAndPasteHelper(self, menu):
        widget = self.topLevel.focus_get()
        self.copyAndPaste.setUp(widget)

        if menu == "Cut":
            self.copyAndPaste.cut()
        elif menu == "Copy":
            self.copyAndPaste.copy()
        elif menu == "Paste":
            self.copyAndPaste.paste()
        elif menu == "Select All":
            self.copyAndPaste.selectAll()
        elif menu == "Clear Clipboard":
            self.copyAndPaste.clearClipboard()
        elif menu == "Clear All":
            self.copyAndPaste.clearText()
        elif menu == "Undo":
            self.copyAndPaste.undo()
        elif menu == "Redo":
            self.copyAndPaste.redo()

    # add a single entry for a menu
    def addSubMenu(self, menu, subMenu):
        self.addMenuItem(menu, subMenu, None, "sub")

    def addMenu(self, name, func, shortcut=None, underline=-1):
        self.addMenuItem(None, name, func, "topLevel", shortcut, underline)

    def addMenuSeparator(self, menu):
        self.addMenuItem(menu, "-")

    def addMenuCheckBox(
            self,
            menu,
            name,
            func=None,
            shortcut=None,
            underline=-1):
        self.addMenuItem(menu, name, func, "cb", shortcut, underline)

    def addMenuRadioButton(
            self,
            menu,
            name,
            value,
            func=None,
            shortcut=None,
            underline=-1):
        self.addMenuItem(menu, name, func, "rb", shortcut, underline, value)

    #################
    # wrappers for setters

    def __setMenu(self, menu, title, value, kind):
        title = menu + kind + title
        var = self.__verifyItem(self.n_menuVars, title)
        if kind == "rb":
            var.set(value)
        elif kind == "cb":
            if value is True:
                var.set("1")
            elif value is False:
                var.set("0")
            else:
                if var.get() == "1":
                    var.set("0")
                else:
                    var.set("1")

    def setMenuCheckBox(self, menu, name, value=None):
        self.__setMenu(menu, name, value, "cb")

    def setMenuRadioButton(self, menu, name, value):
        self.__setMenu(menu, name, value, "rb")

    # set align = "none" to remove text
    def setMenuImage(self, menu, title, image, align="left"):
        theMenu = self.__verifyItem(self.n_menus, menu)
        imageObj = self.__getImage(image)
        if 16 != imageObj.width() or imageObj.width() != imageObj.height():
            self.warn("Invalid image resolution for menu item " +
                      title + " (" + image + ") - should be 16x16")
            #imageObj = imageObj.subsample(2,2)
        theMenu.entryconfigure(title, image=imageObj, compound=align)

    def setMenuIcon(self, menu, title, icon, align="left"):
        image = os.path.join(self.icon_path, icon.lower() + ".png")
        myWarn = self.__pauseWarn()
        self.setMenuImage(menu, title, image, align)
        self.__resumeWarn(myWarn)

    def disableMenubar(self):
        for theMenu in self.n_menus:
            self.disableMenu(theMenu)

        # loop through top level menus
        # and diable any that got missed
        numMenus = self.menuBar.index("end")
        if numMenus is not None:
            for item in range(numMenus+1):
                self.menuBar.entryconfig(item, state=DISABLED)

    def enableMenubar(self):
        for theMenu in self.n_menus:
            self.enableMenu(theMenu)

        # loop through toplevel menus
        # and enable anythat got missed
        numMenus = self.menuBar.index("end")
        if numMenus is not None:
            for item in range(numMenus+1):
                self.menuBar.entryconfig(item, state=NORMAL)

    def disableMenu(
        self,
        title,
        limit=None): self.__changeMenuState(
        title,
        DISABLED,
        limit)

    def enableMenu(
        self,
        title,
        limit=None): self.__changeMenuState(
        title,
        NORMAL,
        limit)

    def __changeMenuState(self, title, state, limit=None):
        theMenu = self.__verifyItem(self.n_menus, title)
        numMenus = theMenu.index("end")
        if numMenus is not None:  # MAC_APP (and others?) returns None
            for item in range(numMenus + 1):
                if limit is not None and limit == item:
                    break
                try:
                    theMenu.entryconfigure(item, state=state)
                except:
                    pass  # separator
        # also diable the toplevel menu that matches this one
        try:
            self.menuBar.entryconfig(self.menuBar.index(title), state=state)
        except TclError:
            # ignore if we fail...
            pass

    def disableMenuItem(self, title, item):
        theMenu = self.__verifyItem(self.n_menus, title)
        theMenu.entryconfigure(item, state=DISABLED)

    def enableMenuItem(self, title, item):
        theMenu = self.__verifyItem(self.n_menus, title)
        theMenu.entryconfigure(item, state=NORMAL)

    #################
    # wrappers for getters

    def __getMenu(self, menu, title, kind):
        title = menu + kind + title
        var = self.__verifyItem(self.n_menuVars, title)
        if kind == "rb":
            return var.get()
        elif kind == "cb":
            if var.get() == "1":
                return True
            else:
                return False

    def getMenuCheckBox(self, menu, title):
        return self.__getMenu(menu, title, "cb")

    def getMenuRadioButton(self, menu, title):
        return self.__getMenu(menu, title, "rb")

    #################
    # wrappers for platform specific menus

    # enables the preferences item in the app menu
    def addMenuPreferences(self, func):
        if self.platform == self.MAC:
            self.__initMenu()
            u = self.MAKE_FUNC(func, "preferences")
            self.topLevel.createcommand('tk::mac::ShowPreferences', u)
        else:
            self.warn("The Preferences Menu is specific to Mac OSX")

    # MAC help mnenu
    def addMenuHelp(self, func):
        if self.platform == self.MAC:
            self.__initMenu()
            helpMenu = Menu(self.menuBar, name='help')
            self.menuBar.add_cascade(menu=helpMenu, label='Help')
            u = self.MAKE_FUNC(func, "help")
            self.topLevel.createcommand('tk::mac::ShowHelp', u)
            self.n_menus["MAC_HELP"] = helpMenu
        else:
            self.warn("The Help Menu is specific to Mac OSX")

    # Shows a Window menu
    def addMenuWindow(self):
        if self.platform == self.MAC:
            self.__initMenu()
            windowMenu = Menu(self.menuBar, name='window')
            self.menuBar.add_cascade(menu=windowMenu, label='Window')
            self.n_menus["MAC_WIN"] = windowMenu
        else:
            self.warn("The Window Menu is specific to Mac OSX")

    # adds an edit menu - by default only as a pop-up
    # if inMenuBar is True - then show in menu too
    def addMenuEdit(self, inMenuBar=False):
        self.__initMenu()
        editMenu = Menu(self.menuBar, tearoff=False)
        if inMenuBar:
            self.menuBar.add_cascade(menu=editMenu, label='Edit ')
        self.n_menus["EDIT"] = editMenu
        self.copyAndPaste.inUse = True

        if gui.GET_PLATFORM() == gui.LINUX:
            self.addMenuSeparator("EDIT")

        if gui.GET_PLATFORM() == gui.MAC:
            shortcut = "Cmd+"
        else:
            shortcut = "Control-"

        eList = [
            ('Cut',
             lambda e: self.__copyAndPasteHelper("Cut"),
             "X",
             False),
            ('Copy',
             lambda e: self.__copyAndPasteHelper("Copy"),
             "C",
             False),
            ('Paste',
             lambda e: self.__copyAndPasteHelper("Paste"),
             "V",
             False),
            ('Select All',
             lambda e: self.__copyAndPasteHelper("Select All"),
             "A",
             True if gui.GET_PLATFORM() == gui.MAC else False),
            ('Clear Clipboard',
             lambda e: self.__copyAndPasteHelper("Clear Clipboard"),
             "B",
             True)]

        for (txt, cmd, sc, bind) in eList:
            acc = shortcut + sc
            self.addMenuItem(
                "EDIT",
                txt,
                cmd,
                shortcut=acc,
                createBinding=bind)

        # add a clear option
        self.addMenuSeparator("EDIT")
        self.addMenuItem(
            "EDIT",
            "Clear All",
            lambda e: self.__copyAndPasteHelper("Clear All"))

        self.addMenuSeparator("EDIT")
        self.addMenuItem(
            "EDIT",
            'Undo',
            lambda e: self.__copyAndPasteHelper("Undo"),
            shortcut=shortcut + "Z",
            createBinding=False)
        self.addMenuItem("EDIT", 'Redo', lambda e: self.__copyAndPasteHelper(
            "Redo"), shortcut="Shift-" + shortcut + "Z", createBinding=True)
        self.disableMenu("EDIT")

    def appJarAbout(self, menu=None):
        self.infoBox("About appJar", "appJar\nCopyright Richard Jarvis, 2016")

    def appJarHelp(self, menu=None):
        self.infoBox("appJar Help", "For help, visit http://appJar.info")

    def addAppJarMenu(self):
        if self.platform == self.MAC:
            self.addMenuItem("MAC_APP", "About appJar", self.appJarAbout)
            self.addMenuWindow()
            self.addMenuHelp(self.appJarHelp)
        elif self.platform == self.WINDOWS:
            self.addMenuSeparator('WIN_SYS')
            self.addMenuItem("WIN_SYS", "About appJar", self.appJarAbout)
            self.addMenuItem("WIN_SYS", "appJar Help", self.appJarHelp)

#####################################
# FUNCTIONS for status bar
#####################################
    def addStatus(self, header="", fields=1, side=None):
        self.warn("addStatus() is deprecated, please use addStatusbar()")
        self.addStatusbar(header, fields, side)

    def addStatusbar(self, header="", fields=1, side=None):
        self.hasStatus = True
        self.header = header
        self.statusFrame = Frame(self.appWindow)
        self.statusFrame.config(bd=1, relief=SUNKEN)
        self.statusFrame.pack(side=BOTTOM, fill=X, anchor=S)

        self.status = []
        for i in range(fields):
            self.status.append(Label(self.statusFrame))
            self.status[i].config(
                bd=1,
                relief=SUNKEN,
                anchor=W,
                font=self.statusFont,
                width=10)
            self.__addTooltip(self.status[i], "Status bar", True)

            if side == "LEFT":
                self.status[i].pack(side=LEFT)
            elif side == "RIGHT":
                self.status[i].pack(side=RIGHT)
            else:
                self.status[i].pack(side=LEFT, expand=1, fill=BOTH)

    def setStatus(self, text, field=0):
        self.warn("setStatus() is deprecated, please use setStatusbar()")
        self.setStatusbar(text, field)

    def setStatusbar(self, text, field=0):
        if self.hasStatus:
            if field is None:
                for status in self.status:
                    status.config(text=self.__getFormatStatus(text))
            elif field >= 0 and field < len(self.status):
                self.status[field].config(text=self.__getFormatStatus(text))
            else:
                raise Exception("Invalid status field: " + str(field) +
                                ". Must be between 0 and " + str(len(self.status) - 1))

    def setStatusBg(self, colour, field=None):
        self.warn("setStatusBg() is deprecated, please use setStatusbarBg()")
        self.setStatusbarBg(colour, field)

    def setStatusbarBg(self, colour, field=None):
        if self.hasStatus:
            if field is None:
                for status in self.status:
                    status.config(background=colour)
            elif field >= 0 and field < len(self.status):
                self.status[field].config(background=colour)
            else:
                raise Exception("Invalid status field: " + str(field) +
                                ". Must be between 0 and " + str(len(self.status) - 1))

    def setStatusbarFg(self, colour, field=None):
        if self.hasStatus:
            if field is None:
                for status in self.status:
                    status.config(foreground=colour)
            elif field >= 0 and field < len(self.status):
                self.status[field].config(foreground=colour)
            else:
                raise Exception("Invalid status field: " + str(field) +
                                ". Must be between 0 and " + str(len(self.status) - 1))

    def setStatusbarWidth(self, width, field=None):
        if self.hasStatus:
            if field is None:
                for status in self.status:
                    status.config(width=width)
            elif field >= 0 and field < len(self.status):
                self.status[field].config(width=width)
            else:
                raise Exception("Invalid status field: " + str(field) +
                                ". Must be between 0 and " + str(len(self.status) - 1))

    def clearStatusbar(self, field=None):
        if self.hasStatus:
            if field is None:
                for status in self.status:
                    status.config(text=self.__getFormatStatus(""))
            elif field >= 0 and field < len(self.status):
                self.status[field].config(text=self.__getFormatStatus(""))
            else:
                raise Exception("Invalid status field: " + str(field) +
                                ". Must be between 0 and " + str(len(self.status) - 1))

    # formats the string shown in the status bar
    def __getFormatStatus(self, text):
        text = str(text)
        if len(text) == 0:
            return ""
        elif len(self.header) == 0:
            return text
        else:
            return self.header + ": " + text
#####################################
# TOOLTIPS
#####################################

    def __addTooltip(self, item, text, hideWarn=False):
        if TOOLTIP_AVAILABLE:
            # turn off warnings about tooltips
            if hideWarn:
                myWarn = self.__pauseWarn()
            var = StringVar(self.topLevel)
            var.set(text)
            tip = ToolTip(item, delay=500, follow_mouse=1, textvariable=var)
            item.tooltip = tip
            if hideWarn:
                self.__resumeWarn(myWarn)
            return var
        elif not hideWarn:
            self.warn(
                "ToolTips unavailable - check tooltip.py is in the lib folder")

#####################################
# FUNCTIONS to show pop-up dialogs
#####################################
    def infoBox(self, title, message):
        self.topLevel.update_idletasks()
        messagebox.showinfo(title, message)
        self.__bringToFront()

    def errorBox(self, title, message):
        self.topLevel.update_idletasks()
        messagebox.showerror(title, message)
        self.__bringToFront()

    def warningBox(self, title, message):
        self.topLevel.update_idletasks()
        messagebox.showwarning(title, message)
        self.__bringToFront()

    def yesNoBox(self, title, message):
        self.topLevel.update_idletasks()
        return messagebox.askyesno(title, message)

    def questionBox(self, title, message):
        self.topLevel.update_idletasks()
        return messagebox.askquestion(title, message)

    def okBox(self, title, message):
        self.topLevel.update_idletasks()
        return messagebox.askokcancel(title, message)

    def retryBox(self, title, message):
        self.topLevel.update_idletasks()
        return messagebox.askretrycancel(title, message)

    def openBox(
            self,
            title=None,
            fileName=None,
            dirName=None,
            fileExt=".txt",
            fileTypes=None,
            asFile=False):
        self.topLevel.update_idletasks()
        if fileTypes is None:
            fileTypes = [('all files', '.*'), ('text files', '.txt')]
        # define options for opening
        options = {}
        options['defaultextension'] = fileExt
        options['filetypes'] = fileTypes
        options['initialdir'] = dirName
        options['initialfile'] = fileName
        options['title'] = title

        if asFile:
            return filedialog.askopenfile(mode="r", **options)
        # will return "" if cancelled
        else:
            return filedialog.askopenfilename(**options)

    def saveBox(
            self,
            title=None,
            fileName=None,
            dirName=None,
            fileExt=".txt",
            fileTypes=None,
            asFile=False):
        self.topLevel.update_idletasks()
        if fileTypes is None:
            fileTypes = [('all files', '.*'), ('text files', '.txt')]
        # define options for opening
        options = {}
        options['defaultextension'] = fileExt
        options['filetypes'] = fileTypes
        options['initialdir'] = dirName
        options['initialfile'] = fileName
        options['title'] = title

        if asFile:
            return filedialog.asksaveasfile(mode='w', **options)
        # will return "" if cancelled
        else:
            return filedialog.asksaveasfilename(**options)

    def directoryBox(self, title=None, dirName=None):
        self.topLevel.update_idletasks()
        options = {}
        options['initialdir'] = dirName
        options['title'] = title
        options['mustexist'] = False
        file = filedialog.askdirectory(**options)
        if file == "":
            return None
        else:
            return file

    def colourBox(self, colour='#ff0000'):
        self.topLevel.update_idletasks()
        col = askcolor(colour)
        if col[1] is None:
            return None
        else:
            return col[1]

    def textBox(self, title, question):
        self.topLevel.update_idletasks()
        return TextDialog(self.topLevel, title, question).result

    def numberBox(self, title, question): self.numBox(title, question)

    def numBox(self, title, question):
        self.topLevel.update_idletasks()
        return NumDialog(self.topLevel, title, question).result

#####################################
# ProgressBar Class
# from: http://tkinter.unpythonic.net/wiki/ProgressMeter
#####################################


class Meter(Frame):

    def __init__(
            self,
            master,
            width=100,
            height=20,
            bg='white',
            fillColour='orchid1',
            value=0.0,
            text=None,
            font=None,
            textColour='black',
            *args,
            **kw):
        Frame.__init__(
            self,
            master,
            bg=bg,
            width=width,
            height=height,
            *args,
            **kw)
        self._value = value
        self.config(relief='ridge', bd=3)

#            self._canv = Canvas(self, bg=self['bg'], height=self['height'], highlightthickness=0, relief='flat', bd=0)
        self._canv = Canvas(
            self,
            bg=self['bg'],
            width=self['width'],
            height=self['height'],
            highlightthickness=0,
            relief='flat',
            bd=0)
        self._canv.pack(fill='both', expand=1)
        self._rect = self._canv.create_rectangle(
            0, 0, 0, self._canv.winfo_reqheight(), fill=fillColour, width=0)
        self._text = self._canv.create_text(
            self._canv.winfo_reqwidth() / 2,
            self._canv.winfo_reqheight() / 2,
            text='',
            fill=textColour)
        if font:
            self._canv.itemconfigure(self._text, font=font)

        self.set(value, text)
        self.bind('<Configure>', self._update_coords)

    def config(self, cnf=None, **kw):
        self.configure(cnf, **kw)

    def configure(self, cnf=None, **kw):
        # properties to propagate to CheckBoxes
        kw = gui.CLEAN_CONFIG_DICTIONARY(**kw)

        if "fill" in kw:
            self._canv.itemconfigure(self._rect, fill=kw.pop("fill"))
        if "fg" in kw:
            self._canv.itemconfigure(self._text, fill=kw.pop("fg"))
        if "backfill" in kw:
            self._canv.config(bg=kw.pop("backfill"))
        if "width" in kw:
            self._canv.config(width=kw.pop("width"))
        if "height" in kw:
            self._canv.config(height=kw.pop("height"))

        # propagate anything left
        if PYTHON2:
            Frame.config(self, cnf, **kw)
        else:
            super(Frame, self).config(cnf, **kw)

    def _update_coords(self, event):
        '''Updates the position of the text and rectangle inside the canvas when the size of the widget gets changed.'''
        self._setCanvas()

    def _setCanvas(self):
        # looks like we have to call update_idletasks() twice to make sure
        # to get the results we expect
        self._canv.update_idletasks()
        self._canv.coords(
            self._text,
            self._canv.winfo_width() / 2,
            self._canv.winfo_height() / 2)
        self._canv.coords(
            self._rect,
            0,
            0,
            self._canv.winfo_width() *
            self._value,
            self._canv.winfo_height())
        self._canv.update_idletasks()

    def get(self):
        val = self._value
        try:
            txt = self._canv.itemcget(self._text, 'text')
        except:
            txt = None
        return val, txt

    def set(self, value=0.0, text=None):
        # make the value failsafe:
        if value < 0.0:
            value = 0.0
        elif value > 1.0:
            value = 1.0
        self._value = value

        # if no text is specified use the default percentage string:
        if text is None:
            text = str(int(round(100 * value))) + ' %'

        self._canv.coords(
            self._rect,
            0,
            0,
            self._canv.winfo_width() *
            value,
            self._canv.winfo_height())
        self._canv.itemconfigure(self._text, text=text)
        self._canv.update_idletasks()

    def tint(self, col, brightness_offset=1):
        ''' dim or brighten the specified colour by the specified offset '''
        # http://chase-seibert.github.io/blog/2011/07/29/python-calculate-lighterdarker-rgb-colors.html
        rgb_hex = self._canv.winfo_rgb(col)
        new_rgb_int = [hex_value + brightness_offset for hex_value in rgb_hex]
        # make sure new values are between 0 and 65535
        new_rgb_int = [min([65535, max([0, i])]) for i in new_rgb_int]
        return new_rgb_int

#####################################
# SplitMeter Class extends the Meter above
#  Used to allow bi-directional metering, starting from a mid point
# Two colours should be provided - left & right fill
#  A gradient fill will be applied to the Meter
#####################################


class SplitMeter(Meter):

    def __init__(
            self,
            master,
            width=100,
            height=20,
            bg='white',
            leftfillColour='red',
            rightfillColour='blue',
            value=0.0,
            text=None,
            font=None,
            textColour='white',
            *args,
            **kw):

        Frame.__init__(
            self,
            master,
            bg=bg,
            width=width,
            height=height,
            *args,
            **kw)

        self._value = value
        self.config(relief='ridge', bd=3)

        self._leftFill = leftfillColour
        self._rightFill = rightfillColour
        self._midFill = textColour

        self._canv = Canvas(
            self,
            bg=self['bg'],
            width=self['width'],
            height=self['height'],
            highlightthickness=0,
            relief='flat',
            bd=0)
        self._canv.pack(fill='both', expand=1)

        self.bind('<Configure>', self._update_coords)

    def _update_coords(self, event):
        '''Updates the position of the text and rectangle inside the canvas when the size of the widget gets changed.'''
        self._setCanvas()

    def setFill(self, cols):
        self._leftFill = cols[0]
        self._rightFill = cols[1]
        self._setCanvas()

    def setFg(self, col):
        self._midFill = col
        self._setCanvas()

    def _setCanvas(self):
        self._canv.update_idletasks()
        self.drawLines()
        self._canv.update_idletasks()

    def drawLines(self):
        '''Draw a gradient'''
        # http://stackoverflow.com/questions/26178869/is-it-possible-to-apply-gradient-colours-to-bg-of-tkinter-python-widgets

        self._canv.delete("gradient")
        self._canv.delete("midline")

        # get range to draw lines
        width = self._canv.winfo_width()
        height = self._canv.winfo_height()
        start = width / 2
        fin = start + (start * self._value)

        # determine start & end colour
        if self._value == 0:
            col = self._midFill
        elif self._value < 0:
            col = self._leftFill
        else:
            col = self._rightFill
        (r1, g1, b1) = self.tint(col, -30000)
        (r2, g2, b2) = self.tint(col, 30000)

        # determine a direction & range
        if self._value < 0:
            direction = -1
            limit = int(start - fin)
        else:
            direction = 1
            limit = int(fin - start)

        # if no lines to draw, end it here - with a midline
        if limit == 0:
            self._canv.create_line(
                start,
                0,
                start,
                height,
                fill=self._midFill,
                tags=(
                    "midline",
                ))
            return

        # work out the ratios
        r_ratio = float(r2 - r1) / limit
        g_ratio = float(g2 - g1) / limit
        b_ratio = float(b2 - b1) / limit

        # loop through the range of lines, in the right direction
        modder = 0
        for i in range(int(start), int(fin), direction):
            nr = int(r1 + (r_ratio * modder))
            ng = int(g1 + (g_ratio * modder))
            nb = int(b1 + (b_ratio * modder))

            colour = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self._canv.create_line(
                i, 0, i, height, tags=(
                    "gradient",), fill=colour)
            modder += 1

        self._canv.lower("gradient")
        self._canv.create_line(
            start,
            0,
            start,
            height,
            fill=self._midFill,
            tags=(
                "midline",
            ))

    def set(self, value=0.0, text=None):
        # make the value failsafe:
        if value < -1:
            value = -1.0
        elif value > 1.0:
            value = 1.0
        self._value = value
        self._setCanvas()


class DualMeter(SplitMeter):

    def __init__(
            self,
            master,
            width=100,
            height=20,
            bg='white',
            leftfillColour='pink',
            rightfillColour='green',
            value=0.5,
            text=None,
            font=None,
            textColour='white',
            *args,
            **kw):

        Frame.__init__(
            self,
            master,
            bg=bg,
            width=width,
            height=height,
            *args,
            **kw)

        self._value = value
        self.config(relief='ridge', bd=3)

        self._leftFill = leftfillColour
        self._rightFill = rightfillColour
        self._midFill = textColour

        self._canv = Canvas(
            self,
            bg=self['bg'],
            width=self['width'],
            height=self['height'],
            highlightthickness=0,
            relief='flat',
            bd=0)
        width = self._canv.winfo_width()
        mid = width * self._value
        self._r_rect = self._canv.create_rectangle(
            0, 0, width, self._canv.winfo_reqheight(), fill=self._rightFill, width=0)
        self._l_rect = self._canv.create_rectangle(
            0, 0, mid, self._canv.winfo_reqheight(), fill=self._leftFill, width=0)
        self._canv.pack(fill='both', expand=1)

        self.bind('<Configure>', self._update_coords)

    def set(self, value=0.0, text=None):
        # make the value failsafe:
        if value < 0.0:
            value = 0.0
        elif value > 1.0:
            value = 1.0
        self._value = value
        self._setCanvas()

    def drawLines(self):
        width = self._canv.winfo_width()
        mid = width * self._value
        self._canv.coords(self._l_rect, 0, 0, mid, self._canv.winfo_height())
        self._canv.coords(self._r_rect, 0, 0, width, self._canv.winfo_height())


#################################
# TabbedFrame Class
#################################
class TabbedFrame(Frame):

    def __init__(
            self,
            master,
            bg,
            fill=False,
            changeOnFocus=True,
            *args,
            **kwargs):

        # main frame & tabContainer inherit BG colour
        Frame.__init__(self, master, bg=bg)

        # create two containers
        self.tabContainer = Frame(self, bg=bg)
        self.paneContainer = Frame(self, relief=SUNKEN, bd=2, bg=bg, **kwargs)

        # grid the containers
        Grid.columnconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 1, weight=1)
        self.fill = fill
        if self.fill:
            self.tabContainer.grid(row=0, sticky=W + E)
        else:
            self.tabContainer.grid(row=0, sticky=W)
        self.paneContainer.grid(row=1, sticky="NESW")

        # nain store dictionary: name = [tab, pane]
        from collections import OrderedDict
        self.widgetStore = OrderedDict()

        self.selectedTab = None
        self.highlightedTab = None
        self.changeOnFocus = changeOnFocus
        self.changeEvent = None

        # selected tab & all panes
        self.activeFg = "blue"
        self.activeBg = "white"

        # other tabs
        self.inactiveFg = "black"
        self.inactiveBg = "grey"

        # disabled tabs
        self.disabledFg = "lightGray"
        self.disabledBg = "darkGray"

    def config(self, cnf=None, **kw):
        self.configure(cnf, **kw)

    def configure(self, cnf=None, **kw):
        kw = gui.CLEAN_CONFIG_DICTIONARY(**kw)
        # configure fgs
        if "activeforeground" in kw:
            self.activeFg = kw.pop("activeforeground")
            for key in list(self.widgetStore.keys()):
                self.widgetStore[key][0].config(highlightcolor=self.activeFg)
        if "activebackground" in kw:
            self.activeBg = kw.pop("activebackground")
            for key in list(self.widgetStore.keys()):
                self.widgetStore[key][1].configure(bg=self.activeBg)
                for child in self.widgetStore[key][1].winfo_children():
                    gui.SET_WIDGET_BG(child, self.activeBg)

        if "fg" in kw:
            self.inactiveFg = kw.pop("fg")
        if "inactivebackground" in kw:
            self.inactiveBg = kw.pop("inactivebackground")

        if "disabledforeground" in kw:
            self.disabledFg = kw.pop("disabledforeground")
        if "disabledbackground" in kw:
            self.disabledBg = kw.pop("disabledbackground")

        if "bg" in kw:
            self.tabContainer.configure(bg=kw["bg"])
            self.paneContainer.configure(bg=kw["bg"])

        if "command" in kw:
            self.changeEvent = kw.pop("command")

        # update tabs if we have any
        if self.selectedTab is not None:
            self.__colourTabs(False)

        # propagate any left over confs
        if PYTHON2:
            Frame.config(self, cnf, **kw)
        else:
            super(Frame, self).config(cnf, **kw)

    def addTab(self, text, **kwargs):
        # check for duplicates
        if text in self.widgetStore:
            raise Exception("Duplicate tabName: " + text)

        # create the tab, bind events, pack it in
        tab = Label(
            self.tabContainer,
            text=text,
            highlightthickness=1,
            highlightcolor=self.activeFg,
            relief=RIDGE,
            cursor="hand2",
            takefocus=1,
            **kwargs)
        tab.disabled = False

        tab.bind("<Button-1>", lambda *args: self.changeTab(text))
        tab.bind("<Return>", lambda *args: self.changeTab(text))
        tab.bind("<space>", lambda *args: self.changeTab(text))
        tab.bind("<FocusIn>", lambda *args: self.__focusIn(text))
        tab.bind("<FocusOut>", lambda *args: self.__focusOut(text))
        if self.fill:
            tab.pack(side=LEFT, ipady=4, ipadx=4, expand=True, fill=BOTH)
        else:
            tab.pack(side=LEFT, ipady=4, ipadx=4)

        # create the pane
        pane = Frame(self.paneContainer, bg=self.activeBg)
        pane.grid(sticky="nsew", row=0, column=0)
        self.paneContainer.grid_columnconfigure(0, weight=1)
        self.paneContainer.grid_rowconfigure(0, weight=1)

        # log the first tab as the selected tab
        if self.selectedTab is None:
            self.selectedTab = text
            tab.focus_set()
        if self.highlightedTab is None:
            self.highlightedTab = text

        self.widgetStore[text] = [tab, pane]
        self.__colourTabs(self.selectedTab)

        return pane

    def getTab(self, title):
        if title not in self.widgetStore.keys():
            raise Exception("Invalid tab name: " + title)
        else:
            return self.widgetStore[title][1]

    def expandTabs(self, fill=True):
        self.fill = fill

        # update the tabConatiner
        self.tabContainer.grid_forget()
        if self.fill:
            self.tabContainer.grid(row=0, sticky=W + E)
        else:
            self.tabContainer.grid(row=0, sticky=W)

        for key in list(self.widgetStore.keys()):
            tab = self.widgetStore[key][0]
            tab.pack_forget()
            if self.fill:
                tab.pack(side=LEFT, ipady=4, ipadx=4, expand=True, fill=BOTH)
            else:
                tab.pack(side=LEFT, ipady=4, ipadx=4)

    def __focusIn(self, tabName):
        if self.changeOnFocus:
            self.changeTab(tabName)
        else:
            self.highlightedTab = tabName
            self.__colourTabs(False)

    def __focusOut(self, tabName):
        self.highlightedTab = None
        self.__colourTabs(False)

    def disableAllTabs(self, disabled=True):
        for tab in self.widgetStore.keys():
            self.disableTab(tab, disabled)

    def disableTab(self, tabName, disabled=True):
        if tabName not in self.widgetStore.keys():
            raise Exception("Invalid tab name: " + tabName)

        if not disabled:
            self.widgetStore[tabName][0].disabled = False
            self.widgetStore[tabName][0].config(cursor="hand2", takefocus=1)
        else:
            self.widgetStore[tabName][0].disabled = True
            self.widgetStore[tabName][0].config(cursor="X_cursor", takefocus=0)
            if self.highlightedTab == tabName:
                self.highlightedTab = None

            # difficult if the active tab is disabled
            if self.selectedTab == tabName:
                self.widgetStore[tabName][1].grid_remove()
                # find an enabled tab
                self.selectedTab = None
                for key in list(self.widgetStore.keys()):
                    if not self.widgetStore[key][0].disabled:
                        self.changeTab(key)
                        break

        self.__colourTabs()

    def changeTab(self, tabName):
        # quit changing the tab, if it's already selected
        if self.focus_get() == self.widgetStore[tabName][0]:
            return

        if tabName not in self.widgetStore.keys():
            raise Exception("Invalid tab name: " + tabName)

        if self.widgetStore[tabName][0].disabled:
            return

        self.selectedTab = tabName
        self.highlightedTab = tabName
        self.widgetStore[tabName][0].focus_set()
        # this will also regrid the appropriate panes
        self.__colourTabs()

        if self.changeEvent is not None:
            self.changeEvent()

    def getSelectedTab(self):
        return self.selectedTab

    def __colourTabs(self, swap=True):
        # clear all tabs & remove if necessary
        for key in list(self.widgetStore.keys()):
            if self.widgetStore[key][0].disabled:
                self.widgetStore[key][0]['bg'] = self.disabledBg
                self.widgetStore[key][0]['fg'] = self.disabledFg
            else:
                self.widgetStore[key][0]['bg'] = self.inactiveBg
                self.widgetStore[key][0]['fg'] = self.inactiveFg
                if swap:
                    self.widgetStore[key][1].grid_remove()

        # decorate the highlighted tab
        if self.highlightedTab is not None:
            self.widgetStore[self.highlightedTab][0]['fg'] = self.activeFg

        # now decorate the active tab
        if self.selectedTab is not None:
            self.widgetStore[self.selectedTab][0]['bg'] = self.activeBg
            self.widgetStore[self.selectedTab][0]['fg'] = self.activeFg
            # and grid it if necessary
            if swap:
                self.widgetStore[self.selectedTab][1].grid()

#####################################
# Drag Grip Label Class
#####################################


class Grip(Label):

    def __init__(self, *args, **kwargs):
        Label.__init__(self, bitmap="gray25", *args, **kwargs)
        self.config(cursor="fleur")
        self.bind("<ButtonPress-1>", self.StartMove)
        self.bind("<ButtonRelease-1>", self.StopMove)
        self.bind("<B1-Motion>", self.OnMotion)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self, event):
        parent = self.winfo_toplevel()
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = parent.winfo_x() + deltax
        y = parent.winfo_y() + deltay

        parent.geometry("+%s+%s" % (x, y))

#####################################
# Hyperlink Class
#####################################


class Link(Label):

    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self.config(fg="blue", takefocus=1, highlightthickness=0)
        self.page = ""
        self.DEFAULT_TEXT = ""

        if gui.GET_PLATFORM() == gui.MAC:
            self.config(cursor="pointinghand")
        elif gui.GET_PLATFORM() in [gui.WINDOWS, gui.LINUX]:
            self.config(cursor="hand2")

    def registerCallback(self, callback):
        self.bind("<Button-1>", callback)
        self.bind("<Return>", callback)
        self.bind("<space>", callback)

    def launchBrowser(self, event):
        webbrowser.open_new(r"" + self.page)
        # webbrowser.open_new_tab(self.page)

    def registerWebpage(self, page):
        if not page.startswith("http"):
            raise InvalidURLError(
                "Invalid URL: " +
                page +
                " (it should begin as http://)")

        self.page = page
        self.bind("<Button-1>", self.launchBrowser)
        self.bind("<Return>", self.launchBrowser)
        self.bind("<space>", self.launchBrowser)

    def config(self, **kw):
        self.configure(**kw)

    def configure(self, **kw):
        if "text" in kw:
            self.DEFAULT_TEXT = kw["text"]
        if PYTHON2:
            Label.config(self, **kw)
        else:
            super(Label, self).config(**kw)

#####################################
# Properties Widget
#####################################
class Properties(LabelFrame):

    def __init__(
            self,
            parent,
            text,
            props=None,
            haveLabel=True,
            *args,
            **options):
        if haveLabel:
            LabelFrame.__init__(self, parent, text=text, *args, **options)
        else:
            LabelFrame.__init__(self, parent, text="", *args, **options)
        self.parent = parent
        self.config(relief="groove")
        self.props = {}
        self.cbs = {}
        self.title = text
        self.addProperties(props)

    def config(self, cnf=None, **kw):
        self.configure(cnf, **kw)

    def configure(self, cnf=None, **kw):
        # properties to propagate to CheckBoxes
        vals = ["bg", "fg", "disabledforeground", "state", "font", "command"]
        kw = gui.CLEAN_CONFIG_DICTIONARY(**kw)

        # loop through all kw properties received
        for k, v in kw.items():
            if k in vals:
                # and set them on all CheckBoxes if desired
                for prop_key in self.cbs:
                    self.cbs[prop_key][k] = v

        # remove any props the LabelFrame can't handle
        kw.pop("state", None)
        kw.pop("disabledforeground", None)
        kw.pop("command", None)

        if PYTHON2:
            LabelFrame.config(self, cnf, **kw)
        else:
            super(LabelFrame, self).config(cnf, **kw)

    def addProperties(self, props):

        if props is not None:
            for k in sorted(props):
                self.addProperty(k, props[k])

    def addProperty(self, prop, value=False):
        if prop in self.props:
            if value is None:
                del self.props[prop]
                self.cbs[prop].pack_forget()
                del self.cbs[prop]
            else:
                self.props[prop].set(value)
        elif prop is not None:
            var = BooleanVar()
            var.set(value)
            cb = Checkbutton(self)
            cb.config(
                anchor=W,
                text=prop,
                variable=var,
                bg=self.cget("bg"),
                font=self.cget("font"),
                fg=self.cget("fg"))
            cb.pack(fill="x", expand=1)
            self.props[prop] = var
            self.cbs[prop] = cb
        else:
            raise Exception("Can't add a None property to: ", prop)
        # if text is not None: lab.config ( text=text )

    def getProperties(self):
        vals = {}
        for k, v in self.props.items():
            vals[k] = bool(v.get())
        return vals

    def getProperty(self, prop):
        if prop in self.props:
            return bool(self.props[prop].get())
        else:
            raise Exception(
                "Property: " +
                str(prop) +
                " not found in Properties: " +
                self.title)

#####################################
# appJar Frame
#####################################


class ajFrame(Frame):

    def __init__(self, parent, *args, **options):
        Frame.__init__(self, parent, *args, **options)

#####################################
# Simple Separator
#####################################


class Separator(Frame):

    def __init__(self, parent, orient="horizontal", *args, **options):
        Frame.__init__(self, parent, *args, **options)
        self.line = Frame(self)
        if orient == "horizontal":
            self.line.config(
                relief="ridge",
                height=2,
                width=100,
                borderwidth=1)
            self.line.pack(padx=5, pady=5, fill="x", expand=1)
        else:
            self.line.config(
                relief="ridge",
                height=100,
                width=2,
                borderwidth=1)
            self.line.pack(padx=5, pady=5, fill="y", expand=1)

    def config(self, cnf=None, **kw):
        self.configure(cnf, **kw)

    def configure(self, cnf=None, **kw):
        if "fg" in kw:
            self.line.config(bg=kw.pop("fg"))

        if PYTHON2:
            Frame.config(self, cnf, **kw)
        else:
            super(Frame, self).config(cnf, **kw)

#####################################
# Pie Chart Class
#####################################


class PieChart(Canvas):
    # constant for available colours
    COLOURS = [
        "#023fa5",
        "#7d87b9",
        "#bec1d4",
        "#d6bcc0",
        "#bb7784",
        "#8e063b",
        "#4a6fe3",
        "#8595e1",
        "#b5bbe3",
        "#e6afb9",
        "#e07b91",
        "#d33f6a",
        "#11c638",
        "#8dd593",
        "#c6dec7",
        "#ead3c6",
        "#f0b98d",
        "#ef9708",
        "#0fcfc0",
        "#9cded6",
        "#d5eae7",
        "#f3e1eb",
        "#f6c4e1",
        "#f79cd4"]

    def __init__(self, container, fracs, bg="green"):
        Canvas.__init__(self, container, bd=0, highlightthickness=0, bg=bg)
        self.fracs = fracs
        self.arcs = []
        self.__drawPie()
        self.bind("<Configure>", self.__drawPie)

    def __drawPie(self, event=None):
        # remove the existing arcs
        for arc in self.arcs:
            self.delete(arc)
        self.arcs = []

        # get the width * height
        w = self.winfo_width()
        h = self.winfo_height()

        # scale h&w - so they don;t hit the edges
        min_w = w * .05
        max_w = w * .95
        min_h = h * .05
        max_h = h * .95

        # if we're not in a square
        # adjust them to make sure we get a circle
        if w > h:
            extra = (w * .9 - h * .9) / 2.0
            min_w += extra
            max_w -= extra
        elif h > w:
            extra = (h * .9 - w * .9) / 2.0
            min_h += extra
            max_h -= extra

        coord = min_w, min_h, max_w, max_h

        pos = col = 0
        for key, val in self.fracs.items():
            sliceId = "slice" + str(col)
            arc = self.create_arc(
                coord,
                fill=self.COLOURS[
                    col % len(
                        self.COLOURS)],
                start=self.frac(pos),
                extent=self.frac(val),
                activedash=(
                    3,
                    5),
                activeoutline="grey",
                activewidth=3,
                tag=(
                    sliceId,
                ),
                width=1)

            self.arcs.append(arc)

            # generate a tooltip
            if TOOLTIP_AVAILABLE:
                frac = int(val / sum(self.fracs.values()) * 100)
                tip = key + ": " + str(val) + " (" + str(frac) + "%)"
                tt = ToolTip(
                    self,
                    tip,
                    delay=500,
                    follow_mouse=1,
                    specId=sliceId)

            pos += val
            col += 1

    def frac(self, curr):
        return 360. * curr / sum(self.fracs.values())

    def setValue(self, name, value):
        if value == 0 and name in self.fracs:
            del self.fracs[name]
        else:
            self.fracs[name] = value

        self.__drawPie()

#####################################
# Tree Widget Class
# https://www.safaribooksonline.com/library/view/python-cookbook-2nd/0596007973/ch11s11.html
# idlelib -> TreeWidget.py
# modify minidom - https://wiki.python.org/moin/MiniDom
#####################################


class ajTreeNode(TreeNode):

    def __init__(self, canvas, parent, item):

        TreeNode.__init__(self, canvas, parent, item)

        self.bgColour = None
        self.fgColour = None
        self.bgHColour = None
        self.fgHColour = None
        # called (if set) when a leaf is edited
        self.editEvent = None

        if self.parent:
            self.bgColour = self.parent.bgColour
            self.fgColour = self.parent.fgColour
            self.bgHColour = self.parent.bgHColour
            self.fgHColour = self.parent.fgHColour
            self.editEvent = self.parent.editEvent

    def registerEditEvent(self, func):
        self.editEvent = func
        for c in self.children:
            c.registerEditEvent(func)

    def setBgColour(self, colour):
        self.canvas.config(background=colour)
        self.bgColour = colour
        self.__doUpdateColour()

    def setFgColour(self, colour):
        self.fgColour = colour
        self.__doUpdateColour()

    def setBgHColour(self, colour):
        self.bgHColour = colour
        self.__doUpdateColour()

    def setFgHColour(self, colour):
        self.fgHColour = colour
        self.__doUpdateColour()

    def __doUpdateColour(self):
        self.__updateColours(
            self.bgColour,
            self.bgHColour,
            self.fgColour,
            self.fgHColour)
        self.update()

    def __updateColours(self, bgCol, bgHCol, fgCol, fgHCol):
        self.bgColour = bgCol
        self.fgColour = fgCol
        self.bgHColour = bgHCol
        self.fgHColour = fgHCol
        for c in self.children:
            c.__updateColours(bgCol, bgHCol, fgCol, fgHCol)

    # override parent function, so that we can change the label's background
    # colour
    def drawtext(self):
        if PYTHON2:
            TreeNode.drawtext(self)
        else:
            super(ajTreeNode, self).drawtext()

        self.colourLabels()

    # override parent function, so that we can generate an event on finish
    # editing
    def edit_finish(self, event=None):
        if PYTHON2:
            TreeNode.edit_finish(self, event)
        else:
            super(ajTreeNode, self).edit_finish(event)
        if self.editEvent is not None:
            self.editEvent()

    def colourLabels(self):
        try:
            if not self.selected:
                self.label.config(background=self.bgColour, fg=self.fgColour)
            else:
                self.label.config(background=self.bgHColour, fg=self.fgHColour)
        except:
            pass

    def getSelectedText(self):
        item = self.getSelected()
        if item is not None:
            return item.GetText()
        else:
            return None

    def getSelected(self):
        if self.selected:
            return self.item
        else:
            for c in self.children:
                val = c.getSelected()
                if val is not None:
                    return val
            return None

# implementation of container for XML data
# functions implemented as specified in skeleton


class ajTreeData(TreeItem):

    def __init__(self, node):
        self.node = node
        self.dblClickFunc = None
        self.canEdit = True

# REQUIRED FUNCTIONS

    # called whenever the tree expands
    def GetText(self):
        node = self.node
        if node.nodeType == node.ELEMENT_NODE:
            return node.nodeName
        elif node.nodeType == node.TEXT_NODE:
            return node.nodeValue

    def IsEditable(self):
        return self.canEdit and not self.node.hasChildNodes()

    def SetText(self, text):
        self.node.replaceWholeText(text)

    def IsExpandable(self):
        return self.node.hasChildNodes()

    def GetIconName(self):
        if not self.IsExpandable():
            return "python"  # change to file icon

    def GetSubList(self):
        children = self.node.childNodes
        prelist = [ajTreeData(node) for node in children]
        itemList = [item for item in prelist if item.GetText().strip()]
        for item in itemList:
            item.registerDblClick(self.dblClickFunc)
            item.canEdit = self.canEdit
        return itemList

    def OnDoubleClick(self):
        if self.IsEditable():
            # TO DO: start editing this node...
            pass
        if self.dblClickFunc is not None:
            self.dblClickFunc()

#  EXTRA FUNCTIONS

    # TODO: can only set before calling go()
    def setCanEdit(self, value=True):
        self.canEdit = value

    # TODO: can only set before calling go()
    def registerDblClick(self, func):
        self.dblClickFunc = func

    # not used - for DEBUG
    def getSelected(self, spaces=1):
        if spaces == 1:
            print(self.node.tagName)
        for c in self.node.childNodes:
            if c.__class__.__name__ == "Element":
                print(" " * spaces, ">>", c.tagName)
                node = ajTreeData(c)
                node.getSelected(spaces + 2)
            elif c.__class__.__name__ == "Text":
                val = c.data.strip()
                if len(val) > 0:
                    print(" " * spaces, ">>>>", val)

#####################################
# errors
#####################################


class ItemLookupError(LookupError):
    '''raise this when there's a lookup error for my app'''
    pass


class InvalidURLError(ValueError):
    '''raise this when there's a lookup error for my app'''
    pass

#####################################
# ToggleFrame - collapsable frame
# http://stackoverflow.com/questions/13141259/expandable-and-contracting-frame-in-tkinter
#####################################


class ToggleFrame(Frame):

    def __init__(self, parent, title="", *args, **options):
        Frame.__init__(self, parent, *args, **options)

        self.config(relief="raised", borderwidth=2, padx=5, pady=5)
        self.showing = True

        self.titleFrame = Frame(self)
        self.titleFrame.config(bg="DarkGray")

        self.titleLabel = Label(self.titleFrame, text=title)
        self.titleLabel.config(font="-weight bold")

        self.toggleButton = Button(
            self.titleFrame,
            width=2,
            text='-',
            command=self.toggle)

        self.subFrame = Frame(self, relief="sunken", borderwidth=2)

        self.configure(bg="DarkGray")

        self.grid_columnconfigure(0, weight=1)
        self.titleFrame.grid(row=0, column=0, sticky=EW)
        self.titleFrame.grid_columnconfigure(0, weight=1)
        self.titleLabel.grid(row=0, column=0)
        self.toggleButton.grid(row=0, column=1)
        self.subFrame.grid(row=1, column=0, sticky=EW)

    def config(self, cnf=None, **kw):
        self.configure(cnf, **kw)

    def configure(self, cnf=None, **kw):
        kw = gui.CLEAN_CONFIG_DICTIONARY(**kw)
        if "font" in kw:
            self.titleLabel.config(font=kw["font"])
            self.toggleButton.config(font=kw["font"])
            del(kw["font"])
        if "bg" in kw:
            self.titleFrame.config(bg=kw["bg"])
            self.titleLabel.config(bg=kw["bg"])
            self.subFrame.config(bg=kw["bg"])
            if gui.GET_PLATFORM() == gui.MAC:
                self.toggleButton.config(highlightbackground=kw["bg"])
        if "state" in kw:
            if kw["state"] == "disabled":
                if self.showing:
                    self.toggle()
            self.toggleButton.config(state=kw["state"])
            del(kw["state"])

        if PYTHON2:
            Frame.config(self, cnf, **kw)
        else:
            super(Frame, self).config(cnf, **kw)

    def toggle(self):
        if not self.showing:
            self.subFrame.grid()
            self.toggleButton.configure(text='-')
        else:
            self.subFrame.grid_remove()
            self.toggleButton.configure(text='+')
        self.showing = not self.showing

    def getContainer(self):
        return self.subFrame

    def stop(self):
        self.update_idletasks()
        self.titleFrame.config(width=self.winfo_reqwidth())
        self.toggle()

    def isShowing(self):
        return self.showing

#####################################
# Paged Window
#####################################


class PagedWindow(Frame):

    def __init__(self, parent, title=None, **opts):
        # call the super constructor
        Frame.__init__(self, parent, **opts)
        self.config(width=300, height=400)

        # globals to hold list of frames(pages) and current page
        self.currentPage = -1
        self.frames = []
        self.shouldShowLabel = True
        self.shouldShowTitle = True
        self.title = title
        self.navPos = 1
        self.maxX = 0
        self.maxY = 0
        self.pageChangeEvent = None

        # create the 3 components, including a default container frame
        self.titleLabel = Label(self)
        self.prevButton = Button(
            self,
            text="PREVIOUS",
            command=self.showPrev,
            state="disabled",
            width=10)
        self.nextButton = Button(
            self,
            text="NEXT",
            command=self.showNext,
            state="disabled",
            width=10)
        self.prevButton.bind("<Control-Button-1>", self.showFirst)
        self.nextButton.bind("<Control-Button-1>", self.showLast)
        self.posLabel = Label(self, width=8)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # grid the navigation components
        self.prevButton.grid(
            row=self.navPos + 1,
            column=0,
            sticky=N + S + W,
            padx=5,
            pady=(
                0,
                5))
        self.posLabel.grid(
            row=self.navPos + 1,
            column=1,
            sticky=N + S + E + W,
            padx=5,
            pady=(
                0,
                5))
        self.nextButton.grid(
            row=self.navPos + 1,
            column=2,
            sticky=N + S + E,
            padx=5,
            pady=(
                0,
                5))

        # show the title
        if self.title is not None and self.shouldShowTitle:
            self.titleLabel.config(text=self.title, font="-weight bold")
            self.titleLabel.grid(
                row=0, column=0, columnspan=3, sticky=N + W + E)

        # show the label
        self.__setLabel()

    def config(self, cnf=None, **kw):
        self.configure(cnf, **kw)

    def configure(self, cnf=None, **kw):
        kw = gui.CLEAN_CONFIG_DICTIONARY(**kw)

        if "bg" in kw:
            if gui.GET_PLATFORM() == gui.MAC:
                self.prevButton.config(highlightbackground=kw["bg"])
                self.nextButton.config(highlightbackground=kw["bg"])
            self.posLabel.config(bg=kw["bg"])
            self.titleLabel.config(bg=kw["bg"])
        if "fg" in kw:
            self.poslabel.config(fg=kw["fg"])
            self.titleLabel.config(fg=kw["fg"])
            kw.pop("fg")

        if PYTHON2:
            Frame.config(self, cnf, **kw)
        else:
            super(Frame, self).config(cnf, **kw)

#    def setBg(self, colour):
#        self.config(bg=colour)
#
#    def setFg(self, colour):
#        self.poslabel.config(fg=colour)
#        self.titleLabel.config(fg=colour)

    # functions to change the labels of the two buttons
    def setPrevButton(self, title): self.prevButton.config(text=title)

    def setNextButton(self, title): self.nextButton.config(text=title)

    def setNavPositionTop(self, top=True):
        oldNavPos = self.navPos
        pady = (0, 5)
        if top:
            self.navPos = 0
        else:
            self.navPos = 1
        if oldNavPos != self.navPos:
            if self.navPos == 0:
                self.grid_rowconfigure(1, weight=0)
                self.grid_rowconfigure(2, weight=1)
                pady = (5, 0)
            else:
                self.grid_rowconfigure(1, weight=1)
                self.grid_rowconfigure(2, weight=0)
            # grid the navigation components
            self.frames[self.currentPage].grid_remove()
            self.prevButton.grid_remove()
            self.posLabel.grid_remove()
            self.nextButton.grid_remove()

            self.frames[
                self.currentPage].grid(
                row=int(
                    not self.navPos) + 1,
                column=0,
                columnspan=3,
                sticky=N + S + E + W,
                padx=5,
                pady=5)
            self.prevButton.grid(
                row=self.navPos + 1,
                column=0,
                sticky=S + W,
                padx=5,
                pady=pady)
            self.posLabel.grid(
                row=self.navPos + 1,
                column=1,
                sticky=S + E + W,
                padx=5,
                pady=pady)
            self.nextButton.grid(
                row=self.navPos + 1,
                column=2,
                sticky=S + E,
                padx=5,
                pady=pady)

    def showLabel(self, val=True):
        self.shouldShowLabel = val
        self.__setLabel()

    def setTitle(self, title):
        self.title = title
        self.showTitle()

    def showTitle(self, val=True):
        self.shouldShowTitle = val
        if self.title is not None and self.shouldShowTitle:
            self.titleLabel.config(text=self.title, font="-weight bold")
            self.titleLabel.grid(
                row=0, column=0, columnspan=3, sticky=N + W + E)
        else:
            self.titleLabel.grid_remove()

    # function to update the contents of the label
    def __setLabel(self):
        if self.shouldShowLabel:
            self.posLabel.config(
                text=str(self.currentPage + 1) + "/" + str(len(self.frames)))
        else:
            self.posLabel.config(text="")

    # get the current frame being shown - for adding widgets
    def getPage(self): return self.frames[self.currentPage]

    # get current page number
    def getPageNumber(self): return self.currentPage + 1

    # register a function to call when the page changes
    def registerPageChangeEvent(self, event):
        self.pageChangeEvent = event

    # adds a new page, making it visible
    def addPage(self):
        # if we're showing a page, remove it
        if self.currentPage >= 0:
            self.__updateMaxSize()
            self.frames[self.currentPage].grid_forget()

        # add a new page
        self.frames.append(Page(self))
        self.frames[-1].grid(row=int(not self.navPos) + 1,
                             column=0,
                             columnspan=3,
                             sticky=N + S + E + W,
                             padx=5,
                             pady=5)

        self.currentPage = len(self.frames) - 1

        # update the buttons & labels
        if self.currentPage > 0:
            self.prevButton.config(state="normal")
        self.__setLabel()
        return self.frames[-1]

    def stopPage(self):
        self.__updateMaxSize()
        self.showPage(1)

    def __updateMaxSize(self):
        self.frames[self.currentPage].update_idletasks()
        x = self.frames[self.currentPage].winfo_reqwidth()
        y = self.frames[self.currentPage].winfo_reqheight()
        if x > self.maxX:
            self.maxX = x
        if y > self.maxY:
            self.maxY = y

    # function to display the specified page
    # will re-grid, and disable/enable buttons
    # also updates label
    def showPage(self, page):
        if page < 1 or page > len(self.frames):
            raise Exception("Invalid page number: " + str(page) +
                            ". Must be between 1 and " + str(len(self.frames)))

        self.frames[self.currentPage].grid_forget()
        self.currentPage = page - 1
        self.frames[self.currentPage].grid_propagate(False)
        self.frames[
            self.currentPage].grid(
            row=int(
                not self.navPos) + 1,
            column=0,
            columnspan=3,
            sticky=N + S + E + W,
            padx=5,
            pady=5)
        self.frames[self.currentPage].grid_columnconfigure(0, weight=1)
        self.frames[self.currentPage].config(width=self.maxX, height=self.maxY)
        self.__setLabel()

        # update the buttons
        if len(self.frames) == 1:   # only 1 page - no buttons
            self.prevButton.config(state="disabled")
            self.nextButton.config(state="disabled")
        elif self.currentPage == 0:
            self.prevButton.config(state="disabled")
            self.nextButton.config(state="normal")
        elif self.currentPage == len(self.frames) - 1:
            self.prevButton.config(state="normal")
            self.nextButton.config(state="disabled")
        else:
            self.prevButton.config(state="normal")
            self.nextButton.config(state="normal")

    def showFirst(self, event=None):
        if self.currentPage == 0:
            self.bell()
        else:
            self.showPage(1)
            if self.pageChangeEvent is not None:
                self.pageChangeEvent()

    def showLast(self, event=None):
        if self.currentPage == len(self.frames) - 1:
            self.bell()
        else:
            self.showPage(len(self.frames))
            if self.pageChangeEvent is not None:
                self.pageChangeEvent()

    def showPrev(self, event=None):
        if self.currentPage > 0:
            self.showPage(self.currentPage)
            if self.pageChangeEvent is not None:
                self.pageChangeEvent()
        else:
            self.bell()

    def showNext(self, event=None):
        if self.currentPage < len(self.frames) - 1:
            self.showPage(self.currentPage + 2)
            if self.pageChangeEvent is not None:
                self.pageChangeEvent()
        else:
            self.bell()


class Page(Frame):

    def __init__(self, parent, **opts):
        Frame.__init__(self, parent)
        self.config(relief=RIDGE, borderwidth=2)

#########################
# Class to provide auto-completion on Entry boxes
# inspired by: https://gist.github.com/uroshekic/11078820
#########################


class AutoCompleteEntry(Entry):

    def __init__(self, words, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.allWords = words
        self.allWords.sort()

        # store variable - so we can see when it changes
        self.var = self["textvariable"] = StringVar()
        self.var.trace('w', self.textChanged)

        # register events
        self.bind("<Right>", self.selectWord)
        self.bind("<Return>", self.selectWord)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)
        self.bind("<FocusOut>", self.closeList, add="+")

        # no list box - yet
        self.listBoxShowing = False

    # function to see if words match
    def checkMatch(self, fieldValue, acListEntry):
        pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
        return re.match(pattern, acListEntry)

    # function to get all matches as a list
    def getMatches(self):
        return [w for w in self.allWords if self.checkMatch(self.var.get(), w)]

    # called when typed in entry
    def textChanged(self, name, index, mode):
        # if no text - close list
        if self.var.get() == '':
            self.closeList()
        else:
            if not self.listBoxShowing:
                self.makeListBox()
            self.popListBox()

    # add words to the list
    def popListBox(self):
        if self.listBoxShowing:
            self.listbox.delete(0, END)
            shownWords = self.getMatches()
            if shownWords:
                for w in shownWords:
                    self.listbox.insert(END, w)
                self.selectItem(0)

    # function to create & show an empty list box
    def makeListBox(self):
        self.listbox = Listbox(width=self["width"], height=8)
        self.listbox.bind("<Button-1>", self.mouseClickBox)
        self.listbox.bind("<Right>", self.selectWord)
        self.listbox.bind("<Return>", self.selectWord)
        self.listbox.place(
            x=self.winfo_x(),
            y=self.winfo_y() +
            self.winfo_height())
        self.listBoxShowing = True

    # function to handle a mouse click in the list box
    def mouseClickBox(self, e=None):
        self.selectItem(self.listbox.nearest(e.y))
        self.selectWord(e)

    # function to close/delete list box
    def closeList(self, event=None):
        if self.listBoxShowing:
            self.listbox.destroy()
            self.listBoxShowing = False

    # copy word from list to entry, close list
    def selectWord(self, event):
        if self.listBoxShowing:
            self.var.set(self.listbox.get(ACTIVE))
            self.icursor(END)
            self.closeList()
        return "break"

    # wrappers for up/down arrows
    def moveUp(self, event):
        return self.arrow("UP")

    def moveDown(self, event):
        return self.arrow("DOWN")

    # function for handling up/down keys
    def arrow(self, direction):
        if not self.listBoxShowing:
            self.makeListBox()
            self.popListBox()
            curItem = 0
            numItems = self.listbox.size()
        else:
            numItems = self.listbox.size()
            curItem = self.listbox.curselection()

            if curItem == ():
                curItem = -1
            else:
                curItem = int(curItem[0])

            if direction == "UP" and curItem > 0:
                curItem -= 1
            elif direction == "UP" and curItem <= 0:
                curItem = numItems - 1
            elif direction == "DOWN" and curItem < numItems - 1:
                curItem += 1
            elif direction == "DOWN" and curItem == numItems - 1:
                curItem = 0

        self.selectItem(curItem)

        # stop the event propgating
        return "break"

    # function to select the specified item
    def selectItem(self, position):
        numItems = self.listbox.size()
        self.listbox.selection_clear(0, numItems - 1)
        self.listbox.see(position)  # Scroll!
        self.listbox.selection_set(first=position)
        self.listbox.activate(position)

#####################################
# Named classes for containing groups
#####################################


class LabelBox(Frame):

    def __init__(self, parent, **opts):
        Frame.__init__(self, parent)
        self.theLabel = None
        self.theWidget = None


class WidgetBox(Frame):

    def __init__(self, parent, **opts):
        Frame.__init__(self, parent)
        self.theWidgets = []


class ListBox(Frame):

    def __init__(self, parent, **opts):
        Frame.__init__(self, parent)


class Pane(Frame):

    def __init__(self, parent, **opts):
        Frame.__init__(self, parent)

#####################################
# scrollable frame...
# http://effbot.org/zone/tkinter-autoscrollbar.htm
#####################################


class AutoScrollbar(Scrollbar):

    def __init__(self, parent, **opts):
        Scrollbar.__init__(self, parent, **opts)

    # a scrollbar that hides itself if it's not needed
    # only works if you use the grid geometry manager
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

#######################
# Frame with built in scrollbars and canvas for placing stuff on
# http://effbot.org/zone/tkinter-autoscrollbar.htm
# Modified with help from idlelib TreeWidget.py
#######################


class ScrollPane(Frame):
    def __init__(self, parent, **opts):
        Frame.__init__(self, parent)
        self.config(padx=5, pady=5, width=100, height=100)

        # make the ScrollPane expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        if 'yscrollincrement' not in opts:
            opts['yscrollincrement'] = 17
        opts['height'] = 100

        vscrollbar = Scrollbar(self)
        hscrollbar = Scrollbar(self, orient=HORIZONTAL)
        opts['yscrollcommand'] = vscrollbar.set
        opts['xscrollcommand'] = hscrollbar.set

        self.canvas = Canvas(self, **opts)
        self.canvas.config(highlightthickness=0)

        vscrollbar.grid(row=0, column=1, sticky=N + S + E)
        hscrollbar.grid(row=1, column=0, sticky=E + W + S)
        self.canvas.grid(row=0, column=0, sticky=N + S + E + W)

        vscrollbar.config(command=self.canvas.yview)
        hscrollbar.config(command=self.canvas.xview)

        self.canvas.bind("<Key-Prior>", self.page_up)
        self.canvas.bind("<Key-Next>", self.page_down)
        self.canvas.bind("<Key-Up>", self.unit_up)
        self.canvas.bind("<Key-Down>", self.unit_down)
        self.canvas.bind("<Alt-Key-2>", self.zoom_height)
        self.canvas.focus_set()

        self.canvas.bind("<Enter>", self.__mouseEnter)
        self.canvas.bind("<Leave>", self.__mouseLeave)
        self.b_ids = []

        self.interior = interior = Frame(self.canvas)
        self.interior_id = self.canvas.create_window(
            0, 0, window=interior, anchor=NW)

        # removed - was cropping label's width
        #self.canvas.bind('<Configure>', self.__configureCanvas)
        self.interior.bind('<Configure>', self.__configureInterior)

    # track changes to the canvas and frame width and sync them,
    # also updating the scrollbar
    # http://www.scriptscoop2.com/t/35d742299f35/python-tkinter-scrollbar-for-frame.html
    def __configureInterior(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (
            self.interior.winfo_reqwidth(),
            self.interior.winfo_reqheight())
        self.canvas.config(scrollregion="0 0 %s %s" % size)
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canvas.config(width=self.interior.winfo_reqwidth())

    def __configureCanvas(self, event):
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # update the inner frame's width to fill the canvas
            self.canvas.itemconfigure(
                self.interior_id, width=self.canvas.winfo_width())
            pass

    # unbind any saved bind ids
    def __unbindIds(self):
        if len(self.b_ids) == 0:
            return

        if gui.GET_PLATFORM() == gui.LINUX:
            self.canvas.unbind("<4>", self.b_ids[0])
            self.canvas.unbind("<5>", self.b_ids[1])
        else:  # Windows and MacOS
            self.canvas.unbind("<MouseWheel>", self.b_ids[0])

        self.b_ids = []

    # bind mouse scroll to this widget only when mouse is over
    def __mouseEnter(self, event):
        self.__unbindIds()
        if gui.GET_PLATFORM() == gui.LINUX:
            self.b_ids.append(self.canvas.bind_all("<4>", self.__mouseScroll))
            self.b_ids.append(self.canvas.bind_all("<5>", self.__mouseScroll))
        else:  # Windows and MacOS
            self.b_ids.append(
                self.canvas.bind_all(
                    "<MouseWheel>",
                    self.__mouseScroll))

    # remove mouse scroll binding, when mouse leaves
    def __mouseLeave(self, event):
        self.__unbindIds()

    # https://www.daniweb.com/programming/software-development/code/217059/using-the-mouse-wheel-with-tkinter-python
    def __mouseScroll(self, event):
        timer = round(time.time(), 1)

        # get the mouse scroll direciton value
        newDelta = event.delta

        # if windows - make it the same as other platforms
        if gui.GET_PLATFORM() == gui.WINDOWS:
            newDelta = (newDelta / 120) * -1

        # scrolled before
        if hasattr(self, 'lastScrollTime'):

            # too soon to scroll
            if self.lastScrollTime == timer:
                if newDelta in [1, -1, 2, -2]:
                    self.times.append(newDelta)
                self.speed += 1

            # time to scroll
            else:
                # get the delta
                try:
                    delta = max(set(self.times), key=self.times.count)
                except:
                    delta = self.oldDelta

                # windows/mac osx scroll event
                if gui.GET_PLATFORM() in [gui.WINDOWS, gui.LINUX]:
                    if gui.GET_PLATFORM() == gui.WINDOWS:
                        val = delta * -1
                        if delta < 0:
                            val = val * -1
                        if delta < 0:
                            self.speed = self.speed * -1
                    else:
                        val = (self.times.count(delta))
                        if delta > 0:
                            val = val * -1
                        if delta > 0:
                            self.speed = self.speed * -1

                    if delta in [1, -1]:
                        self.canvas.yview_scroll(self.speed, "units")
                    elif delta in [2, -2]:
                        self.canvas.xview_scroll(self.speed, "units")
                    else:
                        pass

                # linux scroll event
                elif gui.GET_PLATFORM() == gui.LINUX:
                    if event.num == 4:
                        self.canvas.yview_scroll(-1 * 2, "units")
                    elif event.num == 5:
                        self.canvas.yview_scroll(2, "units")
                # unknown platform scroll event
                else:
                    pass

                # finally, set some stuff
                self.times = []
                self.oldDelta = delta
                if newDelta in [1, -1, 2, -2]:
                    self.times.append(newDelta)
                self.lastScrollTime = timer
                self.speed = 1

        # no lastScrollTime set
        else:
            self.times = []
            if newDelta in [1, -1, 2, -2]:
                self.times.append(newDelta)
            self.lastScrollTime = timer
            self.speed = 1

    def getPane(self):
        return self.canvas

    def page_up(self, event):
        self.canvas.yview_scroll(-1, "page")
        return "break"

    def page_down(self, event):
        self.canvas.yview_scroll(1, "page")
        return "break"

    def unit_up(self, event):
        self.canvas.yview_scroll(-1, "unit")
        return "break"

    def unit_down(self, event):
        self.canvas.yview_scroll(1, "unit")
        return "break"

    def zoom_height(self, event):
        ZoomHeight.zoom_height(self.master)
        return "break"

#################################
# Additional Dialog Classes
#################################
# the main dialog class to be extended


class Dialog(Toplevel):

    def __init__(self, parent, title=None):
        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)
        self.parent = parent
        self.result = None

        # create a frame to hold the contents
        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        # create the buttons
        self.buttonbox()

        self.grab_set()
        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        gui.CENTER(self)

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
            self.initial_focus.focus_set()  # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        # call the validate function before calling the cancel function
        self.apply()
        self.cancel()

    # called when cancel button pressed
    def cancel(self, event=None):
        self.parent.focus_set()  # give focus back to the parent
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
            self.l1.config(text="")

    def setError(self, message):
        self.parent.bell()
        self.error = True
        self.l1.config(text=message)

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

# captures a number - must be a valid float


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
# Toplevel Stuff
#####################################


class SubWindow(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)
        self.escapeBindId = None  # used to exit fullscreen
        self.stopFunction = None  # used to stop
        self.geometry("+%d+%d" % (100, 100))

# removed for python2.7
#    def __getattr__(self, name):
#        def handlerFunction(*args, **kwargs):
#            print("Unknown function:", name, args, kwargs)
#        return handlerFunction

#####################################
# SimpleGrid Stuff
#####################################

# first row is used as a header


class SimpleGrid(Frame):

    def config(self, cnf=None, **kw):
        self.configure(cnf, **kw)

    def configure(self, cnf=None, **kw):
        kw = gui.CLEAN_CONFIG_DICTIONARY(**kw)
        if "bg" in kw:
            self.mainCanvas.config(bg=kw["bg"])
        if "activebackground" in kw:
            self.cellSelectedBg = kw.pop("activebackground")
        if "inactivebackground" in kw:
            self.cellBg = kw.pop("inactivebackground")
        if "font" in kw:
            font = kw.pop("font")
            self.gdFont.configure(
                family=font.actual("family"),
                size=font.actual("size"))
            self.ghFont.configure(
                family=font.actual("family"),
                size=font.actual("size") + 2,
                weight="bold")
        if "buttonFont" in kw:
            buttonFont = kw.pop("buttonFont")
            self.buttonFont.configure(
                family=buttonFont.actual("family"),
                size=buttonFont.actual("size"))

    def __init__(self, parent, title, data, action=None, addRow=False, **opts):
        if "buttonFont" in opts:
            self.buttonFont = opts.pop("buttonFont")
        else:
            self.buttonFont = font.Font(family="Helvetica", size=12)

        Frame.__init__(self, parent, **opts)

        if "font" in opts:
            self.gdFont = opts["font"]
            self.ghFont = opts["font"]
            self.ghFont.configure(
                size=self.ghFont.actual("size") + 2,
                weight="bold")
        else:
            self.gdFont = font.Font(family="Helvetica", size=12)
            self.ghFont = font.Font(family="Helvetica", size=14, weight="bold")

        # store them in the frame object for access, later
        self.action = action
        self.entries = []
        self.numColumns = 0
        self.numRows = len(data)
        # find out the max number of cells in a row
        for rowNum in range(self.numRows):
            if len(data[rowNum]) > self.numColumns:
                self.numColumns = len(data[rowNum])

        # a list of any selected cells
        from collections import OrderedDict
        self.selectedCells = OrderedDict()

        # colours
        self.cellHeadingBg = "DarkGray"      # HEADING BG
        self.cellBg = "LightCyan"        # CELL BG
        self.cellOverBg = "Silver"       # mouse over BG
        self.cellSelectedBg = "LightGray"     # selected cell BG

        # add a canvas for scrolling
        self.mainCanvas = Canvas(
            self,
            borderwidth=0,
            highlightthickness=2,
            bg=self.cget("bg"))
        vsb = Scrollbar(self, orient="vertical", command=self.mainCanvas.yview)
        hsb = Scrollbar(
            self,
            orient="horizontal",
            command=self.mainCanvas.xview)

        # pack them in
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        self.mainCanvas.pack(side="left", fill="both", expand=True)

        # add the grid cpntainer to the frame
        self.gridContainer = Frame(self.mainCanvas)
        self.mainCanvas.create_window(
            (4, 4), window=self.gridContainer, anchor="nw", tags="self.gridContainer")
        self.gridContainer.bind("<Configure>", self.__refreshGrids)

        # configure scrollCommands
        self.mainCanvas.configure(yscrollcommand=vsb.set)
        self.mainCanvas.configure(xscrollcommand=hsb.set)

        # bind scroll events
        if gui.GET_PLATFORM() == gui.LINUX:
            self.mainCanvas.bind_all(
                "<4>",
                lambda event,
                arg=title: self.__scrollGrid(
                    event,
                    arg))
            self.mainCanvas.bind_all(
                "<5>",
                lambda event,
                arg=title: self.__scrollGrid(
                    event,
                    arg))
        else:
            # Windows and MacOS
            self.mainCanvas.bind_all(
                "<MouseWheel>",
                lambda event,
                arg=title: self.__scrollGrid(
                    event,
                    arg))

        self.__addRows(data, addRow)

    def __addRows(self, data, addEntryRow=False):
        # loop through each row
        for rowNum in range(self.numRows):
            self.__addRow(rowNum, data[rowNum])

        # add a row of entry boxes...
        if addEntryRow:
            self.__addEntryBoxes()

    def addRow(self, rowData):
        self.__removeEntryBoxes()
        self.__addRow(self.numRows, rowData)
        self.numRows += 1
        self.__addEntryBoxes()

    def __addRow(self, rowNum, rowData):
        celContents = []
        # then the cells in that row
        for cellNum in range(self.numColumns):

            # get a val ("" if no val)
            if cellNum >= len(rowData):
                val = ""
            else:
                val = rowData[cellNum]
            celContents.append(val)

            lab = Label(self.gridContainer)
            if rowNum == 0:
                lab.configure(
                    relief=RIDGE,
                    text=val,
                    font=self.ghFont,
                    background=self.cellHeadingBg)
            else:
                lab.configure(
                    relief=RIDGE,
                    text=val,
                    font=self.gdFont,
                    background=self.cellBg)
                lab.bind("<Enter>", self.__gridCellEnter)
                lab.bind("<Leave>", self.__gridCellLeave)
                lab.bind("<Button-1>", self.__gridCellClick)
                gridPos = str(rowNum - 1) + "-" + str(cellNum)
                self.selectedCells[gridPos] = False
                lab.gridPos = gridPos

            lab.grid(row=rowNum, column=cellNum, sticky=N + E + S + W)
            Grid.columnconfigure(self.gridContainer, cellNum, weight=1)
            Grid.rowconfigure(self.gridContainer, rowNum, weight=1)

            # add some buttons for each row
            if self.action is not None:
                widg = Label(self.gridContainer, relief=RIDGE, height=2)
                # add the title
                if rowNum == 0:
                    widg.configure(
                        text="Action",
                        font=self.ghFont,
                        background=self.cellHeadingBg)
                # add a button
                else:
                    but = Button(
                        widg,
                        font=self.buttonFont,
                        text="Press",
                        command=gui.MAKE_FUNC(
                            self.action,
                            celContents))
                    but.place(relx=0.5, rely=0.5, anchor=CENTER)

                widg.grid(row=rowNum, column=cellNum + 1, sticky=N + E + S + W)

    def __removeEntryBoxes(self):
        for e in self.entries:
            e.lab.grid_forget()
            e.place_forget()
        self.ent_but.lab.grid_forget()
        self.ent_but.place_forget()

    def __addEntryBoxes(self):
        self.entries = []
        for cellNum in range(self.numColumns):
            name = "GR" + str(cellNum)
            lab = Label(self.gridContainer, relief=RIDGE, width=6, height=2)
            lab.grid(row=self.numRows, column=cellNum, sticky=N + E + S + W)

            # self.__buildEntry(name, self.gridContainer)
            ent = Entry(lab, width=5)
            ent.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.entries.append(ent)
            ent.lab = lab

        lab = Label(self.gridContainer, relief=RIDGE, height=2)
        lab.grid(
            row=self.numRows,
            column=self.numColumns,
            sticky=N + E + S + W)

        self.ent_but = Button(
            lab,
            font=self.buttonFont,
            text="Press",
            command=gui.MAKE_FUNC(
                self.action,
                "newRow"))
        self.ent_but.lab = lab
        self.ent_but.place(relx=0.5, rely=0.5, anchor=CENTER)

    def getEntries(self):
        return [e.get() for e in self.entries]

    def getSelectedCells(self):
        return dict(self.selectedCells)

    # function to scroll the canvas/scrollbars
    # gets the requested grid
    # and checks the event.delta to determine where to scroll
    # https://www.daniweb.com/programming/software-development/code/217059/using-the-mouse-wheel-with-tkinter-python
    def __scrollGrid(self, event, title):
        if gui.GET_PLATFORM() in [gui.WINDOWS, gui.LINUX]:
            if gui.GET_PLATFORM() == gui.WINDOWS:
                val = event.delta / 120
            else:
                val = event.delta

            val = val * -1

            if event.delta in [1, -1]:
                self.mainCanvas.yview_scroll(val, "units")
            elif event.delta in [2, -2]:
                self.mainCanvas.xview_scroll(val, "units")

        elif gui.GET_PLATFORM() == gui.LINUX:
            if event.num == 4:
                self.mainCanvas.yview_scroll(-1 * 2, "units")
            elif event.num == 5:
                self.mainCanvas.yview_scroll(2, "units")

    def __refreshGrids(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.mainCanvas.configure(scrollregion=self.mainCanvas.bbox("all"))
        #can.itemconfig(_id, height=frame.mainCanvas.height, width=frame.mainCanvas.width)

    def __gridCellEnter(self, event):
        cell = event.widget
        cell.config(background=self.cellOverBg)

    def __gridCellLeave(self, event):
        cell = event.widget
        gridPos = cell.gridPos
        if self.selectedCells[gridPos]:
            cell.config(background=self.cellSelectedBg)
        else:
            cell.config(background=self.cellBg)

    def __gridCellClick(self, event):
        cell = event.widget
        gridPos = cell.gridPos
        if self.selectedCells[gridPos]:
            self.selectedCells[gridPos] = False
            cell.config(background=self.cellBg)
        else:
            self.selectedCells[gridPos] = True
            cell.config(background=self.cellSelectedBg)


##########################
# Simple SplashScreen
##########################


class SplashScreen(Toplevel):
    def __init__(self, parent, text="appJar", fill="red", stripe="black", fg="white", font=44):
        Toplevel.__init__(self, parent)

        lab = Label(self, bg=stripe, fg=fg, text=text, height=3, width=50)
        lab.config(font=("Courier", font))
        lab.place(relx=0.5, rely=0.5, anchor=CENTER)

        width = str(self.winfo_screenwidth())
        height = str(self.winfo_screenheight())
        self.geometry(width+"x"+height)
        self.config(bg=fill)

        self.attributes("-alpha", 0.95)
        self.attributes("-fullscreen", True)
        self.overrideredirect(1)

        self.update()

##########################
# CopyAndPaste Organiser
##########################


class CopyAndPaste():

    def __init__(self, topLevel):
        self.topLevel = topLevel
        self.inUse = False

    def setUp(self, widget):
        self.inUse = True
        # store globals
        self.widget = widget
        self.widgetType = widget.__class__.__name__

        # query widget
        self.canCut = False
        self.canCopy = False
        self.canSelect = False
        self.canUndo = False
        self.canRedo = False

        try:
            self.canPaste = len(self.topLevel.clipboard_get()) > 0
        except:
            self.canPaste = False

        if self.widgetType in ["Entry", "AutoCompleteEntry"]:
            if widget.selection_present():
                self.canCut = self.canCopy = True
            if widget.index(END) > 0:
                self.canSelect = True
        elif self.widgetType in ["ScrolledText", "Text"]:
            if widget.tag_ranges("sel"):
                self.canCut = self.canCopy = True
            if widget.index("end-1c") != "1.0":
                self.canSelect = True
            if widget.edit_modified():
                self.canUndo = True
            self.canRedo = True
        elif self.widgetType == "OptionMenu":
            self.canCopy = True
            self.canPaste = False

    def copy(self):
        if self.widgetType == "OptionMenu":
            self.topLevel.clipboard_clear()
            self.topLevel.clipboard_append(self.widget.var.get())
        else:
            self.widget.event_generate('<<Copy>>')
            self.widget.selection_clear()

    def cut(self):
        if self.widgetType == "OptionMenu":
            self.topLevel.bell()
        else:
            self.widget.event_generate('<<Cut>>')
            self.widget.selection_clear()

    def paste(self):
        self.widget.event_generate('<<Paste>>')
        self.widget.selection_clear()

    def undo(self):
        try:
            self.widget.edit_undo()
        except:
            self.topLevel.bell()

    def redo(self):
        try:
            self.widget.edit_redo()
        except:
            self.topLevel.bell()

    def clearClipboard(self):
        self.topLevel.clipboard_clear()

    def clearText(self):
        try:
            self.widget.delete(0.0, END)  # TEXT
        except:
            try:
                self.widget.delete(0, END)  # ENTRY
            except:
                self.topLevel.bell()

    def selectAll(self):
        try:
            self.widget.select_range(0, END)  # ENTRY
        except:
            try:
                self.widget.tag_add("sel", "1.0", "end")  # TEXT
            except:
                self.topLevel.bell()

    # clear the undo/redo stack
    def resetStack(self): self.widget.edit_reset()

#####################################
# MAIN - for testing
#####################################
if __name__ == "__main__":
    print("This is a library class and cannot be executed.")
    sys.exit()
