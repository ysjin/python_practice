from tkinter import *
from tkinter import ttk

def pixel(image, pos, color):
    r,g,b=color
    x,y=pos
    image.put("#{:02x}{:02x}{:02x}".format((r,g,b), (y,x))

root = Tk()
label = ttk.Label(root, text="Hello, Tkinter!")
label.pack()
label.config(text="howdy, text is changed")
label.config(wraplength=150)
label.config(justify=CENTER)
label.config(foreground='blue', background='yellow')
label.config(font=('Courier', 18, 'bold'))

#logo=PhotoImage(file='flduojk')
#label=config(image=logo)

test_img=PhotoImage(width=100, height=100)
pixel(test_img, (50,50), (255, 0, 0))
label=Label(root, image=test_img)
