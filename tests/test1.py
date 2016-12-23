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
    print("\tTesting labels")
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
    print("\t >> all tests complete")

def test_entries():
    print("\tTesting entries")
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
    print("\t >> all tests complete")

def test_buttons():
    print("\tTesting buttons")
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
    print("\t >> all tests complete")

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
    print("\t >> all tests complete")

def test_checks():
    print("\tTesting checks")
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
    print("\t >> all tests complete")

def test_options():
    print("\tTesting options")
    print(" >> not implemented...")

def test_spins():
    print("\tTesting spins")
    print(" >> not implemented...")

def test_lists():
    print("\tTesting lists")
    print(" >> not implemented...")

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

    assert app.getScale("s1") == 44
    assert app.getScale("s2") == 33
    assert app.getScale("s3") == 100
    assert app.getScale("s4") == 100

    print("\t >> all tests complete")

def test_messages():
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

    app.setTextArea("t1", TEXT_ONE)
    app.setTextArea("t2", TEXT_TWO)
    app.setTextArea("st1", TEXT_THREE)
    app.setTextArea("st2", TEXT_FOUR)

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
    print("\t >> all tests complete")

def test_meters():
    print("\tTesting meters")
    app.addMeter("m1")
#    print("\tpp.getMeter("m1"))
    assert app.getMeter("m1")[0] == 0
    app.setMeter("m1", 45)
#    print("\tpp.getMeter("m1"))
    assert app.getMeter("m1")[0] == 0.45
    print("\t >> all tests complete")

def test_properties():
    print("\tTesting properties")
    print(" >> not implemented...")

def test_separators():
    print("\tTesting separators")
    app.addHorizontalSeparator()
    app.addVerticalSeparator()
    print("\t >> all tests complete")

def test_links():
    print("\tTesting links")
    app.addLink("l1", None)
    app.addWebLink("l1", "http://appJar.info")
    print("\t >> all tests complete")

def test_grips():
    print("\tTesting grips")
    app.addGrip()
    app.addGrip()
    print("\t >> all tests complete")

def test_date_pickers():
    print("\tTesting date pickers")
    print(" >> not implemented...")

print("<<<Starting test suite>>>")
test_labels()
test_entries()
test_buttons()
test_radios()
test_checks()
test_options()
test_spins()
test_lists()
test_scales()
test_messages()
test_text_areas()
test_meters()
test_properties()
test_separators()
test_links()
test_grips()
test_date_pickers()
test_sets()
print("<<<Test suite complete>>>")
