from lexer import tokens
import ply.yacc as yacc



#Direcciones de memoria
global_int = 0
global_float = 1000
global_char = 2000
local_int = 3000
local_float = 4000
local_char = 5000
constante_int = 6000
constante_float = 7000
constante_char = 8000

    
BOOL = 'bool'
INT = "int"
FLOAT = "float"
CHAR = "char"

# Cubo semántico para las operaciones aritméticas
SEMANTIC_CUBE = {
    # Operación suma
    (INT, INT, "+"): INT,
    (INT, FLOAT, "+"): FLOAT,
    (FLOAT, INT, "+"): FLOAT,
    (FLOAT, FLOAT, "+"): FLOAT,

    # Operación resta
    (INT, INT, "-"): INT,
    (INT, FLOAT, "-"): FLOAT,
    (FLOAT, INT, "-"): FLOAT,
    (FLOAT, FLOAT, "-"): FLOAT,

    # Operación multiplicación
    (INT, INT, "*"): INT,
    (INT, FLOAT, "*"): FLOAT,
    (FLOAT, INT, "*"): FLOAT,
    (FLOAT, FLOAT, "*"): FLOAT,

    # Operación división
    (INT, INT, "/"): FLOAT,
    (INT, FLOAT, "/"): FLOAT,
    (FLOAT, INT, "/"): FLOAT,
    (FLOAT, FLOAT, "/"): FLOAT,

    # Operación mayor que
    (INT, INT, ">"): BOOL,
    (INT, FLOAT, ">"): BOOL,
    (FLOAT, INT, ">"): BOOL,
    (FLOAT, FLOAT, ">"): BOOL,
    (BOOL, BOOL, ">"): BOOL,
    

    # Operación menor que
    (INT, INT, "<"): BOOL,
    (INT, FLOAT, "<"): BOOL,
    (FLOAT, INT, "<"): BOOL,
    (FLOAT, FLOAT, "<"): BOOL,
    (BOOL, BOOL, "<"): BOOL,


    # Operación diferente que
    (INT, INT, "!="): BOOL,
    (INT, FLOAT, "!="): BOOL,
    (FLOAT, INT, "!="): BOOL,
    (FLOAT, FLOAT, "!="): BOOL,
    (BOOL, BOOL, "!="): BOOL,

    # Operación mayor o igual que
    (INT, INT, ">="): BOOL,
    (INT, FLOAT, ">="): BOOL,
    (FLOAT, INT, ">="): BOOL,
    (FLOAT, FLOAT, ">="): BOOL,
    (BOOL, BOOL, ">="): BOOL,

    # Operación menor o igual que
    (INT, INT, "<="): BOOL,
    (INT, FLOAT, "<="): BOOL,
    (FLOAT, INT, "<="): BOOL,
    (FLOAT, FLOAT, "<="): BOOL,
    (BOOL, BOOL, "<="): BOOL,

    # Operación igual igual
    (INT, INT, "=="): BOOL,
    (INT, FLOAT, "=="): BOOL,
    (FLOAT, INT, "=="): BOOL,
    (FLOAT, FLOAT, "=="): BOOL,
    (BOOL, BOOL, "=="): BOOL,
}


def validate_operation(left_type, right_type, operator):
    if (left_type, right_type, operator) in SEMANTIC_CUBE:
        return SEMANTIC_CUBE[(left_type, right_type, operator)]
    else:
        raise Exception(f"Operación no válida: {left_type} {operator} {right_type}")





symbol_table = {
    'global': {
        'vars': {},
        'type': None,
        'memory': {
            INT: 0,
            FLOAT: 1000,
            CHAR: 2000
        }
    }
}



memory_counter = {
    'global': {
        INT: 0,
        FLOAT: 1000,
        CHAR: 2000
    },
    'local': {
        INT: 3000,
        FLOAT: 4000,
        CHAR: 5000
    },
    'constant': {
        INT: 6000,
        FLOAT: 7000,
        CHAR: 8000
    }
}


tipo_var = None


param_table = []

#Estructura para Cuadruplos
cuad = []
pila_tipos = []
pila_operadores = []
pila_operandos = []
pila_saltos = []
temporal_count = 0

