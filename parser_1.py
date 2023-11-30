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

# Limites de memoria 
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

# Contador para controlar el almacenamiento
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

# Direcciones de temporales

temporal_int = 15000
temporal_float = 16000
temporal_bool = 17000

MAX_TEMPORAL_INT = 16000
MAX_TEMPORAL_FLOAT = 17000
MAX_TEMPORAL_BOOL = 18000

current_temporal_int_address = temporal_int 
current_temporal_float_address = temporal_float
current_temporal_bool_address = temporal_bool

directorio_funciones = {
    'global': {
        'tipo': None,  # Tipor de retorno defaul
        'vars': {},  # Aquí almaceno variable
        'params': []  # Parametros (por si se ocupan)
    }
}


param_table = []
tabla_cte = {} 
current_function = 'global'

#Estructura para Cuadruplos
cuad = []  # Para cuádruplos con direcciones


pila_tipos = []
pila_operadores = []
pila_operandos = []
pila_saltos = []
temporal_count = 0

current_function_call = None
param_counter = 0

#Reglas sintacticas con semantica
#Esta es la estructura que debe tener mi codigo
def p_program(p):
    '''program : goto_main PROGRAM ID PUNCOM VAR vars acum_func aux_goto_main main'''
    global current_function, cuad
    func_name = p[2]
    current_function = func_name
    print(current_function)
    #Se imprime los resultados obtenidos
    imprimir_directorio_funciones(directorio_funciones)
    imprimir_tabla_constantes(tabla_cte)
    count = 0
    print("/////Cuadruplos con direcciones////")
    for cuadruplo in cuad:
        print(count,cuadruplo)
        count = count+1
    count = 0
    
    p[0] = "ACC"


def p_main(p):
    '''main : MAIN PARIZQ PARDER bloque'''



def p_funcion(p):
    '''funcion : FUNC TIPO ID insert_dirfunc PARIZQ param PARDER save_params vars_local bloque_func RETURN exp PUNCOM end_function
               | FUNC VOID ID insert_dirfunc PARIZQ param PARDER save_params vars_local bloque_func RETURN PUNCOM end_function'''
    

def p_param(p):
    '''param : TIPO ID COMA param
             | TIPO ID'''
    if len(p) == 3:
        # Solo tiene un parametro
        p[0] = [(p[1], p[2])]
    else:
        # Hay mas parametros
        p[0] = [(p[1], p[2])] + p[4]

#En caso de que no haya parametros
def p_param_empty(p):
    '''param : empty'''
    p[0] = []

def p_acum_func(p):
     '''acum_func : funcion acum_func
                  | empty'''


#En las siguiente 4 reglas me ayudan a construir el area de las variables
#tanto como los distintos tipos(en este caso solo int, float, char, bool) como la cantidad

def p_id_lista(p):
    '''id_lista : ID COMA id_lista
               | ID'''
    if len(p) == 4: 
        p[0] = [p[1]] + p[3]
    else: 
        p[0] = [p[1]]

def p_arreglos(p):
    '''arreglos : TIPO ID CORCHIZQ CTEI ARRdot CTEI CORCHDER PUNCOM'''
    array_type = p[1]
    array_id = p[2]
    lower_bound = p[4]
    upper_bound = p[6]
    
    # Asigna memoria y calcula el tamaño del arreglo
    base_address, array_size = assign_array_memory(array_type, lower_bound, upper_bound)

    # Añade la información del arreglo al directorio de funciones
    array_info = {
        'type': array_type,
        'base_address': base_address,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'size': array_size
    }
    directorio_funciones[current_function]['vars'][array_id] = array_info


def p_vars(p):
    '''vars : id_lista DOSPUN TIPO PUNCOM vars
            | arreglos
            | empty'''
    if len(p) == 6:
        global current_function
        var_type = p[3]
        id_list = p[1]
        if current_function != 'global':
            # Aquí manejas las variables como locales
            handle_local_vars(current_function, id_list, var_type)
        else:
            # Manejo de variables globales
            handle_global_vars(id_list, var_type)
        
