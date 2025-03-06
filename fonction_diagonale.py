def diagonale(poly):
    a = poly[0]
    b = poly[1]
    c = poly[2]
    d = poly[3]
    liste_ef = []
    
    for e in range (1, min(a+b,c+d)):
        p1 = a + b + e
        p2 = c + d + e
        aire_abe = sqrt(p1*(p1-a)*(p1-b)*(p1-e))
        aire_cde = sqrt(p2*(p2-c)*(p2-d)*(p2-e))
        aire_abcd = aire_abe +  aire_cde
        f = sqrt(16 * (aire_abcd)**2 +(b**2+d**2-a**2-b**2)**2)/2*e
        if 0 < f < min(a+d,b+c) :
            liste_ef.append((e,f))
    return liste_ef