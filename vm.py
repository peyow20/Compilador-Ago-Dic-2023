from parser_1 import parse, cuad, directorio_funciones, tabla_cte

class MaquinaVirtual:
    def __init__(self, cuad, directorio_funciones, tabla_cte):
        #Inicializo mi maquina virtual
        self.cuad = cuad
        self.directorio_funciones = directorio_funciones
        self.tabla_cte = tabla_cte
        self.salto = []
        self.return_value = None
        self.current_function = 'global'
        #nicializo la mememoria
        self.mem = self.inicializar_mem()
        self.p_cuad = 0  

    def inicializar_mem(self):
        # Inicialización de la mem para constantes y variables globales
        mem = {}
        for cte, info in self.tabla_cte.items():
            mem[info['address']] = cte

        for var_name, var_info in self.directorio_funciones['global']['vars'].items():
            mem[var_info['address']] = None
        return mem

    def run(self):
        #Recorro cada cuadruplo
        while self.p_cuad < len(self.cuad):
            cuad = self.cuad[self.p_cuad]
            #Identifico el tipo de operacion
            operacion = cuad[0]
            # Manejo de diferentes operaciones
            if operacion == '+':
                self.operacion_aritmetica(cuad, operacion)
            elif operacion == '-':
                self.operacion_aritmetica(cuad, operacion)
            elif operacion == '*':
                self.operacion_aritmetica(cuad, operacion)
            elif operacion == '/':
                self.operacion_aritmetica(cuad, operacion)
            elif operacion == '=':
                self.asignacion(cuad)
            elif operacion in ['>', '<', '>=', '<=', '==', '!=']:
                self.operacion_comparacion(cuad, operacion)
            elif operacion == 'AND':
                self.operacion_logica(cuad, operacion)
            elif operacion == 'OR':
                self.operacion_logica(cuad, operacion)
            elif operacion == 'GotoF':
                self.goto_f(cuad)
            elif operacion == 'GOTO':
                self.goto(cuad)
            elif operacion == 'write':
                self.write(cuad)
            elif operacion == 'read':
                self.read(cuad)
            elif operacion == 'GOSUB':
               self.gosub(cuad)
            elif operacion == 'ret':
                self.ret(cuad)
            elif operacion == 'ENDFunc':
                self.end_func(cuad)
            elif operacion == 'PARAMETER':
                self.parameter(cuad)
            #Paso al siguiente paso
            self.p_cuad += 1


#En base a la direccion de los argumentos mandados a la funcion, les asigan su valor a la direccion de los parametros de las funciones
    # Inicializar variables locales
    def parameter(self, cuad):
        arg_address = cuad[1]  # Guardo la direccion del argumento en el cuadruplo
        arg_value = self.get_value(arg_address)  # Obtengo el valor del argumento
        param_address = cuad[3]  # Obtengo la direccion del parametro
        self.set_value(param_address, arg_value) # Le asigno el valor del argumento al parametro

#Basicamente guardo el valor del retorno en base a la direccion de la misma
    def ret(self, cuad):
        # Capturo el valor de retorno
        return_value = self.get_value(cuad[3])
    
        # Obtengo la dirección de retorno para la función actual
        ret_address = self.directorio_funciones[self.current_function]['ret_address']
        
        # Asignar el valor de retorno a la dirección de retorno
        self.set_value(ret_address, return_value)

#Guardo en donde estoy haciendo el salto para luego regresar
    def gosub(self, cuad):
        # Guardo el salto para el termino de la funcion
        self.salto.append(self.p_cuad + 1)
        # Saltar a la dirección de inicio de la función
        self.p_cuad = cuad[3] - 1  #

#Funcion que me devuelve al contexto donde mande llamar la funcion
    def end_func(self, cuad):
        self.p_cuad = self.salto.pop() - 1
            
    def asignacion(self, cuad):
        value = self.get_value(cuad[1])
        result_address = cuad[3]
        self.set_value(result_address, value)
    
