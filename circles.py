from math import sqrt
import matplotlib.pyplot as plt
from fonction_repere import test_repere,afficher_quadrilatere_fix
from fonction_diagonale import diagonale

def check_intersections(cote,y):
    a = cote
    intersections = []
    for i in range(1,a+1):
        for j in range(1,a+1):
            xm = (i**2 - j**2 + a**2) / (2 * a)
            ymcar = i**2-xm**2
            if ymcar > 0:
                ym = sqrt(ymcar)
                if y!=0:
                    intersections.append((xm,-ym+y))
                else:
                    intersections.append((xm,ym+y))
    return intersections

def view_inter(inter, cote,y):
    l = cote
    a=(0,y)
    b=(cote,y)
    plt.plot([a[0],b[0]],[a[1],b[1]],color="red")
    plt.scatter(*zip(*inter),color="g")
    for i in range(1,l+1):
        A = plt.Circle(a,i,color="b",fill=False)
        B = plt.Circle(b,i,color='b',fill=False)
        plt.gca().add_patch(A)
        plt.gca().add_patch(B)
    plt.grid()

def compare(poly):
    coords = test_repere(poly)
    intersect = check_intersections(poly)
    for coord in coords:
        for inter in intersect:
            print(inter,coord[2],coord[3])
            if inter==coord[2] or inter==coord[3]:
                print("appartient auc cercles")

poly = (5,6,5,6)
A = (0,0)
B = (0,poly[0])
inter = check_intersections(max(poly),A[1])
inter2 = check_intersections(max(poly),B[1])
view_inter(inter,max(poly),A[1])
view_inter(inter2,max(poly),B[1])
plt.show()