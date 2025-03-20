from math import sqrt
import matplotlib.pyplot as plt

<<<<<<< HEAD
def check_intersections(cote,y,rotated=False):
    a = cote
=======
def check_intersections(poly):
    a = max(poly)
>>>>>>> a54b841fdb6a8a3bbc1628f43d571f9c73905b48
    intersections = []
    for i in range((2*a)+1):
        for j in range((2*a)+1):
            xm = (i**2 - j**2 + a**2) / (2 * a)
            ymcar = i**2-xm**2
            if ymcar >= 0:
                ym = sqrt(ymcar)
<<<<<<< HEAD
                if rotated:
                    intersections.append((ym+y,xm))
                else:
                    intersections.append((xm,ym+y))
    return intersections

def view_inter(inter, cote,y,rotated=False):
    l = cote
    if rotated:
        a=(y,0)
        b=(y,cote)
    else:
        a=(0,y)
        b=(cote,y)
=======
                intersections.append((xm,ym))
    return intersections

def view_inter(inter, poly):
    afficher_quadrilatere_fix(poly)
    fig, ax = plt.subplots()
    l = max(poly)
    a=(0,0)
    b=(l,0)
>>>>>>> a54b841fdb6a8a3bbc1628f43d571f9c73905b48
    plt.plot([a[0],b[0]],[a[1],b[1]],color="red")
    plt.scatter(*zip(*inter),color="g")
    for i in range(1,(2*l)+1):
        A = plt.Circle(a,i,color="b",fill=False)
        B = plt.Circle(b,i,color='b',fill=False)
        plt.gca().add_patch(A)
        plt.gca().add_patch(B)
    plt.grid()
    plt.show()

<<<<<<< HEAD
poly = (3,4,3,4)
a = poly[0]
b = poly[1]
inter1 = check_intersections(b,0)
view_inter(inter1, b, 0)
=======
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
>>>>>>> a54b841fdb6a8a3bbc1628f43d571f9c73905b48
plt.show()