#Obtengo el valor de la direcciones de memoria
    def get_value(self, address):
        value = self.mem.get(address, None)
        if value is not None:
            if isinstance(value, str):
                if value.lower() in ['true', 'false']:
                    return value.lower() == 'true'
                try:
                    if '.' in value:
                        return float(value)
                    else:
                        return int(value)
                except ValueError:
                    pass  # Si no se puede convertir, deja el valor como está (string)
        return value
    
    #Establezco el valor de una direccion de memoria
    def set_value(self, address, value):
        self.mem[address] = value

    def operacion_aritmetica(self, cuad, operacion):
        left_operand = self.get_value(cuad[1])
        right_operand = self.get_value(cuad[2])
        result_address = cuad[3]
        if left_operand is None or right_operand is None:
            raise Exception("Operación aritmética con operandos no inicializados")

        if operacion == '+':
            result = left_operand + right_operand
        elif operacion == '-':
            result = left_operand - right_operand
        elif operacion == '*':
            result = left_operand * right_operand
        elif operacion == '/':
            result = left_operand / right_operand
        self.set_value(result_address, result)

    def operacion_comparacion(self, cuad, operacion):
        left_operand = self.get_value(cuad[1])
        right_operand = self.get_value(cuad[2])
        result_address = cuad[3]
        if left_operand is None or right_operand is None:
            raise Exception("Operación de comparación con operandos no inicializados")

        if operacion == '>':
            result = left_operand > right_operand
        elif operacion == '<':
            result = left_operand < right_operand
        elif operacion == '>=':
            result = left_operand >= right_operand
        elif operacion == '<=':
            result = left_operand <= right_operand
        elif operacion == '==':
            result = left_operand == right_operand
        elif operacion == '!=':
            result = left_operand != right_operand

        self.set_value(result_address, result)
    
    def operacion_logica(self, cuad, operacion):
        left_operand = self.get_value(cuad[1])
        right_operand = self.get_value(cuad[2])
        result_address = cuad[3]

        if left_operand is None or right_operand is None:
            raise Exception("Operación lógica con operandos no inicializados")
        
        left_operand = bool(left_operand)
        right_operand = bool(right_operand)

        if operacion == 'AND':
            result = left_operand and right_operand
        elif operacion == 'OR':
            result = left_operand or right_operand

        self.set_value(result_address, result)

    def goto_f(self, cuad):
        condition = self.get_value(cuad[1])
        if not condition:
            self.p_cuad = cuad[3] - 1

    def goto(self, cuad):
        self.p_cuad = cuad[3] - 1

    def write(self, cuad):
    # Verifica si el primer elemento del cuádruplo es una dirección
        if isinstance(cuad[1], int):
            value = self.get_value(cuad[1])
        else:
        # Si no es una direccion, usa el valor del cuaduplo
            value = cuad[1]

    # Imprime el valor
        print(value)

    def read(self, cuad):
        var_address = cuad[3]
        #Obtengo la informacion de la variable
        var_name = self.get_variable_name(var_address)
        result_type = self.get_variable_type(var_address)
        #Se verifica si la variable existe
        if var_name is not None:
            input_value = input(f"Ingrese un valor para {var_name}: ")
            #Convierto el dato recibido en su respectivo tipo
            if result_type == 'int':
                converted_value = int(input_value)
            elif result_type == 'float':
                converted_value = float(input_value)
            elif result_type == 'bool':
                pass
            else: 
                converted_value = input_value

            # Almacena el valor convertido
            self.set_value(var_address, converted_value)
        else:
           pass

    #Obtengo la informacion de las variables de mi directorio(direccion)
    def get_variable_name(self, address):
        for func_name, func_info in self.directorio_funciones.items():
            for var_name, var_info in func_info['vars'].items():
                if var_info['address'] == address:
                    return var_name

        # Si no encuentra la dirección, retorna None o lanza un error
        return None
    
    #Esta funcion me ayuda a obtener el tipo de una constante
    def get_variable_type(self, address):
        if address in self.tabla_cte:
            return type(self.tabla_cte[address]['value']).__name__

    # Verifico si la variable está en el directorio de funciones
        for func_name, func_info in self.directorio_funciones.items():
            if address in func_info['vars']:
                var_info = func_info['vars'][address]
                return var_info['type']

    # Si la dirección no está en tabla ni en directorio, regresa None
        return None



# Creación y ejecución de la máquina virtual
vm = MaquinaVirtual(cuad, directorio_funciones, tabla_cte)
vm.run()