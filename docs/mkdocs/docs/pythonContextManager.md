The Power of **with**
--

One thing I really wanted to get into appJar, was some indentation - I wanted the code for the GUI to look more like the actual GUI.  

I also wanted to simplify the creation of containers and even the GUI itself.  

So, now you can!

```
with gui("My first GUI") as app:
    app.addLabel("lab", "Hello world!")
```

That's it - 2 lines to create a GUI.  

If you want to add a container, it's the same process:

```
with gui("My first GUI") as app:

    with app.labelFrame("Left Frame"):
        app.addLabel("lLab", "Hello world!")

    with app.labelFrame("Right Frame", row=0, column=1):
        app.addLabel("rlab", "Hello world again!")
```

And, that's all there is to it.  This feature is available on all containers, and I think is going to revolutionise how people build GUIs!
