def pile():
    # retourne une liste vide
    return []

def vide(p):
    # renvoie True si la pile est vide
    # et False sinon
    return p == []

def empiler(p, x):
    # Ajoute l'émément vide à la pile P
    p.append(x)

def depiler(p):
    # assert puis test booléen cansé être vrai, "message d'erreur"
    assert not vide(p), "Vous ne pouvez pas depiler une liste vide"
    return p.pop()

def taille(p):
    return len(p)

def sommet(p):
    assert not vide(p), "La liste est vide, pas de sommet"
    return p[-1]