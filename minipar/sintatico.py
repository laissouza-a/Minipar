import ply.yacc as yacc
from lexico import tokens

# Precedência dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Regras gramaticais
def p_program(p):
    '''program : stmts'''
    p[0] = ('PROGRAM', p[1])

def p_stmts(p):
    '''stmts : stmt
             | stmts stmt'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_stmt(p):
    '''stmt : bloco_SEQ
            | bloco_PAR
            | atribuicao
            | bloco_IF
            | bloco_WHILE'''
    p[0] = p[1]

def p_bloco_SEQ(p):
    '''bloco_SEQ : SEQ LBRACE stmts RBRACE'''
    p[0] = ('SEQ', p[3])

def p_bloco_PAR(p):
    '''bloco_PAR : PAR LBRACE stmts RBRACE'''
    p[0] = ('PAR', p[3])

def p_atribuicao(p):
    '''atribuicao : ID EQUALS expr'''
    p[0] = ('ATRIB', p[1], p[3])

def p_expr(p):
    '''expr : INT
            | ID
            | expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_error(p):
    print(f"Erro de sintaxe: {p.value if p else 'EOF inesperado'}")

# Constrói o parser
parser = yacc.yacc()
