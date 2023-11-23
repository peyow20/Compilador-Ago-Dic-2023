from parser_1 import parse, cuad, directorio_funciones, tabla_cte

# Leer el código fuente
#with open("/fregy/Documents/Compis_ago_dic/SerieFibo_while.txt", "r") as file:
 #   data = file.read()

# Ejecutar el parser
#parse(data)


class MaquinaVirtual:
    def __init__(self, cuad, directorio_funciones, tabla_cte):
        #Inicializo mi maquina virtual
        self.cuad = cuad
        self.directorio_funciones = directorio_funciones
        self.tabla_cte = tabla_cte
        #nicializo la memoria
        self.memoria = self.inicializar_memoria()
        self.p_cuad = 0  

    def inicializar_memoria(self):
        # Inicialización de la memoria para constantes y variables globales
        memoria = {}
        for cte, info in self.tabla_cte.items():
            memoria[info['address']] = cte

        for var_name, var_info in self.directorio_funciones['global']['vars'].items():
            memoria[var_info['address']] = None

        return memoria

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
            elif operacion == 'GotoF':
                self.goto_f(cuad)
            elif operacion == 'GOTO':
                self.goto(cuad)
            elif operacion == 'write':
                self.write(cuad)
            elif operacion == 'read':
                self.read(cuad)
            #Paso al siguiente paso
            self.p_cuad += 1

    def get_value(self, address):
        return self.memoria.get(address, None)

    def set_value(self, address, value):
        self.memoria[address] = value

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


    def get_variable_name(self, address):
        for func_name, func_info in self.directorio_funciones.items():
            for var_name, var_info in func_info['vars'].items():
                if var_info['address'] == address:
                    return var_name

        # Si no encuentra la dirección, retorna None o lanza un error
        return None
    
    #Esta funcion me ayuda a obtener el tipo
    def get_variable_type(self, address):
        #Verifico si esta en la tabla de constantes
        if address in self.tabla_cte:
            return type(self.tabla_cte[address]['value']).__name__
        #Verifico si la variable esta en el directorio de funciones y verifico si tp_cuado
        for func_info in self.directorio_funciones.items():
            for var_info in func_info['vars'].items():
                if var_info['address'] == address:
                    return var_info['type']

    # Si la direccion no esta en tabla ni en directorio, regresa nulo
        return None



# Creación y ejecución de la máquina virtual
vm = MaquinaVirtual(cuad, directorio_funciones, tabla_cte)
vm.run()