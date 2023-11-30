import sys
from parser_1 import parse, cuad, directorio_funciones, tabla_cte
from vm import MaquinaVirtual

if len(sys.argv) < 2:
    print("Debe proporcionar un archivo para analizar")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, 'r') as f:
        data = f.read()
        result = parse(data)
        if result == "ACC":
            print("Corriendo...")
            # Crear y ejecutar la máquina virtual
            vm = MaquinaVirtual(cuad, directorio_funciones, tabla_cte)
            vm.run()
        else:
            print("Algo anda mal")
except FileNotFoundError:
    print(f"No se encontró un archivo '{filename}'")