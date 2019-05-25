import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')
    app.button('PRESS')
    app.addScrolledTextArea('s')
    app.setTextAreaHeight('s', 1)
    app.ttkStyle.configure("TLabel", foreground="green", background="blue", font=('Helvetica', 20))
    app.ttkStyle.configure("TButton", foreground="green", background="blue", font=('Helvetica', 20))
