from math import sqrt

def diagonale(poly):
    """Calcule la longueur des diagonales d'un rectangle 
    Entrée: tuple (a, b, a, b)
    Sortie: e (int)
    """
    a = poly[0]
    b = poly[1]
    e = sqrt(a*a + b*b)
    if type(e) == int:
        return e
    return None

    

