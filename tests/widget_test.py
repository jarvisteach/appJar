import sys
import datetime
import pytest
try: from tkinter import Event
except: from Tkinter import Event
sys.path.append("../")
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

HASH_ONE = {"a": True, "b": False, "c": True}
HASH_TWO = {"x": False, "y": True, "z": False}

def tester_function(btn=None):
    print(btn)
    return True

from appJar import gui
app = gui()
app.showSplash()
print("NEXT...")


def test_grid_layout():
    print("\tTesting layout")
    app.addLabel("lay1", TEXT_ONE, 1)
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

def test_labels():
    print("\tTesting labels")
    app.addEmptyLabel("el1")
    app.addLabel("l0", TEXT_ONE)
    app.addLabel("l1", TEXT_ONE)
    row = app.getRow()
    app.addLabel("rowl1", TEXT_ONE, row)
    assert app.gr() == row + 1
    app.addFlashLabel("fl1", TEXT_ONE)

    assert app.getLabel("el1") == EMPTY
    assert app.getLabel("l1") == TEXT_ONE
    assert app.getLabel("fl1") == TEXT_ONE

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

    print("\t >> all tests complete")


def test_entries():
    print("\tTesting entries")
    app.addEntry("e1")
    app.addNumericEntry("ne1")
    app.addSecretEntry("se1")
    app.addAutoEntry("ae1", ["a", "b", "c"])
    app.setAutoEntryNumRows("ae1", 5)

    # quick validation check
    app.addValidationEntry("ve1")
    app.setEntryValid("ve1")
    app.setEntryInvalid("ve1")
    app.setEntryWaitingValidation("ve1")

    app.addEntry("tester")
    app.setEntryDefault("tester", TEXT_TWO)
    app.addEntry("tester2")
    app.setEntryDefault("tester2", TEXT_TWO)
    app.addEntry("tester3")
    app.setEntryDefault("tester3", TEXT_TWO)

    app.setEntryMaxLength("tester", 5)
    app.setEntry("tester", MIXED_TEXT)
    assert app.getEntry("tester") == MIXED_TEXT[:5]

    app.setEntryUpperCase("tester2")
    app.setEntry("tester2", MIXED_TEXT)
    assert app.getEntry("tester2") == MIXED_TEXT.upper()

    app.setEntryLowerCase("tester3")
    app.setEntry("tester3", MIXED_TEXT)
    assert app.getEntry("tester3") == MIXED_TEXT.lower()

    app.addLabelEntry("le1")
    app.addLabelNumericEntry("lne1")
    app.addLabelSecretEntry("lse1")
    app.addLabelAutoEntry("lae1", ["a", "b", "c"])

    assert app.getEntry("le1") == EMPTY
    assert app.getEntry("lne1") == 0
    assert app.getEntry("lse1") == EMPTY
    assert app.getEntry("lae1") == EMPTY

    assert app.getEntry("e1") == EMPTY
    assert app.getEntry("ne1") == 0
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

    entryVals = app.getAllEntries()
    assert entryVals["le1"] == EMPTY
    assert entryVals["lne1"] == 0
    assert entryVals["lse1"] == EMPTY
    assert entryVals["lae1"] == EMPTY
    assert entryVals["e1"] == EMPTY
    assert entryVals["ne1"] == 0
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
    assert app.getEntry("ne1") == 0
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

    assert app.getEntry("le1") == EMPTY
    assert app.getEntry("lne1") == 0
    assert app.getEntry("lse1") == EMPTY
    assert app.getEntry("lae1") == EMPTY

    app.setEntry("ne1", "-")
    assert app.getEntry("ne1") == 0
    app.setEntry("ne1", ".")
    assert app.getEntry("ne1") == 0
    app.setEntry("ne1", "0.0")
    assert app.getEntry("ne1") == 0
    app.setEntry("ne1", "-0.0")
    assert app.getEntry("ne1") == 0
    app.setEntry("ne1", ".")
    assert app.getEntry("ne1") == 0

    app.setEntry("lne1", "-")
    assert app.getEntry("lne1") == 0
    app.setEntry("lne1", ".")
    assert app.getEntry("lne1") == 0
    app.setEntry("lne1", "0.0")
    assert app.getEntry("lne1") == 0
    app.setEntry("lne1", "-0.0")
    assert app.getEntry("lne1") == 0
    app.setEntry("lne1", ".")
    assert app.getEntry("lne1") == 0

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
    assert app.getEntry("ne1") == 0
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

    assert app.getEntry("le1") == EMPTY
    assert app.getEntry("lne1") == 0
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
    assert app.getEntry("ne1") == 0
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

    assert app.getEntry("le1") == EMPTY
    assert app.getEntry("lne1") == 0
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


