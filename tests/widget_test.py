# -*- coding: utf-8 -*-
import sys
import time
import datetime
import pytest
import os
import turtle

try: from tkinter import Frame, Event, Label, Entry, Button, Radiobutton, Checkbutton, OptionMenu, Spinbox, Listbox, Message, PhotoImage, Scale, Canvas, LabelFrame, PanedWindow
except: from Tkinter import Frame, Event, Label, Entry, Button, Radiobutton, Checkbutton, OptionMenu, Spinbox, Listbox, Message, PhotoImage, Scale, Canvas, LabelFrame, PanedWindow

try: import ttk
except: from tkinter import ttk

photo="R0lGODlhPQBEAPeoAJosM//AwO/AwHVYZ/z595kzAP/s7P+goOXMv8+fhw/v739/f+8PD98fH/8mJl+fn/9ZWb8/PzWlwv///6wWGbImAP    gTEMImIN9gUFCEm/gDALULDN8PAD6atYdCTX9gUNKlj8wZAKUsAOzZz+UMAOsJAP/Z2ccMDA8PD/95eX5NWvsJCOVNQPtfX/8zM8+QePLl38MGBr8    JCP+zs9myn/8GBqwpAP/GxgwJCPny78lzYLgjAJ8vAP9fX/+MjMUcAN8zM/9wcM8ZGcATEL+QePdZWf/29uc/P9cmJu9MTDImIN+/r7+/vz8/P8VN    QGNugV8AAF9fX8swMNgTAFlDOICAgPNSUnNWSMQ5MBAQEJE3QPIGAM9AQMqGcG9vb6MhJsEdGM8vLx8fH98AANIWAMuQeL8fABkTEPPQ0OM5OSYdG    Fl5jo+Pj/+pqcsTE78wMFNGQLYmID4dGPvd3UBAQJmTkP+8vH9QUK+vr8ZWSHpzcJMmILdwcLOGcHRQUHxwcK9PT9DQ0O/v70w5MLypoG8wKOuwsP    /g4P/Q0IcwKEswKMl8aJ9fX2xjdOtGRs/Pz+Dg4GImIP8gIH0sKEAwKKmTiKZ8aB/f39Wsl+LFt8dgUE9PT5x5aHBwcP+AgP+WltdgYMyZfyywz78    AAAAAAAD///8AAP9mZv///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAKgALAAAAAA9AEQAAAj/AFEJHEiwoMGDCBMqXMiwocAbBww4nEhxoYkUpzJGrMixogkfGUNqlNi    xJEIDB0SqHGmyJSojM1bKZOmyop0gM3Oe2liTISKMOoPy7GnwY9CjIYcSRYm0aVKSLmE6nfq05QycVLPuhDrxBlCtYJUqNAq2bNWEBj6ZXRuyxZyD    RtqwnXvkhACDV+euTeJm1Ki7A73qNWtFiF+/gA95Gly2CJLDhwEHMOUAAuOpLYDEgBxZ4GRTlC1fDnpkM+fOqD6DDj1aZpITp0dtGCDhr+fVuCu3z    lg49ijaokTZTo27uG7Gjn2P+hI8+PDPERoUB318bWbfAJ5sUNFcuGRTYUqV/3ogfXp1rWlMc6awJjiAAd2fm4ogXjz56aypOoIde4OE5u/F9x199d    lXnnGiHZWEYbGpsAEA3QXYnHwEFliKAgswgJ8LPeiUXGwedCAKABACCN+EA1pYIIYaFlcDhytd51sGAJbo3onOpajiihlO92KHGaUXGwWjUBChjSP    iWJuOO/LYIm4v1tXfE6J4gCSJEZ7YgRYUNrkji9P55sF/ogxw5ZkSqIDaZBV6aSGYq/lGZplndkckZ98xoICbTcIJGQAZcNmdmUc210hs35nCyJ58    fgmIKX5RQGOZowxaZwYA+JaoKQwswGijBV4C6SiTUmpphMspJx9unX4KaimjDv9aaXOEBteBqmuuxgEHoLX6Kqx+yXqqBANsgCtit4FWQAEkrNbpq    7HSOmtwag5w57GrmlJBASEU18ADjUYb3ADTinIttsgSB1oJFfA63bduimuqKB1keqwUhoCSK374wbujvOSu4QG6UvxBRydcpKsav++Ca6G8A6Pr1x    2kVMyHwsVxUALDq/krnrhPSOzXG1lUTIoffqGR7Goi2MAxbv6O2kEG56I7CSlRsEFKFVyovDJoIRTg7sugNRDGqCJzJgcKE0ywc0ELm6KBCCJo8DI    PFeCWNGcyqNFE06ToAfV0HBRgxsvLThHn1oddQMrXj5DyAQgjEHSAJMWZwS3HPxT/QMbabI/iBCliMLEJKX2EEkomBAUCxRi42VDADxyTYDVogV+w    SChqmKxEKCDAYFDFj4OmwbY7bDGdBhtrnTQYOigeChUmc1K3QTnAUfEgGFgAWt88hKA6aCRIXhxnQ1yg3BCayK44EWdkUQcBByEQChFXfCB776aQs    G0BIlQgQgE8qO26X1h8cEUep8ngRBnOy74E9QgRgEAC8SvOfQkh7FDBDmS43PmGoIiKUUEGkMEC/PJHgxw0xH74yx/3XnaYRJgMB8obxQW6kL9QYE    J0FIFgByfIL7/IQAlvQwEpnAC7DtLNJCKUoO/w45c44GwCXiAFB/OXAATQryUxdN4LfFiwgjCNYg+kYMIEFkCKDs6PKAIJouyGWMS1FSKJOMRB/Bo    IxYJIUXFUxNwoIkEKPAgCBZSQHQ1A2EWDfDEUVLyADj5AChSIQW6gu10bE/JG2VnCZGfo4R4d0sdQoBAHhPjhIB94v/wRoRKQWGRHgrhGSQJxCS+0    pCZbEhAAOw=="


sys.path.append("../")
from appJar import gui
from appJar.appjar import Meter, Properties, PieChart, DraggableWidget, AjText, AjRectangle, AjPoint, AjScrolledText, SelectableLabel, ToggleFrame, PagedWindow, Page, SubWindow, ScrollPane, FrameStack, WIDGET_NAMES

PY_VER = str(sys.version_info[0]) + "." + str(sys.version_info[1])

EMPTY = ""

TEXT_ONE = "l_one_x"
TEXT_TWO = "l_one_y"
TEXT_THREE = "l_one_z"
TEXT_FOUR = "l_one_a"
TEXT_FIVE = "l_one_b"
MIXED_TEXT = "upper_AND_lower"

NUM_ONE = 23123
NUM_TWO = 33221

COL_ONE = "red"
COL_TWO = "yellow"
COL_THREE = "green"

LIST_ONE = ["a", "b", "c", "d", "e"]
LIST_TWO = ["v", "d", "s", "t", "z"]
LIST_THREE = ["", "v", "- d -", "s", "t", "z"]

HASH_ONE = {"a": True, "b": False, "c": True}
HASH_TWO = {"x": False, "y": True, "z": False}

# used for checking change function has been called...
CHANGE_FUNCTION_VAR=False

def CHANGE_FUNCTION():
    global CHANGE_FUNCTION_VAR
    CHANGE_FUNCTION_VAR = True
    print("CHANGE FUNCTION CALLED")

def CHECK_CHANGE_FUNCTION(value=True):
    global CHANGE_FUNCTION_VAR
    time.sleep(0.01)
    assert CHANGE_FUNCTION_VAR is value
    CHANGE_FUNCTION_VAR = False


def tester_function(btn=None, val1=None, val2=None):
    print(btn)
    return True

def test_grid_layout():
    print("\tTesting layout")
    assert isinstance(app.addLabel("lay1", TEXT_ONE, 1), Label)
    app.addLabel("lay2", TEXT_ONE, 1, 1)
    app.addLabel("lay3", TEXT_ONE, 1, 1, 1)
    app.addLabel("lay4", TEXT_ONE, 1, 1, 1, 1)
    app.addLabel("lay5", TEXT_ONE, 2)
    app.addLabel("lay6", TEXT_ONE, 2, 2)
    app.addLabel("lay7", TEXT_ONE, 2, 2, 2)
    app.addLabel("lay8", TEXT_ONE, 2, 2, 2, 2)

    app.addLabel("lay9", TEXT_ONE, colspan=3, rowspan=3, column=3, row=3)

    app.setSticky("n")
    app.addLabel("lay11", TEXT_ONE, colspan=4, rowspan=4, column=4, row=4)
    app.setSticky("s")
    app.addLabel("lay12", TEXT_ONE, colspan=5, rowspan=5, column=5, row=5)

    print("\t >> all tests complete")

def test_remover():
    app.addLabel("removeMe", TEXT_ONE)
    app.startLabelFrame("RemoveFrame")
    app.startPagedWindow("RemovePage")
    app.startPage()
    app.addLabel("removeMe2", TEXT_ONE)
    app.addLabel("removeMe3", TEXT_ONE)
    app.stopPage()
    app.stopPagedWindow()
    app.stopLabelFrame()
    app.addLabelEntry("removeMe4")
    app.removeAllWidgets()

def test_labels():
    print("\tTesting labels")
    assert isinstance(app.addEmptyLabel("el1"), Label)
    assert isinstance(app.addLabel("l0", TEXT_ONE), Label)
    with pytest.raises(Exception) :
        app.addLabel("l0", "crash here")
    app.addLabel("l1", TEXT_ONE)
    row = app.getRow()
    app.addLabel("rowl1", TEXT_ONE, row)
    assert app.gr() == row + 1
    assert isinstance(app.addFlashLabel("fl1", TEXT_ONE), Label)
    assert isinstance(app.addSelectableLabel("sl1", TEXT_ONE), SelectableLabel)
    assert isinstance(app.addLabel("nl1", None), Label)
    assert isinstance(app.addLabel("nl2", None), Label)

    assert app.getLabel("nl1") == "nl1"
    assert app.getLabel("nl2") == "nl2"

    app.addLabels(LIST_ONE)

    app.setLabelFg("sl1", "yellow")
    assert app.getLabelWidget("sl1").cget("fg") == "yellow"

    assert app.getLabel("el1") == EMPTY
    assert app.getLabel("l1") == TEXT_ONE
    assert app.getLabel("fl1") == TEXT_ONE
    assert app.getLabel("sl1") == TEXT_ONE

    app.setLabel("el1", TEXT_TWO)
    app.setLabel("l1", TEXT_TWO)
    app.setLabel("fl1", TEXT_TWO)

    assert app.getLabel("el1") == TEXT_TWO
    assert app.getLabel("l1") == TEXT_TWO
    assert app.getLabel("fl1") == TEXT_TWO

    app.clearLabel("el1")
    app.clearLabel("l1")
    app.clearLabel("fl1")

    assert app.getLabel("el1") == EMPTY
    assert app.getLabel("l1") == EMPTY
    assert app.getLabel("fl1") == EMPTY

    with pytest.raises(Exception) :
        app.addLabel("l1", "crash here")

    # call generic setter functions
    test_setters("Label", "l1")

    app.label("xx1", row=0, column=0, rowspan=0, colspan=0)
    app.label("xx2", row='p', column=0, rowspan=0, colspan=0)
    app.label("xx3", row='previous', column=0, rowspan=0, colspan=0)
    app.label("xx4", row='n', column=0, rowspan=0, colspan=0)
    app.label("xx5", row='next', column=0, rowspan=0, colspan=0)
    app.label("xx6", pos=(1,2,3,4))
    app.label("xx7", pos=(2,2,3,4))
    app.label("xx8", pos=('p',2,3,4))
    app.label("xx9", pos=('n',2,3,4))
    app.label("xx0", pos=(None,2,3,4))

    print("\t >> all tests complete")


def test_entries():
    print("\tTesting entries")
    assert isinstance(app.addEntry("e1"), Entry)
    with pytest.raises(Exception) :
        app.addEntry("e1")
    assert isinstance(app.addNumericEntry("ne1"), Entry)
    assert isinstance(app.addSecretEntry("se1"), Entry)

    # three key things: after, before, actual
    assert app._validateNumericEntry("1", None, "1", "", "1", None, None, None)
    assert not app._validateNumericEntry("1", None, "a", "", "a", None, None, None)
    assert app._validateNumericEntry("2", None, "a", "", "a", None, None, None)

    app.addFileEntry("ffe1")
    app.addDirectoryEntry("dfe1")
    app.addOpenEntry("ofe1")
    app.addSaveEntry("sfe1")

    assert isinstance(app.addAutoEntry("ae1", ["a", "b", "c"]), Entry)
    app.setAutoEntryNumRows("ae1", 5)
    app.appendAutoEntry("ae1", "newOne")
    app.appendAutoEntry("ae1", ["newTwo", "newThree"])
    app.removeAutoEntry("ae1", "newOne")
    app.changeAutoEntry("ae1", ["a", "b", "c"])

    # quick validation check
    app.addEntry("focusEnt")
    app.addValidationEntry("ve1")
#    app.addLabelValidationEntry("lve1")
    app.setEntryValid("ve1")
    app.setEntryInvalid("ve1")
    app.setEntryWaitingValidation("ve1")
    app.setValidationEntryLabelBg("ve1", "pink")

    # should fail with warning
    app.setEntryValid("e1")
    app.setEntryInvalid("e1")
    app.setEntryWaitingValidation("e1")

    app.addEntry("tester")
    app.setEntryDefault("tester", TEXT_TWO)
    app.addEntry("tester2")
    app.setEntryDefault("tester2", TEXT_TWO)
    app.addEntry("tester3")
    app.setEntryDefault("tester3", TEXT_TWO)

    app._entryIn("tester")
    app._entryOut("tester")
    app._entryIn("tester")
    app._entryOut("tester")

    app.setEntryDefault("tester3", TEXT_ONE)
    app.setEntryDefault("tester3", TEXT_TWO)
    app.setEntryDefault("tester3", TEXT_THREE)

    app.setEntryMaxLength("tester", 3)
    app.setEntryMaxLength("tester", 5)
    app.setEntry("tester", MIXED_TEXT)
    assert app.getEntry("tester") == MIXED_TEXT[:5]

    app.setEntryUpperCase("tester2")
    app.setEntryUpperCase("tester2")
    app.setEntry("tester2", MIXED_TEXT)
    assert app.getEntry("tester2") == MIXED_TEXT.upper()

    app.setEntryLowerCase("tester3")
    app.setEntryLowerCase("tester3")
    app.setEntry("tester3", MIXED_TEXT)
    assert app.getEntry("tester3") == MIXED_TEXT.lower()

    assert isinstance(app.addLabelEntry("le1"), Entry)
    assert isinstance(app.addLabelNumericEntry("lne1"), Entry)
    assert isinstance(app.addLabelSecretEntry("lse1"), Entry)
    assert isinstance(app.addLabelAutoEntry("lae1", ["a", "b", "c"]), Entry)

    assert app.getEntry("le1") == EMPTY
    print( app.getEntry("lne1") )
    assert app.getEntry("lne1") == None
    assert app.getEntry("lse1") == EMPTY
    assert app.getEntry("lae1") == EMPTY

    assert app.getEntry("e1") == EMPTY
    assert app.getEntry("ne1") == None
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

    entryVals = app.getAllEntries()
    assert entryVals["le1"] == EMPTY
    assert entryVals["lne1"] == None
    assert entryVals["lse1"] == EMPTY
    assert entryVals["lae1"] == EMPTY
    assert entryVals["e1"] == EMPTY
    assert entryVals["ne1"] == None
    assert entryVals["se1"] == EMPTY
    assert entryVals["ae1"] == EMPTY


    app.setEntryDefault("e1", TEXT_TWO)
    app.setEntryDefault("ne1", NUM_TWO)
    app.setEntryDefault("se1", TEXT_THREE)
    app.setEntryDefault("ae1", TEXT_FOUR)

    app.setEntryDefault("le1", TEXT_TWO)
    app.setEntryDefault("lne1", NUM_TWO)
    app.setEntryDefault("lse1", TEXT_THREE)
    app.setEntryDefault("lae1", TEXT_FOUR)

    assert app.getEntry("e1") == EMPTY
    assert app.getEntry("ne1") == None
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

    assert app.getEntry("le1") == EMPTY
    assert app.getEntry("lne1") == None
    assert app.getEntry("lse1") == EMPTY
    assert app.getEntry("lae1") == EMPTY

    app.setEntry("ne1", "-")
    assert app.getEntry("ne1") == None
    app.setEntry("ne1", ".")
    assert app.getEntry("ne1") == None
    app.setEntry("ne1", "0.0")
    assert app.getEntry("ne1") == 0
    app.setEntry("ne1", "-0.0")
    assert app.getEntry("ne1") == 0
    app.setEntry("ne1", ".")
    assert app.getEntry("ne1") == None

