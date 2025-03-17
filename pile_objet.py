class Pile(object):
    def __init__(self):
        # Initialisation d'une liste vide
        self.L = []

    def vide(self):
        return self.L == []

    def depiler(self):
        assert not self.vide(), "Vous ne pouvez pas dépiler une pile vide"
        return self.L.pop()

    def empiler(self, x):
        self.L.append(x)
    
    def taille(self):
        return len(self.L)

    def sommet(self):
        assert not self.vide(), "La pile est vide, pas de sommet"
        return self.L[-1]

