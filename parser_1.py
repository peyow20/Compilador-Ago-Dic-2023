from lexer import tokens
import ply.yacc as yacc
from semantic_cube import SEMANTIC_CUBE


#Direcciones de memoria
global_int = 0
global_float = 100
global_char = 200
local_int = 300
local_float = 400
local_char = 500
constante_int = 600
constante_float = 700
constante_char = 800

    
symbol_table = {}
tipo_var = None


param_table = []

#Estructura para Cuadruplos
cuad = [['','','','']]
pila_tipos = []
pila_operadores = []
pila_operandos = []
pila_saltos = []
cont = 0

#Reglas sintacticas
#Esta es la estructura que debe tener mi codigo
def p_program(p):
    '''program : PROGRAM ID PUNCOM VAR vars acum_func MAIN PARIZQ PARDER bloque'''
    print(symbol_table)
    print(cuad)
    p[0] = "ACC"

def p_funcion(p):
     '''funcion : FUNC TIPO ID PARIZQ TIPO ID PARDER vars bloque'''

def p_acum_func(p):
     '''acum_func : funcion acum_func
                  | empty'''
     
#En las siguiente 4 reglas me ayudan a construir el area de las variables
#tanto como los distintos tipos(en este caso solo int y float) como la cantidad

def p_id_lista(p):
    '''id_lista : ID COMA id_lista
               | ID'''
    if len(p) == 4: 
        p[0] = [p[1]] + p[3]
    else: 
        p[0] = [p[1]]

# Función para manejar la declaración de variables
def handle_vars(p):
    var_type = p[3]
    id_list = p[1]
    if 'vars' not in symbol_table:
        symbol_table['vars'] = {} 
    for var_id in id_list:
        symbol_table['vars'][var_id] = var_type
    p[0] = p[5]

def p_vars(p):
    '''vars : id_lista DOSPUN TIPO PUNCOM vars
            | empty'''
    if len(p) == 6:
        handle_vars(p)
    elif len(p) == 2:
        p[0] = None
    

#Esta regla define los tipos de variables que 
def p_TIPO(p):
    '''TIPO : INT
            | FLOAT
            | CHAR'''
    #Identifico los tipos de variables
    p[0] = p[1]

#def p_arreglo(p):
#    '''arreglo : ARR LLAVIZQ CTEI LLAVDER'''

#Esta regla establece la semantica de un bloque de codigo
def p_bloque(p):
    '''bloque : LLAVIZQ multiples_estatutos LLAVDER'''


#Esta regla define los diferente estatutos y la que le sigue
# me ayuda a poder establecer mas de un estatuto, ya sea varias asignaciones 
# o varias condiciones (if else) 
def p_estatuto(p):
    '''estatuto : asignacion
                 | condicion
                 | escritura
                 | while_condicion
                 | for_condicion'''


def p_multiples_estatutos(p):
    '''multiples_estatutos : estatuto multiples_estatutos
                       | empty'''


#Las 6 sigueintes reglas son para establecer la semantica 
# de los difetenes tipos de estatutos 
def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PUNCOM'''

    #Genero cuadruplo de asignacion
    op_derecho = pila_operandos.pop()
    op_izquierdo = p[1] 
    cuad.append(['=', op_derecho, '', op_izquierdo])
    p[0] = p[3]


def p_escritura(p):
    '''escritura : PRINT PARIZQ print_expresion PARDER PUNCOM'''


def p_print_expresion(p):
    '''print_expresion : expresion multiples_print
                       | CTESTRING multiples_print'''


def p_multiples_print(p):
    '''multiples_print : COMA  print_expresion
                 | empty'''


def p_condicion(p):
    '''condicion : IF PARIZQ expresion PARDER bloque PUNCOM
                 | IF PARIZQ expresion PARDER bloque else_condicion PUNCOM'''


def p_else_condicion(p):
    '''else_condicion : ELSE bloque'''


def p_while_condicion(p):
    ''' while_condicion : WHILE PARIZQ expresion PARDER DO bloque'''


def p_for_condicion(p):
      '''for_condicion : FOR asignacion TO expresion DO bloque'''


def p_expresion_and(p):
    '''expresion : expresion AND expresion'''


def p_expresion_or(p):
    '''expresion : expresion OR expresion'''

#Regla que define la jeraquia de dos expresiones
def p_expresion(p):
    '''expresion : exp 
                 | exp MAYOR exp
                 | exp MENOR exp
                 | exp DIFF exp'''

#Las siguientes dos reglas suman o restan 2 terminos con una llamada recursiva
def p_exp(p):
    '''exp : termino exp_operacion'''
    while pila_operadores and pila_operadores[-1] in ['+', '-']:
        op = pila_operadores.pop()
        gen_cuad(op)
        #Funcion para generar un cuadruplo
    p[0] = p[1]


def p_exp_operacion(p):
    '''exp_operacion : MAS termino exp_operacion
                     | MENOS termino exp_operacion
                     | empty'''
    #Inserto el operador a la pila
    if len(p) == 3:
        pila_operadores.append(p[1])
        p[0] = p[2]
    
    
#Las siguientes dos reglas multiplican o dividen 2 factores con una llamada recursiva

def p_termino(p):
    '''termino : factor termino_operador'''
    while pila_operadores and pila_operadores[-1] in ['*', '/']:
        op = pila_operadores.pop()
        #Funcion para generar un cuadruplo
        gen_cuad(op)
    p[0] = p[1]


def p_termino_operador(p):
    '''termino_operador : POR factor termino_operador
                        | DIV factor termino_operador
                        | empty'''
    #Inserto el operador a la pila
    if len(p) == 3:
        pila_operadores.append(p[1])
        p[0] = p[2]


def p_factor(p):
    '''factor : PARIZQ expresion PARDER
              | MAS var_cte
              | MENOS var_cte
              | var_cte
              | empty'''


def p_var_cte(p):
    '''var_cte : ID
               | CTEI
               | CTEF
               | CTEC'''
    #Identifico las constantes aceptadas por el compilador
    pila_operandos.append(p[1])
    if p[1] in symbol_table['vars']:
        pila_tipos.append(symbol_table['vars'][p[1]])
    elif isinstance(p[1], int):
        pila_tipos.append('int')
    elif isinstance(p[1], float):
        pila_tipos.append('float')     

def p_empty(p):
    '''empty :'''
    pass

#Funcion para instertar el cuadruplo en la lista de cuadruplos
def insert_cuad(operador, op_izquierdo, op_derecho, result):
    cuad.append([operador, op_izquierdo, op_derecho, result])
    

#Funcion para generar el cuadruplo
def gen_cuad(op):
    r_operand = pila_operandos.pop()
    l_operand = pila_operandos.pop()

    #Verifico que la operacion sea valida en mi cubo semantico
    result = f"temp{len(cuad)}" 
    insert_cuad(op, l_operand, r_operand, result)
    pila_operandos.append(result)


parser = yacc.yacc()
def parse(data):
    return parser.parse(data)