# should fail...
#    with pytest.raises(Exception) :
    app.setEntry("ne1", TEXT_ONE)

    app.setEntry("lne1", "-")
    assert app.getEntry("lne1") == None
    app.setEntry("lne1", ".")
    assert app.getEntry("lne1") == None
    app.setEntry("lne1", "0.0")
    assert app.getEntry("lne1") == 0
    app.setEntry("lne1", "-0.0")
    assert app.getEntry("lne1") == 0
    app.setEntry("lne1", ".")
    assert app.getEntry("lne1") == None

    app.setEntry("ne1", NUM_ONE)
    app.setEntry("e1", TEXT_ONE)
    app.setEntry("se1", TEXT_ONE)
    app.setEntry("ae1", TEXT_ONE)

    app.setEntry("lne1", NUM_ONE)
    app.setEntry("le1", TEXT_ONE)
    app.setEntry("lse1", TEXT_ONE)
    app.setEntry("lae1", TEXT_ONE)

    assert app.getEntry("e1") == TEXT_ONE
    assert app.getEntry("ne1") == float(NUM_ONE)
    assert app.getEntry("se1") == TEXT_ONE
    assert app.getEntry("ae1") == TEXT_ONE

    assert app.getEntry("le1") == TEXT_ONE
    assert app.getEntry("lne1") == float(NUM_ONE)
    assert app.getEntry("lse1") == TEXT_ONE
    assert app.getEntry("lae1") == TEXT_ONE

    entryVals = app.getAllEntries()
    assert entryVals["e1"] == TEXT_ONE
    assert entryVals["ne1"] == float(NUM_ONE)
    assert entryVals["se1"] == TEXT_ONE
    assert entryVals["ae1"] == TEXT_ONE
    assert entryVals["le1"] == TEXT_ONE
    assert entryVals["lne1"] == float(NUM_ONE)
    assert entryVals["lse1"] == TEXT_ONE
    assert entryVals["lae1"] == TEXT_ONE

    app.clearEntry("e1")
    app.clearEntry("ne1")
    app.clearEntry("se1")
    app.clearEntry("ae1")

    app.clearEntry("le1")
    app.clearEntry("lne1")
    app.clearEntry("lse1")
    app.clearEntry("lae1")

    assert app.getEntry("e1") == EMPTY
    assert app.getEntry("ne1") == None
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

    assert app.getEntry("le1") == EMPTY
    assert app.getEntry("lne1") == None
    assert app.getEntry("lse1") == EMPTY
    assert app.getEntry("lae1") == EMPTY

    app.setEntry("e1", TEXT_TWO)
    app.setEntry("ne1", NUM_TWO)
    app.setEntry("se1", TEXT_TWO)
    app.setEntry("ae1", TEXT_TWO)

    app.setEntry("le1", TEXT_TWO)
    app.setEntry("lne1", NUM_TWO)
    app.setEntry("lse1", TEXT_TWO)
    app.setEntry("lae1", TEXT_TWO)

    assert app.getEntry("e1") == TEXT_TWO
    assert app.getEntry("ne1") == float(NUM_TWO)
    assert app.getEntry("se1") == TEXT_TWO
    assert app.getEntry("ae1") == TEXT_TWO

    assert app.getEntry("le1") == TEXT_TWO
    assert app.getEntry("lne1") == float(NUM_TWO)
    assert app.getEntry("lse1") == TEXT_TWO
    assert app.getEntry("lae1") == TEXT_TWO

    app.clearAllEntries()

    assert app.getEntry("e1") == EMPTY
    assert app.getEntry("ne1") == None
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

    assert app.getEntry("le1") == EMPTY
    assert app.getEntry("lne1") == None
    assert app.getEntry("lse1") == EMPTY
    assert app.getEntry("lae1") == EMPTY

    app.setEntry("e1", TEXT_ONE)
    app.setEntry("ne1", NUM_ONE)
    app.setEntry("se1", TEXT_ONE)
    app.setEntry("ae1", TEXT_ONE)

    app.setEntry("le1", TEXT_ONE)
    app.setEntry("lne1", NUM_ONE)
    app.setEntry("lse1", TEXT_ONE)
    app.setEntry("lae1", TEXT_ONE)

    assert app.getEntry("e1") == TEXT_ONE
    assert app.getEntry("ne1") == float(NUM_ONE)
    assert app.getEntry("se1") == TEXT_ONE
    assert app.getEntry("ae1") == TEXT_ONE

    assert app.getEntry("le1") == TEXT_ONE
    assert app.getEntry("lne1") == float(NUM_ONE)
    assert app.getEntry("lse1") == TEXT_ONE
    assert app.getEntry("lae1") == TEXT_ONE

    # call generic setter functions
    test_setters("Entry", "e1")
    app.clearEntry("ne1")
    test_setters("Entry", "ne1")

    print("\t >> all tests complete")

def tst_but(btn):
    print(btn)

def test_buttons():
    print("\tTesting buttons")
    with pytest.raises(Exception) :
        app.addButton(["brk1", "brk1", "brk1", "brk1"], [None, None])

    assert isinstance(app.addButton("b1_func", tst_but), Button)
    with pytest.raises(Exception):
        app.addButton("b1_func", None)
    assert isinstance(app.addButton("b1", None), Button)
    app.addButtons(["bb1", "bb2", "bb3", "bb4"], None)
    with pytest.raises(Exception) :
        app.addButtons(["brk1", "brk1", "brk1", "brk1"], [None, None])
    with pytest.raises(Exception) :
        app.addButtons("Broken Buttons", None)
    app.addButtons(
            [["a2b1", "a2b2", "a2b3", "a2b4"],
            ["b2b1", "b2b2", "b2b3", "b2b4"],
            ["c2b1", "c2b2", "c2b3", "c2b4"]],
        None)

    def buts(btn):
        print(btn)
    app.addButtons(["bl1", "bl2"], buts)


    def testNoParam():
        pass

    app.addButton("NO PARAM", testNoParam)

    assert isinstance(app.addNamedButton("butName", "nb1", None), Button)  # name/title

    but1 = app.getButtonWidget("b1")
    but2 = app.getButtonWidget("bb1")
    but3 = app.getButtonWidget("a2b1")
    but4 = app.getButtonWidget("nb1")

    assert but1.cget("text") == "b1"
    assert but2.cget("text") == "bb1"
    assert but3.cget("text") == "a2b1"
    assert but4.cget("text") == "butName"

    app.setButton("b1", "newText")
    but1 = app.getButtonWidget("b1")
    assert but1.cget("text") == "newText"

    app.setButtonImage("bb1", "1_entries.gif")
    but1 = app.getButtonWidget("bb1")
    assert but1.cget("text") == ""
    app.setButtonImage("bb1", "1_entries.gif", align="top")

    assert isinstance(app.addImageButton("ib1", None, "1_entries.gif"), Button)
    assert isinstance(app.addIconButton("ib2", None, "map"), Button)

    assert isinstance(app.addImageButton("ib1a", None, "1_entries.gif", align="left"), Button)
    assert isinstance(app.addIconButton("ib2a", None, "map", align="right"), Button)

    but1 = app.getButtonWidget("ib1")
    assert but1.cget("text") == ""

    # call generic setter functions
    test_setters("Button", "b1")

    print("\t >> all tests complete")


def test_radios():
    print("\tTesting radios")
    assert isinstance(app.addRadioButton("rb", TEXT_ONE), Radiobutton)

    app.addRadioButton("rb", TEXT_TWO)
    with pytest.raises(Exception):
        app.addRadioButton("rb", TEXT_TWO)
    app.addRadioButton("rb", TEXT_THREE)

    app.addRadioButton("rb1", TEXT_TWO)
    app.addRadioButton("rb1", TEXT_THREE)

    app.addRadioButton("rb2", TEXT_THREE)
    app.addRadioButton("rb2", TEXT_TWO)

    assert app.getRadioButton("rb") == TEXT_ONE
    assert app.getRadioButton("rb1") == TEXT_TWO
    assert app.getRadioButton("rb2") == TEXT_THREE

    with pytest.raises(Exception):
        app.setRadioButton("rb", "BROKEN_BUTTON")

    app.setRadioButton("rb", TEXT_TWO)
    app.setRadioButton("rb1", TEXT_THREE)

    assert app.getRadioButton("rb") == TEXT_TWO
    assert app.getRadioButton("rb1") == TEXT_THREE
    assert app.getRadioButton("rb2") == TEXT_THREE

    app.setRadioTick("rb")
    app.setRadioTick("rb", True)
    app.setRadioTick("rb", False)

    app.setRadioSquare("rb")
    app.setRadioSquare("rb", True)
    app.setRadioSquare("rb", False)
    assert app.getRadioButton("rb") == TEXT_TWO

    app.setRadioButton("rb", TEXT_THREE)
    assert app.getRadioButton("rb") == TEXT_THREE

    rbs = app.getAllRadioButtons()
    assert rbs["rb"] == TEXT_THREE
    assert rbs["rb1"] == TEXT_THREE
    assert rbs["rb2"] == TEXT_THREE

    # call generic setter functions
    test_setters("RadioButton", "rb", TEXT_TWO)

    app.clearAllRadioButtons()
    assert app.getRadioButton("rb") == TEXT_ONE
    assert app.getRadioButton("rb1") == TEXT_TWO
    assert app.getRadioButton("rb2") == TEXT_THREE

    print("\t >> all tests complete")


def test_checks():
    print("\tTesting checks")
    assert isinstance(app.addCheckBox(TEXT_ONE), Checkbutton)
    app.addCheckBox(TEXT_TWO)
    with pytest.raises(Exception):
        app.addCheckBox(TEXT_TWO)
    app.addCheckBox(TEXT_THREE)
    assert isinstance(app.addNamedCheckBox(TEXT_TWO, "NCB1"), Checkbutton)
    app.addNamedCheckBox(TEXT_TWO, "NCB2")
    ncb3 = app.addNamedCheckBox(TEXT_TWO, "NCB3")

    assert app.getCheckBox(TEXT_ONE) is False
    assert app.getCheckBox(TEXT_TWO) is False
    assert app.getCheckBox(TEXT_THREE) is False
    assert app.getCheckBox("NCB1") is False
    assert app.getCheckBox("NCB2") is False
    assert app.getCheckBox("NCB3") is False

    assert ncb3.cget('text') == TEXT_TWO
    app.setCheckBoxText("NCB3", "new name")
    assert ncb3.cget('text') == "new name"

    cbs = app.getAllCheckBoxes()
    assert cbs[TEXT_ONE] is False
    assert cbs[TEXT_TWO] is False
    assert cbs[TEXT_THREE] is False
    assert cbs["NCB1"] is False
    assert cbs["NCB2"] is False
    assert cbs["NCB3"] is False
    app.setCheckBoxChangeFunction(TEXT_ONE, tester_function)

    app.setCheckBox(TEXT_ONE)
    app.setCheckBox(TEXT_TWO, True)
    app.setCheckBox(TEXT_THREE, False)

    assert app.getCheckBox(TEXT_ONE) is True
    assert app.getCheckBox(TEXT_TWO) is True
    assert app.getCheckBox(TEXT_THREE) is False
    assert app.getCheckBox("NCB1") is False
    assert app.getCheckBox("NCB2") is False
    assert app.getCheckBox("NCB3") is False

    app.setCheckBox("NCB2", True)

    assert app.getCheckBox(TEXT_ONE) is True
    assert app.getCheckBox(TEXT_TWO) is True
    assert app.getCheckBox(TEXT_THREE) is False
    assert app.getCheckBox("NCB1") is False
    assert app.getCheckBox("NCB2") is True
    assert app.getCheckBox("NCB3") is False

    cbs = app.getAllCheckBoxes()
    assert cbs[TEXT_ONE] is True
    assert cbs[TEXT_TWO] is True
    assert cbs[TEXT_THREE] is False
    assert cbs["NCB1"] is False
    assert cbs["NCB2"] is True
    assert cbs["NCB3"] is False

    app.clearAllCheckBoxes()
    assert app.getCheckBox(TEXT_ONE) is False
    assert app.getCheckBox(TEXT_TWO) is False
    assert app.getCheckBox(TEXT_THREE) is False
    assert app.getCheckBox("NCB1") is False
    assert app.getCheckBox("NCB2") is False
    assert app.getCheckBox("NCB3") is False

    # call generic setter functions
    test_setters("CheckBox", TEXT_ONE)

    app.setCheckBox(TEXT_TWO, ticked=True)
    app.setCheckBoxChangeFunction(TEXT_TWO, CHANGE_FUNCTION)
    app.setCheckBox(TEXT_TWO, ticked=False)
    CHECK_CHANGE_FUNCTION(True)
    app.setCheckBox(TEXT_TWO, ticked=True, callFunction=False)
    CHECK_CHANGE_FUNCTION(False)

    app.clearAllCheckBoxes(callFunction=True)
    CHECK_CHANGE_FUNCTION(True)
    app.setCheckBox(TEXT_TWO, ticked=True, callFunction=False)
    app.clearAllCheckBoxes(callFunction=False)
    CHECK_CHANGE_FUNCTION(False)

    print("\t >> all tests complete")


def test_options():
    print("\tTesting options")
    # add two option boxes
    assert isinstance(app.addOptionBox("l1", LIST_ONE), OptionMenu)
    app.addOptionBox("l2", LIST_TWO)
    with pytest.raises(Exception):
        app.addOptionBox("l2", LIST_TWO)

    assert app.getOptionBox("l1") == LIST_ONE[0]
    assert app.getOptionBox("l2") == LIST_TWO[0]

    obs = app.getAllOptionBoxes()
    assert obs["l1"] == LIST_ONE[0]
    assert obs["l2"] == LIST_TWO[0]

    print(LIST_ONE)
    print(LIST_TWO)

    # select new items - by position
    app.setOptionBox("l1", 3)
    app.setOptionBox("l2", 1)

    print( app.getOptionBox("l1") , LIST_ONE[3])
    print( app.getOptionBox("l2") , LIST_TWO[1])

    assert app.getOptionBox("l2") == LIST_TWO[1]
    assert app.getOptionBox("l1") == LIST_ONE[3]

    app.clearOptionBox("l1")
    assert app.getOptionBox("l1") == LIST_ONE[0]

    app.setOptionBox("l1", 2)
    app.clearAllOptionBoxes()
    assert app.getOptionBox("l1") == LIST_ONE[0]
    assert app.getOptionBox("l2") == LIST_TWO[0]

    # select new items - by position
    app.setOptionBox("l1", 2)
    app.setOptionBox("l2", 3)

    # select new items - by value
    app.setOptionBox("l1", LIST_ONE[3])
    app.setOptionBox("l2", LIST_TWO[1])
    app.renameOptionBoxItem("l2", LIST_TWO[0], "newName")

    assert app.getOptionBox("l1") == LIST_ONE[3]
    assert app.getOptionBox("l2") == LIST_TWO[1]

    # change the contents of l1
    app.changeOptionBox("l1", LIST_TWO)
    assert app.getOptionBox("l1") == LIST_TWO[0]
    assert app.getOptionBox("l2") == LIST_TWO[1]

    # delete option 1 from l1
    app.deleteOptionBox("l1", 1)
    app.setOptionBox("l1", 1)
    assert app.getOptionBox("l2") == LIST_TWO[1]
    assert app.getOptionBox("l1") == LIST_TWO[2]

    obs = app.getAllOptionBoxes()
    assert obs["l2"] == LIST_TWO[1]
    assert obs["l1"] == LIST_TWO[2]

    assert isinstance(app.addTickOptionBox("tl1", LIST_ONE), OptionMenu)
    app.addTickOptionBox("tl2", LIST_TWO)

    for item in LIST_ONE:
        assert app.getOptionBox("tl1")[item] is False

    for item in LIST_TWO:
        assert app.getOptionBox("tl2")[item] is False

    app.setOptionBox("tl1", LIST_ONE[1], True)
    app.setOptionBox("tl2", LIST_TWO[2], True)
    assert app.getOptionBox("tl2")[LIST_TWO[2]] is True

    app.clearOptionBox("tl2")
    for item in LIST_TWO:
        assert app.getOptionBox("tl2")[item] is False

    app.setOptionBox("tl2", LIST_TWO[2], True)


    assert app.getOptionBox("tl1")[LIST_ONE[1]] is True
    assert app.getOptionBox("tl2")[LIST_TWO[2]] is True

    app.changeOptionBox("tl1", LIST_TWO)
    for item in LIST_TWO:
        assert app.getOptionBox("tl1")[item] is False

    app.changeOptionBox("tl1", LIST_ONE)
    for item in LIST_ONE:
        assert app.getOptionBox("tl1")[item] is False

    app.renameOptionBoxItem("tl1", LIST_ONE[1], "new")
    NEW_TICKS = app.getOptionBox("tl1")
    NEW_LIST = LIST_ONE
    NEW_LIST.pop(1)
    for item in NEW_LIST:
        assert item in NEW_TICKS

    # test override disabled
    app.addOptionBox("l3", LIST_THREE)
    assert app.getOptionBox("l3") is None
    app.setOptionBox("l3", 1)
    assert app.getOptionBox("l3") == LIST_THREE[1]

    app.setOptionBox("l3", 0)
    assert app.getOptionBox("l3") == LIST_THREE[1]

    app.setOptionBox("l3", 0, override=True)
    assert app.getOptionBox("l3") != LIST_THREE[1]
    assert app.getOptionBox("l3") is None

    app.setOptionBoxDisabledChar("l3", "*")

    # call generic setter functions
    test_setters("OptionBox", "l1")
    test_setters("OptionBox", "tl1")

    app.setOptionBoxChangeFunction("l3", CHANGE_FUNCTION)
    app.setOptionBox("l3", LIST_THREE[2])
    CHECK_CHANGE_FUNCTION(True)
    app.setOptionBox("l3", LIST_THREE[1], callFunction=False)
    CHECK_CHANGE_FUNCTION(False)

    app.clearAllOptionBoxes(callFunction=True)
    CHECK_CHANGE_FUNCTION(True)
    app.setOptionBox("l3", LIST_THREE[2], callFunction=False)
    app.clearAllOptionBoxes(callFunction=False)
    CHECK_CHANGE_FUNCTION(False)

    print("\t>> all tests complete")


