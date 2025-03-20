
import math

def est_carré_parfait(n):
    """Vérifie si n est un carré parfait"""
    racine = int(math.sqrt(n))
    return racine * racine == n

def rectangles_diag_entière(N):
    liste_rect = []
    
    for a in range(1, N):
        for b in range(a, N):  # On prend b ≥ a pour éviter les doublons
            if est_carré_parfait(a * a + b * b):  # Vérifie si la diagonale est entière
                liste_rect.append((a, b, a, b))  

    return liste_rect

print(rectangles_diag_entière(200))
