from math import sqrt
import matplotlib.pyplot as plt
from fonction_diagonale import diagonale
import numpy

a = 5
b = 3
c = 4

xa = 0
xb = a
ya = 0
yb = 0
xc = (a**2+c**2-b**2)/(2*a)
yc = sqrt(c**2-xc**2)

def check_intersections(a):
    intersections = []
    for i in range(a):
        for j in range(a):
            xm = (i**2 - j**2 + a**2) / (2 * a)
            ymcar = i**2-xm**2
            if ymcar >= 0:
                ym = sqrt(ymcar)
                intersections.append((xm,ym))
    return intersections


def visualisation(a=tuple,b=tuple,c=tuple,d=tuple):
    plt.clf()
    plt.plot([a[0],b[0]],[a[1],b[1]],linestyle="--",color="red")
    plt.plot([b[0],c[0]],[b[1],c[1]],linestyle="--",color="red")
    plt.plot([c[0],d[0]],[c[1],d[1]],linestyle="--",color="red")
    plt.plot([d[0],a[0]],[d[1],a[1]],linestyle="--",color="red")
    plt.scatter(*zip(a,b,c),color="red")


def belong_to_circles(poly=tuple):
    L = max(poly)
    sides = poly.pop(L)
    diag = diagonale(poly)
    a = (0,0)
    b = (L,0)
    c = (a**2-diag[0]**2)