def test_buttons():
    print("\tTesting buttons")
    app.addButton("b1", None)
    app.addButtons(["bb1", "bb2", "bb3", "bb4"], None)
    with pytest.raises(Exception) :
        app.addButtons(["brk1", "brk1", "brk1", "brk1"], [None, None])
    app.addButtons(
            [["a2b1", "a2b2", "a2b3", "a2b4"],
            ["b2b1", "b2b2", "b2b3", "b2b4"],
            ["c2b1", "c2b2", "c2b3", "c2b4"]],
        None)
    app.addNamedButton("butName", "nb1", None)  # name/title

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

    app.addImageButton("ib1", None, "1_entries.gif")
    but1 = app.getButtonWidget("ib1")
    assert but1.cget("text") == ""

    # call generic setter functions
    test_setters("Button", "b1")

    print("\t >> all tests complete")


def test_radios():
    print("\tTesting radios")
    app.addRadioButton("rb", TEXT_ONE)
    app.addRadioButton("rb", TEXT_TWO)
    app.addRadioButton("rb", TEXT_THREE)

    assert app.getRadioButton("rb") == TEXT_ONE

    app.setRadioButton("rb", TEXT_TWO)
    assert app.getRadioButton("rb") == TEXT_TWO

    app.setRadioTick("rb")
    assert app.getRadioButton("rb") == TEXT_TWO

    app.setRadioButton("rb", TEXT_THREE)
    assert app.getRadioButton("rb") == TEXT_THREE

    # call generic setter functions
    test_setters("RadioButton", "rb")
    test_setters("Rb", "rb")

    print("\t >> all tests complete")


def test_checks():
    print("\tTesting checks")
    app.addCheckBox(TEXT_ONE)
    app.addCheckBox(TEXT_TWO)
    app.addCheckBox(TEXT_THREE)

    assert app.getCheckBox(TEXT_ONE) is False
    assert app.getCheckBox(TEXT_TWO) is False
    assert app.getCheckBox(TEXT_THREE) is False

    app.setCheckBox(TEXT_ONE)
    app.setCheckBox(TEXT_TWO, True)
    app.setCheckBox(TEXT_THREE, False)

    assert app.getCheckBox(TEXT_ONE) is True
    assert app.getCheckBox(TEXT_TWO) is True
    assert app.getCheckBox(TEXT_THREE) is False

    # call generic setter functions
    test_setters("CheckBox", TEXT_ONE)
    test_setters("Cb", TEXT_ONE)

    print("\t >> all tests complete")


def test_options():
    print("\tTesting options")
    # add two option boxes
    app.addOptionBox("l1", LIST_ONE)
    app.addOptionBox("l2", LIST_TWO)

    assert app.getOptionBox("l1") == LIST_ONE[0]
    assert app.getOptionBox("l2") == LIST_TWO[0]

    # select new items - by position
    app.setOptionBox("l1", 2)
    app.setOptionBox("l2", 3)

    assert app.getOptionBox("l1") == LIST_ONE[2]
    assert app.getOptionBox("l2") == LIST_TWO[3]

    # select new items - by value
    app.setOptionBox("l1", LIST_ONE[3])
    app.setOptionBox("l2", LIST_TWO[1])

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

    app.addTickOptionBox("tl1", LIST_ONE)
    app.addTickOptionBox("tl2", LIST_TWO)

    for item in LIST_ONE:
        assert app.getOptionBox("tl1")[item] is False

    for item in LIST_TWO:
        assert app.getOptionBox("tl2")[item] is False

    app.setOptionBox("tl1", LIST_ONE[1], True)
    app.setOptionBox("tl2", LIST_TWO[2], True)

    assert app.getOptionBox("tl1")[LIST_ONE[1]] is True
    assert app.getOptionBox("tl2")[LIST_TWO[2]] is True

    app.changeOptionBox("tl1", LIST_TWO)
    for item in LIST_TWO:
        assert app.getOptionBox("tl1")[item] is False

    app.changeOptionBox("tl1", LIST_ONE)
    for item in LIST_ONE:
        assert app.getOptionBox("tl1")[item] is False

    # call generic setter functions
    test_setters("OptionBox", "l1")


    print("\t>> all tests complete")


