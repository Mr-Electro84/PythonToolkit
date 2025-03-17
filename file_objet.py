class File(object):
    def __init__(self):
        self.L = []
    
    def vide(self):
        return self.L == []

    def enfiler(self, x):
        self.L.append(x)
    
    def defiler(self):
        assert not self.vide(), "Vous ne pouvez pas défiler une liste vide"
        return self.L.pop(0)

    def taille(self):
        return len(self.L)

    def sommet(self):
        assert not self.vide(), "File vide"
        return self.L[0]

    def queue(self):
        assert not self.vide(), "File vide"
        return self.L[-1]

    def present(self, x):
        return x in self.L