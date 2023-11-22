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






#Direcciones de memoria
global_int = 0
global_float = 1000
global_char = 2000
global_bool = 3000
local_int = 4000
local_float = 5000
local_char = 6000
local_bool = 7000
constante_int = 8000
constante_float = 9000
constante_char = 10000
constante_bool = 11000 

# Limites de memoria para cada tipo
MAX_GLOBAL_INT = 1000
MAX_GLOBAL_FLOAT = 2000
MAX_GLOBAL_CHAR = 3000
MAX_GLOBAL_BOOL = 4000
MAX_LOCAL_INT = 5000
MAX_LOCAL_FLOAT = 6000
MAX_LOCAL_CHAR = 7000
MAX_LOCAL_BOOL = 8000
MAX_CONSTANT_INT = 9000
MAX_CONSTANT_FLOAT = 10000
MAX_CONSTANT_CHAR = 11000
MAX_CONSTANT_BOOL = 12000

# Contadores de memoria para cada tipo
current_global_int_address = global_int
current_global_float_address = global_float
current_global_char_address = global_char
current_global_bool_address = global_bool
current_local_int_address = local_int
current_local_float_address = local_float
current_local_char_address = local_char
current_local_bool_address = local_bool
current_constant_int_address = constante_int
current_constant_float_address = constante_float
current_constant_char_address = constante_char
current_constant_bool_address = constante_bool



symbol_table = {}
param_table = []
tabla_cte = {} 
current_function = None

#Estructura para Cuadruplos
cuad = []  # Para cuádruplos con direcciones
cuad_literales = []  # Para cuádruplos con nombres de variables o valores literales


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
    print("/////Cuadruplos con direcciones////")
    for cuadruplo in cuad:
        print(count,cuadruplo)
        count = count+1
    count = 0
    #print("/////Cuadruplos literales////")
    #for cuadruplo in cuad_literales:
     #   print(count,cuadruplo)
      #  count = count+1
    #count = 0
    print("////Tabla de const////")
    for cte in tabla_cte:
        print(count, cte)
        count = count+1

    p[0] = "ACC"


def p_main(p):
    '''main : MAIN PARIZQ PARDER bloque'''


def p_funcion(p):
    '''funcion : FUNC TIPO ID PARIZQ param PARDER VAR vars bloque RETURN exp PUNCOM
               | FUNC VOID ID PARIZQ param PARDER VAR vars bloque RETURN PUNCOM'''

def p_param(p):
    '''param : TIPO ID COMA param
             | TIPO ID 
             | empty'''



def p_acum_func(p):
     '''acum_func : funcion acum_func
                  | empty'''
     

def p_llamada_funcion(p):
    '''llamada_funcion : ID PARIZQ argumentos_llamada PARDER'''

def p_argumentos_llamada(p):
    '''argumentos_llamada : argumentos_llamada COMA expresion
                          | expresion
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
        address = assign_global_memory(var_type)  # Obtiene la dirección de memoria para la variable
        # Guarda en la tabla de símbolos tanto el tipo como la dirección de memoria
        symbol_table['vars'][var_id] = {
            'type': var_type,
            'address': address
        }
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
                 | while_condicion
                 | llamada_funcion'''


def p_multiples_estatutos(p):
    '''multiples_estatutos : estatuto multiples_estatutos
                       | empty'''