#Reglas sintacticas
#Esta es la estructura que debe tener mi codigo
def p_program(p):
    '''program : PROGRAM ID PUNCOM VAR vars main'''
    print(symbol_table)
    for cuadruplo in cuad:
        print(cuadruplo)
    p[0] = "ACC"


def p_main(p):
    '''main : MAIN PARIZQ PARDER bloque'''

#def p_funcion(p):
 #    '''funcion : FUNC TIPO ID PARIZQ param PARDER vars_func bloque_func
  #              | FUNC VOID ID PARIZQ param PARDER vars_func bloque_func'''

#def p_acum_func(p):
 #    '''acum_func : funcion acum_func
  #                | empty'''
     
#def p_bloque_func(p):
 #    '''bloque_func : LLAVIZQ multiples_estatutos RETURN LLAVDER PUNCOM'''


#def p_param(p):
 #    '''param : TIPO ID COMA param
  #            | TIPO ID'''
     
#def p_var_func(p):
 #   '''var_func : id_lista_func DOSPUN TIPO PUNCOM vars_func
  #              | empty'''

#def p_id_list_func(p):
 #   '''id_list_func : ID COMA id_lista_func
  #                  | ID'''
     
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
def handle_vars(p, scope='global'):
    var_type = p[3]
    id_list = p[1]
    for var_id in id_list:
        current_address = memory_counter[scope][var_type]
        symbol_table[scope]['vars'][var_id] = {
            'type': var_type,
            'address': current_address
        }
        memory_counter[scope][var_type] += 1

def p_vars(p):
    '''vars : id_lista DOSPUN TIPO PUNCOM vars
            | empty'''
    if len(p) == 6:
        handle_vars(p, scope='global')
    elif len(p) == 2:
        p[0] = None
    

#Esta regla define los tipos de variables que 
def p_TIPO(p):
    '''TIPO : INT
            | FLOAT
            | CHAR
            | BOOL'''
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
                 | while_condicion'''


def p_multiples_estatutos(p):
    '''multiples_estatutos : estatuto multiples_estatutos
                       | empty'''


#Las 6 sigueintes reglas son para establecer la semantica 
# de los difetenes tipos de estatutos 
def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PUNCOM'''
    var_name = p[1]  # Nombre de la variable a la que se asigna

    current_scope = "global" 

    if var_name in symbol_table[current_scope]['vars']:
        var_type = symbol_table[current_scope]['vars'][var_name]['type']

        if len(pila_tipos) > 0:
            expr_type = pila_tipos.pop() 
        else:
            raise Exception("Error de pila de tipos")

        # Verificar compatibilidad
        if expr_type == var_type or (var_type == FLOAT and expr_type == INT):
            operando_izq = p[1]
            operando_der = pila_operandos.pop()
            cuadruplo_asignacion = ('=', operando_der, '', operando_izq)
            cuad.append(cuadruplo_asignacion)
        else:
            raise Exception(f"Tipo no compatible en la asignación a '{var_name}'")
    else:
        raise Exception(f"Variable '{var_name}' no declarada o fuera de ámbito")
    

def p_escritura(p):
    '''escritura : PRINT PARIZQ print_expresion PARDER PUNCOM'''


def p_print_expresion(p):
    '''print_expresion : expresion multiples_print
                       | CTESTRING multiples_print'''


def p_multiples_print(p):
    '''multiples_print : COMA  print_expresion
                 | empty'''


def p_condicion(p):
    '''condicion : IF PARIZQ expresion PARDER verificar_if bloque verificar_bloque_if PUNCOM'''
    # | IF PARIZQ expresion verificar_if PARDER bloque verificar_bloque_if ELSE bloque verificar_bloque_else'''

def p_verificar_if(p):
    '''verificar_if : '''
    # Generar cuádruplo GotoF
    result_condicion = pila_operandos.pop()
    jump_position_if = len(cuad)
    cuad.append(('GotoF', result_condicion, '', jump_position_if))
    pila_saltos.append(jump_position_if)

def p_verificar_bloque_if(p):
    '''verificar_bloque_if : '''
    jump_position_if = pila_saltos.pop()
    # Actualizar GotoF con la dirección después del if
    cuad[jump_position_if] = (cuad[jump_position_if][0], cuad[jump_position_if][1], cuad[jump_position_if][2], len(cuad))
    

def p_while_condicion(p):
    ''' while_condicion : WHILE PARIZQ expresion PARDER DO bloque'''


