import sys
from parser_1 import parse

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
        else:
            print("Algo anda mal")
except FileNotFoundError:
    print(f"No se encontro un archivo '{filename}'")