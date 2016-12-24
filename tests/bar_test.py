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

LIST_ONE = ["a", "b", "c", "d", "e"]
LIST_TWO = ["v", "d", "s", "t", "z"]

HASH_ONE = { "a":True, "b": False, "c": True }
HASH_TWO = { "x":False, "y": True, "z": False }

from appJar import gui
app=gui()

def status_test():
    print("\tTesting bars")
    app.addStatusbar()
    app.setStatusbar(TEXT_ONE)
    app.clearStatusbar()
    app.setStatusbarWidth(40)
    print(" >> not implemented...")
#    print("\t >> all tests complete")

def menu_test():
    print("\tTesting menus")
    print(" >> not implemented...")
#    print("\t >> all tests complete")

def bar_test():
    print("\tTesting bars")
    print(" >> not implemented...")
#    print("\t >> all tests complete")

print("<<<Starting Bar Test Suite>>>")
status_test()
bar_test()
menu_test()
print("<<<Bar Test Suite Complete>>>")
