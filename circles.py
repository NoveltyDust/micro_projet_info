from math import sqrt
import matplotlib.pyplot as plt

def check_intersections(cote,y,rotated=False):
    a = cote
    intersections = []
    for i in range(1,a+1):
        for j in range(1,a+1):
            xm = (i**2 - j**2 + a**2) / (2 * a)
            ymcar = i**2-xm**2
            if ymcar > 0:
                ym = sqrt(ymcar)
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
    plt.plot([a[0],b[0]],[a[1],b[1]],color="red")
    plt.scatter(*zip(*inter),color="g")
    for i in range(1,l+1):
        A = plt.Circle(a,i,color="b",fill=False)
        B = plt.Circle(b,i,color='b',fill=False)
        plt.gca().add_patch(A)
        plt.gca().add_patch(B)
    plt.grid()

poly = (3,4,3,4)
a = poly[0]
b = poly[1]
inter1 = check_intersections(b,0)
view_inter(inter1, b, 0)
plt.show()