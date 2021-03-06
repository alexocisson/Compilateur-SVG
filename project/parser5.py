import ply.yacc as yacc

from lex5 import tokens
import AST

vars = {}

def p_programme_statement(p):
    ''' programme : statement '''
    p[0] = AST.ProgramNode(p[1])

def p_programme_recursive(p):
    ''' programme : statement ';' programme '''
    p[0] = AST.ProgramNode([p[1]]+p[3].children)

def p_statement(p):
    ''' statement : assignation
        | structure 
        | figure'''
    p[0] = p[1]

def p_pinceau(p):
    ''' pinceau : PINCEAU '(' parametreCouleur ',' parametreCouleur ',' expression ')' '''
    p[0] = AST.PinceauNode([p[3], p[5], p[7]])

def p_figure(p):
    ''' figure : FIGURE '(' expression ',' expression ',' expression ',' expression ')' '''
    p[0] = AST.FigureNode(p[1], [p[3], p[5], p[7], p[9]])

def p_figure_couleur(p):
    ''' figure : FIGURE '(' expression ',' expression ',' expression ',' expression ',' parametrePinceau ')' '''
    p[0] = AST.FigureNode(p[1], [p[3], p[5], p[7], p[9], p[11]])

def p_couleur(p):
    ''' couleur : COULEUR 
        | '[' expression ',' expression ',' expression ']' '''
    if len(p)==2:
        p[0] = AST.ColorNode(p[1])
    else:
        p[0] = AST.RGBNode([p[2], p[4], p[6]])


def p_parametre(p):
    ''' parametre : NUMBER
        | IDENTIFIER
        | expression'''
    p[0] = AST.TokenNode(p[1])


def p_parametre_couleur(p):
    ''' parametreCouleur : parametre
        | couleur'''
    p[0] = p[1]

def p_parametre_pinceau(p):
    ''' parametrePinceau : parametre
        | pinceau'''
    p[0] = p[1]
    	
def p_statement_print(p):
    ''' statement : PRINT expression '''
    p[0] = AST.PrintNode(p[2])

def p_structure(p):
    ''' structure : WHILE expression '{' programme '}' '''
    p[0] = AST.WhileNode([p[2],p[4]])

def p_expression_op(p):
    '''expression : expression ADD_OP expression
            | expression MUL_OP expression'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])
    	
def p_expression_num_or_var(p):
    '''expression : NUMBER
        | IDENTIFIER '''
    p[0] = AST.TokenNode(p[1])
    	
def p_expression_paren(p):
    '''expression : '(' expression ')' '''
    p[0] = p[2]
    	
def p_minus(p):
    ''' expression : ADD_OP expression %prec UMINUS'''
    p[0] = AST.OpNode(p[1], [p[2]])
    	
def p_assign(p):
    ''' assignation : IDENTIFIER '=' expression 
        | IDENTIFIER '=' couleur
        | IDENTIFIER '=' pinceau'''
    p[0] = AST.AssignNode([AST.TokenNode(p[1]),p[3]])

def p_error(p):
    if p:
        print ("Syntax error in line %d" % p.lineno)
        yacc.errok()
    else:
        print ("Sytax error: unexpected end of file!")


precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('right', 'UMINUS'),  
)

def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys 
    	
    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    if result:
        print (result)
            
        import os
        os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
        graph = result.makegraphicaltree()
        name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
        graph.write_pdf(name) 
        print ("wrote ast to", name)
    else:
        print ("Parsing returned no result!")