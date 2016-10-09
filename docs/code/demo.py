import os,sys

fileList = os.listdir(".")
fileList.remove("demo.py")
fileList.remove("other")

fileList.sort()

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
                break
        except:
            pass
