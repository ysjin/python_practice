from tkinter import *
import random


class App:
    def __init__(self, t):
        self.i = PhotoImage(width=100, height=100)
        colors = [[random.randint(0, 255) for i in range(0, 3)] for j in range(0, 10000)]
        row = 0
        col = 0
        for color in colors:
            self.i.put('#%02x%02x%02x' % tuple(color), (row, col))
            col += 1
            if col == 100:
                row += 1
                col = 0
        #pixels=" ".join(("{"+" ".join(('#%02x%02x%02x' % tuple(next(colors)) for i in range(100)))+"}" for j in range(100)))
        #self.i.put(pixels,(0,0,100,100))
        c = Canvas(t, width=100, height=100)
        c.pack()
        c.create_image(0, 0, image=self.i, anchor=NW)

t = Tk()
a = App(t)
t.mainloop()
