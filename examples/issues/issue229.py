import sys
sys.path.append("../../")

import appJar
class app(appJar.gui):
    def __init__(self, **kwargs):
        """Setup appJar and the defaults."""
        super().__init__()
        self.setTitle('main_win_title')
        self.main_widgets()

    def press(self, btn):
        print(self.getOptionBox("ob"))
        print(self.getOptionBox("ob2"))

    def main_widgets(self):
        self.addOptionBox("ob", ["a", "b", "c", "d"])
        self.addButton("PRESS", self.press)
                            
app = app()
app.go()