def test_spins():
    print("\tTesting spins")

    app.addSpinBox("s1", ["a", "b", "c", "d", "e"])
    app.addSpinBox("s2", ["a", "b", "c", "d", "e"])
    app.addSpinBoxRange("s3", 5, 200)
    app.addSpinBoxRange("s4", 25, 200)

    assert app.getSpinBox("s1") == "a"
    assert app.getSpinBox("s2") == "a"
    assert app.getSpinBox("s3") == "5"
    assert app.getSpinBox("s4") == "25"

    app.setSpinBox("s1", "b")
    app.setSpinBox("s2", "d")
    app.setSpinBox("s3", "200")
    app.setSpinBox("s4", "150")

    assert app.getSpinBox("s1") == "b"
    assert app.getSpinBox("s2") == "d"
    assert app.getSpinBox("s3") == "200"
    assert app.getSpinBox("s4") == "150"

    # call generic setter functions
    test_setters("SpinBox", "s1")


    print("\t>> all tests complete")


def test_lists():
    print("\tTesting lists")

    app.addListBox("l1", LIST_ONE)
    app.addListBox("l2", LIST_TWO)
    app.setListBoxFunction("l1", tester_function)

    app.setListItemBg("l1", LIST_ONE[1], "red")
    app.setListItemFg("l1", LIST_ONE[1], "green")

    assert app.getListItems("l1") == []
    assert app.getListItems("l2") == []

    assert app.getAllListItems("l1") == LIST_ONE
    assert app.getAllListItems("l2") == LIST_TWO

    app.addListItem("l1", "f")
    assert app.getListItems("l1") == ["f"]
    assert app.getAllListItems("l1") == LIST_ONE+["f"]

    app.addListItems("l2", LIST_ONE)
    assert app.getAllListItems("l2") == LIST_TWO+LIST_ONE
    assert app.getListItems("l2") == [LIST_ONE[len(LIST_ONE)-1]]

    app.setListBoxRows("l1", 2)
    app.setListBoxRows("l2", 10)

    assert app.getListItems("l2") == [LIST_ONE[len(LIST_ONE)-1]]
#    print(app.getListItems("l1"))
#    assert app.getListItems("l1") == ["f"]

    app.clearListBox("l1")
    assert app.getListItems("l1") == []
    assert app.getListItems("l2") == [LIST_ONE[len(LIST_ONE)-1]]

    app.updateListItems("l1", LIST_ONE)
    app.selectListItem("l1", LIST_ONE[0])
    app.selectListItem("l1", LIST_ONE[3])
    assert app.getListItems("l1") == [LIST_ONE[3]]

    app.setListBoxMulti("l1")
    app.selectListItem("l1", LIST_ONE[0])
    app.selectListItem("l1", LIST_ONE[3])
#    print(app.getListItems("l1"))
#    assert app.getListItems("l1") == [LIST_ONE[0], LIST_ONE[3]]

    app.updateListItems("l2", LIST_TWO)
    assert app.getAllListItems("l2") == LIST_TWO
#    print(app.getListItems("l2"))
#    assert app.getListItems("l2") == []
# SELECTING THE LAST ONE...

    app.removeListItem("l2", LIST_TWO[1])
    tmp_list = LIST_TWO
    tmp_list.remove(tmp_list[1])
    assert app.getAllListItems("l2") == tmp_list

    # call generic setter functions
    test_setters("ListBox", "l1")
    test_setters("Lb", "l1")

    print("\t>> all tests complete")


def test_scales():
    print("\tTesting scales")
    app.addScale("s1")
    app.addScale("s2")
    app.addScale("s3")
    app.addScale("s4")

    assert app.getScale("s1") == 0
    assert app.getScale("s2") == 0
    assert app.getScale("s3") == 0
    assert app.getScale("s4") == 0

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
    app.orientScaleHor("s2")
    app.orientScaleHor("s2", False)

    assert app.getScale("s1") == 44
    assert app.getScale("s2") == 33
    assert app.getScale("s3") == 100
    assert app.getScale("s4") == 100

    sc = app.getWidget(app.SCALE, "s1")

    sc._ajScale__jump("trough1")
    sc._ajScale__jump("trough2")


    # call generic setter functions
    test_setters("Scale", "s1")

    print("\t >> all tests complete")


