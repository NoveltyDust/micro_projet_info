from math import sqrt
import matplotlib.pyplot as plt
from fonction_repere import repere
from fonction_diagonale import diagonale

def check_intersections(poly):
    a = max(poly)
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
    plt.scatter(*zip(a,b,c,d),color="red")
    print((d[1]-c[1])/(d[0]-c[0]))
    plt.show()

def view_inter(inter, poly):
    a = max(poly)
    A = (0,0)
    B = (a,0)
    plt.plot([A[0],B[0]],[A[1],B[1]],color="red")
    plt.scatter(*zip(*inter),color="red")
    plt.show()

def compare(poly):
    diag = diagonale(poly)[0]
    a,b,c,d = repere(poly,*diag)
    intersect = check_intersections(poly)
    for inter in intersect:
        print(inter,c,d)
        if c==inter or d==inter:
            print("appartient au cercles")

poly = (1,2,3,4)
compare(poly)