import AST
from AST import addToClass
from functools import reduce
import myObjects as obj

operations = {
'+':lambda x,y:x+y,
'-':lambda x,y:x-y,
'*':lambda x,y:x*y,
'/':lambda x,y:x/y,}

stack = []
vars={}

@addToClass(AST.ProgramNode)
def execute(self):
    for c in self.children:
        c.execute()

@addToClass(AST.TokenNode)
def execute(self):
    if isinstance(self.tok, str):
        try:
            return vars[self.tok]
        except KeyError:
            print("*** Error: variable %s undefined! " % self.tok)
    return self.tok

@addToClass(AST.OpNode)
def execute(self):
    args = [c.execute() for c in self.children]
    if len(args) == 1:
        args.insert(0,0)
    return reduce(operations[self.op], args)

@addToClass(AST.AssignNode)
def execute(self):
    vars[self.children[0].tok] = self.children[1].execute()

@addToClass(AST.FigureNode)
def execute(self):
    print (self.figure + "(" + str(self.x) + "," + str(self.y) + ")")

@addToClass(AST.PrintNode)
def execute(self):
    print (self.children[0].execute())

@addToClass(AST.WhileNode)
def execute(self):
    while(self.children[0].execute() != 0):
        self.children[1].execute()

@addToClass(AST.RGBNode)
def execute(self):
    args = [c.execute() for c in self.children]
    color = obj.Couleur(args[0], args[1], args[2])
    return color

@addToClass(AST.ColorNode)
def execute(self):
    if self.color == "Rouge":
        color = obj.Couleur(255, 0, 0)
    elif self.color == "Noir":
        color = obj.Couleur(255, 255, 255)
    else:
        color = obj.Couleur(0, 0, 0)
    return color

@addToClass(AST.PinceauNode)
def execute(self):
    args = [c.execute() for c in self.children]
    pinceau = obj.Pinceau(args[0], args[1], args[2])
    return pinceau

@addToClass(AST.FigureNode)
def execute(self):
    args = [c.execute() for c in self.children]
    if self.figure == "Cercle":
        if len(args) > 4:
            fig = obj.Cercle(args[0], args[1], args[2], args[3], args[4])
        else:
            fig = obj.Cercle(args[0], args[1], args[2], args[3])
    elif self.figure == "Rectangle":
        if len(args) > 4:
            fig = obj.Rectangle(args[0], args[1], args[2], args[3], args[4])
        else:
            fig = obj.Rectangle(args[0], args[1], args[2], args[3])
    print(fig)

if __name__ == "__main__" :
    from parser5 import parse
    import sys
    prog = open(sys.argv[1]).read()
    ast = parse(prog)

    ast.execute()