def test_message_boxes():
    print("\tTesting messages")
    app.addMessage("m1", TEXT_ONE)
    app.addMessage("m2", TEXT_TWO)
    app.addEmptyMessage("m3")
    app.addEmptyMessage("m4")

    assert app.getMessageWidget("m1").cget("text") == TEXT_ONE
    assert app.getMessageWidget("m2").cget("text") == TEXT_TWO
    assert app.getMessageWidget("m3").cget("text") == EMPTY
    assert app.getMessageWidget("m4").cget("text") == EMPTY

    app.setMessage("m1", EMPTY)
    app.setMessage("m2", TEXT_ONE)
    app.setMessage("m3", TEXT_THREE)
    app.setMessage("m4", EMPTY)

    assert app.getMessageWidget("m1").cget("text") == EMPTY
    assert app.getMessageWidget("m2").cget("text") == TEXT_ONE
    assert app.getMessageWidget("m3").cget("text") == TEXT_THREE
    assert app.getMessageWidget("m4").cget("text") == EMPTY

    app.clearMessage("m2")
    app.clearMessage("m3")

    assert app.getMessageWidget("m1").cget("text") == EMPTY
    assert app.getMessageWidget("m2").cget("text") == EMPTY
    assert app.getMessageWidget("m3").cget("text") == EMPTY
    assert app.getMessageWidget("m4").cget("text") == EMPTY

    # call generic setter functions
    test_setters("Message", "m1")

    print("\t >> all tests complete")


def test_text_areas():
    print("\tTesting text areas")
    app.addTextArea("t1")
    app.addTextArea("t2")
    app.addScrolledTextArea("st1")
    app.addScrolledTextArea("st2")

    assert app.getTextArea("t1") == EMPTY
    assert app.getTextArea("t2") == EMPTY
    assert app.getTextArea("st1") == EMPTY
    assert app.getTextArea("st2") == EMPTY

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

    app.clearTextArea("t2")
    app.clearTextArea("st1")

    assert app.getTextArea("t1") == TEXT_ONE
    assert app.getTextArea("t2") == EMPTY
    assert app.getTextArea("st1") == EMPTY
    assert app.getTextArea("st2") == TEXT_FOUR

    # call generic setter functions
    test_setters("TextArea", "t1")

    print("\t >> all tests complete")


def test_meters():
    print("\tTesting meters")
    app.addMeter("m1")
    assert app.getMeter("m1")[0] == 0

    app.setMeter("m1", 45)
    assert app.getMeter("m1")[0] == 0.45

    app.addSplitMeter("spm")
    app.addDualMeter("dum")

    app.setMeter("spm", 50)
    app.setMeter("dum", [50, 10])

    app.setMeterFill("spm", ["red", "green"])
    app.setMeterFill("dum", ["red", "pink"])

    app.getMeter("spm")
    app.getMeter("dum")

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
    app.addProperties("p1", HASH_ONE)
    app.addProperties("p2")

    assert compareDictionaries(app.getProperties("p1"), HASH_ONE)
    assert app.getProperties("p2") == {}

    validateProp("p1", HASH_ONE)

    app.setProperties("p2", HASH_TWO)
    validateProp("p2", HASH_TWO)
    assert compareDictionaries(app.getProperties("p2"), HASH_TWO)

    hash_all = HASH_ONE.copy()
    hash_all.update(HASH_TWO)

    app.setProperties("p2", HASH_ONE)
    validateProp("p2", hash_all)
    assert compareDictionaries(app.getProperties("p2"), hash_all)

    for key in hash_all.keys():
        hash_all[key] = False

    assert not compareDictionaries(app.getProperties("p2"), hash_all)
    app.setProperties("p2", hash_all)
    assert compareDictionaries(app.getProperties("p2"), hash_all)

    app.setProperty("p2", "a", True)
    assert app.getProperty("p2", "a") is True

    # call generic setter functions
    test_setters("Properties", "p1")

    print("\t >> all tests complete")


def test_separators():
    print("\tTesting separators")
    app.addHorizontalSeparator()
    app.addVerticalSeparator()
    print("\t >> all tests complete")


def test_links():
    print("\tTesting links")
    app.addLink("l1", None)
    app.addWebLink("l1", "http://appJar.info")

    # call generic setter functions
    test_setters("Link", "l1")

    print("\t >> all tests complete")


def test_grips():
    print("\tTesting grips")
    app.addGrip()
    app.addGrip()
    print("\t >> all tests complete")


