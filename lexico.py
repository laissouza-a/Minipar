import ply.lex as lex

# Lista de tokens da linguagem MiniPar
tokens = [
    'SEQ', 'PAR', 'IF', 'ELSE', 'WHILE', 'INPUT', 'OUTPUT',
    'SEND', 'RECEIVE',
    'ID', 'INT', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'COMMA', 'EQUALS', 'LESS_THAN', 'GREATER_THAN', 
    'LESS_THAN_EQUALS', 'GREATER_THAN_EQUALS', 
    'EQUALS_EQUALS', 'NOT_EQUALS', 'C_CHANNEL', 'DOT',
    'AND', 'OR','SEMICOLON' 
]

# Regras de expressões regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_EQUALS = r'='
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_LESS_THAN_EQUALS = r'<='
t_GREATER_THAN_EQUALS = r'>='
t_EQUALS_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_DOT = r'\.'
t_AND = r'&&'
t_OR = r'\|\|'
t_SEMICOLON = r';'


# Palavras reservadas
reserved = {
    'SEQ': 'SEQ', 'PAR': 'PAR', 'if': 'IF', 'else': 'ELSE', 
    'while': 'WHILE', 'Input': 'INPUT', 'Output': 'OUTPUT',
    'send': 'SEND', 'receive': 'RECEIVE', 'c_channel': 'C_CHANNEL'
}

# Token ID com verificação de palavras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é palavra reservada
    return t

# Token para inteiros
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Token para strings
def t_STRING(t):
    r'"[^"\n]*"|\'[^\']*\''
    t.value = t.value[1:-1]  # Remove as aspas
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t\n\r'

# Regra para ignorar comentários
def t_COMMENT(t):
    r'\#.*\n?'
    pass 

# Tratamento de erros
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

# Constrói o analisador léxico
lexer = lex.lex()
