

def polygone(N):
    liste_poly = []
    for a in range(1,N):  
        for b in range(a, N):  
            for c in range(b, N):  
                for d in range(c, N):
                    if a + b + c > d:
                        liste_poly.append((a, b, c, d))
                        if a !=b and c != d :
                            liste_poly.append((a, b, d, c))
                        if b != c :
                            liste_poly.append((a, b, d, c))                         

    return(liste_poly)

list=polygone()
poly = (17,1,78,98)

def verif(L,poly): 
    if poly in L:
        print("Trouvé !")
    else:
        print("Pas trouvé.")

verif(list,poly)
print(len(list))