def test_spins():
    print("\tTesting spins")

    assert isinstance(app.addSpinBox("s1", ["a", "b", "c", "d", "e"]), Spinbox)
    app.addSpinBox("s2", ["a", "b", "c", "d", "e"])
    assert isinstance(app.addSpinBoxRange("s3", 5, 200), Spinbox)
    app.addSpinBoxRange("s4", 25, 200)
    with pytest.raises(Exception) :
        app.addSpinBoxRange("s4", 25, 200)

    with pytest.raises(Exception) :
        app.addSpinBox("bs", 77)

    assert app.getSpinBox("s1") == "a"
    assert app.getSpinBox("s2") == "a"
    assert app.getSpinBox("s3") == "5"
    assert app.getSpinBox("s4") == "25"

    sbs = app.getAllSpinBoxes()
    assert sbs["s1"] == "a"
    assert sbs["s2"] == "a"
    assert sbs["s3"] == "5"
    assert sbs["s4"] == "25"

    app.setSpinBoxPos("s4", 1)
    with pytest.raises(Exception) :
        app.setSpinBoxPos("s4", -50)
    with pytest.raises(Exception) :
        app.setSpinBoxPos("s4", 50000)
    with pytest.raises(Exception) :
        app.setSpinBox("s4", "not in spinbox")


    app.setSpinBox("s1", "b")
    app.setSpinBox("s2", "d")
    app.setSpinBox("s3", "200")
    app.setSpinBox("s4", "150")

    assert app.getSpinBox("s1") == "b"
    assert app.getSpinBox("s2") == "d"
    assert app.getSpinBox("s3") == "200"
    assert app.getSpinBox("s4") == "150"

    sbs = app.getAllSpinBoxes()
    assert sbs["s1"] == "b"
    assert sbs["s2"] == "d"
    assert sbs["s3"] == "200"
    assert sbs["s4"] == "150"

    app.clearAllSpinBoxes()
    assert app.getSpinBox("s1") == "a"
    assert app.getSpinBox("s2") == "a"
    assert app.getSpinBox("s3") == "5"
    assert app.getSpinBox("s4") == "25"

    # call generic setter functions
    test_setters("SpinBox", "s1")

    print("\t>> all tests complete")

def test_lists():
    print("\tTesting lists")

    assert isinstance(app.addListBox("l1", LIST_ONE), Listbox)
    app.addListBox("l2", LIST_TWO)
    app.setListBoxChangeFunction("l2", CHANGE_FUNCTION)
    with pytest.raises(Exception) :
        app.addListBox("l2", LIST_TWO)
    app.setListBoxSubmitFunction("l1", tester_function)

    app.setListItemBg("l1", LIST_ONE[1], "red")
    app.setListItemFg("l1", LIST_ONE[1], "green")

    assert app.getListBox("l1") == []
    assert app.getListBox("l2") == []

    assert app.getAllListItems("l1") == LIST_ONE
    assert app.getAllListItems("l2") == LIST_TWO

    app.addListItem("l1", "f")
    assert app.getListBox("l1") == ["f"]
    assert app.getAllListItems("l1") == LIST_ONE+["f"]

    app.addListItems("l2", LIST_ONE)
    assert app.getAllListItems("l2") == LIST_TWO+LIST_ONE
    assert app.getListBox("l2") == [LIST_ONE[len(LIST_ONE)-1]]

    app.setListBoxRows("l1", 2)
    app.setListBoxRows("l2", 10)

    assert app.getListBox("l2") == [LIST_ONE[len(LIST_ONE)-1]]

    app.clearListBox("l1")
    assert app.getListBox("l1") == []
    assert app.getListBox("l2") == [LIST_ONE[len(LIST_ONE)-1]]

    app.updateListBox("l1", LIST_ONE)
    app.selectListItem("l1", LIST_ONE[0])
    app.selectListItem("l1", LIST_ONE[3])
    assert app.getListBox("l1") == [LIST_ONE[3]]
    print("POS=", app.getListBoxPos("l1"))
    assert app.getListBoxPos("l1") == [3]

    app.setListBoxMulti("l1")
    app.setListBoxMulti("l1", True)
    app.setListBoxMulti("l1", False)
    app.setListBoxMulti("l1")

    app.selectListItem("l1", LIST_ONE[0])
    app.selectListItem("l1", LIST_ONE[3])
    assert app.getListBox("l1") == [LIST_ONE[0], LIST_ONE[3]]

    app.updateListBox("l2", LIST_TWO)
    assert app.getAllListItems("l2") == LIST_TWO
# SELECTING THE LAST ONE...

    app.updateListBox("l2", LIST_TWO, True)
    assert app.getListBox("l2") == [LIST_TWO[len(LIST_TWO)-1]]

    app.addListItem("l2", "new item")
    assert app.getListBox("l2") == ["new item"]

    app.addListItem("l2", "another new item", select=False)
    assert app.getListBox("l2") == ["new item"]

    app.addListBox("cl1", LIST_ONE)
    app.setListBoxChangeFunction("cl1", CHANGE_FUNCTION)
    app.setListItemAtPos("cl1", 0, "new_word")
    assert app.getAllListItems("cl1")[0] == "new_word"
    app.setListItem("cl1", "new_word", "newer_word")
    assert app.getAllListItems("cl1")[0] == "newer_word"
    app.setListItem("cl1", "newer_word", "newest_word", first=True)
    assert app.getAllListItems("cl1")[0] == "newest_word"

    app.updateListBox("l2", LIST_TWO, True, callFunction=True)
    CHECK_CHANGE_FUNCTION(True)
    app.updateListBox("l2", LIST_TWO, True, callFunction=False)
    CHECK_CHANGE_FUNCTION(False)
    app.removeListItem("l2", LIST_TWO[1])
    tmp_list = LIST_TWO
    tmp_list.remove(tmp_list[1])
    assert app.getAllListItems("l2") == tmp_list

    app.updateListBox("l2", LIST_TWO, True)
    app.removeListItemAtPos("l2", 1)
    with pytest.raises(Exception) :
        app.removeListItemAtPos("l2", 10000)

    tmp_list = LIST_TWO
    tmp_list.remove(tmp_list[1])
    assert app.getAllListItems("l2") == tmp_list

    app.addListBox("g1", LIST_ONE)
    app.setListBoxChangeFunction("g1", CHANGE_FUNCTION)
    app.addListBox("g2", LIST_TWO)
    app.setListBoxChangeFunction("g2", CHANGE_FUNCTION)

    app.selectListItemAtPos("g1", 1)
    assert app.getListBox("g1") == [LIST_ONE[1]]

    app.selectListItemAtPos("g1", 2)
    assert app.getListBox("g1") == [LIST_ONE[2]]

    app.selectListItem("g1", LIST_ONE[0])
    assert app.getListBox("g1") == [LIST_ONE[0]]
    assert app.getListBox("g2") == []

    lbs = app.getAllListBoxes()
    assert lbs["g1"] == [LIST_ONE[0]]
    assert lbs["g2"] == []

    app.selectListItem("g2", LIST_TWO[0])
    assert app.getListBox("g1") == []
    assert app.getListBox("g2") == [LIST_TWO[0]]

    app.updateListBox("g1", LIST_ONE)
    app.updateListBox("g2", LIST_TWO)

    app.setListBoxGroup("g1")
    app.setListBoxGroup("g2")

    app.selectListItem("g1", LIST_ONE[0])

    assert app.getListBox("g1") == [LIST_ONE[0]]
    assert app.getListBox("g2") == []

    lbs = app.getAllListBoxes()
    assert lbs["g1"] == [LIST_ONE[0]]
    assert lbs["g2"] == []

    app.selectListItem("g2", LIST_TWO[0])

    assert app.getListBox("g1") == [LIST_ONE[0]]
    assert app.getListBox("g2") == [LIST_TWO[0]]

    app.clearAllListBoxes()
    assert app.getListBox("g1") == []
    assert app.getListBox("g2") == []

    # call generic setter functions
    test_setters("ListBox", "l1")

    print("\t>> all tests complete")


def test_scales():
    print("\tTesting scales")
    assert isinstance(app.addScale("s1"), Scale)
    app.addScale("s2")
    with pytest.raises(Exception) :
        app.addScale("s2")
    app.addScale("s3")
    sc = app.addScale("s4")

    event = Event()
    event.widget = sc
    event.x_root = sc.winfo_rootx() + 5
    event.y_root = sc.winfo_rooty() + 5
    event.x = sc.winfo_rootx() + 5
    event.y = sc.winfo_rooty() + 5
    sc.jump(event)

    assert app.getScale("s1") == 0
    assert app.getScale("s2") == 0
    assert app.getScale("s3") == 0
    assert app.getScale("s4") == 0

    scales = app.getAllScales()
    assert scales["s1"] == 0
    assert scales["s2"] == 0
    assert scales["s3"] == 0
    assert scales["s4"] == 0

    app.setScale("s1", 20)
    app.setScale("s2", 73)
    app.setScale("s3", 100)
    app.setScale("s4", 101)

    app.setScaleIncrement("s1", 20)
    app.setScaleIncrement("s2", 73)

    assert app.getScale("s1") == 20
    assert app.getScale("s2") == 73
    assert app.getScale("s3") == 100
    assert app.getScale("s4") == 100

    scales = app.getAllScales()
    assert scales["s1"] == 20
    assert scales["s2"] == 73
    assert scales["s3"] == 100
    assert scales["s4"] == 100

    app.setScaleRange("s1", 44, 88)
    app.setScaleRange("s2", 22, 55, 33)
    assert app.getScale("s1") == 44
    assert app.getScale("s2") == 33

    app.showScaleIntervals("s3", 5)
    app.showScaleValue("s4", 101)
    assert app.getScale("s3") == 100
    assert app.getScale("s4") == 100

    app.setScaleHorizontal("s1")
    app.setScaleVertical("s2")
    app.setScaleHorizontal("s3")
    app.setScaleVertical("s4")

    assert app.getScale("s1") == 44
    assert app.getScale("s2") == 33
    assert app.getScale("s3") == 100
    assert app.getScale("s4") == 100

    app.setScaleWidth("s1", 220)
    app.setScaleLength("s1", 110)
    app.setScaleWidth("s3", 47)
    app.setScaleLength("s4", 88)

    assert app.getScale("s1") == 44
    assert app.getScale("s2") == 33
    assert app.getScale("s3") == 100
    assert app.getScale("s4") == 100

    sc = app.getWidget(app.Widgets.Scale, "s1")

    sc._jump("trough1")
    sc._jump("trough2")

    app.clearAllScales()
    print( app.getScale("s1"))
    assert app.getScale("s1") == 44
    assert app.getScale("s2") == 22
    assert app.getScale("s3") == 0
    assert app.getScale("s4") == 0

    # call generic setter functions
    test_setters("Scale", "s1")

    app.setScaleChangeFunction("s2", CHANGE_FUNCTION)
    app.setScale("s2", 22)
    CHECK_CHANGE_FUNCTION(True)
    app.setScale("s2", 88, callFunction=False)
    CHECK_CHANGE_FUNCTION(False)

    app.clearAllScales(callFunction=True)
    CHECK_CHANGE_FUNCTION(True)
    app.setScale("s2", 33, callFunction=False)
    app.clearAllScales(callFunction=False)
    CHECK_CHANGE_FUNCTION(False)

    print("\t >> all tests complete")


def test_message_boxes():
    print("\tTesting messages")
    assert isinstance(app.addMessage("m1", TEXT_ONE), Message)
    app.addMessage("m2", TEXT_TWO)
    with pytest.raises(Exception) :
        app.addMessage("m2", TEXT_TWO)
    assert isinstance(app.addEmptyMessage("m3"), Message)
    app.addEmptyMessage("m4")

    app.addMessage(TEXT_TWO)

    assert app.getMessage("m1") == TEXT_ONE
    assert app.getMessage("m2") == TEXT_TWO
    assert app.getMessage("m3") == EMPTY
    assert app.getMessage("m4") == EMPTY
    assert app.getMessage(TEXT_TWO) == TEXT_TWO

    app.setMessage("m1", EMPTY)
    app.setMessage("m2", TEXT_ONE)
    app.setMessage("m3", TEXT_THREE)
    app.setMessage("m4", EMPTY)
    app.setMessage(TEXT_TWO, TEXT_THREE)

    assert app.getMessage("m1") == EMPTY
    assert app.getMessage("m2") == TEXT_ONE
    assert app.getMessage("m3") == TEXT_THREE
    assert app.getMessage("m4") == EMPTY
    assert app.getMessage(TEXT_TWO) == TEXT_THREE

    app.setMessageAspect("m1", 200)
    app.setMessageWidth("m2", 40)

    app.clearMessage("m2")
    app.clearMessage("m3")
    app.clearMessage(TEXT_TWO)

    assert app.getMessageWidget("m1").cget("text") == EMPTY
    assert app.getMessageWidget("m2").cget("text") == EMPTY
    assert app.getMessageWidget("m3").cget("text") == EMPTY
    assert app.getMessageWidget("m4").cget("text") == EMPTY
    assert app.getMessageWidget(TEXT_TWO).cget("text") == EMPTY

    # call generic setter functions
    test_setters("Message", "m1")

    print("\t >> all tests complete")


def test_text_areas():
    print("\tTesting text areas")
    assert isinstance(app.addTextArea("t1"), AjText)
    ta2 = app.addTextArea("t2")
    with pytest.raises(Exception) :
        app.addTextArea("t2")
    assert isinstance(app.addScrolledTextArea("st1"), AjScrolledText)
    app.addScrolledTextArea("st2")

    app.textAreaCreateTag("t2", "red", background="red", foreground="white")
    app.textAreaChangeTag("t2", "red", background="red", foreground="white")
    assert "red" in app.getTextAreaTags("t2")
    app.textAreaDeleteTag("t2", "red")
    assert "red" not in app.getTextAreaTags("t2")
    app.textAreaCreateTag("t2", "red", background="red", foreground="white")
    assert "red" in app.getTextAreaTags("t2")
    app.getTextAreaTag("t2", "red")
    app.textAreaCreateTag("t2", "green", background="green", foreground="white")
    app.textAreaTagPattern("t2", "red", "this")

    assert app.getTextArea("t1") == EMPTY
    assert app.getTextArea("t2") == EMPTY
    assert app.getTextArea("st1") == EMPTY
    assert app.getTextArea("st2") == EMPTY

    tas = app.getAllTextAreas()

    assert tas["t1"] == EMPTY
    assert tas["t2"] == EMPTY
    assert tas["st1"] == EMPTY
    assert tas["st2"] == EMPTY

    app.logTextArea("t1")
    assert app.textAreaChanged("t1") is False
    app.logTextArea("t2")
    assert app.textAreaChanged("t2") is False
    app.logTextArea("st1")
    assert app.textAreaChanged("st1") is False
    app.logTextArea("st2")
    assert app.textAreaChanged("st2") is False

    app.setTextArea("t1", TEXT_ONE)
    app.setTextArea("t2", TEXT_TWO)
    app.setTextArea("st1", TEXT_THREE)
    app.setTextArea("st2", TEXT_FOUR)

    assert app.getTextArea("t1") == TEXT_ONE
    assert app.getTextArea("t2") == TEXT_TWO
    assert app.getTextArea("st1") == TEXT_THREE
    assert app.getTextArea("st2") == TEXT_FOUR

    # test disabled overriding
    ta2.config(state='disabled')
    assert ta2.cget('state') == 'disabled'
    app.setTextArea("t2", TEXT_ONE)
    assert app.getTextArea("t2") == TEXT_TWO+TEXT_ONE
    app.clearTextArea("t2")
    assert app.getTextArea("t2") == ""
    app.setTextArea("t2", TEXT_TWO)
    assert app.getTextArea("t2") == TEXT_TWO
    assert ta2.cget('state') == 'disabled'
    ta2.config(state='normal')
    assert ta2.cget('state') == 'normal'

    # test end flag
    app.setTextArea("t2", TEXT_TWO, end=True)
    assert app.getTextArea("t2") == TEXT_TWO+TEXT_TWO
    app.setTextArea("t2", TEXT_ONE, end=False)
    assert app.getTextArea("t2") == TEXT_ONE+TEXT_TWO+TEXT_TWO

    app.clearTextArea("t2")
    assert app.getTextArea("t2") == ""
    app.setTextArea("t2", TEXT_TWO)
    assert app.getTextArea("t2") == TEXT_TWO



    # nothing selected - so these have no effect
    app.textAreaTagSelected("t2", "red")
    app.textAreaUntagSelected("t2", "red")
    app.textAreaToggleTagSelected("t2", "red")
    app.highlightTextArea("t2", "1.0", "1.3")
    app.textAreaTagSelected("t2", "red")
    app.textAreaUntagSelected("t2", "red")
    app.textAreaToggleTagSelected("t2", "red")
    app.textAreaToggleTagSelected("t2", "red")
    app.textAreaToggleTagSelected("t2", "red")

    app.textAreaTagPattern("t2", "red", TEXT_TWO[2:4])
    app.textAreaTagRange("t2", "green", 1.0, 1.2)
    app.textAreaUntagRange("t2", "green", 1.0, 1.2)

    app.textAreaToggleTagRange("t2", "green", 1.0, 1.2)
    app.textAreaToggleTagRange("t2", "green", 1.0, 1.2)

    assert app.textAreaChanged("t1") is True
    assert app.textAreaChanged("t2") is True
    assert app.textAreaChanged("st1") is True
    assert app.textAreaChanged("st2") is True

    app.logTextArea("t1")
    assert app.textAreaChanged("t1") is False
    app.logTextArea("t2")
    assert app.textAreaChanged("t2") is False
    app.logTextArea("st1")
    assert app.textAreaChanged("st1") is False
    app.logTextArea("st2")
    assert app.textAreaChanged("st2") is False

    assert app.getTextArea("t1") == TEXT_ONE
    assert app.getTextArea("t2") == TEXT_TWO
    assert app.getTextArea("st1") == TEXT_THREE
    assert app.getTextArea("st2") == TEXT_FOUR

    tas = app.getAllTextAreas()
    assert tas["t1"] == TEXT_ONE
    assert tas["t2"] == TEXT_TWO
    assert tas["st1"] == TEXT_THREE
    assert tas["st2"] == TEXT_FOUR

    app.clearTextArea("t2")
    app.clearTextArea("st1")

    assert app.getTextArea("t1") == TEXT_ONE
    assert app.getTextArea("t2") == EMPTY
    assert app.getTextArea("st1") == EMPTY
    assert app.getTextArea("st2") == TEXT_FOUR

    print(app.searchTextArea("t1", TEXT_ONE, "1.0"))
    assert app.searchTextArea("t1", TEXT_ONE, "1.0") == "1.0"

    app.clearAllTextAreas()
    assert app.getTextArea("t1") == EMPTY
    assert app.getTextArea("t2") == EMPTY
    assert app.getTextArea("st1") == EMPTY
    assert app.getTextArea("st2") == EMPTY

    app.setTextAreaFont("t1", size=20, family='Verdana')
    app.setTextArea("t1", TEXT_ONE)
    app.highlightTextArea("t1", "1.0")

    app.textAreaToggleFontSelected("t1", "BOLD")
    app.textAreaToggleFontSelected("t1", "BOLD")
    app.textAreaApplyFontSelected("t1", "BOLD")

    app.textAreaToggleFontSelected("t1", "ITALIC")
    app.textAreaToggleFontSelected("t1", "ITALIC")
    app.textAreaApplyFontSelected("t1", "ITALIC")

    app.textAreaToggleFontSelected("t1", "UNDERLINE")
    app.textAreaToggleFontSelected("t1", "UNDERLINE")
    app.textAreaApplyFontSelected("t1", "UNDERLINE")

    app.textAreaToggleFontSelected("t1", "BOLD_ITALIC")
    app.textAreaToggleFontSelected("t1", "BOLD_ITALIC")
    app.textAreaApplyFontSelected("t1", "BOLD_ITALIC")

    # call generic setter functions
    test_setters("TextArea", "t1")

    print("\t >> all tests complete")

