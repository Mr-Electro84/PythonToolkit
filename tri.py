
def minimum(tab):
    '''fontion qui charche le minimum d'un tableau
    compris entre la fonction renverra l'indice du mini'''
    mini = tab[0]
    index_min = 0
    for i in range(1, len(tab)) :
        if tab[i] < mini :
            mini = tab[i]
            index_min = i
    return index_min, mini

def echange(tab, x, y):
    '''fonction qui échange les valeurs
    d'un tableau situées aux indices x et y'''
    temp_ech = tab[x]
    tab[x] = tab[y]
    tab[y] = temp_ech
    return tab

#tests :
#faire afficher l'indice du minimum de L
#faire afficher l'indice du minimum de L en ignorant les 2 premières valeurs de L

def tri_selec_croissant(L):
    N = len(L)
    for i in range(0, N-1): # N-1 est exclue, donc arret à N-2
        min = i
        for j in range(i+1, N): # N est exclue, donc arret à N-1
            if L[j] < L[min]:
                min = j
        tmp = L[min]
        L[min] = L[i]
        L[i] = tmp
    return L

def tri_selec_decroissant(L):
    N = len(L)
    for i in range(0, N-1): # N-1 est exclue, donc arret à N-2
        max = i
        for j in range(i+1, N): # N est exclue, donc arret à N-1
            if L[j] > L[max]:
                max = j
        tmp = L[max]
        L[max] = L[i]
        L[i] = tmp
    return L

def tri_inser(L):
    N = len(L)
    for i in range(1, N): #N est exclu donc atter à N-1
        tmp = L[i]
        j = i
        while j > 0 and L[j-1] > tmp :
            L[j] = L[j-1] #on fait reculer la valeur
            j = j-1 #on passe à l'indice précedent
        L[j] = tmp
    return L

CPS = [5, 8, 4, 28, 47, 11, 0, 20.1, 444, 5, -888]
CPSA = tri_inser(CPS)
print(CPSA)



##CPS = [5, 8, 4, 28, 47, 11, 0, 20.1, 444, 5, -888]
##CPSA = tri_selec_decroissant(CPS)
##print(CPSA)
