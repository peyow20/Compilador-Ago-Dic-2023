# Compilador-Ago-Dic-2023
### Alfredo Jose Welsh Martinez A00825988
## Avance 1
Se declararon todos los tokens y palabras reservadas ademas de realizarse casi toda la sintaxis, ya que aun tiene un par de errores

## Avance 2
Se arreglo la sintaxis, se hizo el cubo semantico, y se realizo parte de la semantica basica, solo se creo tabla de variables y se agregaban

## Avance 4
Se establecieron direcciones de memoria y se establecieron se agregaron las estructuras necesarias. Se tuvo un problema y la tabla de variables y cuadruplos no estan listos, hubo un error y se va a rehacer

## Avance 5
Se hizo un cambio en la forma que se realizaran los puntos neuralgicos

## Avance 6
Se agregaron y desarrollaron varios puntos neuralgicos y se empezo con la creacion de cuadruplos

## Avance 7
Se tienen ya cuadruplos de asignacion y en un 80% de expresiones

## Avance 8
Se estan terminando funciones con su direccionamiento adecuado


# MANUAL DE USUARIO


Estructura del programa
```
program *NOMBRE DEL PROGRAMA*;
var
    /*DECLARACION DE VARIABLES PARA EL MAIN: INT, FLOAT, BOOL*/
    x,y,z:int

/*EN CASO DE TENER, DESARROLLAR AQUI FUNCIONES*/
func int suma(int a, int b)
var
    /*DECLARACION DE VARIABLES PARA LA FUNCION: INT, FLOAT, BOOL*/
    x,y,z:int
{
/*BLOQUE DE CODIGO*/
}
return /*Expresion*/;

/*INICIALIZAR EL MAIN*/
main()
{
/*BLOQUE DE CODIGO*/
}
```


## OPCION DE "BLOQUE"
```
/*SE PUEDEN REALIZAR MULTIPLES EXPRESIONES ARITMETICAS EN LA MISMA LINEA, CON PPRIORIDAD CLASICA*/
SUMAS -> x=x+y;
RESTAS -> x=x-y;
MULTIPLICACION -> x=x*y;
DIVISION -> x=x/y;
ASGINACION -> x=x+1;
/*SE PUEDEN INDEXAR MULTIPLES COMPARACIONES*/
CONDICIONES IF-> if(x>y){
                  x=x-1;   
                  };
CONDICIONES IF-ELSE-> if(x>y){
                  x=x-1;   
                  }else{
                  x=x+1;
                   };
CONDICIONES WHILE-> while (x>y) do{
                    x=x-1;
                    }
/*EXPRESIONES CONDICIONALES VALIDAS*/
MAYOR QUE -> >
MENOR QUE -> <
IGUAL QUE -> ==
MAYORIGUAL -> >=
MENORIGUAL -> <=
DIFFERENTE -> !=
AND -> &&
OR -> ||
```