def test_auto_labels():
    print("\tTesting auto_labels")
    app.addLabelEntry("lab_ent")
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
    app.addDatePicker("d2")
    app.addDatePicker("d3")

    assert app.getDatePicker("d1") == datetime.date(1970, 1, 1)
    assert app.getDatePicker("d2") == datetime.date(1970, 1, 1)
    assert app.getDatePicker("d3") == datetime.date(1970, 1, 1)

    app.setDatePicker("d1")
    app.setDatePicker("d2", datetime.date(1980, 5, 5))
    app.setDatePicker("d3", datetime.date(1990, 10, 10))

    assert app.getDatePicker("d1") == datetime.date.today()
    assert app.getDatePicker("d2") == datetime.date(1980, 5, 5)
    assert app.getDatePicker("d3") == datetime.date(1990, 10, 10)

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

    # call generic setter functions
    test_setters("DatePicker", "d1")

    print("\t >> all tests complete")


def test_pies():
    print("\tTesting Pies")
    app.addPieChart("p1", {"apples": 50, "oranges": 200, "grapes": 75, "beef": 300, "turkey": 150})
    app.setPieChart("p1", "beef", 5)
    app.setPieChart("p1", "fish", 20)
    app.setPieChart("p1", "apples", 0)

    # call generic setter functions
    test_setters("PieChart", "p1")

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_trees():
    print("\tTesting Trees")
    app.addTree("t1",
        """<people>
        <person><name>Fred</name><age>45</age><gender>Male</gender></person>
        <person><name>Tina</name><age>37</age><gender>Female</gender></person>
        <person><name>CLive</name><age>28</age><gender>Male</gender></person>
        <person><name>Betty</name><age>51</age><gender>Female</gender></person>
        </people>""")

    app.setTreeDoubleClickFunction("t1", tester_function)
    app.setTreeEditFunction("t1", tester_function)
    app.setTreeEditable("t1", True)
    app.setTreeEditable("t1", False)
    app.setTreeBg("t1", "red")
    app.setTreeFg("t1", "yellow")
    app.setTreeHighlightBg("t1", "orange")
    app.setTreeHighlightFg("t1", "pink")
    app.getTreeXML("t1")
    app.getTreeSelected("t1")
    app.getTreeSelectedXML("t1")

    app.setTreeColours("t1", "red", "yellow", "yellow", "red")

    # call generic setter functions
    test_setters("Tree", "t1")

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
        addRow=True)

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
    app.setTransparency(50)
    app.setTransparency(50)

    app.setGeometry("100x100")
    app.setGeometry(200,200)
    app.setGeometry("fullscreen")
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

    app.setGuiPadding(20,20)
    app.setGuiPadding([20,20])
    app.hideTitleBar()
    app.showTitleBar()

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


def test_events():
    print("\tTesting events")

    app.enableEnter(tester_function)
    app.disableEnter()

    app.bindKey("b", tester_function)
    app.unbindKey("b")

    app.registerEvent(tester_function)
    app.setPollTime(2)
    app.setPollTime(0.5)

    app.setStopFunction(tester_function)

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_images():
    print("\tTesting images")

    app.addImage("im1", "1_flash.gif")

    app.setAnimationSpeed("im1", 10)
    app.startAnimation("im1")
    app.stopAnimation("im1")
    app.startAnimation("im1")

    app.addImage("im2", "1_entries.gif")
    app.addImage("im3", "1_checks.png")
    app.addImage("im4", "sc.jpg")

# jpeg...

    app.setImage("im3", "1_entries.gif")
    app.reloadImage("im3", "1_entries.gif")
    app.setImageMouseOver("im1", "1_checks.png")
    app.setImageSize("im2", 40, 40)
    app.zoomImage("im1", 2)

    app.shrinkImage("im3", 2)
    app.growImage("im3", 2)

#    app.setBgImage("1_checks.png")
#    app.removeBgImage()

    app.setImageLocation("images")
    app.addImage("iml", "1_entries.gif")

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_status():
    print("\tTesting Statusbar")

    app.addStatusbar()
    app.setStatusbar(TEXT_ONE)
    app.clearStatusbar()
    app.setStatusbarWidth(40)

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_menus():
    print("\tTesting Menubar")

    app.addMenuList("a", LIST_ONE, tester_function)
    app.createMenu("MEN2")
    app.addMenuItem("MEN2", "MM2", tester_function, shortcut="k", underline=2)
    app.addMenuSeparator("MEN2")
    app.addMenuCheckBox("MEN2", "CB2", tester_function, shortcut="c", underline=2)
    app.addMenuRadioButton("MEN2", "a", "BB2", tester_function, shortcut="r", underline=2)
    app.addMenuRadioButton("MEN2", "a", "BB3", tester_function)
    app.addSubMenu("MEN2", "sub1")
    app.addMenuItem("sub1", "MMM2", tester_function, shortcut="w", underline=2)
    app.addMenuSeparator("sub1")
    app.addMenuCheckBox("sub1", "CB23", tester_function, shortcut="x", underline=2)
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

    app.createRightClickMenu("RCLICK")
    app.addLabel("RCLICK", "RCLICK")
    app.setLabelRightClick("RCLICK", "RCLICK")

    app.addEntry("RCLICK")
    app.addMenuEdit()