#Las 6 sigueintes reglas son para establecer la semantica 
# de los difetenes tipos de estatutos 
def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PUNCOM'''
    var_name = p[1]  # Nombre de la variable a la que se asigna

    if var_name in symbol_table['vars']:
        var_type = symbol_table['vars'][var_name]['type']
        var_address = symbol_table['vars'][var_name]['address']  # Dirección de la variable

        if len(pila_tipos) > 0:
            expr_type = pila_tipos.pop()
        else:
            raise Exception("Error de pila de tipos")

        # Verificar compatibilidad de tipos
        if expr_type == var_type or (var_type == FLOAT and expr_type == INT):
            operando_izq_address = var_address
            operando_izq_literal = var_name
            operando_der = pila_operandos.pop()

            # Cuádruplo con direcciones
            cuadruplo_asignacion = ('=', operando_der, '', operando_izq_address)
            cuad.append(cuadruplo_asignacion)

            # Cuádruplo con nombres de variables o valores literales
            cuadruplo_asignacion_literal = ('=', get_literal_or_name(operando_der), '', operando_izq_literal)
            cuad_literales.append(cuadruplo_asignacion_literal)
        else:
            raise Exception(f"Tipo no compatible en la asignación a '{var_name}'")
    else:
        raise Exception(f"Variable no declarada: {var_name}")

def get_literal_or_name(operand):
    if operand in symbol_table['vars']:
        # Si el operando es una variable, devuelve su nombre
        return symbol_table['vars'][operand]['name'] 
    else:
        # Si es un valor literal o un temporal, devuelve el operando tal cual
        return operand

def p_escritura(p):
    '''escritura : WRITE PARIZQ print_expresion PARDER PUNCOM'''


def p_print_expresion(p):
    '''print_expresion : expresion multiples_print
                       | CTESTRING multiples_print'''
    if len(p) == 3:
        if isinstance(p[1], str):
            # Si es una constante string, se imprime directamente
            cuad.append(('write', p[1], '', ''))
        else:
            # Es una expresión, el resultado está en la cima de la pila de operandos
            result = pila_operandos.pop()
            cuad.append(('write', result, '', ''))


def p_multiples_print(p):
    '''multiples_print : COMA  print_expresion
                 | empty'''

def p_condicion(p):
    '''condicion : IF PARIZQ expresion PARDER verificar_if bloque verificar_bloque_if PUNCOM
                 | IF PARIZQ expresion PARDER verificar_if bloque verificar_bloque_else ELSE bloque verificar_bloque_if PUNCOM'''

def p_while_condicion(p):
    '''while_condicion : WHILE PARIZQ guardar_posicion_while expresion verificar_expresion_while PARDER DO bloque llenar_cuadruplo_while'''
    

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
        left_operand = pila_operandos.pop()  # Luego el operando izquierdo
        
        right_type = pila_tipos.pop() 
        left_type = pila_tipos.pop()  
        operator = p[2]  # El operador de comparación

        if isinstance(right_type, dict) or isinstance(left_type, dict):
            raise TypeError("Los tipos de operandos deben ser primitivos, no diccionarios.")

        result_type = validate_operation(left_type, right_type, operator)
        if result_type != 'ERROR':
            result = generate_temporal()
            cuad.append((operator, left_operand, right_operand, result))
            pila_operandos.append(result)
            pila_tipos.append(result_type)
        else:
            raise Exception("Error de comparación")

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
        # Si es una constante, asigna una dirección de memoria y empuja esa dirección y su tipo a la pila.
        const_address = assign_constant_memory(p[1])  # Obtiene o asigna una dirección para la constante
        pila_operandos.append(const_address)  # Dirección de memoria de la constante
        if isinstance(p[1], int):
            pila_tipos.append('int')  # Empuja 'int' para constantes enteras
        elif isinstance(p[1], float):
            pila_tipos.append('float')  # Empuja 'float' para constantes flotantes
        elif isinstance(p[1], str) and len(p[1]) == 1:
            pila_tipos.append('char')  # Empuja 'char' para constantes de caracter
        elif isinstance(p[1], str) and p[1] in ['true', 'false']:
            pila_tipos.append('bool')  # Empuja 'bool' para constantes booleanas


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



###FUNCIONES

# Función para asignar dirección de memoria a una variable global
def assign_global_memory(var_type):
    global current_global_int_address, current_global_float_address, current_global_char_address, current_global_bool_address

    if var_type == INT:
        if current_global_int_address < MAX_GLOBAL_INT:
            address = current_global_int_address
            current_global_int_address += 1
            return address
        else:
            raise Exception("Error: Overflow de variables enteras globales.")
    elif var_type == FLOAT:
        if current_global_float_address < MAX_GLOBAL_FLOAT:
            address = current_global_float_address
            current_global_float_address += 1
            return address
        else:
            raise Exception("Error: Overflow de variables flotantes globales.")
    elif var_type == CHAR:
        if current_global_char_address < MAX_GLOBAL_CHAR:
            address = current_global_char_address
            current_global_char_address += 1
            return address
        else:
            raise Exception("Error: Overflow de variables de tipo char globales.")
    elif var_type == BOOL:
        if current_global_bool_address < MAX_GLOBAL_BOOL:
            address = current_global_bool_address
            current_global_bool_address += 1
            return address
        else:
            raise Exception("Error: Overflow de variables booleanas globales.")
    else:
        raise Exception(f"El dato: {var_type}, no se maneja en este compilador")
    

def assign_constant_memory(const_value):
    global current_constant_int_address, current_constant_float_address, current_constant_char_address, current_constant_bool_address, tabla_cte
    
    if const_value in tabla_cte:
        return tabla_cte[const_value]['address']

    if const_value in tabla_cte:
        return tabla_cte[const_value]['address']

    # Asignar dirección según el tipo de constante
    if isinstance(const_value, int):
        if current_constant_int_address < MAX_CONSTANT_INT:
            address = current_constant_int_address
            current_constant_int_address += 1
        else:
            raise Exception("Error: No puedes usar tantas constantes enteras.")
    elif isinstance(const_value, float):
        if current_constant_float_address < MAX_CONSTANT_FLOAT:
            address = current_constant_float_address
            current_constant_float_address += 1
        else:
            raise Exception("Error: No puedes usar tantas constantes flotantes.")
    elif isinstance(const_value, str) and len(const_value) == 1:
        if current_constant_char_address < MAX_CONSTANT_CHAR:
            address = current_constant_char_address
            current_constant_char_address += 1
        else:
            raise Exception("Error: No puedes usar tantas constantes de tipo char.")
    elif isinstance(const_value, str) and const_value in ['true', 'false']:
        if current_constant_bool_address < MAX_CONSTANT_BOOL:
            address = current_constant_bool_address
            current_constant_bool_address += 1
        else:
            raise Exception("Error: No puedes usar tantas constantes booleanas.")
    else:
        raise Exception(f"Tipo de constante no manejado: {type(const_value)}")

    # Almacenar la constante y su dirección en la tabla
    tabla_cte[const_value] = {
        'value': const_value,
        'address': address
    }
    return address
    

def assign_local_memory(const_value):
    global current_local_int_address, current_local_float_address, current_local_char_address, current_local_bool_address

    # Asumiendo que las constantes son solo INT o FLOAT
    if isinstance(const_value, int):
        if current_local_int_address < MAX_LOCAL_INT:
            address = current_local_int_address
            current_local_int_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo local enteras.")
    elif isinstance(const_value, float):
        if current_local_float_address < MAX_LOCAL_FLOAT:
            address = current_local_float_address
            current_local_float_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo local flotantes.")
    elif isinstance(const_value, str) and len(const_value) == 1: 
        if current_local_char_address < MAX_LOCAL_CHAR:
            address = current_local_char_address
            current_local_char_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo local de tipo char.")
    elif isinstance(const_value, str) and const_value in ['true', 'false']:  # Asumiendo que las constantes bool son 'true' o 'false'
        if current_local_bool_address < MAX_LOCAL_BOOL:
            address = current_local_bool_address
            current_local_bool_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo local booleanas.")
    else:
        raise Exception(f"Tipo de constante no manejado: {type(const_value)}")





###PUNTOS NEURLAGICOS 

#IF

def p_verificar_if(p):
    '''verificar_if : '''
    global cuad, pila_saltos, pila_operandos, pila_tipos
    result_condicion = pila_operandos.pop()
    exp_type = pila_tipos.pop()
    #Verifico que sea el tipo de dato correcto
    if exp_type != BOOL:
        raise Exception("Error de tipo: Se esperaba una expresión booleana")
    else:
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
