# Librares
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

rhol = 1
vl = 0
pl = 1
rhor = 3
vr = 0
pr = 3

xmax = 1.0
xmin = 0
t = 1.0

def minmod(a, b):
    if abs(a) < abs(b) and a*b > 0.0:
        return a
    elif abs(b) < abs(a) and a*b > 0.0:
        return b
    else:
        return 0.0

class gydra:
    def __init__(self, xmin, xmax, t):
        self.Nx = 10
        self.xmin = xmin
        self.xmax = xmax
        self.t = t
        self.x = np.zeros(self.Nx)

    def Init(self):
        dx = (self.xmax - self.xmin) / (self.Nx)

        i = 0
        while i < self.Nx:
            self.x[i] = self.xmin + dx * i

            i += 1


    def View(self, a):
        print(a)

g = gydra(xmin, xmax, t)

g.Init()
g.View(g.x)
