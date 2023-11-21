from lexer import tokens
import ply.yacc as yacc
from pprint import pprint


    
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


#Direcciones de memoria
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
    },
    'temporal': {
        INT: 9000,
        FLOAT: 10000,
        CHAR: 11000
    }
}


param_table = []
current_function = None

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
    '''program : PROGRAM ID PUNCOM VAR vars acum_func main'''
    print(symbol_table)
    count = 0
    for cuadruplo in cuad:
        print(count,cuadruplo)
        count = count+1
    p[0] = "ACC"


def p_main(p):
    '''main : MAIN PARIZQ PARDER bloque'''


def p_funcion(p):
    '''funcion : FUNC TIPO insertar_nombre_funcion ID PARIZQ param PARDER VAR vars bloque RETURN exp fin_declaracion_funcion
               | FUNC VOID insertar_nombre_funcion ID PARIZQ param PARDER VAR vars bloque RETURN fin_declaracion_funcion'''

def p_param(p):
    '''param : TIPO ID guardar_param COMA param
             | TIPO ID guardar_param
             | empty'''

def p_insertar_nombre_funcion(p):
    '''insertar_nombre_funcion : '''
    function_name = p[-1]  # Nombre de la función
    function_type = p[-2]  # Tipo de la función, 'void
    if function_name not in symbol_table['global']['vars']:
        symbol_table['global']['vars'][function_name] = {
        'type': function_type,
        'params': [],
        'vars': {},
        'start': len(cuad), # La posición del primer cuádruplo de la función
        }
# Cambiar el ámbito actual a local para la nueva función
    memory_counter['current_scope'] = function_name
    memory_counter[function_name] = {
        'INT': 3000,
        'FLOAT': 4000,
        'CHAR': 5000,
        }


def p_guardar_param(p):
    '''guardar_param : '''
    global current_function, memory_counter, symbol_table

    param_name = p[-1]  # Nombre del parámetro
    param_type = p[-2]  # Tipo del parámetro
    function_scope = current_function  # El alcance es el nombre de la función actual

    # Asignar dirección de memoria basada en el tipo y el alcance
    param_address = memory_counter['local'][param_type]
    memory_counter['local'][param_type] += 1  # Incrementar el contador para el siguiente parámetro

    # Insertar parámetro en la tabla de símbolos de la función
    if function_scope not in symbol_table:
        symbol_table[function_scope] = {'vars': {}, 'type': None, 'params': []}

    symbol_table[function_scope]['vars'][param_name] = {
        'type': param_type,
        'address': param_address
    }
    
    # Agregar parámetro a la lista de parámetros de la función
    symbol_table[function_scope]['params'].append(param_name)

def p_fin_declaracion_funcion(p):
    '''fin_declaracion_funcion : '''
    function_name = memory_counter['current_scope'] # Nombre de la función actual
# Generar el cuádruplo para el final de la función
    cuad.append(('ENDFunc', '', '', ''))

# Se actualizar la tabla de funciones con la cantidad de memoria para variables locales y temporales

    local_size = sum(memory_counter[function_name].values())
    symbol_table['global']['vars'][function_name]['size'] = local_size
# Restablecer el ámbito actual a global después de terminar la función
    memory_counter['current_scope'] = 'global'

def p_acum_func(p):
     '''acum_func : funcion acum_func
                  | empty'''

#En las siguiente 4 reglas me ayudan a construir el area de las variables
#tanto como los distintos tipos(en este caso solo int y float) como la cantidad

def p_id_lista(p):
    '''id_lista : ID COMA id_lista
               | ID
               | arreglo'''
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

def p_arreglo(p):
   '''arreglo : ARR LLAVIZQ CTEI LLAVDER'''

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
            #Genero el cuadruplo de asignacion
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


###PUNTOS NEURLAGICOS 

#IF
def p_condicion(p):
    '''condicion : IF PARIZQ expresion PARDER verificar_if bloque verificar_bloque_if PUNCOM
                 | IF PARIZQ expresion PARDER verificar_if bloque verificar_bloque_else ELSE bloque verificar_bloque_if PUNCOM'''
    



def p_verificar_if(p):
    '''verificar_if : '''
    global cuad, pila_saltos, pila_operandos
    result_condicion = pila_operandos.pop()
    cuad.append(('GotoF', result_condicion, '', None))  # Se deja el lugar de salto como None para luego actualizarlo
    jump_position_if = len(cuad) - 1
    pila_saltos.append(jump_position_if)


def p_verificar_bloque_if(p):
    '''verificar_bloque_if : '''
    global cuad, pila_saltos
    if len(p) == 1:  # Corresponde a la regla de producción de if-else y actualiza el salto del goto
        jump_position_else = pila_saltos.pop()
        cuad[jump_position_else] = (cuad[jump_position_else][0], cuad[jump_position_else][1], cuad[jump_position_else][2], len(cuad))

    else:  # Solo if y actualiza su salto
        jump_position_if = pila_saltos.pop()
        cuad[jump_position_if] = (cuad[jump_position_if][0], cuad[jump_position_if][1], cuad[jump_position_if][2], len(cuad))


def p_verificar_bloque_else(p):
    '''verificar_bloque_else : '''
    global pila_saltos
    jump_position_if = pila_saltos.pop()
    cuad.append(('GOTO', '', '', None))  # Cuádruplo de salto para el ELSE
    jump_position_goto = len(cuad) - 1
    pila_saltos.append(jump_position_goto)
    #Actualizo el salto del gotof
    cuad[jump_position_if] = (cuad[jump_position_if][0], cuad[jump_position_if][1], cuad[jump_position_if][2], len(cuad))

#WHILE

def p_while_condicion(p):
    '''while_condicion : WHILE PARIZQ guardar_posicion_while expresion verificar_expresion_while PARDER DO bloque llenar_cuadruplo_while'''
    
     
def p_guardar_posicion_while(p):
    '''guardar_posicion_while : '''
    global pila_saltos, cuad
    #Guardo en que posicion esta el while en los cuadruplos para el goto
    pila_saltos.append(len(cuad))

def p_verificar_expresion_while(p):
    '''verificar_expresion_while : '''
    global pila_tipos, pila_operandos, cuad, pila_saltos
    exp_type = pila_tipos.pop()
    #Verifico que sea el tipo de dato correcto
    if exp_type != BOOL:
        raise Exception("Error de tipo: Se esperaba una expresión booleana")
    else:
        result = pila_operandos.pop()
        cuad.append(('GotoF', result, '', None))
        pila_saltos.append(len(cuad) - 1)

def p_llenar_cuadruplo_while(p):
    '''llenar_cuadruplo_while : '''
    global pila_saltos, cuad
    #Le hago pop a el salto del gotof
    inicio_while = pila_saltos.pop(-2)
    goto_f_position = pila_saltos.pop()
    cuad.append(('GOTO', '', '', inicio_while))
    #Actualizo el salto del gotof del while
    cuad[goto_f_position] = (cuad[goto_f_position][0], cuad[goto_f_position][1], cuad[goto_f_position][2], len(cuad))





parser = yacc.yacc()
def parse(data):
    return parser.parse(data)
