import sys
sys.path.append("../../")

import appJar
from concurrent.futures import ThreadPoolExecutor 

class app(appJar.gui):
    def __init__(self, **kwargs):
        super().__init__()
        self.setTitle('main_win_title')
        self.main_widgets()
        self.executor = ThreadPoolExecutor(max_workers=1)
                
    def task(self, runnable, *args, **kwargs):
        """Add background task to queue.

        :param runnable: Method to run in the background.
        :param args: Optional positional args (for the runnable).
        :param kwargs: Optional keyword args (for the runnable).
        """
        try:
            future = self.executor.submit(runnable, *args, **kwargs)
        except:
            print("ouch")
                
    def press(self, btn):
        self.task(self.press_task)

    def press_task(self):
        print(self.getOptionBox("ob"))
        print(self.getOptionBox("ob2"))
        print('Won\'t get called..')

    def main_widgets(self):
        self.addOptionBox("ob", ["a", "b", "c", "d"])
        self.addButton("PRESS", self.press)
            
app = app()
app.go()
