from math import sqrt

def diagonale(poly):
    """fonction qui calcule la longeur des diagonales d'un quadrilatère
    entrée: tuple
    sortie: liste de tuples"""
    a, b, c, d = poly
    liste_ef = []
    e = abs(b-a)
    while e < min(a + b, c + d):
        p1 = (a + b + e) / 2  # Demi-périmètre
        p2 = (c + d + e) / 2  

        try:
            aire_abe = sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - e))
            aire_cde = sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - e))
            aire_abcd = aire_abe + aire_cde

            f = sqrt(16 * aire_abcd**2 + (b**2 + d**2 - a**2 - c**2)**2) / (2 * e)
            
            if 0 < f < min(a + d, b + c):
                liste_ef.append((e, f))
        except ValueError:
            # Gestion des erreurs mathématiques si sqrt reçoit une valeur négative
            continue  

    return liste_ef