def test_meters():
    print("\tTesting meters")
    assert isinstance(app.addMeter("m1"), Meter)
    with pytest.raises(Exception) :
        app.addMeter("m1")
    assert app.getMeter("m1")[0] == 0

    app.setMeter("m1", 45)
    assert app.getMeter("m1")[0] == 0.45

    assert isinstance(app.addSplitMeter("spm"), Meter)
    assert isinstance(app.addDualMeter("dum"), Meter)

    app.setMeter("spm", 50)
    app.setMeter("dum", [50, 10])

    mets = app.getAllMeters()
    assert mets["m1"][0] == 0.45
    assert mets["spm"][0] == 0.5
    assert mets["dum"][0] == [-0.5,0.1]

    app.setMeterFill("spm", ["red", "green"])
    app.setMeterFill("dum", ["red", "pink"])

    app.getMeter("spm")
    app.getMeter("dum")

    app.setMeter("m1", 25, TEXT_ONE)
    app.setMeter("m1", 5000)
    app.setMeter("m1", -5000)

    # call generic setter functions
    test_setters("Meter", "m1")

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def compareDictionaries(d1, d2):
    for key in d1.keys():
        if d1[key] != d2[key]:
            return False
    for key in d2.keys():
        if d1[key] != d2[key]:
            return False
    return True


def validateProp(p, d):
    for key in d.keys():
        assert app.getProperty(p, key) == d[key]


def test_properties():
    print("\tTesting properties")

    app.startToggleFrame("PP_frame")
    assert isinstance(app.addProperties("tog_p1", HASH_ONE), Properties)
    app.stopToggleFrame()


    assert isinstance(app.addProperties("p1", HASH_ONE), Properties)
    app.addProperties("p2")
    with pytest.raises(Exception) :
        app.addProperties("p2")

    assert compareDictionaries(app.getProperties("p1"), HASH_ONE)
    assert app.getProperties("p2") == {}

    app.resetProperties("p1")
    assert compareDictionaries(app.getProperties("p1"), HASH_ONE)
    app.resetProperties("p1")
    assert app.getProperties("p2") == {}

    app.resetAllProperties()
    assert compareDictionaries(app.getProperties("p1"), HASH_ONE)
    assert app.getProperties("p2") == {}

    props = app.getAllProperties()
    assert compareDictionaries(props["p1"], HASH_ONE)
    assert props["p2"] == {}

    validateProp("p1", HASH_ONE)
    app.setPropertyText("p2", "a", "new text")
    app.setPropertyText("p2", "b")

    app.setPropertiesBoxBg("p2", "red")
    app.setPropertiesSelectColour("p2", "red")

    app.setProperties("p2", HASH_TWO)
    validateProp("p2", HASH_TWO)
    assert compareDictionaries(app.getProperties("p2"), HASH_TWO)

    hash_all = HASH_ONE.copy()
    hash_all.update(HASH_TWO)

    app.setProperties("p2", HASH_ONE)
    validateProp("p2", hash_all)
    assert compareDictionaries(app.getProperties("p2"), hash_all)
    props = app.getAllProperties()
    assert compareDictionaries(props["p2"], hash_all)

    for key in hash_all.keys():
        hash_all[key] = False

    assert not compareDictionaries(app.getProperties("p2"), hash_all)
    app.setProperties("p2", hash_all)
    assert compareDictionaries(app.getProperties("p2"), hash_all)

    app.setProperty("p2", "a", True)
    assert app.getProperty("p2", "a") is True

    for p in HASH_ONE:
        app.deleteProperty("p2", p)

    app.setProperties("p2", HASH_TWO)
    assert compareDictionaries(HASH_TWO, app.getProperties("p2"))

    EMPTY_HASH={}
    for key in HASH_TWO.keys():
        EMPTY_HASH[key] = False

    app.resetProperties("p2")
    assert compareDictionaries(HASH_TWO, app.getProperties("p2"))

    app.clearProperties("p2")
    assert compareDictionaries(EMPTY_HASH, app.getProperties("p2"))

    app.resetProperties("p2")
    assert compareDictionaries(HASH_TWO, app.getProperties("p2"))

    app.clearAllProperties()
    assert compareDictionaries(EMPTY_HASH, app.getProperties("p2"))

    # call generic setter functions
    test_setters("Properties", "p1")

    print("\t >> all tests complete")


def test_separators():
    print("\tTesting separators")
    assert isinstance(app.addHorizontalSeparator(), Frame)
    assert isinstance(app.addHorizontalSeparator(colour="green"), Frame)
    assert isinstance(app.addVerticalSeparator(), Frame)
    assert isinstance(app.addVerticalSeparator(colour="pink"), Frame)
    print("\t >> all tests complete")

def linkPressed(link=None):
    print(link)

def test_links():
    print("\tTesting links")
    assert isinstance(app.addLink("l1", None), Label)
#    with pytest.raises(Exception) :
#        app.addLink("l1", None)
    assert isinstance(app.addLink("l2", linkPressed), Label)
    assert isinstance(app.addWebLink("l3", "http://appJar.info"), Label)
    with pytest.raises(Exception) :
        app.addWebLink("l4", "appJar.info")

    link = app.addLink("lx", linkPressed)
    link.enter(None)
    link.leave(None)

    # call generic setter functions
    test_setters("Link", "l1")
    test_setters("Link", "l2")

    print("\t >> all tests complete")


def test_grips():
    print("\tTesting grips")
    assert isinstance(app.addGrip(), Label)
    grip = app.addGrip()
    event = Event()
    event.widget = grip
    event.x = 100
    event.y = 100
    grip.StartMove(event)
    event.x = 150
    event.y = 150
    grip.OnMotion(event)
    grip.StopMove(event)
    print("\t >> all tests complete")


def test_auto_labels():
    print("\tTesting auto_labels")
    app.addLabelEntry("lab_ent")
    app.addLabelFileEntry("lab_ent_file")
    app.addLabelOpenEntry("lab_ent_open")
    app.addLabelSaveEntry("lab_ent_save")
    app.addLabelDirectoryEntry("lab_ent_dir")
    app.addLabelNumericEntry("lab_num_ent")
    app.addLabelSecretEntry("lab_sec_ent")
    app.addLabelAutoEntry("lab_auto_ent", LIST_ONE)
    app.addLabelScale("lab_scale")
    app.addLabelOptionBox("lab_opt_box", LIST_ONE)
    app.addLabelTickOptionBox("lab_tick_box", LIST_ONE)
    app.addLabelSpinBox("lab_spin_box", LIST_ONE)
    app.addLabelSpinBoxRange("lab_spin_box_range", 0, 20)
    print("\t >> all tests complete")


def test_date_pickers():
    print("\tTesting date pickers")
    app.addDatePicker("d1")
    with pytest.raises(Exception) :
        app.addDatePicker("d1")
    app.addDatePicker("d2")
    app.addDatePicker("d3")

    def changer(btn):
        print(btn)
    app.setDatePickerChangeFunction("d2", changer)

    assert app.getDatePicker("d1") == datetime.date(1970, 1, 1)
    assert app.getDatePicker("d2") == datetime.date(1970, 1, 1)
    assert app.getDatePicker("d3") == datetime.date(1970, 1, 1)

    app.setDatePicker("d1")
    app.setDatePicker("d2", datetime.date(1980, 5, 5))
    app.setDatePicker("d3", datetime.date(1990, 10, 10))

    app.setDatePickerFg("d1", "green")

    print(app.getDatePicker("d1"))
    print(datetime.date.today())
    assert app.getDatePicker("d1") == datetime.date.today()
    assert app.getDatePicker("d2") == datetime.date(1980, 5, 5)
    assert app.getDatePicker("d3") == datetime.date(1990, 10, 10)

    dps = app.getAllDatePickers()
    assert dps["d1"] == datetime.date.today()
    assert dps["d2"] == datetime.date(1980, 5, 5)
    assert dps["d3"] == datetime.date(1990, 10, 10)

    app.setDatePickerRange("d1", 1940, None)
    app.setDatePickerRange("d1", 1940, 1960)
    app.setDatePickerRange("d2", 1980, 2020)
    app.setDatePickerRange("d3", 2020, 2040)

    assert app.getDatePicker("d1") == datetime.date(1940,
                                        datetime.date.today().month,
                                        datetime.date.today().day)
    assert app.getDatePicker("d2") == datetime.date(1980, 5, 5)
    assert app.getDatePicker("d3") == datetime.date(2020, 10, 10)

    app.setDatePicker("d1", datetime.date(1950, 5, 5))
    app.setDatePicker("d2", datetime.date(1990, 5, 5))
    app.setDatePicker("d3", datetime.date(2021, 10, 10))

    assert app.getDatePicker("d1") == datetime.date(1950, 5, 5)
    assert app.getDatePicker("d2") == datetime.date(1990, 5, 5)
    assert app.getDatePicker("d3") == datetime.date(2021, 10, 10)

    dps = app.getAllDatePickers()
    assert dps["d1"] == datetime.date(1950, 5, 5)
    assert dps["d2"] == datetime.date(1990, 5, 5)
    assert dps["d3"] == datetime.date(2021, 10, 10)

    app.clearDatePicker("d1")
    assert app.getDatePicker("d1") == datetime.date(1940, 1, 1)

    app.clearAllDatePickers()
    assert app.getDatePicker("d1") == datetime.date(1940, 1, 1)
    assert app.getDatePicker("d2") == datetime.date(1980, 1, 1)
    assert app.getDatePicker("d3") == datetime.date(2020, 1, 1)


    # call generic setter functions
#    test_setters("DatePicker", "d1")

    print("\t >> all tests complete")


def test_pies():
    print("\tTesting Pies")
    assert isinstance(app.addPieChart("p1", {"apples": 50, "oranges": 200, "grapes": 75, "beef": 300, "turkey": 150}), PieChart)
    app.setPieChart("p1", "beef", 5)
    app.setPieChart("p1", "fish", 20)
    app.setPieChart("p1", "apples", 0)

    with pytest.raises(Exception) :
        app.addPieChart("p1", {"apples": 50, "oranges": 200, "grapes": 75, "beef": 300, "turkey": 150})

    # call generic setter functions
    test_setters("PieChart", "p1")

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_trees():
    print("\tTesting Trees")
    xml_str = """<people>
        <person><name>Fred</name><age>45</age><gender>Male</gender></person>
        <person a="aaa"><name>Tina</name><age>37</age><gender>Female</gender></person>
        <person><name>CLive</name><age>28</age><gender>Male</gender></person>
        <person><name>Betty</name><age>51</age><gender b='bbb'>Female</gender></person>
        </people>"""

    app.addTree("t1", xml_str)

    with pytest.raises(Exception) :
        app.addTree("t1", xml_str)

    app.setTreeDoubleClickFunction("t1", tester_function)
    app.setTreeEditFunction("t1", tester_function)
    app.setTreeEditable("t1", True)
    app.showTreeAttributes("t1")
    app.setTreeEditable("t1", False)
    app.setTreeBg("t1", "red")
    app.setTreeFg("t1", "yellow")
    app.setTreeHighlightBg("t1", "orange")
    app.setTreeHighlightFg("t1", "pink")
    
    app.getTreeXML("t1")
    app.getTreeSelected("t1")
    app.getTreeSelectedXML("t1")

    app.setTreeColours("t1", "red", "yellow", "yellow", "red")

    from xml.dom.minidom import parseString

    app.tree("t2", parseString(xml_str), attributes=True, click=tester_function, dbl=tester_function, edit=tester_function, editable=True,
                fg="green", bg="yellow", fgH="pink", bgH="blue")

    # call generic setter functions
#    test_setters("Tree", "t1")

    print(" >> not implemented...")
    #print("\t >> all tests complete")

def test_tables():
    print("\tTesting Tables")
    app.addTable("t1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["Tina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]],
        action=tester_function,
        actionButton=["aaa", "bbb"],
        horizontal=False,
        addRow=tester_function,
        wrap=200,
        inactiveFg='red',
        inactiveBg='red',
        activeFg='red',
        activeBg='red',
        )

    with pytest.raises(Exception) :
        app.addTable("g1", [])

    app.getTableEntries("t1")
    app.getTableSelectedCells("t1")
    app.addTableRow("t1", ["aaa", 22, "Male"])

    app.setTableActiveFg('t1', 'green')
    app.setTableActiveBg('t1', 'green')
    app.setTableInactiveFg('t1', 'green')
    app.setTableInactiveBg('t1', 'green')

    # call generic setter functions
    test_setters("Table", "g1")

    app.addDbTable('db1', 'test.db',
        table='projects',
        actionButton=["aaa", "bbb"],
        horizontal=True)
    app.addReplaceDbTable('db1', 'test.db', 'projects')
    app.addRefreshDbTable('db1')

    app.addDbOptionBox('db1', 'test.db')
    app.refreshDbOptionBox('db1', 'test.db')

    app.getTableRow("db1", 1)
    app.getTableEntries("db1")
    app.getTableSelectedCells("db1")
    app.getTableEntries("db1")

    app.addTableRows("db1", ['a', 'b', 'c'])
    app.replaceTableRow("db1", 0, ['a', 'b', 'c'])

    print(" >> not implemented...")
    #print("\t >> all tests complete")



def test_grids():
    print("\tTesting Grids")
    app.addGrid("g1",
        [["Name", "Age", "Gender"],
        ["Fred", 45, "Male"],
        ["Tina", 37, "Female"],
        ["Clive", 28, "Male"],
        ["Betty", 51, "Female"]],
        action=tester_function,
        addRow=tester_function)

    with pytest.raises(Exception) :
        app.addGrid("g1", [])

    app.getGridEntries("g1")
    app.getGridSelectedCells("g1")
    app.addGridRow("g1", ["aaa", 22, "Male"])

    # call generic setter functions
    test_setters("Grid", "g1")

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_gui_options():
    print("\tTesting gui options")
    app.setTitle("New title")
    assert app.getTitle() == "New title"
    assert app.title == "New title"

    app.title = "Newer title"
    assert app.title == "Newer title"
    assert app.getTitle() == "Newer title"

    app.setTransparency(50)
    app.setTransparency(50)

    app.setSize("100x100")
    app.setSize(200,200)
    app.setSize("Fullscreen")
    app.setSize("fullscreen")
    app.exitFullscreen()

    app.setResizable()
    assert app.getResizable() is True
    app.setResizable(True)
    assert app.getResizable() is True
    app.setResizable(False)
    assert app.getResizable() is False
    app.setResizable()
    assert app.getResizable() is True

    app.setLocation(-200,2000)
    app.setLocation(200,200)
    app.setLocation("CENTER")

    app.setGuiPadding(20,20)
    app.setGuiPadding([20,20])
    app.hideTitleBar()
    app.showTitleBar()

    app.resizeBgImage()
    app.setBgImage("1_entries.gif")
    app.resizeBgImage()
    app.removeBgImage()

    app.setBg("green")
    app.setFg("orange")
    app.setFont(20)
    app.decreaseFont()
    app.increaseFont()
    app.setLabelFont(20)
    app.increaseLabelFont()
    app.decreaseLabelFont()
    app.setButtonFont(20)
    app.increaseButtonFont()
    app.decreaseButtonFont()
    app.setStatusFont(9)

    app.setBgImage("1_entries.gif")
    app.resizeBgImage()
    app.removeBgImage()

    app.setRowspan(4)
    assert app.getRowspan() == 4
    app.setRowspan(0)
    assert app.getRowspan() == 0
    app.setColspan(4)
    assert app.getColspan() == 4
    app.setColspan(0)
    assert app.getColspan() == 0

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_widget_arranging():
    print("\tTesting widget arranging")

    app.setStretch("none")
    app.setStretch("row")
    app.setStretch("column")
    app.setStretch("both")

    app.setSticky("n")
    app.setSticky("ne")
    app.setSticky("nw")
    app.setSticky("ew")
    app.setSticky("news")
    app.setSticky("")

    app.setPadding(5,10)
    app.setInPadding(5,10)

    app.setPadding([5,10])
    app.setInPadding([5,10])

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def eventTester(e=None, a=0, b=0, c=0):
    print(e)