#def p_for_condicion(p):
 #     '''for_condicion : FOR asignacion TO expresion DO bloque'''


def p_expresion_and(p):
    '''expresion : expresion AND expresion'''


def p_expresion_or(p):
    '''expresion : expresion OR expresion'''

#Regla que define la jeraquia de dos expresiones
def p_expresion(p):
    '''expresion : exp 
                 | exp MAYOR exp
                 | exp MENOR exp
                 | exp DIFF exp
                 | exp IGIG exp
                 | exp MAYIG exp
                 | exp MENIG exp'''
    
    if len(p) > 2:
        # Manejo de operadores de comparación
        right_operand = pila_operandos.pop()  # Extrae primero el operando derecho
        right_type = pila_tipos.pop()
        left_operand = pila_operandos.pop()  # Luego el operando izquierdo
        left_type = pila_tipos.pop()
        operator = p[2]  # El operador de comparación

        result_type = validate_operation(left_type, right_type, operator)
        if result_type != 'ERROR':
            result = generate_temporal()
            cuad.append((operator, left_operand, right_operand, result))
            pila_operandos.append(result)
            pila_tipos.append(result_type)
        else:
            raise Exception("Error de comparacion")

#Las siguientes dos reglas suman o restan 2 terminos con una llamada recursiva
def p_exp(p):
    '''exp : termino exp_operacion'''



def p_exp_operacion(p):
    '''exp_operacion : MAS termino exp_operacion
                     | MENOS termino exp_operacion
                     | empty'''
    if len(p) > 2:
        #Se obtiene el operador
        operador = p[1]  
        pila_operadores.append(operador)
        check_for_quad_generation()

    
    
#Las siguientes dos reglas multiplican o dividen 2 factores con una llamada recursiva

def p_termino(p):
    '''termino : factor termino_operador'''



def p_termino_operador(p):
    '''termino_operador : POR factor termino_operador
                        | DIV factor termino_operador
                        | empty'''
    #Verifico si es operador * o / y despues de doy su push en la pila
    if len(p) > 2:
        operador = p[1] 
        pila_operadores.append(operador)
        #Genero el cuadruplo de acorde al operador
        check_for_quad_generation()


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
               | CTEC
               | CTEB'''
    #Identifico las constantes aceptadas por el compilador
    pila_operandos.append(p[1])
    
    # Aquí debes verificar en qué ámbito (scope) estás actualmente trabajando
    # Por ejemplo, si estás en una función, deberías buscar la variable en el espacio de esa función
    # Si no estás en una función, deberías buscar en el espacio global
    current_scope = "global"  # o el nombre de la función actual si estás dentro de una
    if p[1] in symbol_table[current_scope]['vars']:
        pila_tipos.append(symbol_table[current_scope]['vars'][p[1]]['type'])
    elif isinstance(p[1], int):
        pila_tipos.append('int')
    elif isinstance(p[1], float):
        pila_tipos.append('float')
    else:
        # Manejar el caso en que la variable no esté definida
        raise Exception(f"Variable '{p[1]}' no declarada")


def p_error(p):
    print(f"Syntax error at '{p.value}'")  

def p_empty(p):
    '''empty :'''
    pass


def check_for_quad_generation():
    if len(pila_operadores) > 0:
        # Verificar la precedencia del operador
        top_operator = pila_operadores[-1]
        if top_operator in ['+', '-', '*', '/']:
            # Implementa aquí la lógica para generar cuádruplos
            generate_quad()


def generate_quad():
    right_operand = pila_operandos.pop()
    right_type = pila_tipos.pop()
    left_operand = pila_operandos.pop()
    left_type = pila_tipos.pop()
    operator = pila_operadores.pop()

    result_type = validate_operation(left_type, right_type, operator)
    if result_type != 'ERROR':
        result = generate_temporal()
        cuad.append((operator, left_operand, right_operand, result))
        pila_operandos.append(result)
        pila_tipos.append(result_type)
    else:
        print(f"Error de tipo en la operación: {left_type} {operator} {right_type}")


def generate_temporal():
    global temporal_count
    temporal_name = f"t{temporal_count}"
    temporal_count += 1
    return temporal_name


parser = yacc.yacc()
def parse(data):
    return parser.parse(data)
