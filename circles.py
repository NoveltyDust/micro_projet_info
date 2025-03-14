from math import sqrt
import matplotlib.pyplot as plt
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

intersections = []

for i in range(a):
    for j in range(a):
        xm = (i**2 - j**2 + a**2) / (2 * a)
        ymcar = i**2-xm**2
        if ymcar >= 0:
            ym = sqrt(ymcar)
            intersections.append((xm,ym))

plt.clf()
plt.plot([xa,xb],[ya,yb],linestyle="--",color="red")
plt.plot([xa,xc],[ya,yc],linestyle="--",color="red")
plt.plot([xb,xc],[yb,yc],linestyle="--",color="red")
plt.scatter(*zip((xa,ya),(xb,yb)),color="red")
for inter in intersections:
    if inter==(xc,yc):
        plt.scatter(xc,yc,color="green")
plt.show()