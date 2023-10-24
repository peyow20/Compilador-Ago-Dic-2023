from lexer import tokens
import ply.yacc as yacc


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

    
symbol_table = { 'vars':{},
                'Dir' : {}}

#Estructura para Cuadruplos
cuad = [['','','','']]
cont = 0
pila_operadores = []
pila_operandos = []
pila_saltos = []

#Pruebas
print(symbol_table)
print(cuad)


#Reglas sintacticas
#Esta es la estructura que debe tener mi codigo
def p_program(p):
    '''program : PROGRAM ID PUNCOM vars acum_func MAIN PARIZQ PARDER bloque'''
    p[0] = "ACC"

def p_funcion(p):
     '''funcion : FUNC TIPO ID PARIZQ TIPO ID PARDER vars bloque'''

def p_acum_func(p):
     '''acum_func : funcion acum_func
                  | empty'''
     
#En las siguiente 4 reglas me ayudan a construir el area de las variables
#tanto como los distintos tipos(en este caso solo int y float) como la cantidad
def p_vars(p):
    '''vars : VAR id DOSPUN TIPO PUNCOM asignacion_id'''

def p_id(p):
    '''id : ID acum_id'''

def p_acum_id(p):
    '''acum_id : COMA ID acum_id
                | empty'''

def p_asignacion_id(p):
    '''asignacion_id : id DOSPUN TIPO PUNCOM asignacion_id
                  | empty'''
#Esta regla define los tipos de variables que 
def p_TIPO(p):
    '''TIPO : INT
            | FLOAT
            | CHAR'''

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


def p_exp_operacion(p):
    '''exp_operacion : MAS termino exp_operacion
                     | MENOS termino exp_operacion
                     | empty'''

#Las siguientes dos reglas multiplican o dividen 2 factores con una llamada recursiva

def p_termino(p):
    '''termino : factor termino_operador'''


def p_termino_operador(p):
    '''termino_operador : POR factor termino_operador
                        | DIV factor termino_operador
                        | empty'''


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

def p_empty(p):
    '''empty :'''
    pass



#Puntos neuralgicos
#Punto neuralagico para guardar variables
def p_save_var(p):
    'save_var'

#Punto neuralgico para reconocer el tipo
def p_type_var(p):
    'type_var'

#Punto neuralgico para asignarle el tipo a cada variable
def p_set_vartype(p):
    'set_vartype'


#Punto neuralgico para agregar operadores a la pila de operadores
def p_add_operador(p):
    'add_operador'


#Punto neuralgico para agregar el operador de mas
def p_add_operando_mas(p):
    'add_operando_mas'

#Punto neuralgico para agregar el operador de menos
def p_add_operando_menos(p):
    'add_operando_menos'

#Punto neuralgico para agregar el operador de mas
def p_add_operando_producto(p):
    'add_operando_producto'


#Punto neuralgico para agregar el operador de mas
def p_add_operando_div(p):
    'add_operando_div'


#Punto neuralgico para agregar el operador de mas
def p_add_operando_condicion(p):
    'add_operando_condicion'

#Punto neuralgico para agregar el operador logico
def p_add_operando_OR(p):
    'add_operando_OR'

def p_add_operando_AND(p):
    'add_operando_AND'

#Funcion para generacion de cuad
def p_gen_quad(p):
    'gen_quad'



parser = yacc.yacc()
def parse(data):
    return parser.parse(data)