def test_events():
    print("\tTesting events")

    app.enableEnter(tester_function)
    app.disableEnter()

    app.bindKey("b", tester_function)
    app.unbindKey("B")

    app.bindKeys(["c", "d", "<Up>", "<F1>"], tester_function)
    app.unbindKeys(["C", "<Up>", "<F1>"])

    app.registerEvent(tester_function)
    app.setPollTime(2)
    app.setPollTime(0.5)

    app.setStopFunction(tester_function)

    app.afterIdle(eventTester)
    app.after(0, eventTester)
    app.after(5, eventTester)
    e_id = app.after(10, eventTester)
    app.afterCancel(e_id)

    app.afterIdle(eventTester, "a")
    app.after(5, eventTester, "a")

    print(" >> not implemented...")
    #print("\t >> all tests complete")

def run_events(param1, bbb):

    time.sleep(1)
    assert app.getLabel("test_threads") == "full"
    app.queuePriorityFunction(app.setLabel, "test_threads", "priority")
    app.queuePriorityFunction(checkPriority)

def checkPriority():
    print("SHOULD be PRIOR>>>", app.getLabel("test_threads"))
    assert app.getLabel("test_threads") == "priority"

def test_images():
    print("\tTesting images")

    assert isinstance(app.addImage("im1", "1_flash.gif", compound="left"), PhotoImage)
    with pytest.raises(Exception) :
        app.addImage("im1", "1_flash.gif")
    app.addImage("anim1", "1_flash.gif")

    app.setAnimationSpeed("im1", -10)
    app.setAnimationSpeed("im1", 10)
    app.startAnimation("im1")
    app.stopAnimation("im1")
    app.startAnimation("im1")

    im = app.addImage("im2", "1_entries.gif")
    ic = app.addIcon("ic2", "map")
    ic2 = app.addImage("ic3", os.path.join(app.icon_path, "map.png"))

    coords = {
        "America":[32, 17, 242, 167],
        "South America":[126, 170, 226, 292],
    }

    def click(area):
        print(area)

    app.setImageMap("im2", click, coords)
    event = Event()
    event.widget = im
    event.x = 100
    event.y = 100
    app._imageMap("im2", event)

    assert isinstance(app.addImage("im3", "1_checks.png"), PhotoImage)
    assert isinstance(app.addImage("im4", "sc.jpg"), PhotoImage)
    dat = app.getImageDimensions("im3")
    assert dat[0] == 115
    assert dat[1] == 146

# jpeg...

    app.setImage("im3", None)
    app.setImage("im3", "1_entries.gif")
    app.reloadImage("im3", "1_entries.gif")
    app.setImageMouseOver("im1", "1_checks.png")
    app.setImageSize("im2", 40, 40)
    app.zoomImage("im1", -2)
    app.zoomImage("im1", 2)

    app.shrinkImage("im3", 2)
    app.growImage("im3", 2)

#    app.setBgImage("1_checks.png")
#    app.removeBgImage()

    assert app.getImagePath(None) is None

    with pytest.raises(Exception) :
        app.setImageLocation("FRance")

    app.setImageLocation("images")
    app.addImage("iml", "1_entries.gif")
    app.setImageSubmitFunction("im1", click)

    assert isinstance(app.addImageData("id1", photo), PhotoImage)
    app.setImageData("id1", photo)
    app.reloadImageData("id1", photo)
    app.clearImageCache()

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_status():
    print("\tTesting Statusbar")

    app.addStatusbar(TEXT_ONE, 4, "RIGHT")
    assert len(app._statusFields) == 4

    with pytest.raises(Exception) :
        app.setStatusbar(TEXT_ONE, 43)

    assert len(app._statusFields) == 4
    app.removeStatusbarField(3)
    assert len(app._statusFields) == 3

    app.removeStatusbar()
    assert len(app._statusFields) == 0

    app.addStatusbar(TEXT_ONE, 3, "RIGHT")
    assert len(app._statusFields) == 3

    app.setStatusbar(TEXT_ONE)
    app.setStatusbar(TEXT_ONE, None)
    app.setStatusbar(TEXT_ONE, 2)

    app.setStatusbarBg("red")
    app.setStatusbarBg("red", None)
    app.setStatusbarBg("pink", 0)
    with pytest.raises(Exception) :
        app.setStatusbarBg("orange", -4)

    app.setStatusbarFg("red")
    app.setStatusbarFg("yellow", None)
    app.setStatusbarFg("yellow", 1)
    with pytest.raises(Exception) :
        app.setStatusbarFg("orange", -4)

    app.setStatusbarWidth(100)
    app.setStatusbarWidth(100, None)
    app.setStatusbarWidth(100, 2)
    with pytest.raises(Exception) :
        app.setStatusbarWidth(100, 5)

    app.clearStatusbar()
    app.clearStatusbar(None)
    app.clearStatusbar( 2)
    with pytest.raises(Exception) :
        app.clearStatusbar(5)

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_menus():
    print("\tTesting Menubar")

    app.addMenuList("a", LIST_ONE, tester_function)
    app.createMenu("MEN2")
    app.addMenuItem("MEN2", "MM2", tester_function, shortcut="Control-k", underline=2)
    app.addMenuSeparator("MEN2")
    app.addMenuCheckBox("MEN2", "CB2", tester_function, shortcut="Control-Shift-c", underline=2)
    app.addMenuRadioButton("MEN2", "a", "BB2", tester_function, shortcut="Control-2", underline=2)
    app.addMenuRadioButton("MEN2", "a", "BB3", tester_function)
    app.addSubMenu("MEN2", "sub1")
    app.addMenuItem("sub1", "MMM2", tester_function, shortcut="Alt-w", underline=2)
    app.addMenuSeparator("sub1")
    app.addMenuCheckBox("sub1", "CB23", tester_function, shortcut="Alt-Shift-x", underline=2)
    app.addMenuRadioButton("sub1", "b", "BB23", tester_function, shortcut="y", underline=2)
    app.addMenuRadioButton("sub1", "b", "BB33", tester_function, underline=0)
    app.addMenu("PRESS", tester_function, "P", 4)

    assert app.getMenuCheckBox("MEN2", "CB2") is False
    assert app.getMenuCheckBox("sub1", "CB23") is False

    assert app.getMenuRadioButton("MEN2", "a") == "BB2"
    assert app.getMenuRadioButton("sub1", "b") == "BB23"

    app.setMenuCheckBox("MEN2", "CB2")

    app.setMenuRadioButton("MEN2", "a", "BB3")

    assert app.getMenuCheckBox("MEN2", "CB2") is True
    assert app.getMenuCheckBox("sub1", "CB23") is False

    assert app.getMenuRadioButton("MEN2", "a") == "BB3"
    assert app.getMenuRadioButton("sub1", "b") == "BB23"

    app.setMenuRadioButton("sub1", "b", "BB33")

    assert app.getMenuRadioButton("MEN2", "a") == "BB3"
    assert app.getMenuRadioButton("sub1", "b") == "BB33"

    app.setMenuCheckBox("MEN2", "CB2", True)
    app.setMenuCheckBox("sub1", "CB23", True)

    assert app.getMenuCheckBox("MEN2", "CB2") is True
    assert app.getMenuCheckBox("sub1", "CB23") is True

    app.setMenuCheckBox("MEN2", "CB2", True)
    app.setMenuCheckBox("sub1", "CB23", False)

    assert app.getMenuCheckBox("MEN2", "CB2") is True
    assert app.getMenuCheckBox("sub1", "CB23") is False

    app.addMenuPreferences(tester_function)
    app.addMenuWindow()
    app.addMenuHelp(tester_function)

    app.addEntry("RCLICK2")
    app.addMenuEdit()
    app.setLogLevel('TRACE')

    app.enableMenubar()
    app.disableMenubar()
    app.enableMenubar()

    app.enableMenu("MEN2")
    app.disableMenu("MEN2")
    app.enableMenu("MEN2")

    app.enableMenuItem("MEN2", "MM2")
    app.disableMenuItem("MEN2", "MM2")
    app.enableMenuItem("MEN2", "MM2")

    app.enableMenuItem("MEN2", "will_fail")
    app.disableMenuItem("MEN2", "will_fail")
    app.renameMenuItem("MEN2", "will_fail", 'failed')

    print(" >> not implemented...")
    #print("\t >> all tests complete")

def dismissEditMenu():
    for i in range(5):
        print("dismissit...")
        app.widgetManager.get(WIDGET_NAMES.Menu, "EDIT").unpost()
        app.widgetManager.get(WIDGET_NAMES.Menu, "EDIT").invoke(i)
        time.sleep(.2)

def test_rightClick():
# called in a thread
# this causes testing to hang - the popup doesn't go....
    ent = app.addEntry("RCLICK")
    app.setEntryFocus("RCLICK")
    event = Event()
    event.widget = ent
    event.x_root = 100
    event.y_root = 100

    for type in [None, "9", "3", "4", "2"]:
        event.type = type
        app._rightClick(event)
        app.setEntry("RCLICK", "text")
        app._rightClick(event)

# this breaks - there is no widget in focus??
    for action in ["Cut", "Copy", "Paste", "Select All", "Clear Clipboard", "Clear All", "Undo", "Redo"]:
        print(action, action, action, action)
        app.setEntry("RCLICK", action)
        app.setEntryFocus("RCLICK")
        ent.focus_set()
        app._prepareCopyAndPaste(event, widget=ent)
        app._copyAndPasteHelper(action)


def test_toolbars():
    print("\tTesting Toolbar")

    app.addToolbar(["a", "b", "c", "ABOUT"], 
        [tester_function, tester_function, tester_function, tester_function],
        True)

    app.setToolbarBg('red')

    app.addToolbarButton("d", tester_function)
    with pytest.raises(Exception) :
        app.addToolbarButton("d", tester_function)

    app.removeToolbarButton("d")
    with pytest.raises(Exception) :
        app.removeToolbarButton("d")

    app.addToolbarButton("d", tester_function)
    app.removeToolbarButton("d", hide=False)

    app.removeToolbar()
    app.removeToolbar()

    app.addToolbar(["a", "b", "c", "ABOUT"], 
        [tester_function, tester_function, tester_function, tester_function],
        True)

    app.removeToolbar(hide=False)
    app.addToolbar(["a", "b", "c", "ABOUT"], 
        [tester_function, tester_function, tester_function, tester_function],
        True)

    app.setToolbarEnabled()
    app.setToolbarDisabled()
    app.setToolbarDisabled()
    app.setToolbarEnabled()

    app.setToolbarButtonEnabled("a")
    app.setToolbarButtonDisabled("a")
    app.setToolbarButtonEnabled("a")

    app.setToolbarPinned()
    app.setToolbarPinned(True)
    app.setToolbarPinned(False)

    app.showToolbar()
    app.hideToolbar()
    app.showToolbar()

    app.setToolbarImage("a", "1_entries.gif")
    app.setToolbarImage("b", "1_checks.png")

    app._minToolbar()
    app._minToolbar()
    app._maxToolbar()
    app._minToolbar()

    app._toggletb()
    app._toggletb()
    app._toggletb()

    app.setToolbarEnabled()
    app.setToolbarDisabled()
    app.setToolbarDisabled()
    app.setToolbarEnabled()

# doesn't work in python 2.7
    app.setToolbarIcon("a", "web")
    app.setToolbarIcon("b", "weight")
    app.setToolbarIcon("c", "wi-fi")

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_langs():
    app.enableDebug()
    print("\tTesting langs")
    # test exception handling
    app.changeLanguage("ENGLISH")
    app.setLanguage("GERMAN")
    # test real stuff
    app.setLanguage("FRENCH")
    app.translate("this")
    try:
        app.playSound("error1.wav")
    except:
        pass # only works on windows
    app.changeLanguage("ENGLISH")
    print(" >> not implemented...")
    #print("\t >> all tests complete")
    app.disableDebug()


def test_tooltips():
    print("\tTesting tooltip")
    app.addLabel("TestLabelTooltip")
    app.addEntry("EntryTooltip")
    app.addNumericEntry("NumericEntryTooltip")
    app.addSecretEntry("SecretEntryTooltip")

    app.setLabelTooltip("TestLabelTooltip", "message")
    app.setLabelTooltip("TestLabelTooltip", "")
    app.setLabelTooltip("TestLabelTooltip", "updated message")
    app.disableLabelTooltip("TestLabelTooltip")
    app.enableLabelTooltip("TestLabelTooltip")
    lab = app.getLabelWidget("TestLabelTooltip")
    tip = lab.tooltip
    tip.enter()
    tip.leave()
    tip.motion()

    app.setEntryTooltip("EntryTooltip", "tooltip text")
    app.setEntryTooltip("NumericEntryTooltip", "tooltip text")
    app.setEntryTooltip("SecretEntryTooltip", "tooltip text")

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_messages():
    print("\tTesting messages")
    app.warn("warn message")
    app.debug("debug message")

    app.warn("warn message")
    app.debug("debug message")

    app.warn("warn message")
    app.debug("debug message")
    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_sounds():
    print("\tTesting sounds")
# only support windows
    app.bell()
    try:
        app.soundError()
        app.soundWarning()
    except:
        print("Sound not supported on this platform")

    try:
        app.playSound("error1.wav")
        app.stopSound()
        app.soundLoop("error2.wav")
        app.stopSound()
    except:
        print("Sound not supported on this platform")

    with pytest.raises(Exception) :
        app.setSoundLocation("FRance")
    app.setSoundLocation("sounds")

    try:
        app.playSound("error3.wav")
        app.stopSound()
        app.soundLoop("error4.wav")
        app.stopSound()
    except:
        print("Sound not supported on this platform")

    try:
        app.playNote("b7", "BREVE")
    except:
        print("Sound not supported on this platform")
    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_hideShow():
    print("\tTesting hideshow")

    app.disableLabel("l0")
    app.enableLabel("l0")

    app.hideLabel("l0")
    app.hideLabel("l0")
    app.showLabel("l0")
    app.removeLabel("l0")

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_setters(widg_type, widg_id, widg_val=None):
    print("\tTesting setters")
    exec("app.set" + widg_type + "Bg(\""+widg_id +"\", \"red\")")
    exec("app.set" + widg_type + "Fg(\""+widg_id +"\", \"red\")")
    exec("app.set" + widg_type + "DisabledFg(\""+widg_id +"\", \"red\")")
    exec("app.set" + widg_type + "DisabledBg(\""+widg_id +"\", \"red\")")
    exec("app.set" + widg_type + "ActiveFg(\""+widg_id +"\", \"red\")")
    exec("app.set" + widg_type + "ActiveBg(\""+widg_id +"\", \"red\")")

