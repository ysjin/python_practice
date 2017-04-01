#!/usr/bin/python3
from math import *
import numpy as np

class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

def dct_coef(i,j,N):
    return sqrt ( (1 if i==0 else 2)/N) * cos (pi * (2*j +1)*i/(2*N))
    

def dct_mat(N, scale=128):
    return np.matrix([ [ round(dct_coef(i,j,N)*scale) for j in range(N) ] for i in range (N) ])

def odd_half(M):
    return [ [ M[y,x] for x in range(int(len(M)/2))] for y in range(len(M)) if y%2==1 ]

# dct_mat_butterfly implementation
def dct_mat_bf(I, N, scale=128):
    if N==2:
        return dct_mat(N, scale)
    else:
        A = [ I[] for c in range(N/2)] for r in range 
        #y_even = dct_mat(N/2, scale) * 
        #y_odd  = 

def main():
    A = dct_mat(4)
    print(A)
    At = A.transpose()
    print(At)
    A_odd_half = odd_half(A)
    print(A_odd_half)
    A_HEVC = dct_mat(4, 16384)
    print(A_HEVC)
  
if __name__ == "__main__": main()
