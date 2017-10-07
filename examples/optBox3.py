import sys, pytest
sys.path.append("../")

LIST_ONE = ["a", "b", "c", "d", "e"]
LIST_TWO = ["v", "d", "s", "t", "z"]
print(LIST_ONE)
print(LIST_TWO)

from tkinter import OptionMenu
from appJar import gui

def get(btn):
    a = app.getOptionBoxWidget("l1")
    b = app.getOptionBoxWidget("l2")
    c = app.getOptionBoxWidget("l3")

    print("VAR ARRAY: ", app.n_optionVars["l1"], app.n_optionVars["l2"], app.n_optionVars["l2"])
    print("LINKED VARS: ", a.var, b.var, c.var)
    print("ORIG GET: ", app.getOptionBox("l1"), app.getOptionBox("l2"))
    print("LINKED VARS: ", a.var.get(), b.var.get())
    print("STORED VARS: ", app.n_optionVars["l1"].get(), app.n_optionVars["l2"].get())

def test0(btn=None):
    print(LIST_ONE[0], LIST_TWO[0])
    assert app.getOptionBox("l1") == LIST_ONE[0]
    assert app.getOptionBox("l2") == LIST_TWO[0]

def test1(btn=None):
    print(LIST_ONE[0], LIST_TWO[0])
    obs = app.getAllOptionBoxes()
    assert obs["l1"] == LIST_ONE[0]
    assert obs["l2"] == LIST_TWO[0]


def test2(btn=None):
    # select new items - by position
    app.setOptionBox("l1", 3)
    app.setOptionBox("l2", 2)

    print( LIST_ONE[3], LIST_TWO[2])

    assert app.getOptionBox("l1") == LIST_ONE[3]
    assert app.getOptionBox("l2") == LIST_TWO[2]

def test3(btn=None):
    app.clearOptionBox("l1")
    print( LIST_ONE[0], LIST_TWO[2])

    assert app.getOptionBox("l1") == LIST_ONE[0]
    assert app.getOptionBox("l2") == LIST_TWO[2]

def test4(btn=None):
    app.setOptionBox("l1", 2)
    app.clearAllOptionBoxes()
    print( LIST_ONE[0], LIST_TWO[0])
    assert app.getOptionBox("l1") == LIST_ONE[0]
    assert app.getOptionBox("l2") == LIST_TWO[0]

def test5(btn=None):
    # select new items - by position
    app.setOptionBox("l1", 2)
    app.setOptionBox("l2", 3)

def test6(btn=None):
    # select new items - by value
    app.setOptionBox("l1", LIST_ONE[3])
    app.setOptionBox("l2", LIST_TWO[1])
    app.renameOptionBoxItem("l2", LIST_TWO[0], "newName")

    assert app.getOptionBox("l1") == LIST_ONE[3]

with gui() as app:
    print("\tTesting options")
    # add two option boxes
    assert isinstance(app.addOptionBox("l1", LIST_ONE), OptionMenu)
    app.addOptionBox("l2", LIST_TWO)
    with pytest.raises(Exception):
        app.addOptionBox("l2", LIST_TWO)
    app.addOptionBox("l3", LIST_TWO)

    app.addButtons(["0", "1", "2", "3", "4", "5", "6"], [test0, test1, test2, test3, test4, test5, test6])
    app.addButton("get", get)