# only applicable for tabbed panes
    exec("app.set" + widg_type + "InactiveFg(\""+widg_id +"\", \"red\")")
    exec("app.set" + widg_type + "InactiveBg(\""+widg_id +"\", \"red\")")

    exec("app.set" + widg_type + "Width(\""+widg_id +"\", 20)")
    exec("app.set" + widg_type + "Height(\""+widg_id +"\", 20)")

    exec("app.set" + widg_type + "Padding(\""+widg_id +"\", [20, 20])")
    exec("app.set" + widg_type + "IPadding(\""+widg_id +"\", [20, 20])")
    exec("app.set" + widg_type + "InPadding(\""+widg_id +"\", [20, 20])")
    exec("app.set" + widg_type + "Padding(\""+widg_id +"\", 20, 20)")
    exec("app.set" + widg_type + "IPadding(\""+widg_id +"\", 20, 20)")
    exec("app.set" + widg_type + "InPadding(\""+widg_id +"\", 20, 20)")

    exec("app.set" + widg_type + "Relief(\""+widg_id +"\", 'sunken')")
    exec("app.set" + widg_type + "Relief(\""+widg_id +"\", 'raised')")
    exec("app.set" + widg_type + "Relief(\""+widg_id +"\", 'groove')")
    exec("app.set" + widg_type + "Relief(\""+widg_id +"\", 'ridge')")
    exec("app.set" + widg_type + "Relief(\""+widg_id +"\", 'flat')")

    exec("app.set" + widg_type + "Align(\""+widg_id +"\", 'left')")
    exec("app.set" + widg_type + "Align(\""+widg_id +"\", 'center')")
    exec("app.set" + widg_type + "Align(\""+widg_id +"\", 'right')")

    exec("app.set" + widg_type + "Anchor(\""+widg_id +"\", 'n')")
    exec("app.set" + widg_type + "Anchor(\""+widg_id +"\", 'ne')")
    exec("app.set" + widg_type + "Anchor(\""+widg_id +"\", 'nw')")
    exec("app.set" + widg_type + "Anchor(\""+widg_id +"\", 'e')")
    exec("app.set" + widg_type + "Anchor(\""+widg_id +"\", 's')")
    exec("app.set" + widg_type + "Anchor(\""+widg_id +"\", 'se')")
    exec("app.set" + widg_type + "Anchor(\""+widg_id +"\", 'sw')")
    exec("app.set" + widg_type + "Anchor(\""+widg_id +"\", 'w')")
    exec("app.set" + widg_type + "Anchor(\""+widg_id +"\", 'center')")

    exec("app.set" + widg_type + "Cursor(\""+widg_id +"\", 'plus')")
    exec("app.set" + widg_type + "Focus(\""+widg_id +"\")")

    exec("app.set" + widg_type + "Sticky(\""+widg_id +"\", 'left')")
    exec("app.set" + widg_type + "Sticky(\""+widg_id +"\", 'right')")
    exec("app.set" + widg_type + "Sticky(\""+widg_id +"\", 'both')")
    exec("app.set" + widg_type + "Sticky(\""+widg_id +"\", 'n')")
    exec("app.set" + widg_type + "Sticky(\""+widg_id +"\", 'w')")

    exec("app.set" + widg_type + "DragFunction(\""+widg_id +"\", tester_function )")
    exec("app.set" + widg_type + "DragFunction(\""+widg_id +"\", [tester_function,tester_function] )")
    exec("app.set" + widg_type + "OverFunction(\""+widg_id +"\", tester_function)")
    exec("app.set" + widg_type + "OverFunction(\""+widg_id +"\", [tester_function, tester_function])")
    exec("app.set" + widg_type + "ChangeFunction(\""+widg_id +"\", tester_function)")
    exec("app.set" + widg_type + "SubmitFunction(\""+widg_id +"\", tester_function)")
    exec("app.set" + widg_type + "RightClick('" + widg_id + "', 'RCLICK')")

    if widg_val is not None:
        exec('app.get'+widg_type+'Widget("'+widg_id+'", "'+widg_val+'")')
    else:
        exec('app.get'+widg_type+'Widget("'+widg_id+'")')

    exec("app.hide" + widg_type+ "(\""+widg_id +"\")")
    exec("app.show" + widg_type+ "(\""+widg_id +"\")")
    exec("app.disable" + widg_type+ "(\""+widg_id +"\")")
    exec("app.enable" + widg_type+ "(\""+widg_id +"\")")
    exec("app.remove" + widg_type+ "(\""+widg_id +"\")")
    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_sets():
    print("\tTesting setters")
    app.setLabelBg("xx1", COL_ONE)
    app.setLabelFg("xx1", COL_TWO)
    app.setLabelDisabledFg("xx1", COL_THREE)
    app.setLabelWidth("xx1", 77)
    app.setLabelHeight("xx1", 33)
    app.setLabelRelief("xx1", "sunken")
    app.setLabelState("xx1", "disabled")

    lab = app.getLabelWidget("xx1")

    assert lab.cget("bg") == COL_ONE
    assert lab.cget("fg") == COL_TWO
    assert lab.cget("disabledforeground") == COL_THREE
    assert lab.cget("width") == 77
    assert lab.cget("height") == 33
    assert lab.cget("relief") == "sunken"
    assert lab.cget("state") == "disabled"
    print("\t >> all tests complete")

def test_containers():
    print("\tTesting containers")

    ## LABEL FRAMES
    lf = app.startLabelFrame("lf1")
    assert isinstance(lf , LabelFrame)
    app.setLabelFrameAnchor("lf1", "east")
    app.addLabel("lf1_l1", TEXT_ONE)
    app.stopLabelFrame()

    with pytest.raises(Exception) :
        app.stopLabelFrame()

    container = app.openLabelFrame("lf1")
    assert isinstance(container , LabelFrame)
    app.addLabel("lf1_l2", TEXT_ONE)
    app.stopLabelFrame()

    app.setLabelFrameTitle("lf1", "New title")
    assert lf.cget("text") == "New title"
    app.setLabelFrameAnchor("lf1", "ne")
    assert lf.cget("labelanchor") == "ne"

    with pytest.raises(Exception) :
        app.openLabelFrame("crash here")

    ## TOGGLE FRAMES

    tog = app.startToggleFrame("tf1")
    assert isinstance(tog , ToggleFrame)
    app.addLabel("tf1_l1", TEXT_ONE)
    app.stopToggleFrame()

    with pytest.raises(Exception) :
        app.stopToggleFrame()

    app.setToggleFrameText("tf1", "New text")
    assert tog.cget("text") == "New text"

    assert app.getToggleFrameState("tf1") is False

    app.toggleToggleFrame("tf1")
    assert app.getToggleFrameState("tf1") is True
    app.toggleToggleFrame("tf1")
    assert app.getToggleFrameState("tf1") is False

    container = app.openToggleFrame("tf1")
    assert container is not None
    app.addLabel("tf1_l2", TEXT_ONE)
    app.stopToggleFrame()

    app.disableToggleFrame("tf1")
    app.disableToggleFrame("tf1")
    app.enableToggleFrame("tf1")
    app.enableToggleFrame("tf1")
    app.disableToggleFrame("tf1")

    ## TABBED FRAMES

    tf = app.startTabbedFrame("tbf1")
    assert tf is not None
    tb = app.startTab("tab1", beforeTab='a', afterTab='a')
    assert tb is not None
    app.addLabel("tbf1_l1", TEXT_ONE)
    app.startTab("tab2", beforeTab="tab1")
    app.addLabel("tbf2_l1", TEXT_ONE)
    app.stopTab()
    app.startTab("tab3", afterTab="tab1")
    # empty tab
    app.stopTab()
    app.stopTabbedFrame()

    with pytest.raises(Exception) :
        app.startTab()

    with pytest.raises(Exception) :
        app.stopTab()

    with pytest.raises(Exception) :
        app.stopTabbedFrame()

    app.setTabText("tbf1", "tab2", "new text")
    app.setTabText("tbf1", "tab3")

    app.setTabBg("tbf1", "tab2", "red")


    assert app.getTabbedFrameSelectedTab("tbf1") == "tab1"

    app.setTabbedFrameSelectedTab("tbf1", "tab2")
    assert app.getTabbedFrameSelectedTab("tbf1") == "tab2"

    app.setTabbedFrameChangeFunction('tbf1', CHANGE_FUNCTION)

    app.setTabbedFrameSelectedTab("tbf1", "tab1")
    CHECK_CHANGE_FUNCTION(True)
    assert app.getTabbedFrameSelectedTab("tbf1") == "tab1"

    app.setTabbedFrameSelectedTab("tbf1", "tab2", callFunction=False)
    CHECK_CHANGE_FUNCTION(False)
    assert app.getTabbedFrameSelectedTab("tbf1") == "tab2"

    container = app.openTabbedFrame("tbf1")
    assert container is not None
    app.startTab("tab4")
    app.addLabel("tbf4_l1", TEXT_ONE)
    app.stopTabbedFrame()

    app.setTabbedFrameInactiveFg("tbf1", "red")
    app.setTabbedFrameInactiveBg("tbf1", "red")

    container = app.openTab("tbf1", "tab4")
    assert container is not None
    app.addLabel("tbf4_l2", TEXT_ONE)
    app.stopTab()

    with pytest.raises(Exception) :
        app.setTabbedFrameSelectedTab("tbf1", "tab3303")

    app.setTabbedFrameDisabledTab("tbf1", "tab3")
    assert app.setTabbedFrameSelectedTab("tbf1", "tab3") is None
    app.setTabbedFrameDisableAllTabs("tbf1")

    app.setTabbedFrameTabExpand("tbf1")

    def tabber(btn):
        print(btn)

    app.setTabbedFrameCommand("tbf1", tabber)
    app.setTabbedFrameDisableAllTabs("tbf1", False)
    app.setTabbedFrameSelectedTab("tbf1", "tab3")
    assert app.getTabbedFrameSelectedTab("tbf1") == "tab3"

    ## PANED FRAMES

    pf = app.startPanedFrame("p1")
    assert isinstance(pf, PanedWindow)
    app.addLabel("p1_l1", TEXT_ONE)
    pf = app.startPanedFrame("p2")
    assert isinstance(pf, PanedWindow)
    app.addLabel("p2_l1", TEXT_ONE)
    app.stopPanedFrame()
    app.setPaneSashPosition(0.3, 'p2')
    pf = app.startPanedFrameVertical("p3")
    assert isinstance(pf, PanedWindow)
    app.addLabel("p3_l1", TEXT_ONE)
    app.stopPanedFrame()
    app.setPaneSashPosition(88, 'p3')
    app.stopAllPanedFrames()

    container = app.openPanedFrame("p1")
    app.setPaneSashPosition(40)
    assert isinstance(container , PanedWindow)
    app.addLabel("p1_l11", TEXT_ONE)
    app.stopPanedFrame()

    ## PAGED WINDOWS

    pw = app.startPagedWindow("pg1")
    assert isinstance(pw, PagedWindow)
    pg = app.startPage()
    # should be a page...
    assert isinstance(pg, Frame)
    app.addLabel("pg1_l1", TEXT_ONE)
    app.startPage()
    app.addLabel("pg2_l1", TEXT_ONE)
    app.stopPage()
    app.startPage()
    app.addLabel("pg3_l1", TEXT_ONE)
    app.stopPage()
    app.stopPagedWindow()

    with pytest.raises(Exception) :
        app.startPage()

    with pytest.raises(Exception) :
        app.stopPage()

    with pytest.raises(Exception) :
        app.stopPagedWindow()

    app.startPagedWindow("ppp2")
    app.startPage()
    app.addLabel("ppp2_p1_l1")
    app.stopPagedWindow()

    assert app.getPagedWindowPageNumber("pg1") == 1
    app.setPagedWindowPage("pg1", 2)
    assert app.getPagedWindowPageNumber("pg1") == 2
    app.setPagedWindowPage("pg1", 3)
    assert app.getPagedWindowPageNumber("pg1") == 3
    try: app.setPagedWindowPage("pg1", 30)
    except: pass

    app.setPagedWindowTitle("pg1", TEXT_TWO)
    with pytest.raises(Exception) :
        app.setPagedWindowButtons("pg1", ["A"])
    app.setPagedWindowButtons("pg1", ["A", "B"])
    app.setPagedWindowButtonsTop("pg1")
    app.setPagedWindowButtonsTop("pg1", False)
    app.setPagedWindowFunction("pg1", tester_function)

    app.showPagedWindowPageNumber("pg1")
    app.showPagedWindowPageNumber("pg1", False)
    app.showPagedWindowPageNumber("pg1", True)

    app.showPagedWindowTitle("pg1")
    app.showPagedWindowTitle("pg1", False)
    app.showPagedWindowTitle("pg1", True)

    container = app.openPagedWindow("pg1")
    assert isinstance(container, PagedWindow)
    app.startPage()
    app.addLabel("pg4_l1", TEXT_ONE)
    app.stopPage()
    app.stopPagedWindow()

    container = app.openPage("pg1", 2)
    assert isinstance(container, Frame)
    app.addLabel("pg2_np", TEXT_ONE)
    app.stopPage()

    pw = app.getWidget(WIDGET_NAMES.PagedWindow, "pg1")
    assert isinstance(pw, PagedWindow)
    pw.showFirst()
    pw.showFirst()
    pw.showPrev()
    pw.showNext()
    pw.showLast()
    pw.showLast()
    pw.showNext()
    pw.showPrev()

    ## SUB WINDOWS

# breaks under python2.7
    sub = app.startSubWindow("sb1", modal=False, transient=False, blocking=False, grouped=False)
    assert isinstance(sub, SubWindow)
    app.addLabel("sb1_l", TEXT_ONE)
    test_gui_options()
    app.stopSubWindow()
    with pytest.raises(Exception) :
        app.stopSubWindow()

    container = app.openSubWindow("sb1")
    assert isinstance(container, SubWindow)
    app.addLabel("sb1_l2", TEXT_ONE)
    app.stopSubWindow()

    app.setSubWindowLocation("sb1", 50,50)

    app.showSubWindow("sb1")
    app.hideSubWindow("sb1")

    def stopper(btn=None):
        return True

# causes problems - children still in config dicitonaries...
# setLang, etc will try to modify them
    app.destroySubWindow("sb1")

# modal stops the popup from closing....
#    app.startSubWindow("sb2", modal=True, transient=True, blocking=False, grouped=True)
#    app.addLabel("sb2_l", TEXT_ONE)
#    app.setStopFunction(stopper)
#    app.stopSubWindow()
#
#    def stopSubWindow(btn=None):
#        app.hideSubWindow("sb2")
#
#    app.registerEvent(stopSubWindow)
#    app.showSubWindow("sb2")
#    app.hideSubWindow("sb2")

    ## FRAMES

    fr = app.startFrame("fr1")
    assert isinstance(fr, Frame)
    app.addLabel("fr1_l", TEXT_ONE)
    app.stopFrame()
    container = app.openFrame("fr1")
    assert isinstance(container, Frame)
    app.addLabel("fr1_l2", TEXT_ONE)
    app.stopFrame()

    with pytest.raises(Exception) :
        app.stopFrame()

    sp = app.startScrollPane("sp1")
    assert isinstance(sp, ScrollPane)
    app.addLabel("sp_l", TEXT_ONE)
    app.stopScrollPane()
    container = app.openScrollPane("sp1")
    assert isinstance(container, ScrollPane)
    app.addLabel("sp_l2", TEXT_ONE)
    app.stopScrollPane()
    with pytest.raises(Exception) :
        app.stopScrollPane()

    sp = app.getWidget(WIDGET_NAMES.ScrollPane, "sp1")
    assert isinstance(sp, ScrollPane)

    for hHidden in [True, False]:
        for vHidden in [True, False]:
            sp.hscrollbar.hidden = hHidden
            sp.vscrollbar.hidden = vHidden

            testScrollPaneScrolling(sp)


    # JUGGLING FRAMES
    with app.frame("a_frame", 1, 1) as fr:
        app.label("a_frame a")
    assert isinstance(fr, Frame)
    with app.frame("b_frame", 1, 1):
        app.label("b_frame a")
    with app.frame("c_frame", 1, 1):
        app.label("c_frame a")

    app.raiseFrame("a_frame")
    app.raiseFrame("b_frame")
    app.raiseFrame("c_frame")

    ## FRAME STACKS
    fStack = app.startFrameStack("stack")
    assert isinstance(fStack, FrameStack)
    fr = app.startFrame()
    assert isinstance(fr, Frame)
    app.addLabel("stack-1", "stack-1")
    app.stopFrame()
    app.startFrame()
    app.addLabel("stack-2", "stack-2")
    app.stopFrame()
    app.startFrame()
    app.addLabel("stack-3", "stack-3")
    app.stopFrame()
    app.stopFrameStack()

    assert app.countFrames("stack") == 3
    assert app.getCurrentFrame("stack") == 2
    assert app.getPreviousFrame("stack") == 1

    app.firstFrame("stack")
    assert app.getCurrentFrame("stack") == 0
    assert app.frameStackAtStart("stack")
    assert not app.frameStackAtEnd("stack")
    assert app.getPreviousFrame("stack") == 2

    app.lastFrame("stack")
    assert app.getCurrentFrame("stack") == 2
    assert not app.frameStackAtStart("stack")
    assert app.frameStackAtEnd("stack")
    assert app.getPreviousFrame("stack") == 0

    app.prevFrame("stack")
    assert app.getCurrentFrame("stack") == 1
    assert app.getPreviousFrame("stack") == 2

    app.prevFrame("stack")
    assert app.getCurrentFrame("stack") == 0
    assert app.getPreviousFrame("stack") == 1

    app.prevFrame("stack")
    assert app.getCurrentFrame("stack") == 0
    assert app.getPreviousFrame("stack") == 1

    app.nextFrame("stack")
    assert app.getCurrentFrame("stack") == 1
    assert app.getPreviousFrame("stack") == 0

    app.nextFrame("stack")
    assert app.getCurrentFrame("stack") == 2
    assert app.getPreviousFrame("stack") == 1

    app.nextFrame("stack")
    assert app.getCurrentFrame("stack") == 2
    assert app.getPreviousFrame("stack") == 1

    fStack.setChangeFunction(CHANGE_FUNCTION)
    app.selectFrame("stack", 1)
    CHECK_CHANGE_FUNCTION(True)
    assert app.getCurrentFrame("stack") == 1
    assert app.getPreviousFrame("stack") == 2

    app.selectFrame("stack", 2, callFunction=False)
    CHECK_CHANGE_FUNCTION(False)
    assert app.getCurrentFrame("stack") == 2
    assert app.getPreviousFrame("stack") == 1

    app.prevFrame("stack")
    CHECK_CHANGE_FUNCTION(True)
    app.nextFrame("stack")
    CHECK_CHANGE_FUNCTION(True)

    app.prevFrame("stack", callFunction=False)
    CHECK_CHANGE_FUNCTION(False)
    app.nextFrame("stack", callFunction=False)
    CHECK_CHANGE_FUNCTION(False)

    app.firstFrame("stack", callFunction=True)
    CHECK_CHANGE_FUNCTION(True)
    app.lastFrame("stack", callFunction=True)
    CHECK_CHANGE_FUNCTION(True)

    app.firstFrame("stack", callFunction=False)
    CHECK_CHANGE_FUNCTION(False)
    app.lastFrame("stack", callFunction=False)
    CHECK_CHANGE_FUNCTION(False)

    app.selectFrame("stack", 2, callFunction=False)
    app.selectFrame("stack", 1, callFunction=False)

    with pytest.raises(Exception) :
        app.selectFrame("stack", 3)
    assert app.getCurrentFrame("stack") == 1
    assert app.getPreviousFrame("stack") == 2

    container = app.openFrameStack('stack')
    assert container is not None
    app.startFrame()
    app.addLabel("stack-4", "stack-4")
    app.stopFrame()
    app.stopFrameStack()

    assert app.countFrames("stack") == 4
    assert app.getCurrentFrame("stack") == 3
    assert app.getPreviousFrame("stack") == 1

    app.selectFrame("stack", 0)
    assert app.getCurrentFrame("stack") == 0
    assert app.getPreviousFrame("stack") == 3

    app.selectFrame("stack", 3)
    assert app.getCurrentFrame("stack") == 3
    assert app.getPreviousFrame("stack") == 0

    app.prevFrame("stack")
    assert app.getCurrentFrame("stack") == 2
    assert app.getPreviousFrame("stack") == 3

    app.prevFrame("stack")
    assert app.getCurrentFrame("stack") == 1
    assert app.getPreviousFrame("stack") == 2

    app.prevFrame("stack")
    assert app.getCurrentFrame("stack") == 0
    assert app.getPreviousFrame("stack") == 1

    app.prevFrame("stack")
    assert app.getCurrentFrame("stack") == 0
    assert app.getPreviousFrame("stack") == 1

    def changer(): print("changed")
    def noChange(): return False

    app.startFrameStack("sstack", start=1, change=changer)
    app.startFrame()
    app.addLabel("sstack-1", "stack-1")
    app.stopFrame()
    app.startFrame()
    app.addLabel("sstack-2", "stack-2")
    app.stopFrame()
    app.startFrame()
    app.addLabel("sstack-3", "stack-3")
    app.stopFrame()
    app.stopFrameStack()

    assert app.countFrames("sstack") == 3
    assert app.getCurrentFrame("sstack") == 1
    assert app.getPreviousFrame("sstack") == 2

    app.selectFrame("sstack", 2)
    assert app.getCurrentFrame("sstack") == 2
    assert app.getPreviousFrame("sstack") == 1

    app.selectFrame("sstack", 0, callFunction = False)
    assert app.getCurrentFrame("sstack") == 0
    assert app.getPreviousFrame("sstack") == 2

    app.setFrameStackChangeFunction('sstack', noChange)

    app.selectFrame("sstack", 2)
    assert app.getCurrentFrame("sstack") == 0
    assert app.getPreviousFrame("sstack") == 2

    app.selectFrame("sstack", 2, callFunction = False)
    assert app.getCurrentFrame("sstack") == 2
    assert app.getPreviousFrame("sstack") == 0

    print("Making final stack - start with 1")
    app.startFrameStack("fstack")
    app.setStartFrame("fstack", 1)
    app.startFrame()
    app.addLabel("fstack-1", "stack-1")
    app.stopFrame()
    app.startFrame()
    app.addLabel("fstack-2", "stack-2")
    app.stopFrame()
    app.startFrame()
    app.addLabel("fstack-3", "stack-3")
    app.stopFrame()
    app.stopFrameStack()
    print( "DONE - Curr:", app.getCurrentFrame("fstack"), "Prev", app.getPreviousFrame("fstack") )

    assert app.countFrames("fstack") == 3
    assert app.getCurrentFrame("fstack") == 1
    assert app.getPreviousFrame("fstack") == 2

