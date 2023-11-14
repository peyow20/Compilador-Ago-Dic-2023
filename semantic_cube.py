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


def verificar_result(operador_izq, operador_der, operador):
    if (operador_izq, operador_der, operador) in SEMANTIC_CUBE:
        resultado = SEMANTIC_CUBE[(operador_izq, operador_der, operador)]
        return f"El resultado es válido: {resultado}"
    else:
        return 'ERROR'