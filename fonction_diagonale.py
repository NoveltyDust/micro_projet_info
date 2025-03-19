from math import sqrt

def diagonale(poly):
    """Calcule la longueur des diagonales d'un quadrilatère en ne gardant que celles donnant une aire entière.
    
    Entrée: tuple (a, b, c, d)
    Sortie: liste de tuples [(e, f), ...]
    """
    a, b, c, d = poly
    liste_ef = []
    e = abs(b - a)

    while e < min(a + b, c + d):
        p1 = (a + b + e) / 2  
        p2 = (c + d + e) / 2  

        try:
            # Vérifier que l'expression sous la racine n'est pas négative avant d'appeler sqrt()
            aire_abe_sq = p1 * (p1 - a) * (p1 - b) * (p1 - e)
            aire_cde_sq = p2 * (p2 - c) * (p2 - d) * (p2 - e)

            if aire_abe_sq > 0 and aire_cde_sq > 0:
                aire_abe = sqrt(aire_abe_sq)
                aire_cde = sqrt(aire_cde_sq)
                aire_abcd = aire_abe + aire_cde

                # Vérification de l'aire : doit être proche d'un entier
                if abs(aire_abcd - round(aire_abcd)) < 0.01:
                    f_sq = 16 * aire_abcd**2 + (b**2 + d**2 - a**2 - c**2)**2
                    if f_sq >= 0:  
                        f = sqrt(f_sq) / (2 * e)
                        if abs(d - c) < f < min(a + d, b + c):
                            liste_ef.append((e, f))
        except ValueError:
            pass  # Éviter l'erreur si la racine carrée est négative
        
        e += 0.1 
    return liste_ef

