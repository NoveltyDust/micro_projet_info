"""Fonction repere : détermine les coordonnées des sommets d'un rectangle ABCD
petit dessin :  D_____a______C
              b |            |b
                A_____a______B
"""

from math import sqrt
from fonction_diagonale import diagonale

def repere(polygone, e):
    """renvoie une liste contenant les coordonnées de chaque sommet d'un quadrilatere
    entree : polygone(tuple), e(int)
    sortie : coordonnes(tuple)"""
    a, b = polygone
    A = (0, 0)  
    B = (a, 0)        
    C = (a, b)     
    D = (0, b)
    return (A, B, C, D)
    


"""
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
    quadrilatere = [A, B, C, D, A]  # Fermer le quadrilatère

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
    plt.title("Quadrilatère Fixe")"""