def testScrollPaneScrolling(sp):
    event = Event()

    sp._mouseEnter(event)
    sp._mouseLeave(event)

    for num in [4, 5]:
        event.num = num
        sp._horizMouseScroll(event)
        sp._vertMouseScroll(event)

    event.num = 0
    for delta in [300, 30, -300, -30]:
        event.delta = delta
        sp._horizMouseScroll(event)
        sp._vertMouseScroll(event)

    # shift=0x0001, ctrl=0x0004, alt=0x0008
    states = [0, 0x0004, 0x0001, 0x0008, 0x0080]

    event.type = "2"    # always 2
    for state in states:
        event.state = state
        for key in ["Up", "Down", "Left", "Right", "Prior", "Next", "Home", "End"]:
            event.keysym = key
            sp._keyPressed(event)

    event = Event()
    sp._mouseEnter(event)

    for num in [4, 5]:
        event.num = num
        sp._horizMouseScroll(event)
        sp._vertMouseScroll(event)

    event.num = 0
    for delta in [300, 30, -300, -30]:
        event.delta = delta
        sp._horizMouseScroll(event)
        sp._vertMouseScroll(event)

    event.type = "2"    # always 2
    for state in states:
        event.state = state
        for key in ["Up", "Down", "Left", "Right", "Prior", "Next", "Home", "End"]:
            event.keysym = key
            sp._keyPressed(event)

    event = Event()
    sp._mouseLeave(event)

    sp.scrollLeft()
    sp.scrollRight()
    sp.scrollTop()
    sp.scrollBottom()

    event = Event()
    sp._mouseEnter(event)
    sp.scrollLeft()
    sp.scrollRight()
    sp.scrollTop()
    sp.scrollBottom()
    event = Event()
    sp._mouseLeave(event)

    print(" >> not implemented...")
    #print("\t >> all tests complete")

def closePop():
    POP_UP = app.getPopUp()
    print("closing:", app.getPopUp())
    if POP_UP is not None: POP_UP.cancel()

def test_plots():
    print("\tTesting plots:", PY_VER)
    if PY_VER == "3.3":
        print("cancelling - plots not supported")
    else:
        x = [1,2,3,4,5]
        y = [2,4,6,8,10]
        axes = app.addPlot("p1", x, y, showNav=True)
        axes.legend(["key data"])
        axes.set_xlabel("X lab")
        axes.set_ylabel("Y lab")
        axes.set_title("title")
        app.refreshPlot("p1")
        app.updatePlot("p1", x, y)
        app.updatePlot("p1", x, y, keepLabels=True)

        app.plot('p2', x, y, width=100, height=200, nav=True)
        print(type(app.plot('p2')))
        assert isinstance(app.addPlot("p2"), turtle.RawTurtle)

        print(" >> not implemented...")
        #print("\t >> all tests complete")

def test_googlemap():
    print("\tTesting GoogleMaps:", PY_VER)
    gm2 = app.addGoogleMap("gm2")
    with pytest.raises(Exception) :
        app.addGoogleMap("gm2")
    app.setGoogleMapLocation("gm2", "spain")
    app.searchGoogleMap("gm2", "germany")
    app.setGoogleMapTerrain("gm2", "Satellite")
    app.setGoogleMapSize("gm2", "350x450")
    app.setGoogleMapZoom("gm2", 15)
    assert app.getGoogleMapZoom("gm2") == 15
    app.zoomGoogleMap("gm2", 5)
    app.zoomGoogleMap("gm2", "+")
    app.zoomGoogleMap("gm2", "-")

    assert app.getGoogleMapZoom("gm2") == 5
    assert app.getGoogleMapTerrain("gm2") == "Satellite"
    assert app.getGoogleMapLocation("gm2") == "germany"
    assert app.getGoogleMapSize("gm2") == "350x450"

    app.setGoogleMapMarker("gm2", "france")
    app.setGoogleMapMarker("gm2", "paris", label="A")
    app.removeGoogleMapMarker("gm2", label="A")
    app.setGoogleMapMarker("gm2", "leon")

    app.setGoogleMapMarker("gm2", "")
    app.saveGoogleMap("gm2", "gm.gif")
    gm2.getMapFile("image.map")

    print(" >> not implemented...")
    #print("\t >> all tests complete")

def test_turtle():
    print("\tTesting turtles:", PY_VER)
    assert isinstance(app.addTurtle("t1"), turtle.RawTurtle)
    t = app.getTurtle("t1")
    t.fd(100)
    s = app.getTurtleScreen("t1")
    assert isinstance(s, turtle.TurtleScreen)
    s.bgcolor("orange")
    test_setters("Turtle", "t1")

    print(" >> not implemented...")
    #print("\t >> all tests complete")

def test_canvas():
    print("\tTesting canvas:", PY_VER)
    assert isinstance(app.addCanvas("c1"), Canvas)
    c = app.getCanvas("c1")
    c.create_line(0, 0, 255, 244, width=5)

    app.addCanvasCircle("c1", 10, 10, 10)
    app.addCanvasOval("c1", 10, 10, 10, 10)
    app.addCanvasRectangle("c1", 10, 10, 10, 10)
    app.addCanvasLine("c1", 10, 10, 10, 10)
    app.addCanvasText("c1", 10, 10, "test text")
    app.addCanvasImage("c1", 10, 10, "1_checks.png")
    app.clearCanvas("c1")

    coords = {
        "America":[32, 17, 242, 167],
        "South America":[126, 170, 226, 292],
    }

    def click(area):
        print(area)

    app.setCanvasMap("c1", click, coords)
    event = Event()
    event.widget = c
    event.x = 100
    event.y = 100
    app._imageMap("c1", event)

    test_setters("Canvas", "c1")

    print(" >> not implemented...")
    #print("\t >> all tests complete")

def test_microbits():
    print("\tTesting plots:", PY_VER)
    app.addMicroBit("mb1")
    with pytest.raises(Exception) :
        app.addMicroBit("mb1")
    app.clearMicroBit("mb1")
    app.setMicroBitImage("mb1", "09090:90909:90009:09090:00900")
    app.clearMicroBit("mb1")
    app.setMicroBitPixel("mb1", 2, 2, 5)
    app.clearMicroBit("mb1")

    test_setters("MicroBit", "mb1")

    print(" >> not implemented...")
    #print("\t >> all tests complete")

def test_padding():
    print("\tTesting padding:", PY_VER)
    app.setIPadX()
    app.setIPadY()
    app.setIPadding(5, 5)

    app.setInPadX()
    app.setInPadY()

#    app.setIcon("images/favicon.ico")

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_pop_ups():
    print("\tTesting popups")
    print("Registering event:")
    app.topLevel.after(500, closePop)
    a = app.textBox("POP_TEXT", "a", "initial")
    assert a is None
    print("Registering event:")
    app.topLevel.after(500, closePop)
    a = app.numberBox("POP_NUM", "a")
    assert a is None

    print(" >> not implemented...")
    #print("\t >> all tests complete")

def test_logging():
    print("\tTesting logging")

    app.setLogLevel("DEBUG")
    app.logMessage("test logging", "CRITICAL")
    app.logMessage("test logging", "ERROR")
    app.logMessage("test logging", "WARNING")
    app.logMessage("test logging", "INFO")
    app.logMessage("test logging", "DEBUG")
    app.logMessage("test logging", "BROKEN")

    app.critical("test logging")
    app.error("test logging")
    app.warn("test logging")
    app.debug("test logging")
    app.info("test logging")
    app.exception(Exception("aaa"))

    import logging
    logger = logging.getLogger("appJar")
    logger.error("WITH LOGGING")

    app.setLogFile("msg.log")
    app.debug("in the log")
    app.error("in the log")

    print(" >> not implemented...")
    #print("\t >> all tests complete")

def test_gui_properties():

    def propFunc(param=None): return True

    app.config(
        title='aaa',
#        icon='images/favicon.ico',
        transparency=49,
        visible=False,
        padding=(1,2),
        inPadding=(3,4),
        guiPadding=(5,6),
        size=(377,377),
        location=(50,50),
        resizable=True,
        sticky='new',
        stretch='column',
        expand='column',
        row=5,
        fg='red',
        bg='green',
        font={'size':20, 'family':'helvetica'},
        buttonFont={'size':19, 'family':'helvetica'},
        labelFont={'size':18, 'family':'helvetica'},
        statusFont={'size':15, 'family':'helvetica'},
        editMenu=True,
        stopFunction=propFunc,
        startFunction=propFunc,
        fastStop=False,
        enterKey=propFunc,
        logLevel='trace',
        logFile='aaa.txt',
        language='french',
        rowspan=1,
        colspan=1,
    )

    assert app.title == 'aaa'
##    assert app.icon == 'images/favicon.ico'

# not on linux
#    assert app.transparency == 49
    assert app.visible is False
    assert app.padding == (1,2)
    assert app.inPadding == (3,4)
    assert app.guiPadding == (5,6)
    assert app.location == (50,50)

    assert app.size == (377,377)
    app.configure(fullscreen=True)
    assert app.fullscreen is True
# breaks on linux
#    assert app.size != (377,377)
    app.configure(fullscreen=False)

    assert app.resizable is True
    assert app.sticky.lower() == 'new'
    assert app.stretch.lower() == 'column'
    assert app.expand.lower() == 'column'
    assert app.row == 5
    assert app.rowspan == 1
    assert app.colspan == 1
    assert app.fg == 'red'
    assert app.bg == 'green'
    assert app.font['size'] == 18
    assert app.buttonFont['size'] == 19
    assert app.labelFont['size'] == 18
    assert app.statusFont['size'] == 15
    assert app.editMenu is True
#    assert app.stopFunction == propFunc
#    assert app.enterKey == propFunc
    assert app.logLevel.lower() == 'trace'
    assert app.logFile.endswith('aaa.txt')
    assert app.language == 'french'

    app.title = "aaa"
    assert app.title == "aaa"
#    app.icon = "images/favicon.ico"
#    assert app.icon == "images/favicon.ico"

    # not on linux
    app.transparency = 70
#    assert app.transparency == 70

    app.visible = True
    assert app.visible is True
    app.visible = False
    assert app.visible is False
    app.visible = True
    assert app.visible is True

    # fails under Travis
    app.top
    app.top = True
#    assert app.top is True
    app.top = False
#    assert app.top is False

    app.padding = (20,21)
    assert app.padding == (20,21)
    app.padding = 5
    assert app.padding == (5,5)
    app.inPadding = (22,23)
    assert app.inPadding == (22,23)
    app.inPadding = 7
    assert app.inPadding == (7,7)
    app.guiPadding = (24,25)
    assert app.guiPadding == (24,25)
    app.guiPadding = 3
    assert app.guiPadding == (3,3)

    app.location = (300,300)
    assert app.location == (300,300)
    app.location = "CENTER"
    assert app.location != (300,300)

    app.fullscreen = True
    assert app.fullscreen is True
    app.fullscreen = False
    assert app.fullscreen is False
    app.fullscreen = True
    assert app.fullscreen is True

    app.resizable = True
    assert app.resizable is True
    app.resizable = False
    assert app.resizable is False
    app.resizable = True
    assert app.resizable is True

#    app.size = (777,777)
#    print(app.size)
#    assert app.size == (777,777)

    app.sticky = "new"
    assert app.sticky == "new"
    app.sticky = "n"
    assert app.sticky == "n"
    app.sticky = "news"
    assert app.sticky == "news"

    app.stretch = "row"
    assert app.stretch.lower() == "row"
    app.stretch = "column"
    assert app.stretch.lower() == "column"
    app.stretch = "both"
    assert app.stretch.lower() == "all"

    app.row = 5
    assert app.row == 5

    app.rowspan = 5
    assert app.rowspan == 5
    app.colspan = 4
    assert app.colspan == 4

    app.rowspan = 0
    assert app.rowspan == 0
    app.colspan = 0
    assert app.colspan == 0

    app.fg = "blue"
    assert app.fg == "blue"
    app.bg = "red"
    assert app.bg == "red"

    myFont = str(app.fonts[11])
    myFont1 = str(app.fonts[12])
    myFont2 = str(app.fonts[13])
    print(myFont, myFont1, myFont2)

    app.font = 30
    assert app.font['size'] == 30

    app.font = {'size':25, 'family':myFont}
    assert app.font['size'] == 25
    assert app.font['family'] == myFont

    app.buttonFont = 24
    assert app.buttonFont['size'] == 24

    app.statusFont = 17
    assert app.statusFont['size'] == 17

    app.buttonFont = {'size':23, 'family':myFont1}
    assert app.buttonFont['size'] == 23
    assert app.buttonFont['family'] == myFont1

    app.labelFont = 22
    assert app.labelFont['size'] == 22

    app.labelFont = {'size':21, 'family':myFont2}
    assert app.labelFont['size'] == 21
    assert app.labelFont['family'] == myFont2

    app.editMenu = False
    assert app.editMenu is False
    app.editMenu = True
    assert app.editMenu is True
    app.editMenu = False
    assert app.editMenu is False

    app.stopFunction = propFunc
    app.startFunction = propFunc
    app.stopFunction = False
    app.fastStop = True
    assert app.fastStop is True
    app.fastStop = False
    assert app.fastStop is False
    app.enterKey = propFunc
    app.enterKey = None

    app.logLevel = "error"
    assert app.logLevel.lower() == "error"
    app.logLevel = "warn"
    assert app.logLevel.lower() == "warning"
    app.logLevel = "debug"
    assert app.logLevel.lower() == "debug"
    app.logLevel = "trace"
    assert app.logLevel.lower() == "trace"

    app.logFile = "logger.txt"
    assert app.logFile.endswith("logger.txt")
    app.language = "french"
    assert app.language == "french"

