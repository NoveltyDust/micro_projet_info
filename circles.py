from math import sqrt
import matplotlib.pyplot as plt
from fonction_repere import test_repere,afficher_quadrilatere_fix
from fonction_diagonale import diagonale

def check_intersections(poly):
    a = max(poly)
    intersections = []
    for i in range((2*a)+1):
        for j in range((2*a)+1):
            xm = (i**2 - j**2 + a**2) / (2 * a)
            ymcar = i**2-xm**2
            if ymcar >= 0:
                ym = sqrt(ymcar)
                intersections.append((xm,ym))
    return intersections

def view_inter(inter, poly):
    afficher_quadrilatere_fix(poly)
    fig, ax = plt.subplots()
    l = max(poly)
    a=(0,0)
    b=(l,0)
    plt.plot([a[0],b[0]],[a[1],b[1]],color="red")
    plt.scatter(*zip(*inter),color="g")
    for i in range(1,(2*l)+1):
        A = plt.Circle(a,i,color="b",fill=False)
        B = plt.Circle(b,i,color='b',fill=False)
        plt.gca().add_patch(A)
        plt.gca().add_patch(B)
    plt.grid()
    plt.show()

def compare(poly):
    coords = test_repere(poly)
    intersect = check_intersections(poly)
    for coord in coords:
        for inter in intersect:
            print(inter,coord[2],coord[3])
            if inter==coord[2] or inter==coord[3]:
                print("appartient auc cercles")

poly = (5,5,6,4)
inter = check_intersections(poly)
view_inter(inter,poly)
plt.show()