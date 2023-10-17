import sys
from parser_1 import parse

# Define la tabla de símbolos como un diccionario global
symbol_table = {}

if len(sys.argv) < 2:
    print("Debe proporcionar un archivo para analizar")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, 'r') as f:
        data = f.read()
        result = parse(data)
        if result == "ACC":
            print("Correcto")
            print("Tabla de Símbolos:")
            for variable, tipo in symbol_table.items():
                print(f"Variable: {variable}, Tipo: {tipo}")
        else:
            print("Algo anda mal")
except FileNotFoundError:
    print(f"No se encontró un archivo '{filename}'")