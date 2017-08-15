HASH_ONE = {"a": True, "b": False, "c": True}
HASH_TWO = {"x": False, "y": True, "z": False}

import sys
sys.path.append("../")

def validateProp(p, d):
    for key in d.keys():
        assert app.getProperty(p, key) == d[key]

def compareDictionaries(d1, d2):
    for key in d1.keys():
        if d1[key] != d2[key]:
            return False
    for key in d2.keys():
        if d1[key] != d2[key]:
            return False
    return True

from appJar import gui, Properties
app=gui()

print("\tTesting properties")
isinstance(app.addProperties("p1", HASH_ONE), Properties)
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

print("\t >> all tests complete")
app.go()
