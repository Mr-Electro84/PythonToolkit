def file():
    return []

def vide(f):
    return f==[]

def enfiler(f, x):
    return f.append(x)

def defiler(f):
    assert not vide(f), "Vous ne pouvez pas défiler une file vide"
    return f.pop(0)

def taille(f):
    return len(f)

def sommet(f):
    return f[0]

def queue(f):
    return f[-1]

def est_present(f, x):
    return x in f