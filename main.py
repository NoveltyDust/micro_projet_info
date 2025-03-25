"""Fichier contenant le code central du projet"""
from rectangles_diag_entière import liste_rect
from circles import verif_inter_3_4, check_intersections
from time import time
from csv_manage import add_rows

def calcul_sol(cote_lim, N,E):
    """Renvoie le nombre de rectangles ( de cotés <= cote_lim et de diagonales entiers) admettant exactement/au moins N arbres entiers.
    entree : cote_lim ,N (int); E(str) : pour indiquer si on veut au moins/exactement N points.
    sortie : chaine de caracteres indiquant le nombre de solution"""
    start=time()
    values = [["Largeur","Longueur","Nombres de points"]]
    assert cote_lim > 1 and type(cote_lim) == int and E in ("exactement", "au moins")
    l_rectangle = liste_rect(cote_lim)
    nbr_solution = 0
    l_solution = []
    if E == "exactement":
        for i in range (len(l_rectangle)):
            a,b = l_rectangle[i][0],l_rectangle[i][1]
            l_solution = verif_inter_3_4(check_intersections(a,b), (a,b))
            values.append([a,b,len(l_solution)])
            if len(l_solution) == N:
                nbr_solution += 1
    else :
        for i in range (len(l_rectangle)):
            a,b = l_rectangle[i][0],l_rectangle[i][1]
            l_solution = verif_inter_3_4(check_intersections(a,b), (a,b))
            values.append([a,b,len(l_solution)])
            if len(l_solution) >= N:
                nbr_solution += 1     
    add_rows(values,"rectangles.csv")               
    print(f"Chronomètre: {time()-start} s")        
    return f"Le nombre de rectangles de côtés entiers inférieurs ou égals à {cote_lim} admettant {E} {N} solution est : {nbr_solution} parmi {len(l_rectangle)} rectangles "       

print(calcul_sol(100,1,"au moins"))
print("\n********************END********************")


