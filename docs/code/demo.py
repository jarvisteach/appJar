import os,sys

fileList = os.listdir(".")
while True:
    print("Demo Files")
    print("**********")
    for p,f in enumerate(fileList):
        print(p, f)
    while True:
        choice = input(">> Which one:")
        if choice.lower() == "q":
            sys.exit(0)
        try:
            choice=int(choice)
            with open(fileList[choice]) as f:
                code = compile(f.read(), fileList[choice], 'exec')
                exec(code)
        except:
            pass