#Esta regla define los tipos de variables que 
def p_TIPO(p):
    '''TIPO : INT
            | FLOAT
            | CHAR
            | BOOL'''
    #Identifico los tipos de variables
    p[0] = p[1]

    # Asignar memoria para el arreglo y almacenar su información
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
                 | lectura
                 | while_condicion
                 | call_func
                 | funcion_media'''




def p_multiples_estatutos(p):
    '''multiples_estatutos : estatuto multiples_estatutos
                       | empty'''


#Las 6 sigueintes reglas son para establecer la semantica 
# de los difetenes tipos de estatutos 
def p_asignacion(p):
    '''asignacion : ID IGUAL call_func
                  | ID IGUAL expresion PUNCOM'''
    
    var_name = p[1]  # Nombre de la variable a la que se asigna

    if len(p) == 5 : 
    # Buscar la variable en el directorio de funciones bajo el contexto actual
        func_context = directorio_funciones[current_function if current_function in directorio_funciones else 'global']
        if var_name in func_context['vars']:
            var_type = func_context['vars'][var_name]['type']
            var_address = func_context['vars'][var_name]['address']

            if len(pila_tipos) > 0:
                expr_type = pila_tipos.pop()
            else:
                raise Exception("Error de pila de tipos")

                # Verificar compatibilidad de tipos
            if expr_type == var_type or (var_type == FLOAT and expr_type == INT):
                operando_izq_address = var_address
                operando_der = pila_operandos.pop()

                    # Cuádruplo con direcciones
                cuadruplo_asignacion = ('=', operando_der, '', operando_izq_address)
                cuad.append(cuadruplo_asignacion)
            else:
                raise Exception(f"Tipo no compatible en la asignación a '{var_name}'")
        else:
                raise Exception(f"Variable no declarada: {var_name}")
    else :
        var_info = get_variable_info(var_name, current_function)
        if var_info is None:
            raise Exception(f"Error: Variable no declarada '{var_name}'")

        # Obtiene el tipo de la variable y el valor de retorno de la pila
        var_type = var_info['type']
        return_value = pila_operandos.pop()
        return_type = pila_tipos.pop()

        # Verifica que el tipo del valor de retorno coincida con el tipo de la variable
        if var_type != return_type:
            raise Exception(f"Error de tipo: Intento de asignar {return_type} a {var_type}")

        # Genera el cuádruplo de asignación del valor de retorno a la variable
        cuad.append(('=', return_value, '', var_info['address']))
        

def p_lectura(p):
    '''lectura : READ PARIZQ ID PARDER PUNCOM'''
    var_name = p[3]  # Nombre de la variable a la que se asignará el valor leído

    # Verifico si la variable ha sido declarada
    if var_name in directorio_funciones[current_function]['vars']:
        var_info = directorio_funciones[current_function]['vars'][var_name]
        var_address = var_info['address']

        # Generar cuádruplo para la lectura
        cuad.append(('read', "", "", var_address))
    else:
        raise Exception(f"Error: Variable no declarada '{var_name}'")

def p_escritura(p):
    '''escritura : WRITE PARIZQ print_expresion PARDER PUNCOM'''


def p_print_expresion(p):
    '''print_expresion : expresion multiples_print
                       | CTESTRING multiples_print'''
    if len(p) == 3:
        if isinstance(p[1], str):
            # Es una constante string, imprímela directamente
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
    '''while_condicion : WHILE PARIZQ save_position_while expresion check_while_exp PARDER DO bloque fill_jump_while'''
    

#def p_for_condicion(p):
 #     '''for_condicion : FOR asignacion TO expresion DO bloque'''


def p_expresion_and(p):
    '''expresion : expresion AND expresion'''
    gen_cuad_logico(p, 'AND')


def p_expresion_or(p):
    '''expresion : expresion OR expresion'''
    gen_cuad_logico(p, 'OR')

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
        right_operand = pila_operandos.pop()
        left_operand = pila_operandos.pop()
    
        right_type = pila_tipos.pop()  # Asumiendo que aquí se extrae un string que indica el tipo
        left_type = pila_tipos.pop()  # Asumiendo que aquí también se extrae un string que indica el tipo

        operator = p[2]  # El operador de comparación

        if isinstance(right_type, dict) or isinstance(left_type, dict):
            raise TypeError("Los tipos de operandos deben ser primitivos, no diccionarios.")

        result_type = validate_operation(left_type, right_type, operator)
        if result_type != 'ERROR':
            result = generate_temporal(result_type)
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
    
    scope = directorio_funciones[current_function] if current_function else directorio_funciones['global']
    if isinstance(p[1], str) and p[1] in scope['vars']:
        var_info = scope['vars'][p[1]]
        pila_operandos.append(var_info['address'])
        pila_tipos.append(var_info['type'])
    else:
        # Si es una constante, asigna una dirección de memoria y empuja esa dirección y su tipo a la pila.
        const_address = assign_constant_memory(p[1])  # Obtiene o asigna una dirección para la constante
        pila_operandos.append(const_address)  # Dirección de memoria de la constante
        if isinstance(p[1], int):
            pila_tipos.append('int')  # Empujo 'int' para constantes enteras
        elif isinstance(p[1], float):
            pila_tipos.append('float')  # Empujo 'float' para constantes flotantes
        elif isinstance(p[1], str) and len(p[1]) == 1:
            pila_tipos.append('char')  # Empujo 'char' para constantes de caracter
        elif isinstance(p[1], str) and p[1] in ['true', 'false']:
            pila_tipos.append('bool')  # Empujo 'bool' para constantes booleanas


def p_funcion_media(p):
    '''funcion_media : MEDIA PARIZQ argumentos_funcion PARDER PUNCOM'''

    
def p_argumentos_funcion(p):
    '''argumentos_funcion : CTEI COMA argumentos_funcion
                          | CTEI'''


def p_error(p):
    print(f"Syntax error at '{p.value}'")  

def p_empty(p):
    '''empty :'''
    pass



#/////////////////////////FUNCIONES////////////////////

# Función para asignar dirección de memoria a una variable global
def assign_global_memory(var_type):
    global current_global_int_address, current_global_float_address, current_global_char_address, current_global_bool_address

    if var_type == INT:
        if current_global_int_address < MAX_GLOBAL_INT:
            address = current_global_int_address
            current_global_int_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo de variables enteras globales.")
    elif var_type == FLOAT:
        if current_global_float_address < MAX_GLOBAL_FLOAT:
            address = current_global_float_address
            current_global_float_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo de variables flotantes globales.")
    elif var_type == CHAR:
        if current_global_char_address < MAX_GLOBAL_CHAR:
            address = current_global_char_address
            current_global_char_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo de variables de tipo char.")
    elif var_type == BOOL:
        if current_global_bool_address < MAX_GLOBAL_BOOL:
            address = current_global_bool_address
            current_global_bool_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo de variables booleanas.")
    else:
        raise Exception(f"Tipo de dato no manejado: {var_type}")
    

#Funcion asigna la memoria correspondiente a las constantes del programa
def assign_constant_memory(const_value):
    global current_constant_int_address, current_constant_float_address, current_constant_char_address, current_constant_bool_address, tabla_cte
    
    if const_value in tabla_cte:
        return tabla_cte[const_value]['address']

    if const_value in tabla_cte:
        return tabla_cte[const_value]['address']

    if isinstance(const_value, int):
        if current_constant_int_address < MAX_CONSTANT_INT:
            address = current_constant_int_address
            current_constant_int_address += 1
        else:
            raise Exception("Error: Se ha excedido el número máximo de constantes enteras.")
    elif isinstance(const_value, float):
        if current_constant_float_address < MAX_CONSTANT_FLOAT:
            address = current_constant_float_address
            current_constant_float_address += 1
        else:
            raise Exception("Error: Se ha excedido el número máximo de constantes flotantes.")
    elif isinstance(const_value, str) and len(const_value) == 1:
        if current_constant_char_address < MAX_CONSTANT_CHAR:
            address = current_constant_char_address
            current_constant_char_address += 1
        else:
            raise Exception("Error: Se ha excedido el número máximo de constantes de tipo char.")
    elif isinstance(const_value, str) and const_value in ['true', 'false']:
        if current_constant_bool_address < MAX_CONSTANT_BOOL:
            address = current_constant_bool_address
            current_constant_bool_address += 1
        else:
            raise Exception("Error: Se ha excedido el número máximo de constantes booleanas.")
    else:
        raise Exception(f"Tipo de constante no manejado: {type(const_value)}")

    # Almacenar la constante y su dirección en la tabla
    tabla_cte[const_value] = {
        'value': const_value,
        'address': address
    }
    return address
    
#Funcion que asignar direccion a las variables locales
def assign_local_memory(var_type):
    global current_local_int_address, current_local_float_address, current_local_char_address, current_local_bool_address
    if var_type == INT:
        if current_local_int_address < MAX_LOCAL_INT:
            address = current_local_int_address
            current_local_int_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo de variables enteras locales.")
    elif var_type == FLOAT:
        if current_local_float_address < MAX_LOCAL_FLOAT:
            address = current_local_float_address
            current_local_float_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo de variables flotantes locales.")
    elif var_type == CHAR:
        if current_local_char_address < MAX_LOCAL_CHAR:
            address = current_local_char_address
            current_local_char_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo de variables de tipo char.")
    elif var_type == BOOL:
        if current_local_bool_address < MAX_LOCAL_BOOL:
            address = current_local_bool_address
            current_local_bool_address += 1
            return address
        else:
            raise Exception("Error: Se ha excedido el número máximo de variables booleanas.")
    else:
        raise Exception(f"Tipo de dato no manejado: {var_type}")

def assign_array_memory(array_type, lower_bound, upper_bound):
    global current_local_int_address, current_local_float_address, current_local_char_address, current_local_bool_address
    global current_global_int_address, current_global_float_address, current_global_char_address, current_global_bool_address, current_function
    size = upper_bound - lower_bound + 1
    if current_function != 'global':
        if array_type == INT:
            address = current_local_int_address
            current_local_int_address += size
        elif array_type == FLOAT:
            address = current_local_float_address
            current_local_float_address += size
        elif array_type == CHAR:
            address = current_local_char_address
            current_local_char_address += size
        elif array_type == BOOL:
            address = current_local_bool_address
            current_local_bool_address += size
        else:
            raise Exception(f"Tipo de dato no manejado para arreglos: {array_type}")
    else : 
        if array_type == INT:
            address = current_global_int_address
            current_global_int_address += size
        elif array_type == FLOAT:
            address = current_global_float_address
            current_global_float_address += size
        elif array_type == CHAR:
            address = current_global_char_address
            current_global_char_address += size
        elif array_type == BOOL:
            address = current_global_bool_address
            current_global_bool_address += size
        else:
            raise Exception(f"Tipo de dato no manejado para arreglos: {array_type}")
        

    return address, size

def get_variable_info(var_name, current_function):
    if var_name in directorio_funciones[current_function]['vars']:
        return directorio_funciones[current_function]['vars'][var_name]
    elif var_name in directorio_funciones['global']['vars']:
        return directorio_funciones['global']['vars'][var_name]
    return None


#Funcion para verificar el tipo de cadruplo que se genera con el operador
def check_for_quad_generation():
    if len(pila_operadores) > 0:
        # Verificar la precedencia del operador
        top_operator = pila_operadores[-1]
        if top_operator in ['+', '-', '*', '/']:
            gen_cuad_op()

#Funcion que genera el cuadruplo de comparativa logica
def gen_cuad_logico(p, operador):
    global pila_tipos, pila_operandos, cuad
    right_operand = pila_operandos.pop()
    print("der",right_operand)
    right_type = pila_tipos.pop()
    left_operand = pila_operandos.pop()
    print("izq",left_operand)

    left_type = pila_tipos.pop()

    if left_type == BOOL and right_type == BOOL:
        temporal_address = generate_temporal(BOOL)
        cuad.append((operador, left_operand, right_operand, temporal_address))
        pila_operandos.append(temporal_address)
        pila_tipos.append(BOOL)
    else:
        raise Exception(f"Error semántico: Operación '{operador}' no válida entre {left_type} y {right_type}")

#Funcion que genera el cuadruplo de operacion
def gen_cuad_op():
    right_operand = pila_operandos.pop()
    right_type = pila_tipos.pop()
    left_operand = pila_operandos.pop()
    left_type = pila_tipos.pop()
    operator = pila_operadores.pop()

    result_type = validate_operation(left_type, right_type, operator)
    if result_type != 'ERROR':
        # Llama a generate_temporal con el tipo resultante
        result = generate_temporal(result_type)
        cuad.append((operator, left_operand, right_operand, result))
        pila_operandos.append(result)
        pila_tipos.append(result_type)
    else:
        print(f"Error de tipo en la operación: {left_type} {operator} {right_type}")

#Funcion que genera temporales
def generate_temporal(var_type):
    global current_temporal_int_address, current_temporal_float_address, current_temporal_bool_address

    # Verifica el tipo de dato y asigna una dirección de memoria temporal correspondiente
    if var_type == INT:
        if current_temporal_int_address < MAX_TEMPORAL_INT:
            address = current_temporal_int_address
            current_temporal_int_address += 1
            return address
        else:
            raise Exception("Limite de variables enteras.")
    elif var_type == FLOAT:
        if current_temporal_float_address < MAX_TEMPORAL_FLOAT:
            address = current_temporal_float_address
            current_temporal_float_address += 1
            return address
        else:
            raise Exception("Limite de variables flotantes.")
    elif var_type == BOOL:
        if current_temporal_bool_address < MAX_TEMPORAL_BOOL:
            address = current_temporal_bool_address
            current_temporal_bool_address += 1
            return address
        else:
            raise Exception("Limite de variables booleanas.")
    else:
        raise Exception("Tipo de variable temporal no reconocido.")


# Función para manejar la declaración de variables globales
def handle_global_vars(id_list, var_type):
    #Paso por cada variable del contexto global
    for var_id in id_list:
        #Verifico el tipo de la variable y le asigno su direccion a cada variable global
        address = assign_global_memory(var_type)
        directorio_funciones['global']['vars'][var_id] = {
            'type': var_type,
            'address': address
        }

# Función para manejar la declaración de variables locales a una función
def handle_local_vars(current_name, id_list, var_type):
    #Paso por cada variable del contexto local
    for var_id in id_list:
        #Verifico el tipo de la variable y le asigno su direccion a cada variable local
        address = assign_local_memory(var_type)
        directorio_funciones[current_name]['vars'][var_id] = {
            'type': var_type,
            'address': address
        }


#Imprimo lo guardado en mi directorio de funciones
def imprimir_directorio_funciones(directorio):
    print("Directorio de Funciones:")
    for nombre_funcion, info_funcion in directorio.items():
        print(f"\nFunción: {nombre_funcion}")
        print(f"  Tipo de retorno: {info_funcion['tipo']}")
        print(f"  Cantidad de parámetros: {len(info_funcion['params'])}")
        print("  Parámetros:")
        for param in info_funcion['params']:
            print(f"    {param[0]}: {param[1]}")
        print("  Variables Locales:")
        for var_nombre, var_info in info_funcion['vars'].items():
            print(f"    {var_nombre}:")
            print(f"      Tipo: {var_info['type']}")
            if 'size' in var_info:  # Es un arreglo
                print(f"      Dirección base: {var_info['base_address']}")
                print(f"      Límites: [{var_info['lower_bound']}, {var_info['upper_bound']}]")
                print(f"      Tamaño: {var_info['size']}")
            else:  # Es una variable normal
                print(f"      Dirección: {var_info['address']}")
#Aqui imprimo la tabla de constantes y direcciones
def imprimir_tabla_constantes(tabla_cte):
    print("/////Tabla de Constantes/////")
    for constante, info in tabla_cte.items():
        print(f"Cons {constante}, Dir: {info['address']}")


#/////////////////////PUNTOS NEURLAGICOS/////////////////////

#Estructura
#Punto para hacer el salto al main
def p_goto_main(p):
    '''goto_main : '''
    global cuad
    cuad.append(('GOTO', 'Main', '', None))  # Se deja el lugar de salto como None para luego actualizarlo

def p_aux_goto_main(p):
    '''aux_goto_main : '''
    global cuad
    cuad[0] = (cuad[0][0], cuad[0][1], cuad[0][2], len(cuad)) 


#IF

#Punto que verficia la expresion, guarda la posicion del gotof y genera su cuadruplo
def p_verificar_if(p):
    '''verificar_if : '''
    global cuad, pila_saltos, pila_operandos, pila_tipos
    #Se guarda el resultado de la expresion
    result_condicion = pila_operandos.pop()
    exp_type = pila_tipos.pop()
    #Verifico que sea el tipo de dato correcto
    if exp_type != BOOL:
        raise Exception("Error de tipo: Se esperaba una expresión booleana")
    else:
        cuad.append(('GotoF', result_condicion, '', None))  # Se deja el lugar de salto como None para luego actualizarlo
        jump_position_if = len(cuad) - 1
        pila_saltos.append(jump_position_if)

#Punto que verifica a donde salta el gotof o el goto dependiendo si es if o ifelse
def p_verificar_bloque_if(p):
    '''verificar_bloque_if : '''
    global cuad, pila_saltos
    if len(p) == 1:  # Si es if-else sobrescribe el cuadruplo para el salto goto
        jump_position_else = pila_saltos.pop()
        cuad[jump_position_else] = (cuad[jump_position_else][0], cuad[jump_position_else][1], cuad[jump_position_else][2], len(cuad))

    else:  # Si solo tiene un if, sobreescribo el cuadruplo del gotof con el salto
        jump_position_if = pila_saltos.pop()
        cuad[jump_position_if] = (cuad[jump_position_if][0], cuad[jump_position_if][1], cuad[jump_position_if][2], len(cuad))


#Punto que verifica el bloque del else, genera el cuadruplo del else y guarda su posicion
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

#Punto que guarda la posicion del while 
def p_save_position_while(p):
    '''save_position_while : '''
    global pila_saltos, cuad
    #Guardo en que posicion esta el while en la pila para el goto
    pila_saltos.append(len(cuad))

#Punto que verifica el tipo de dato generado de la expresion y se genera el cuadruplo del gotof
def p_check_while_exp(p):
    '''check_while_exp : '''
    global pila_tipos, pila_operandos, cuad, pila_saltos
    exp_type = pila_tipos.pop()
    #Verifico que sea el tipo de dato correcto
    if exp_type != BOOL:
        raise Exception("Error de tipo: Se esperaba una expresión booleana")
    else:
        #Genero el cuadruplo del gotof y guardo la posicion
        result = pila_operandos.pop()
        cuad.append(('GotoF', result, '', None))
        pila_saltos.append(len(cuad) - 1)

#Punto que llena los saltos del goto y gotof del while
def p_fill_jump_while(p):
    '''fill_jump_while : '''
    global pila_saltos, cuad
    #Le hago pop a el salto del gotof
    inicio_while = pila_saltos.pop(-2)
    goto_f_position = pila_saltos.pop()
    cuad.append(('GOTO', '', '', inicio_while))
    #Actualizo el salto del gotof del while
    cuad[goto_f_position] = (cuad[goto_f_position][0], cuad[goto_f_position][1], cuad[goto_f_position][2], len(cuad))



#FUNCIONES
#Funcion que guarda el tipo, el nombre y valida que no exista la funcion

def p_insert_dirfunc(p):
    '''insert_dirfunc :'''
    global current_function, current_temporal_int_address, current_temporal_float_address
    current_name = p[-1]  # El nombre de la función es el último token reconocido
    current_type = p[-2] if p[-2] != 'VOID' else None  # 'None' para funciones sin tipo de retorno
    
    # Verificar la semántica
    if current_name in directorio_funciones:
        raise Exception(f"Error: La función '{current_name}' ya está declarada.")
    else:
        ret_address = None
        if current_type == 'int':
            ret_address = current_temporal_int_address
            current_temporal_int_address += 1
        elif current_type == 'float':
            ret_address = current_temporal_float_address
            current_temporal_float_address += 1
        # Añadir otros tipos según sea necesario
        
        # Insertar en la tabla DirFunc
        directorio_funciones[current_name] = {
            'tipo': current_type,
            'vars': {},
            'params': [],
            'cuad_start': None,  # Esto se actualizará cuando se defina el inicio del bloque de la función
            'ret_address': ret_address  # Agregar la dirección de retorno
        }
    # La función actual pasa a ser la función que se está definiendo
    current_function = current_name
    p[0] = current_name 


#Punto que guarda los parametros y les asigna direcciones locales
def p_save_params(p):
    '''save_params : '''
    global current_function, directorio_funciones, param_table
    params = p[-2]
    if current_function != 'global':
        param_count = 0
        for param_type, param_name in params:
            address = assign_local_memory(param_type)
            directorio_funciones[current_function]['vars'][param_name] = {
                'type': param_type,
                'address': address
            }

            # Cambio aquí: Ahora guardamos una tupla con el nombre, tipo y dirección
            directorio_funciones[current_function]['params'].append((param_name, param_type, address))
            param_count += 1

        directorio_funciones[current_function]['param_count'] = param_count
    else:
        print("Error: intentando agregar parámetros fuera del contexto de una función")


#Punto que guarda las variables locales de una funcion
def p_vars_local(p):
    '''vars_local : VAR vars'''
    global current_function, directorio_funciones, cuad
    local_vars = p[2]
    #Verifico que no este en el main
    if current_function != 'global' and local_vars is not None:
        #Le asigno su direccion de memoria a las variables locales de la funcion
        for var_name, var_type in local_vars:
            address = assign_local_memory(var_type)
            directorio_funciones[current_function]['vars'][var_name] = {
                'type': var_type,
                'address': address
            }
        cuad_start = len(cuad)
        print(cuad_start)
    elif current_function == 'global':
        raise Exception("Error: Declaracion de variables locales en contexto global.")   
    
#Punto donde guardo el inicio de generacion de cuadurplos de la funcion
def p_bloque_func(p):
    '''bloque_func : start_cuad bloque'''

def p_start_cuad(p):
    '''start_cuad : '''
    global cuad, directorio_funciones, current_function
    if current_function != 'global':
        #Guardo el numero de cuadruplo en donde inicia las intrucciones de la funcion
        start_quad = len(cuad) 
        directorio_funciones[current_function]['cuad_start'] = start_quad
    else:
        raise Exception("Error: No se pueden asignar el inicio del cuadurplo de contexto global")   
    

#Punto donde termina la funcion y genera el cuadruplo, ademas de resetear datos de 
# nombre de funciones y temporales
def p_end_function(p):
    '''end_function : '''
    global cuad, pila_operandos, current_function, temporal_count, current_local_bool_address, current_local_char_address, current_local_int_address, current_local_float_address
    
    # Verificar si la función actual tiene un tipo de retorno y no es void
    if directorio_funciones[current_function]['tipo'] is not None:
        if len(pila_operandos) > 0:
            # Pop el valor de retorno de la pila de operandos
            return_value = pila_operandos.pop()
            # Obtener la dirección de retorno de la función actual
            ret_address = directorio_funciones[current_function]['ret_address']
            # Generar cuádruplo para asignar el valor de retorno a la dirección de retorno
            cuad.append(('=', return_value, '', ret_address))
        else:
            raise Exception(f"Error: Función '{current_function}' esperaba un valor de retorno.")
    cuad.append(('ENDFunc', '', '', ''))

    #Reseteo las variables locales
    current_local_int_address = local_int
    current_local_float_address = local_float
    current_local_char_address=local_char
    current_local_bool_address=local_bool

    # Reseteo el contador de variables temporales
    temporal_count = 0
    # Me regreso al contexto global ("main")
    current_function = 'global'
               
#Punto que genera el cuadruplo que me regresa a la funcion
def p_generate_gosub(p):
    '''generate_gosub :'''
    global current_function_call, cuad, param_counter

    if current_function_call is not None:
        start_address = directorio_funciones[current_function_call]['cuad_start']
        ret_address = directorio_funciones[current_function_call]['ret_address']  # Asumiendo que 'ret_address' es donde se almacena el valor de retorno

        # Genera el cuádruplo GOSUB
        cuad.append(('GOSUB', current_function_call, '', start_address))

        # Genera un cuádruplo para asignar el valor de retorno a un temporal
        temp_ret = generate_temporal(directorio_funciones[current_function_call]['tipo'])
        print ("temp_ret", temp_ret)
        cuad.append(('=', ret_address, '', temp_ret))

        # Agrega el temporal a la pila de operandos y tipos
        pila_operandos.append(temp_ret)
        pila_tipos.append(directorio_funciones[current_function_call]['tipo'])

    # Reinicia para la siguiente llamada a función
    current_function_call = None
    param_counter = 0


def p_call_func(p):
    '''call_func : ID func_name_call PARIZQ gen_era argumentos_llamada verify_param_count PARDER generate_gosub PUNCOM'''
    
def p_argumentos_llamada(p):
    '''argumentos_llamada : expresion verify_argument_type COMA argumentos_llamada
                          | expresion verify_argument_type 
                          | empty'''
    if len(p) == 4:
        # Manejar múltiples argumentos
        p[0] = [p[1]] + p[4]
    elif len(p) == 3:
        # Manejar un solo argumento
        p[0] = [p[1]]
    else:
        # No hay argumentos
        p[0] = []
    
def p_func_name_call(p):
    '''func_name_call :'''
    global current_function_call, param_counter

    function_name = p[-1]
    if function_name not in directorio_funciones:
        raise Exception(f"Error: La función '{function_name}' no está declarada.")

    current_function_call = function_name

def p_gen_era(p):
    '''gen_era :'''
    global param_counter
    function_name = p[-3]
    # Generar acción ERA
    era_size = None
    cuad.append(('ERA', '', era_size, function_name))


#Punto que verifica si la cantidad de parametros es la correcta
def p_verify_param_count(p):
    '''verify_param_count :'''
    global param_counter, current_function_call
    if current_function_call is not None:
        expected_param_count = len(directorio_funciones[current_function_call]['params'])
        if param_counter != expected_param_count:
            raise Exception(f"Error: Número incorrecto de argumentos para la función '{current_function_call}'. Esperado: {expected_param_count}, Recibido: {param_counter}")

#Punto que me ayuda a identificar si el tipo de dato que paso coincide con el parametro de la funcion
def p_verify_argument_type(p):
    '''verify_argument_type :'''
    global param_counter, current_function_call

    if pila_operandos:
        argument = pila_operandos.pop()
        argument_type = pila_tipos.pop()
        function_params = directorio_funciones[current_function_call]['params']

        if param_counter >= len(function_params):
            raise Exception(f"Error: Más argumentos de los esperados para la función '{current_function_call}'")

        # Obtenemos la dirección del parámetro desde la tupla almacenada
        param_address = function_params[param_counter][2]
        current_param_type = function_params[param_counter][1]

        if argument_type != current_param_type:
            raise Exception(f"Error de tipo: Argumento {argument_type} no coincide con el parámetro {current_param_type}")

        # Genera el cuádruplo de acción PARAMETER
        cuad.append(('PARAMETER', argument, '', param_address))
        param_counter += 1
    else:
        pass

parser = yacc.yacc()
def parse(data):
    return parser.parse(data)