from parser_1 import parse, cuad, directorio_funciones, tabla_cte

class MaquinaVirtual:
    def __init__(self, cuad, directorio_funciones, tabla_cte):
        #Inicializo mi maquina virtual
        self.cuad = cuad
        self.directorio_funciones = directorio_funciones
        self.tabla_cte = tabla_cte
        #nicializo la mememoria
        self.mem = self.inicializar_mem()
        self.pila_retornos = []
        self.pila_contextos = []
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
            #elif operacion == 'ERA':
             #   self.era(cuad)
            #elif operacion == 'GOSUB':
             #   self.gosub(cuad)
            #elif operacion == 'RET':
             #   self.ret(cuad)
            #elif operacion == 'ENDFunc':
             #   self.end_func(cuad)
            #Paso al siguiente paso
            self.p_cuad += 1



    
    #def era(self, cuad):

    # Inicializar variables locales
        

    #def gosub(self, cuad):



    #def ret(self, cuad):


    #def end_func(self, cuad):

    
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

    def asignacion(self, cuad):
        value = self.get_value(cuad[1])
        result_address = cuad[3]
        self.set_value(result_address, value)

    def goto_f(self, cuad):
        condition = self.get_value(cuad[1])
        if not condition:
            self.p_cuad = cuad[3] - 1

    def goto(self, cuad):
        self.p_cuad = cuad[3] - 1

    def write(self, cuad):
        value = self.get_value(cuad[1]) if cuad[1] != '' else cuad[1]
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
            else:  # Para 'char' o cualquier otro tipo, lo deja como string
                converted_value = input_value

            # Almacena el valor convertido
            self.set_value(var_address, converted_value)
        else:
        # Manejar el error o la situación de no encontrar el nombre
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