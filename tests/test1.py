EMPTY=""

TEXT_ONE = "l_one_x"
TEXT_TWO = "l_one_y"

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


test_labels()
test_entries()
test_sets()
