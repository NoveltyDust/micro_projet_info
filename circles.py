
# On importe les modules
from math import sqrt
from fonctions_rectangle import repere


def check_intersections(a):
    """
    Renvoie une liste de tuple contenant les coordonnées des points d'intersection des 2 cercles basé sur le côté maximal du rectangle.

    entree : long:int, larg:int
    sortie : intersections:list
    """
    
    # On définit la liste pour les intersections
    intersections = []
    
    # Boucle de la fonction
    for i in range(1,a+1):
        for j in range(1,a+1):
            
            # On définit les coordonnées de cercles
            xm = (i*i - j*j + a*a) / (2 * a)
            ymcar = i*i-xm*xm
            
            if ymcar > 0:
                
                ym = sqrt(ymcar)
                
                if a!=0:
                    
                    intersections.append((xm, ym))
                    
                else:
                    
                    intersections.append((xm,-ym))
    
    # On retourne la liste                         
    return intersections


def verif_inter_3_4(intersections, a, b):
    """
    Renvoie un tuple contenant le point d'intersection des 4 cercles.
    
    entrée : intersections:list, rect:tuple
    sortie : point_inter:list
    """
    
    # On définit les valeurs nécessaires
    co = repere(b, a)
    C, D = co[2], co[3]
    x_c ,y_c = C    
    x_d, y_d = D
    rect = sorted(rect, reverse=True)
    point_inter = []
    
    # Boucle de la fonction
    for xm, ym in intersections:
        for i in range (1,max(a,b)) :
            for j in range (1,max(a,b)):
                if (abs((xm- x_c) * (xm- x_c) + (ym- y_c) * (ym- y_c) - i*i) < (10 **-9)) and (abs((xm- x_d) * (xm- x_d) + (ym- y_d) * (ym- y_d) - j*j) <(10 **-9)) and (0<ym<b) and (0<xm<a):
                    point_inter.append((xm,ym))

    return point_inter # On retourne la liste des points
 

def trace_rectangle_et_cercles(a, b):
    """
    Trace un rectangle de longueur b et de largeur a, les cercles centrées sur ses sommets,
    avec des rayons allant de 1 à a, et affiche les intersections.
    
    entree : a:int, b:int
    """
    
    import matplotlib.pyplot as plt
    co = repere(b, a)
    
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
    intersections = check_intersections(b)
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
