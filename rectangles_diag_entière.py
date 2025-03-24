from math import sqrt


def liste_rect(N):
    """Renvoie une liste de tuple contenant les dimensions d'un rectangle de cotes entiers <= N et de diagonales entieres.
    entree: N(int)
    sortie: rect(list)"""
    rect = []  
    for a in range(1,N):
        for b in range(a,N+1):
            e = sqrt(a**2+b**2)
            if int(e)==e :
                rect.append((a,b))
    return rect
