def verif_une_sol (e):
    """fonction qui verifie si un rectangle admet au moins un arbre entier(diagonale paire ou non)
    entrée: e(int) -> diagonale du rectangle
    sortie: booleen """
    if e % 2 == 0:
        return True
    return False
