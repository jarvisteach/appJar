poo = None
try:
    import sys as poo
except:
    poo = False


if poo is None:
    print("didn't try")
elif poo is False:
    print("failed")
else:
    print("got it")
