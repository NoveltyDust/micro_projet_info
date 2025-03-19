from math import sqrt

def pointin(M, quadri, e, f):
    x, y = M
    a, b, c, d = quadri

    if x < 0:
        return False

    s = (d * d - e * e + c * c) / (2 * d)
    t = sqrt(c * c - ((d * d - e * e + c * c) ** 2) / (4 * d * d))

    if (t / s) * x < y:
        return False

    u = (d * d - a * a + f * f) / (2 * d)
    v = sqrt(f * f - ((d * d - a * a + f * f) ** 2) / (4 * d * d))

    if v * (x - d) / (u - d) < y:
        return False

    if (t - (v * s - u * t) / (s - u)) * (x / s) + (v * s - u * t) / (s - u) < y:
        return False

    return True


inter= [(1.0, 0.0), (2.0, 0.0), (1.25, 1.5612494995995996), (3.0, 0.0), (2.4166666666666665, 1.7775607506417954), (1.6666666666666667, 2.494438257849294), (4.0, 0.0), (3.5833333333333335, 1.777560750641795), (3.0, 2.6457513110645907), (2.25, 3.307189138830738), (5.0, 0.0), (4.75, 1.5612494995995996), (4.333333333333333, 2.494438257849295), (3.75, 3.307189138830738), (3.0, 4.0)]
point_val=[]

for tuples in inter : 
    if pointin(tuples,(5, 3, 4, 6),2.2, 3.746079520128148): 
        point_val.append(tuples)
print("Les points valides sont : ",point_val)