def dragFunc(val=None):
    pass

def dropFunc(val=None):
    pass

def test_dnd():
    dw = DraggableWidget(app.topLevel.canvasPane, "a", "b", [10,10])
    app.addLabel("ddd", "DND TESTER")
    tb = app.addTrashBin("tb")
    tb.config(fg="red")
    tb.dnd_commit(dw, None)

    # internal drag & drop
    app.registerLabelDroppable("ddd", dropFunc)
    app.registerLabelDraggable("ddd", dragFunc)

    # external drag & drop
    app.setLabelDropTarget("ddd", dropFunc)
    app.setLabelDragSource("ddd", dragFunc)

def test_focus():
    print("testing focus\n")

    app.addEntry("entFocus")
    app.setEntryFocus("entFocus")
    try: assert app.getFocus() == "entFocus"
    except: pass

    app.addLabel("labFocus", "text")
    app.setLabelFocus("labFocus")
    with pytest.raises(Exception) :
        assert app.getFocus() == "labFocus"

    print(" >> not implemented...")
    #print("\t >> all tests complete")


app = gui()
#with pytest.raises(Exception) :
#    app3 = gui()
app.createRightClickMenu("RCLICK")
app.setFastStop()
print(app.SHOW_VERSION())
print(app.SHOW_PATHS())
app.showSplash()
print("NEXT...")

print("<<<Starting Widget Test Suite>>>")
test_remover()
test_remover()
test_gui_options()
test_widget_arranging()
test_grid_layout()
test_labels()
test_entries()
test_buttons()
test_radios()
test_checks()
test_options()
test_spins()
test_lists()
test_scales()
test_widget_arranging()
test_padding()
test_message_boxes()
test_text_areas()
test_meters()
test_properties()
test_gui_properties()
test_separators()
test_links()
test_grips()
test_date_pickers()
try: test_plots()
except: print("Skipping plot tests - MatPlotLib not available")
test_microbits()
test_turtle()
test_canvas()
if PY_VER != "3.3":
    test_googlemap()

test_logging()

test_status()
test_menus()
test_toolbars()

test_auto_labels()

test_pies()
test_trees()
test_grids()
test_tables()

test_images()
test_sounds()
test_tooltips()
test_langs()

test_containers()
test_messages()
test_dnd()

data = app.getAllInputs(extra='something', extra2=True, extra3=4)
assert data['extra'] == 'something'
assert data['ae1'] == TEXT_ONE
assert data['rb'] == TEXT_ONE
assert data["ae1"] == TEXT_ONE

app.showAccess()
app.hideSubWindow('access_access_subwindow')

test_sets()
test_gui_options()
test_events()
test_widget_arranging()

test_hideShow()

def cbA(data):
    print("Doing callback with", data)
    time.sleep(1)
    return True

def cbB(success):
    print("Callback finished with:", success)

doStop = 0
def test_gui(btn=None):
    print("Testing GUI")
    global doStop
    if doStop == 0:
        test_pop_ups()
        app.thread(run_events, "a", bbb="bbb")
        app.setEntryFocus("ffe1")
        app.threadCallback(cbA, cbB, "text")
        app.callback(cbA, cbB, "text2")
        app.thread(dismissEditMenu)
        app.thread(test_rightClick)
        doStop += 1
    elif doStop == 1:
        doStop += 1
    elif doStop == 2:
        test_focus()
        test_sets()
        test_langs()
        test_widget_arranging()
        test_gui_options()
        doStop += 1
    elif doStop == 3:
        app.removeAllWidgets()
        doStop += 1
    elif doStop < 5:
        doStop += 1
        print("Waiting", doStop)
    else:
        print("HERE WE GO: Stopping app")
        app.stop()

app.registerEvent(test_gui)
app.setPollTime(1000)
app.addLabel("test_threads", "empty")
assert app.getLabel("test_threads") == "empty"
app.queueFunction(app.setLabel, "test_threads", "full")
app.saveSettings()
app.go("CANADIAN")

print("<<<Widget Test Suite Complete on app>>>")
del app

print("<<<Starting app3>>>")
with gui(debug=True) as app3:
    app3.toolbar(["a", "b", "file", "open"], tester_function, icons=['a', 'b', 'file', 'open'], status=[1, 0, False, True], bg='pink')
    app3.addStatusbar(TEXT_ONE, 1, "LEFT")
    with app3.tabbedFrame("tf"):
        with app3.tab("t1"):
            with app3.labelFrame("lf1"):
                app3.addLabel("l1", "label")
            with app3.toggleFrame("tf1"):
                app3.addCheckBox("cb1")
        with app3.tab("t2", afterTab='t1'):
            with app3.panedFrame("pf1", sash=50):
                with app3.panedFrame("vpf1", vertical=True):
                    app3.addLabel("l2", "label")
        with app3.tab("t3", beforeTab='t2'):
            with app3.pagedWindow("pages"):
                with app3.page():
                    app3.addLabel("l3", "label")
                with app3.page():
                    app3.addLabel("l4", "label")
        with app3.tab("t4", afterTab='a', beforeTab='a'):
            with app3.frame("f1"):
                app3.addLabel("l5", "label")
            with app3.scrollPane("sf1"):
                app3.addLabel("l6", "label")

        with app3.tab("t5"):
            with app3.frameStack("stacks", start=2, change=cbB):
                with app3.frame():
                    app3.label("stacks-1")
                with app3.frame():
                    app3.label("stacks-2")
                with app3.frame():
                    app3.label("stacks-3")

    with app3.subWindow("s1"):
        app3.addLabel("l7", "label")

    app3.after(2000, app3.stop)

print("<<<Widget Test Suite Complete on app3 >>>")

print("<<<Starting app4>>>")

def press(btn):
    print(
        app4.label("title"),
        app4.label("title2"),
        app4.meter("Cry"),
        app4.entry("data"),
        app4.date("date"),
        app4.button("Clap"),
        app4.radio("happy"),
        app4.check("Clap"),
        app4.tick("tClap"),
        app4.option("feelings"),
        app4.spin("feelings"),
        app4.listbox("feelings"),
        app4.scale("happiness"),
        app4.message("mess"),
        app4.text("mess2"),
        app4.meter("Cry"),
        app4.link("Cry"),
        app4.link("Shout"),
        app4.image("img"),
        app4.image("img2"),
        app4.properties("Toppings"),
    )

    app4.label("title2", "not empty")
    app4.meter("Cry", app4.scale("happiness"), text="fred")
    app4.meter("CryingMore", app4.slider("happiness again"))
    app4.meter("CryingMorer", app4.scale("happiness again"), text="alphabet")
    app4.meter("CryingMorerr", (app4.slider("happiness again"),app4.scale("happiness again")))

def updateApp4(btn=None):
    app4.label("title", "aaa")
    app4.label("title2", "aaa")
    app4.meter("Cry", 50)
    app4.entry("data", "aaa")
#    app4.date("date")
    app4.button("Clap", test_gui4)
    app4.radio("happy", "Miserable")
    app4.check("Clap", True)
    app4.tick("tClap", True)
    app4.option("feelings", 1)
    app4.spin("feelings", 2)
    app4.listbox("feelings", 3)
    app4.scale("happiness", 50)
    app4.message("mess", "aaa")
    app4.text("mess2", "aaa")
    app4.text("mess2", "aaa", replace=False)
    app4.text("mess2", "aaa", replace=True)
    app4.meter("Cry", 50)
    app4.link("Cry", "http://www.google.com")
    app4.link("Shout", updateApp4)
    app4.image("img", "1_flash.gif")
#    app4.image("img2")
    app4.properties("Toppings", {"a":False, "b": True}, boxbg='green')

doStopAgain = 0
def test_gui4(btn=None):
    print("Testing GUI4")
    global doStopAgain
    if doStopAgain == 2:
        press(None)
    elif doStopAgain == 3:
        updateApp4(None)
    elif doStopAgain == 5:
        print("Show app4")
        app4.show()
    elif doStopAgain == 6:
        print("Hide app4")
        app4.hide()
    elif doStopAgain == 8:
        print("Stopping app4")
        app4.stop()
    doStopAgain += 1

def changer(btn=None):
    print(btn)

with gui("Simple Demo", transparency=50, padding=5, location="CENTER", bg="red") as app4:
    app4.toolbar(["a", "b", "file", "open"], changer, findIcon=True, pinned=False, hidden=False, disabled=True)

    app4.status(header="header", fields=3, side="RIGHT", bg='red', fg='green', width=40)
    app4.statusbar(text="a", field=1)
    app4.statusbar("a", field=2)
    app4.statusbar("a", 0)

    app4.EXTERNAL_DND = None
    app4.label("title", "Simple Props Demo", colspan=3, kind="flash")
    app4.label("title2", row=0, column=3)
    app4.setLabelBg("title", "green")

    app4.radio("happy", "Very Happy", row=1, column=0)
    app4.radio("happy", "Ambivalent", row=1, column=1, change=changer, kind='square')
    app4.radio("happy", "Miserable", row=1, column=2, selected=True)

    app4.message("mess", "Simple Sadness", row=2, rowspan=3)
    app4.setMessageBg("mess", "pink")

    app4.text("mess2", "Simple Happiness", row=2, column=2, rowspan=3, scroll=False)
    app4.text("mess3", "Simple Happiness", row=2, column=2, rowspan=3, scroll=True, change=changer)
    app4.setTextAreaBg("mess2", "pink")

    app4.image("img", "1_entries.gif", over="1_flash.gif", row=2, column=3, rowspan=7)
    app4.image("img5", "1_entries.gif", over="1_flash.gif", submit=changer, row=2, column=3, rowspan=7)
    app4.image("img2", "1_entries.gif", over="1_flash.gif", row=2, column=3, rowspan=7, map={"A":[1,1,5,5]}, submit=changer)
    app4.image("img3", "1_entries.gif", over="1_flash.gif", row=2, submit=changer, column=3, rowspan=7)
    app4.image("img4", "1_entries.gif", over="1_flash.gif", row=2, column=3, rowspan=7, compound="top")
    app4.image("img2", "OPEN", row=2, column=4, rowspan=3, kind="icon")

    app4.canvas("cnv1", row=2, column=3, rowspan=7, map={"A":[1,1,5,5]}, submit=changer)

    app4.check("Clap", row=2, column=1)
    app4.check("Cheer", True, row=3, column=1)
    app4.check("Cry", row=4, column=1, change=changer, text='something else')

    app4.tick("tClap", row=2, column=1)
    app4.tick("tCheer", True, row=3, column=1)
    app4.tick("tCry", row=4, column=1, change=changer)

    app4.entry("data", colspan=3, kind="directory")
    app4.entry("data2", value="lots of data", colspan=3, focus=True, case="upper", limit=15)
    app4.entry("data3", colspan=3, default="france", kind="validation", labBg='orange')
    app4.entry("data4", value=["a", "aa", "aba", "abc", "abd"], colspan=3, kind="auto", rows=4)

    app4.entry("se1", row=0, column=1, default="standard", submit=changer, change=changer, limit=5, case="lower", rows=3)
    app4.entry("sv1", row=1, column=1, kind="validation", default="validation", submit=changer, change=changer, limit=5, case="upper", rows=3)
    app4.entry("sf1", row=2, column=1, kind="file", default="file", text='press', submit=changer, change=changer, limit=5, case="upper", rows=3)
    app4.entry("sd1", row=3, column=1, kind="directory", default="directory", text='press', submit=changer, change=changer, limit=5, case="upper", rows=3)
    app4.entry("so1", row=3, column=1, kind="open", default="open", text='press', submit=changer, change=changer, limit=5, case="upper", rows=3)
    app4.entry("ss1", row=3, column=1, kind="save", default="save", text='press', submit=changer, change=changer, limit=5, case="upper", rows=3)

    app4.entry("sn1", row=4, column=1, kind="numeric", default="numeric", submit=changer, change=changer, limit=5, case="upper", rows=3)
    app4.entry("sa1", ["a", "b", "bb", "bbb"], row=5, column=1, kind="auto", default="auto", submit=changer, change=changer, limit=5, case="upper", rows=3)
    app4.entry("ss1", row=6, column=1, secret=True, default="secret", submit=changer, change=changer, limit=5, case="upper", rows=3)

    app4.entry("lse1", row=7, column=1,label=True)
    #app4.entry("lsv1", row=8, column=1, kind="validation",label=True)
    app4.entry("lsf1", row=8, column=1, kind="file",label=True)
    app4.entry("lsd1", row=9, column=1, kind="directory",label=True)
    app4.entry("lsn1", row=10, column=1, kind="numeric",label=True)
    app4.entry("lsa1", ["a", "b", "bb", "bbb"], row=11, column=1, kind="auto",label=True)
    app4.entry("lss1", row=12, column=1, secret=True,label=True)


    row=app4.gr()

    app4.button("Clap", press, icon="OPEN", row=row, column=0)
    app4.button("Cheer", press, row=row, column=1)
    app4.button("Cheer", "")
    app4.button("Cheery", press, image="1_entries.gif")
    app4.button("Cry", press, row=row, column=2)

    app4.date("date", row=row, column=3, rowspan=4, change=changer)

    app4.scale("happiness", colspan=3, increment=1, show=True, change=press)


    row=app4.gr()
    app4.option("feelings", ["happy", "bored", "angry"], column=0, row=row, change=press, disabled="$")
    app4.option("feelings2", ["happy", "bored", "angry"], kind="ticks", column=0, row=row, change=press)
    app4.option("feelings3", ["happy", "bored", "angry"], column=0, row=row, change=press)
    app4.spin("feelings", ["happy", "bored", "angry"], change=changer, column=1, row=row, item="angry")
    app4.listbox("feelings", ["happy", "bored", "angry"], column=2, row=row, rows=4, multi=True, group=True, change=press)

    app4.separator(colspan=3)
    app4.spin("vals", 4, endValue=10, colspan=3, pos=3)
    app4.separator(colspan=3, direction="horizontal")

    row=app4.gr()
    app4.meter("Cry", row=row, column=0, fill="orange")
    with app4.labelFrame("Links", row=row, column=1):
        app4.link("Cry", "http://www.google.com")
        app4.link("Shout", press)
        app4.separator(row=0, column=1, rowspan=2, direction="vertical")
        app4.slider("happiness again", value=45, row=0, rowspan=2, direction="horizontal", show=True, column=2, interval=5, change=press)
        app4.scale("Hhappiness again", value=45, row=0, rowspan=2, direction="vertical", column=2, interval=25, change=press)

    #    app4.grip(row=row, column=2)
    toppings={"Cheese":False, "Tomato":False, "Bacon":False, "Corn":False, "Mushroom":False}

    app4.properties("Toppings", toppings, row=row, column=2, change=changer)
    app4.meter("CryingMor", fill="yellow")
    app4.meter("CryingMore", 50, colspan=3, kind="other")
    app4.meter("CryingMorer", 50, colspan=3, kind="split", fill=["green", "blue"])
    app4.meter("CryingMorerr", (50,70), colspan=3, kind="dual", fill=["green", "blue"])

    app4.registerEvent(test_gui4)
    app4.setPollTime(1000)

print("<<<Widget Test Suite Complete on app4 >>>")

doStopAgain = 0
def test_gui2(btn=None):
    print("Testing GUI2")
    global doStopAgain
    if doStopAgain == 5:
        print("Show app2")
        app2.show()
    elif doStopAgain == 6:
        print("Hide app2")
        app2.hide()
    elif doStopAgain == 8:
        print("Stopping app2")
        app2.stop()
    doStopAgain += 1

print("<<<Starting app2>>>")

app2 = gui(warn=True, useTtk=True)
app2.addStatusbar()
app2.setStatusbar("a")
app2.addToolbar("a", tester_function, True)
app2.setTtkTheme()
try: app2.setTtkTheme("broken")
except: pass
app2.setTtkTheme("default")
app2.ttkTheme = "default"
nb = app2.startNotebook("nb1")
assert isinstance(nb, ttk.Notebook)
nt = app2.startNote("nb1_n1")
assert isinstance(nt, ttk.Frame)
app2.addLabel("nb1_l1", TEXT_ONE)
app2.startNote("nb1_n2")
app2.addLabel("nb2_l1", TEXT_ONE)
app2.stopNote()
app2.startNote("nb1_n3")
app2.addLabel("nb3_l1", TEXT_ONE)
app2.stopNote()
app2.stopNotebook()

with pytest.raises(Exception) :
    app2.startNote()

with pytest.raises(Exception) :
    app2.stopNote()

with pytest.raises(Exception) :
    app2.stopNotebook()

with pytest.raises(Exception) :
    app2.startNotebook("nb1")

app2.showSplash(text="New test", fill="green", stripe="pink", fg="green", font=50)
app2.startLabelFrame("l1", hideTitle=True)
app2.addLabel("l1", "here")
app2.registerEvent(test_gui2)
app2.setPollTime(1000)
app2.setSize("fullscreen")
app2.startSubWindow("login")
app2.addLabel("log_l1", "Login page")
app2.stopSubWindow()

with app2.notebook("wnb"):
    with app2.note("wn"):
        app2.addLabel("wnlabel", "wnlabel")

app2.go(startWindow="login")

del app2
print("<<<Widget Test Suite Complete on app2 >>>")

print("<<<Widget Test Suite Complete>>>")
