#!/usr/bin/python3

import sys
import numpy
from tkinter import *
from tkinter import ttk
#from tkfiledialog   import askopenfilename


def NewFile():
    print ("New File!")


def OpenFile():
    pass
    # name = askopenfilename()
    # print (name)


def About():
    print ("This is a simple example of a menu")


def bytes_from_file(fp, size):
    while True:
        chunk = fp.read(size)
        if chunk:
            for b in chunk:
                yield b
        else:
            break


def read_yuv(filename, width, height):
    fp = open(filename, "rb")

    frame_i=0
    Y = []
    U = []
    V = []


    while True:
        # Y
        for b in bytes_from_file(fp, width*height):
            Y.append(b)

        for r in range(height//2):
            row = []
            for b in bytes_from_file(fp, width//2):
                row += ([b]*2)
            U += (row*2)

        for r in range(height//2):
            row = []
            for b in bytes_from_file(fp, width//2):
                row += ([b]*2)
            V += (row*2)

        # for r in range(height):
        #     for c in range(width):
        #         Y.append(ord(f_y.read(1)))

        # # U with supersampling
        # for r in range(height//2):
        #     row = []
        #     for c in range(width//2):
        #         row += ([ord(f_uv.read(1))]*2)
        #     U += (row*2)

        # # V with supersampling
        # for r in range(height//2):
        #     row = []
        #     for c in range(width//2):
        #         row += ([ord(f_uv.read(1))]*2)
        #     V += (row*2)


        # frame_i += 1
        # if  f_y is None or f_uv is None:
        #     break

    return (Y, U, V)


def fill(image, color):
    width  = image.width()
    height = image.height()
    code = ''
    for r in range(height):
        rowcode=''
        for c in range(width):
            hexcode='#{:02x}{:02x}{:02x} '.format(color[r*width+c][0], color[r*width+c][1], color[r*width+c][2])
            rowcode+=hexcode
        code += '{' + rowcode + '} '
    image.put(code)

def yuv2rgb (y, u, v):
    b = int(numpy.clip(1.164 * (y-16) + 2.018 * (u - 128), 0, 255))
    g = int(numpy.clip(1.164 * (y-16) - 0.813 * (v - 128) - 0.391 * (u - 128), 0, 255))
    r = int(numpy.clip(1.164 * (y-16) + 1.596 * (v - 128), 0, 255))
    return (r, g, b)

def main():
    yuv_file_name = sys.argv[1]
    yuv_width = int(sys.argv[2])
    yuv_height = int(sys.argv[3])

    (Y, U, V) = read_yuv(yuv_file_name, yuv_width, yuv_height)

# print(len(Y))

#b = list(map(lambda y, u: int(1.164 * (y-16) + 2.018 * (u - 128)), Y, U))
#b = [int(1.164 * (y-16) + 2.018 * (u - 128)) for y, u, v in zip(Y, U, V)]
#g = [int(1.164 * (y-16) - 0.813 * (v - 128) - 0.391 * (u - 128))
#     for y, u, v in zip(Y, U, V)]
#r = [int(1.164 * (y-16) + 1.596 * (v - 128)) for y, u, v in zip(Y, U, V)]
#rgb_bitmap = list(zip(r,g,b))

    rgb_bitmap = [yuv2rgb(y, u, v) for y, u, v in zip(Y, U, V)]

    root=Tk()

#label = ttk.Label(root, text="Hello, Tkinter!")
#label.pack()

# photoimage
    picture=PhotoImage(width=yuv_width, height=yuv_height)
    fill(picture, rgb_bitmap)
    #picture=picture.zoom(2, 2)

# canvas
    canvas = Canvas(root,
                    width=yuv_width+20,
                    height=yuv_height+20)
    canvas.pack()
    canvas.create_image(10, 10, anchor=NW, image=picture)

    # label = Label(root,
    #               image=picture,
    #               padx=10)
    # label.grid()

# menu
    menu = Menu(root)
    filemenu=Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open...", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)



    root.config(menu=menu)
    root.mainloop()

if __name__ == "__main__":
    main()
