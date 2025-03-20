"""Fonction repere : détermine les coordonnées des sommets d'un rectangle ABCD
petit dessin :  D_____a______C
              b |            |b
                A_____a______B
"""

from math import sqrt
from fonction_diagonale import diagonale

def repere(polygone):
    """renvoie une liste contenant les coordonnées de chaque sommet d'un quadrilatere
    entree : polygone(tuple), e(int)
    sortie : coordonnes(tuple)"""
    polygone = sorted(polygone, reverse=True)
    a, b = polygone
    A = (0, 0)  
    B = (a, 0)        
    C = (a, b)     
    D = (0, b)
    return (A, B, C, D)
    


