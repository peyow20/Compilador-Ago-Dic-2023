import ply.lex as lex


#Defino mis palabras reservadas
reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'print': 'PRINT',
    'arr' : 'ARR',
    'func' : 'FUNC',
    'void' : 'VOID',
    'to' : 'TO',
    'do' : 'DO',
    'return' : 'RETURN',
    'main' : 'MAIN',
    'arr' : 'ARR',
}

#Defino mis tokens
tokens = ['PROGRAM', 'VAR', 'INT', 'FLOAT', 'CHAR', 'CTEI', 'CTEF', 'CTESTRING', 'CTEC', 
          'ID', 'IF', 'ELSE', 'WHILE', 'MAYOR', 'FOR', 'MENOR', 'DIFF', 'MAS', 'MENOS', 'POR', 'DIV', 'MOD',
          'LLAVIZQ', 'VOID', 'LLAVDER', 'PARIZQ', 'PARDER', 'CORCHIZQ', 'CORCHDER', 'DOSPUN', 'PUNCOM', 
          'COMA', 'IGUAL', 'PRINT', 'AND', 'OR', 'ARR', 'TO', 'DO', 'RETURN', 'MAIN', 'FUNC']


t_ignore = " \t"


#Defino mis expresiones regulares que su simbolo o manera de usar varia
def t_ID(t):
    r'[A-za-z]+'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTEF(t):
    r'[0-9]*\.[0-9]+|[0-9]+'
    t.value = float(t.value)
    return t

def t_CTEC(t):
    r"'[a-zA-Z0-9]'"
    t.value = t.value[1]
    return t

def t_CTESTRING(t):
    r'\".*\"'
    return t

#Defino las expresiones regulares para los tokens que son sencillos

def t_AND(t):
    r'\&\&'
    return t

def t_OR(t):
    r'\|\|'
    return t

def t_MAYOR(t):
    r'\>'
    return t


def t_MENOR(t):
    r'\<'
    return t

def t_IGUAL(t):
    r'\='
    return t

def t_ARR(t):
    r'ARR'
    return t

def t_DIFF(t):
    r'\!'
    return t

def t_LLAVIZQ(t):
    r'\{'
    return t

def t_LLAVDER(t):
    r'\}'
    return t

def t_MAS(t):
    r'\+'
    return t

def t_MENOS(t):
    r'\-'
    return t

def t_POR(t):
    r'\*'
    return t

def t_DIV(t):
    r'\/'
    return t

def t_MOD(t):
    r'\%'
    return t

def t_PARIZQ(t):
    r'\('
    return t

def t_PARDER(t):
    r'\)'
    return t

def t_CORCHIZQ(t):
    r'\['
    return t

def t_CORCHDER(t):
    r'\]'
    return t

def t_PUNCOM(t):
    r'\;'
    return t

def t_DOSPUN(t):
    r'\:'
    return t

def t_COMA(t):
    r'\,'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_comment(t):
    r'\//.*'
    pass

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Con esto construyo mi lexico
lex.lex()