# this causes testing to hang - the popup doesn't go....

#    event = Event()
#    event.widget = ent
#    event.x_root = 100
#    event.y_root = 100
#
#    for type in [None, "9", "3", "4", "2"]:
#        event.type = type
#        app._gui__rightClick(event)
#        app.setEntry("RCLICK", "text")
#        app._gui__rightClick(event)


# this breaks - there is no widget in focus??
#    for action in ["Cut", "Copy", "Paste", "Select All", "Clear Clipboard", "Clear All", "Undo", "Redo"]:
#        app.setEntry("RCLICK", action)
#        app.setEntryFocus("RCLICK")
#        app._gui__copyAndPasteHelper(action)


    app.enableMenubar()
    app.disableMenubar()
    app.enableMenubar()

    app.enableMenu("MEN2")
    app.disableMenu("MEN2")
    app.enableMenu("MEN2")

    app.enableMenuItem("MEN2", "MM2")
    app.disableMenuItem("MEN2", "MM2")
    app.enableMenuItem("MEN2", "MM2")

    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_toolbars():
    print("\tTesting Toolbar")

    app.addToolbar(["a", "b", "c"],tester_function)

    app.setToolbarEnabled()
    app.setToolbarDisabled()
    app.setToolbarEnabled()

    app.setToolbarButtonEnabled("a")
    app.setToolbarButtonDisabled("a")
    app.setToolbarButtonEnabled("a")

    app.showToolbar()
    app.hideToolbar()
    app.showToolbar()

    app.setToolbarImage("a", "1_entries.gif")
    app.setToolbarImage("b", "1_checks.png")

# doesn't work in python 2.7
#    app.setToolbarIcon("a", "web")
#    app.setToolbarIcon("b", "weight")
#    app.setToolbarIcon("c", "wi-fi")

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
    app.changeLanguage("ENGLISH")
    print(" >> not implemented...")
    #print("\t >> all tests complete")
    app.disableDebug()


def test_tooltips():
    print("\tTesting tooltip")
    app.setLabelTooltip("l1", "message")
    lab = app.getLabelWidget("l1")
    tip = lab.tooltip
    tip.enter()
    tip.leave()
    tip.motion()
    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_messages():
    print("\tTesting messages")
    app.warn("warn message")
    app.debug("debug message")

    app.disableWarnings()
    app.warn("warn message")
    app.debug("debug message")

    app.enableDebug()
    app.warn("warn message")
    app.debug("debug message")
    print(" >> not implemented...")
    #print("\t >> all tests complete")
    app.disableDebug()
    app.enableWarnings()


def test_sounds():
    print("\tTesting sounds")
# only support windows
    try:
        app.soundError()
        app.soundWarning()
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


def test_setters(widg_type, widg_id):
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

    exec("app.set" + widg_type + "DragFunction(\""+widg_id +"\", tester_function )")
    exec("app.set" + widg_type + "DragFunction(\""+widg_id +"\", [tester_function,tester_function] )")
    exec("app.set" + widg_type + "OverFunction(\""+widg_id +"\", tester_function)")
    exec("app.set" + widg_type + "OverFunction(\""+widg_id +"\", [tester_function, tester_function])")
    exec("app.set" + widg_type + "Command(\""+widg_id +"\", tester_function)")
    exec("app.set" + widg_type + "Func(\""+widg_id +"\", tester_function)")
    exec("app.set" + widg_type + "Function(\""+widg_id +"\", tester_function)")
    exec("app.set" + widg_type + "ChangeFunction(\""+widg_id +"\", tester_function)")
    exec("app.set" + widg_type + "SubmitFunction(\""+widg_id +"\", tester_function)")
    exec("app.set" + widg_type + "RightClick(\""+widg_id +"\", tester_function)")

    exec("app.get"+widg_type+"Widget(\""+widg_id+"\")")

