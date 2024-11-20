import ply.yacc as yacc
from lexico import tokens

# Precedência dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'EQUALS_EQUALS', 'NOT_EQUALS', 'LESS_THAN', 'GREATER_THAN', 
     'LESS_THAN_EQUALS', 'GREATER_THAN_EQUALS'),
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
            | bloco_WHILE
            | input_stmt
            | output_stmt
            | send_stmt
            | receive_stmt'''
    p[0] = p[1]

def p_bloco_SEQ(p):
    '''bloco_SEQ : SEQ LBRACE stmts RBRACE SEMICOLON'''
    p[0] = ('SEQ', p[3])

def p_bloco_PAR(p):
    '''bloco_PAR : PAR LBRACE stmts RBRACE SEMICOLON'''
    p[0] = ('PAR', p[3])

def p_atribuicao(p):
    '''atribuicao : ID EQUALS expr SEMICOLON'''
    p[0] = ('ATRIB', p[1], p[3])

def p_bloco_IF(p):
    '''bloco_IF : IF LPAREN expr RPAREN LBRACE stmts RBRACE
                | IF LPAREN expr RPAREN LBRACE stmts RBRACE ELSE LBRACE stmts RBRACE SEMICOLON'''
    if len(p) == 8:  # Sem ELSE
        p[0] = ('IF', p[3], p[6])
    else:  # Com ELSE
        p[0] = ('IF', p[3], p[6], p[10])

def p_bloco_WHILE(p):
    '''bloco_WHILE : WHILE LPAREN expr RPAREN LBRACE stmts RBRACE SEMICOLON'''
    p[0] = ('WHILE', p[3], p[6])

def p_input_stmt(p):
    '''input_stmt : INPUT LPAREN ID RPAREN SEMICOLON'''
    p[0] = ('INPUT', p[3])

def p_output_stmt(p):
    '''output_stmt : OUTPUT LPAREN output_args RPAREN SEMICOLON'''
    p[0] = ('OUTPUT', p[3])

def p_output_args(p):
    '''output_args : expr
                   | STRING
                   | output_args COMMA expr
                   | output_args COMMA STRING'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_send_stmt(p):
    '''send_stmt : SEND LPAREN C_CHANNEL DOT ID COMMA expr RPAREN SEMICOLON'''
    p[0] = ('SEND', (p[3], p[5]), p[7])

def p_receive_stmt(p):
    '''receive_stmt : RECEIVE LPAREN C_CHANNEL DOT ID COMMA ID RPAREN SEMICOLON'''
    p[0] = ('RECEIVE', (p[3], p[5]), p[7])

def p_expr(p):
    '''expr : INT
            | ID
            | expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr EQUALS_EQUALS expr
            | expr NOT_EQUALS expr
            | expr LESS_THAN expr
            | expr GREATER_THAN expr
            | expr LESS_THAN_EQUALS expr
            | expr GREATER_THAN_EQUALS expr'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

def p_error(p):
    print(f"Erro de sintaxe: {p.value if p else 'EOF inesperado'}")

# Constrói o parser
parser = yacc.yacc()
