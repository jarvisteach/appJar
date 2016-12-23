import sys
sys.path.append("../")

EMPTY=""

TEXT_ONE = "l_one_x"
TEXT_TWO = "l_one_y"
TEXT_THREE = "l_one_z"
TEXT_FOUR = "l_one_a"
TEXT_FIVE = "l_one_b"

NUM_ONE = 23123
NUM_TWO = 33221

COL_ONE = "red"
COL_TWO = "yellow"
COL_THREE = "green"

from appJar import gui 
app=gui()


def test_labels():
    app.addEmptyLabel("el1")
    app.addLabel("l1", TEXT_ONE)
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

def test_entries():
    app.addEntry("e1")
    app.addNumericEntry("ne1")
    app.addSecretEntry("se1")
    app.addAutoEntry("ae1", ["a", "b", "c"])

    assert app.getEntry("e1") == EMPTY
#    assert app.getEntry("ne1") == EMPTY
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

    app.setEntry("e1", TEXT_ONE)
    app.setEntry("ne1", NUM_ONE)
    app.setEntry("se1", TEXT_ONE)
    app.setEntry("ae1", TEXT_ONE)

    assert app.getEntry("e1") == TEXT_ONE
#    assert app.getEntry("ne1") == NUM_ONE
    assert app.getEntry("se1") == TEXT_ONE
    assert app.getEntry("ae1") == TEXT_ONE

    app.clearEntry("e1")
    app.clearEntry("ne1")
    app.clearEntry("se1")
    app.clearEntry("ae1")

    assert app.getEntry("e1") == EMPTY
#    assert app.getEntry("ne1") == EMPTY
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

    app.setEntry("e1", TEXT_TWO)
    app.setEntry("ne1", NUM_TWO)
    app.setEntry("se1", TEXT_TWO)
    app.setEntry("ae1", TEXT_TWO)

    assert app.getEntry("e1") == TEXT_TWO
#    assert app.getEntry("ne1") == NUM_TWO
    assert app.getEntry("se1") == TEXT_TWO
    assert app.getEntry("ae1") == TEXT_TWO

    app.clearAllEntries()

    assert app.getEntry("e1") == EMPTY
#    assert app.getEntry("ne1") == EMPTY
    assert app.getEntry("se1") == EMPTY
    assert app.getEntry("ae1") == EMPTY

def test_buttons():
    app.addButton("b1", None)
    app.addButtons(["bb1", "bb2", "bb3", "bb4"], None)
    app.addButtons([["a2b1", "a2b2", "a2b3", "a2b4"], ["b2b1", "b2b2", "b2b3", "b2b4"], ["c2b1", "c2b2", "c2b3", "c2b4"]], None)
    app.addNamedButton("butName", "nb1", None) # name/title

    but1 = app.getButtonWidget("b1")
    but2 = app.getButtonWidget("bb1")
    but3 = app.getButtonWidget("a2b1")
#    but4 = app.getButtonWidget("nb1")
    assert but1.cget("text") == "b1"
    assert but2.cget("text") == "bb1"
    assert but3.cget("text") == "a2b1"
#    assert but4.cget("text") == "butName"

def test_sets():
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

def test_radios():
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

def test_checks():
    app.addCheckBox(TEXT_ONE)
    app.addCheckBox(TEXT_TWO)
    app.addCheckBox(TEXT_THREE)

    assert app.getCheckBox(TEXT_ONE) == False
    assert app.getCheckBox(TEXT_TWO) == False
    assert app.getCheckBox(TEXT_THREE) == False

    app.setCheckBox(TEXT_ONE)
    app.setCheckBox(TEXT_TWO, True)
    app.setCheckBox(TEXT_THREE, False)

    assert app.getCheckBox(TEXT_ONE) == True
    assert app.getCheckBox(TEXT_TWO) == True
    assert app.getCheckBox(TEXT_THREE) == False


test_labels()
test_entries()
test_buttons()
test_radios()
test_checks()

test_sets()