#    exec("app.show" + widg_type+ "(\""+widg_id +"\")")
#    exec("app.hide" + widg_type+ "(\""+widg_id +"\")")
#    exec("app.enable" + widg_type+ "(\""+widg_id +"\")")
#    exec("app.disable" + widg_type+ "(\""+widg_id +"\")")
#    exec("app.remove" + widg_type+ "(\""+widg_id +"\")")
    print(" >> not implemented...")
    #print("\t >> all tests complete")


def test_sets():
    print("\tTesting setters")
    app.setLabelBg("l1", COL_ONE)
    app.setLabelFg("l1", COL_TWO)
    app.setLabelDisabledFg("l1", COL_THREE)
    app.setLabelWidth("l1", 77)
    app.setLabelHeight("l1", 33)
    app.setLabelRelief("l1", "sunken")
    app.setLabelState("l1", "disabled")

    lab = app.getLabelWidget("l1")

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

    app.startLabelFrame("lf1")
    app.setLabelFrameAnchor("lf1", "east")
    app.addLabel("lf1_l1", TEXT_ONE)
    app.stopLabelFrame()

    app.openLabelFrame("lf1")
    app.addLabel("lf1_l2", TEXT_ONE)
    app.stopLabelFrame()

    with pytest.raises(Exception) :
        app.openLabelFrame("crash here")

    app.startToggleFrame("tf1")
    app.addLabel("tf1_l1", TEXT_ONE)
    app.stopToggleFrame()

    assert app.getToggleFrameState("tf1") is False

    app.toggleToggleFrame("tf1")
    assert app.getToggleFrameState("tf1") is True
    app.toggleToggleFrame("tf1")
    assert app.getToggleFrameState("tf1") is False

    app.openToggleFrame("tf1")
    app.addLabel("tf1_l2", TEXT_ONE)
    app.stopToggleFrame()

    app.disableToggleFrame("tf1")
    app.enableToggleFrame("tf1")

    app.startTabbedFrame("tbf1")
    app.startTab("tab1")
    app.addLabel("tbf1_l1", TEXT_ONE)
    app.stopTab()
    app.startTab("tab2")
    app.addLabel("tbf2_l1", TEXT_ONE)
    app.stopTab()
    app.startTab("tab3")
    # empty tab
    app.stopTab()
    app.stopTabbedFrame()

    app.setTabBg("tbf1", "tab2", "red")

    assert app.getTabbedFrameSelectedTab("tbf1") == "tab1"
    app.setTabbedFrameSelectedTab("tbf1", "tab2")
    assert app.getTabbedFrameSelectedTab("tbf1") == "tab2"

    app.openTabbedFrame("tbf1")
    app.startTab("tab4")
    app.addLabel("tbf4_l1", TEXT_ONE)
    app.stopTab()
    app.stopTabbedFrame()

    app.setTabbedFrameInactiveFg("tbf1", "red")
    app.setTabbedFrameInactiveBg("tbf1", "red")

    app.openTab("tbf1", "tab4")
    app.addLabel("tbf4_l2", TEXT_ONE)
    app.stopTab()

    app.setTabbedFrameDisabledTab("tbf1", "tab3")
    app.setTabbedFrameDisableAllTabs("tbf1")

    app.setTabbedFrameTabExpand("tbf1")

    app.startPanedFrame("p1")
    app.addLabel("p1_l1", TEXT_ONE)
    app.startPanedFrame("p2")
    app.addLabel("p2_l1", TEXT_ONE)
    app.stopPanedFrame()
    app.startPanedFrameVertical("p3")
    app.addLabel("p3_l1", TEXT_ONE)
    app.stopPanedFrame()
    app.stopAllPanedFrames()

    app.openPanedFrame("p1")
    app.addLabel("p1_l11", TEXT_ONE)
    app.stopPanedFrame()

    app.startPagedWindow("pg1")
    app.startPage()
    app.addLabel("pg1_l1", TEXT_ONE)
    app.stopPage()
    app.startPage()
    app.addLabel("pg2_l1", TEXT_ONE)
    app.stopPage()
    app.startPage()
    app.addLabel("pg3_l1", TEXT_ONE)
    app.stopPage()
    app.stopPagedWindow()

    app.startPagedWindow("ppp2")
    app.startPage("ppp2_p1")
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

    app.openPagedWindow("pg1")
    app.startPage()
    app.addLabel("pg4_l1", TEXT_ONE)
    app.stopPage()
    app.stopPagedWindow()

    app.openPage("pg1", 2)
    app.addLabel("pg2_np", TEXT_ONE)
    app.stopPage()

    pw = app.getWidget("pagedWindow", "pg1")
    pw.showFirst()
    pw.showFirst()
    pw.showPrev()
    pw.showNext()
    pw.showLast()
    pw.showLast()
    pw.showNext()
    pw.showPrev()

