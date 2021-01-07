class Couleur(object):

    def __init__(self, r=0, g=0, b=0):
        self.r = r%256
        self.g = g%256
        self.b = b%256

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
    
    def getSvg(self):
        return f'<ellipse cx="{self.x}" cy="{self.y}" rx="{self.w}" ry="{self.h}" fill="rgb({self.p.fill.r}, {self.p.fill.g}, {self.p.fill.b})" stroke="rgb({self.p.border.r}, {self.p.border.g}, {self.p.border.b})" stroke-width="{self.p.w}" />'
        

class Rectangle(object):

    def __init__(self, x=0, y=0, w=0, h=0, p=Pinceau()):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.p = p

    def __str__(self):
        return f'Rectangle: x"{self.x}", y"{self.y}", w"{self.w}", h"{self.h}", "{self.p}'
    
    def getSvg(self):
        return f'<rect x="{self.x}" y="{self.y}" width="{self.w}" height="{self.h}" fill="rgb({self.p.fill.r}, {self.p.fill.g}, {self.p.fill.b})" stroke="rgb({self.p.border.r}, {self.p.border.g}, {self.p.border.b})" stroke-width="{self.p.w}" />'