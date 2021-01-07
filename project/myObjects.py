class Couleur(object):

    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f'Couleur : r"{self.r}" g"{self.g}" b"{self.b}"'

class Pinceau(object):

    def __init__(self, border=Couleur(), fill=Couleur(), w=0):
        self.border = border
        self.fill = fill
        self.w = w

    def __str__(self):
        return f'Pinceau: bordure : ("{self.border}"), interieur : ("{self.fill}"), rayon : ("{self.w}")'

class Cercle(object):

    def __init__(self, x=0, y=0, w=0, h=0, p=Pinceau()):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.p = p

    def __str__(self):
        return f'Cercle: x"{self.x}", y"{self.y}", w"{self.w}", h"{self.h}", "{self.p}"'

class Rectangle(object):

    def __init__(self, x=0, y=0, w=0, h=0, p=Pinceau()):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.p = p

    def __str__(self):
        return f'Rectangle: x"{self.x}", y"{self.y}", w"{self.w}", h"{self.h}", "{self.p}'