# breaks under python2.7
    app.startSubWindow("sb1", modal=False, transient=False, blocking=False, grouped=False)
    app.addLabel("sb1_l", TEXT_ONE)
    app.stopSubWindow()

    app.openSubWindow("sb1")
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


    app.startFrame("fr1")
    app.addLabel("fr1_l", TEXT_ONE)
    app.stopFrame()
    app.openFrame("fr1")
    app.addLabel("fr1_l2", TEXT_ONE)
    app.stopFrame()

    app.startScrollPane("sp1")
    app.addLabel("sp_l", TEXT_ONE)
    app.stopScrollPane()
    app.openScrollPane("sp1")
    app.addLabel("sp_l2", TEXT_ONE)
    app.stopScrollPane()

    sp = app.getWidget(app.SCROLLPANE, "sp1")

    event = Event()

    sp._ScrollPane__mouseEnter(event)
    sp._ScrollPane__mouseLeave(event)

    for num in [4, 5]:
        event.num = num
        sp._ScrollPane__horizMouseScroll(event)
        sp._ScrollPane__vertMouseScroll(event)

    event.num = 0
    for delta in [300, 30, -300, -30]:
        event.delta = delta
        sp._ScrollPane__horizMouseScroll(event)
        sp._ScrollPane__vertMouseScroll(event)

    event.type = "2"    # always 2
    for state in [0]: # shift=0x0001, ctrl=0x0004, alt=0x20000
        event.state = state
        for key in ["Up", "Down", "Left", "Right", "Prior", "Next", "Home", "End"]:
            event.keysym = key
            sp._ScrollPane__keyPressed(event)

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
        axes = app.addPlot("p1", x, y)
        axes.legend(["key data"])
        app.refreshPlot("p1")
        app.updatePlot("p1", x, y)
        print(" >> not implemented...")
        #print("\t >> all tests complete")

def test_microbits():
    print("\tTesting plots:", PY_VER)
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
    a = app.textBox("a", "a", "initial")
    assert a is None
    print("Registering event:")
    app.topLevel.after(500, closePop)
    a = app.numberBox("a", "a")
    assert a is None

    print(" >> not implemented...")
    #print("\t >> all tests complete")


print("<<<Starting Widget Test Suite>>>")
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
test_separators()
test_links()
test_grips()
test_date_pickers()
try: test_plots()
except: print("Skipping plot tests - MatPlotLib not available")
test_microbits()

test_status()
test_menus()
test_toolbars()

test_auto_labels()

test_pies()
test_trees()
test_grids()

test_images()
test_sounds()
test_tooltips()
test_langs()

test_containers()
test_messages()


test_sets()
test_gui_options()
test_events()
test_widget_arranging()

test_hideShow()

doStop = 0
def test_gui(btn=None):
    print("Testing GUI")
    global doStop
    if doStop == 0:
        test_pop_ups()
    if doStop == 2:
        test_sets()
        test_langs()
        test_widget_arranging()
        test_gui_options()
        doStop += 1
    elif doStop == 3:
        try:
            app.removeAllWidgets()
        except:
# test_gui is sitll in event loop for second GUI - causes this to be called - but no app...
            print("weird error")
        doStop += 1
    elif doStop < 5:
        doStop += 1
        print("Waiting", doStop)
    else:
        print("Stopping app")
        try:
            app.stop()
        except:
            print("weird error...")

app.registerEvent(test_gui)
app.setPollTime(1000)
app.go("CANADIAN")

print("<<<Widget Test Suite Complete>>>")
del app

doStop = 0
def test_gui2(btn=None):
    print("Testing GUI2")
    global doStop
    if doStop == 5:
        print("Show app2")
        app2.show()
    elif doStop == 6:
        print("Hide app2")
        app2.hide()
    elif doStop == 8:
        print("Stopping app2")
        app2.stop()
    doStop += 1

app2 = gui()
app2.showSplash(text="New test", fill="green", stripe="pink", fg="green", font=50)
app2.startLabelFrame("l1")
app2.addLabel("l1", "here")
app2.registerEvent(test_gui2)
app2.setPollTime(1000)
app2.setGeometry("fullscreen")
app2.startSubWindow("login")
app2.addLabel("log_l1", "Login page")
app2.stopSubWindow()
app2.go(startWindow="login")

print("<<<Widget Test Suite Complete>>>")
