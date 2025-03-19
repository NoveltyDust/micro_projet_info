"""Fonction repere : détermine les coordonnées des sommets d'un quadrilatère ABCD
petit dessin :  C_____b_____D
              c |            |a
                A_____d______B
"""

from math import sqrt
from fonction_diagonale import diagonale

def repere(polygone, e,f):
    """renvoie une liste contenant les coordonnées de chaque sommet d'un quadrilatere
    entree : polygone(tuple), e(float), f(float)
    sortie : coordonnes(list)"""
    polygone = sorted(polygone)
    a, b, c, d = polygone
    A = (0, 0)  
    B = (d,0)  
    
    s = (d*d - e*e + c*c) / (2 * d)  # Correction de la priorité des opérations
    t = sqrt(max(c*c - s*s, 0))  # Correction de la racine carrée

    C = (s, t)  
    
    u = (d*d - a*a + f*f) / (2 * d)  
    v = sqrt(max(f*f - u*u, 0))  

    D = (u, v)
    return (A, B, C, D)
    
def test_repere(polygone):
    l_diagonale = diagonale(polygone)
    coordon = []
    for e, f in l_diagonale:
        coords = repere(polygone, e, f)
        if coords:
            coordon.append(coords)
    return coordon


import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def afficher_quadrilatere_fix(polygone):
    #Affiche un seul quadrilatère en utilisant la première paire (e, f) valide
    l_diagonale = diagonale(polygone)

    if not l_diagonale:
        print("Aucune diagonale valide trouvée.")
        return

    # Prendre la première diagonale trouvée
    e, f = l_diagonale[0]
    coords = repere(polygone, e, f)

    if not coords:
        print("Impossible de calculer les coordonnées.")
        return

    A, B, C, D = coords
    quadrilatere = [A, B, D, C, A]  # Fermer le quadrilatère

    fig, ax = plt.subplots()

    # Dessiner le quadrilatère
    poly = Polygon(quadrilatere, closed=True, edgecolor='b', fill=True, alpha=0.3)
    ax.add_patch(poly)

    # Ajouter les sommets
    for i, (x, y) in enumerate([A, B, C, D]):
        ax.plot(x, y, 'ro')  # Points rouges
        ax.text(x, y, f"{chr(65+i)}", fontsize=12, verticalalignment='bottom', horizontalalignment='right')

    # Ajuster les axes
    ax.set_xlim(-1, max(polygone) + 2)
    ax.set_ylim(-1, max(polygone) + 2)
    ax.set_aspect('equal')

    plt.grid()
    plt.title("Quadrilatère Fixe")