

def polygone(N):
    liste_poly = []
    n=0
    for a in range(1,N):  
        for b in range(a, N):  
            for c in range(b, N):  
                for d in range(c, N):
                    if a + b + c > d:
                        liste_poly.append((a, b, c, d))
                        n=n+1
                        if a !=b and c != d :
                            liste_poly.append((a, b, d, c))
                            n=n+1
                        if b != c :
                            liste_poly.append((a, b, d, c)) 
                            n=n+1
    return(liste_poly)
    
N=5

#list=polygone()
poly = (17,1,78,98)

def verif(L,poly): 
    if poly in L:
        print("Trouvé !")
    else:
        print("Pas trouvé.")

#verif(list,poly)
#print(len(list))
