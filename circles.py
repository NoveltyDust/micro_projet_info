from math import sqrt
from fonction_repere import repere


def check_intersections(long, larg):
    """Renvoie une liste de tuple contenant les coordonnes des points d'intersection des 2 cercles
    dont les origines sont : (0,0) et (a,0), a est la longueur du rectangle. (Rayon variable)
    entree: long(int), larg(int)
    sortie : intersections (list)"""
    a = max(long,larg)
    intersections = []
    for i in range(1,a+1):
        for j in range(1,a+1):
            xm = (i*i - j*j + a*a) / (2 * a)
            ymcar = i*i-xm*xm
            if ymcar > 0:
                ym = sqrt(ymcar)
                if larg!=0:
                    intersections.append((xm, ym))
                else:
                    intersections.append((xm,-ym))
    #print (intersections)                
    return intersections


def verif_inter_3_4(intersections, rect):
    """Renvoie un tuple contenant le point d'inetrsection des 4 cercles
    entrée : intersections(list), rect(tuple)
    sortie: point_inter (list) """
    co = repere(rect)
    C, D = co[2], co[3]
    x_c ,y_c = C    
    x_d, y_d = D
    rect = sorted(rect, reverse=True)
    a , b = rect
    point_inter = []
    for xm, ym in intersections:
        for i in range (1,max(a,b)) :
            for j in range (1,max(a,b)):
                if (abs((xm- x_c) * (xm- x_c) + (ym- y_c) * (ym- y_c) - i*i) < (10 **-9)) and (abs((xm- x_d) * (xm- x_d) + (ym- y_d) * (ym- y_d) - j*j) <(10 **-9)) and (0<ym<b) and (0<xm<a):
                    point_inter.append((xm,ym))
    #print ("inter cercles (rect :",rect,"):",point_inter)
    return point_inter
 

def trace_rectangle_et_cercles(a, b):
    
    #Trace un rectangle de dimensions a x b, les cercles centrés sur ses sommets,
    #avec des rayons allant de 1 à a, et affiche les intersections.
    
    import matplotlib.pyplot as plt
    rect = (a, b)
    co = repere(rect)
    
    # Création de la figure
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Tracer le rectangle
    rectangle_x = [co[0][0], co[1][0], co[2][0], co[3][0], co[0][0]]
    rectangle_y = [co[0][1], co[1][1], co[2][1], co[3][1], co[0][1]]
    ax.plot(rectangle_x, rectangle_y, 'k-', label='Rectangle')
    
    # Tracer les cercles pour chaque sommet avec des rayons de 1 à a
    for (x, y) in co:
        for r in range(1, max(a + 1,b+1)):
            cercle = plt.Circle((x, y), r, color='b', fill=False, alpha=0.3)
            ax.add_patch(cercle)
    
    # Rechercher les intersections des cercles
    intersections = check_intersections(a,b)
    intersection = verif_inter_3_4(intersections, rect)
    
    # Tracer les intersections
    if intersection:
        for i in range (len(intersection)):
            ax.plot(intersection[i][0], intersection[i][1], 'ro', label='Intersection')
    
    # Réglages de l'affichage
    ax.set_ylim(-a, a + a)
    ax.set_xlim(-b, b + b)
    ax.set_aspect('equal')
    plt.legend()
    plt.title("Rectangle, Cercles et Intersections")
    plt.grid()
    plt.show()
