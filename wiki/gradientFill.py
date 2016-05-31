import tkinter as tk

class Example(tk.Frame):
      def __init__(self, parent):
            tk.Frame.__init__(self, parent)
            f = GradientFrame(root, "khaki1", "right")
            f.pack(fill="both", expand=True)

''' http://stackoverflow.com/questions/26178869/is-it-possible-to-apply-gradient-colours-to-bg-of-tkinter-python-widgets '''
class GradientFrame(tk.Canvas):
      '''A gradient frame which uses a canvas to draw the background'''
      def __init__(self, parent, colour, direction):
            tk.Canvas.__init__(self, parent, borderwidth=1, relief="sunken")
            self._color = colour
            self._direction=direction
            self.bind("<Configure>", self._draw_gradient)

      def _draw_gradient(self, event=None):
            '''Draw the gradient'''
            self.delete("gradient")
            width = self.winfo_width()
            height = self.winfo_height()
            limit = width
            if self._direction=="left":
                  (r1,g1,b1) = self.tint(30000)
                  (r2,g2,b2) = self.tint(-30000)
            else:
                  (r1,g1,b1) = self.tint(-30000)
                  (r2,g2,b2) = self.tint(30000)
            r_ratio = float(r2-r1) / limit
            g_ratio = float(g2-g1) / limit
            b_ratio = float(b2-b1) / limit

            for i in range(limit):
                  nr = int(r1 + (r_ratio * i))
                  ng = int(g1 + (g_ratio * i))
                  nb = int(b1 + (b_ratio * i))
                  color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
                  self.create_line(i,0,i,height, tags=("gradient",), fill=color)
            self.lower("gradient")

      def _remove_lines(self):
            self.delete("gradient")

      ''' http://chase-seibert.github.io/blog/2011/07/29/python-calculate-lighterdarker-rgb-colors.html '''
      def tint(self, brightness_offset=1):
            rgb_hex = self.winfo_rgb(self._color)
            new_rgb_int = [hex_value + brightness_offset for hex_value in rgb_hex]
            new_rgb_int = [min([65535, max([0, i])]) for i in new_rgb_int] # make sure new values are between 0 and 65535
            return new_rgb_int

if __name__ == "__main__":
      root = tk.Tk()
      Example(root).pack(fill="both", expand=True)
      root.mainloop()
