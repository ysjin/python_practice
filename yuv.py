#!/usr/bin/python3

import mmap
import itertools

class yuv:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wh = width*height
        self.size = int(self.wh * 1.5)
        pass

    def open(self, filename):
        with open(filename, 'rb') as f:
            self.frame_n = 0
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
                for frame in zip(*[iter(m)]*self.size):
                    for y in itertools.islice(frame, self.size):
                        self.Y.append(y)
                        pass
                    for u in itertools.islice(frame, self.size, self.size+self.size//4):
                        self.U.append(u)
                        pass
                    for v in itertools.islice(frame, self.size, self.size+self.size//4):
                        self.V.append(u)
                        pass
                    self.frame_n += 1

    # return i-th frame
    def get_rgb(self, frame_i):
        return # fram

    def grouper(iterable, n):
        return zip(*[iter(iterable)]*n)


