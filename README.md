# symbol-table

## Elementos presentes en el programa

### Tipos de datos
- `int`
- `float`
- `string`
- `char`

### Identificadores o símbolos
El símbolo corresponde al nombre de la variable o de la función.
Por ejemplo:
- `int foo()`
La cadena `foo` corresponde al símbolo. Mientra que `int` es el tipo de dato.
- `string var`
La cadena `var` corresponde al símbolo. Mientra que `string` es el tipo de dato.  

### Enfoques

- Programa principal: Desde la primer linea del archivo de texto hasta la última, **exista o no** una función ***main***.
- Uso de la palabra reservada ***if***: Este bloque comienza desde el cierre del paréntesis de la expresión y se extiende hasta "".
- Uso de la palabra reservada ***while***: Este bloque comienza desde el cierre del paréntesis de la expresión y se extiende hasta "".

### Errores

Para cada error (en cuanto a símbolos) en el archivo de texto, existirá un código y una descripción (`string`) asociada a este, para la notificación al usuario.

| Código |                                                  Descripción                                                  |
|:------:|:-------------------------------------------------------------------------------------------------------------:|
|    1   | El identificador <`identificador`> no está declarado en este enfoque.                                           |
|    2   | El tipo de valor de retorno no coincide con el valor de retorno de <`función`>.                                 |
|    3   | La lista de parámetros de la función <`función`> no coincide con los parámetros <`parámetros erróneos`>.          |
|    4   | No es posible la operación lógica <`operación`> entre los identificadores <`identificador1, identificador2`>.     |
|    5   | No es posible la operación aritmética <`operación`> entre los identificadores <`identificador1, identificador2`>. |
|    6   | Doble declaración de identificador <`identificador`>.                                                           |
|    7   | ...                                                                                                           |
|    n   | ...                                                                                                           |
# DISEÑO 1 (PRIMER PROTOTIPO)

## `SymbolTable`

Una clase que implementa las funcionalidades básicas de una tabla de símbolos:
- `lookup(<identificador>)`
- `insert(<identificador>, <tipo de dato>)`

## `TextfileReader`

Esta clase tiene la responsabilidad de leer un archivo de texto mientras carga su contenido en una  instancia de la clase SymbolTable.

Siendo un sub-árbol n-ario *A* y su raíz *r*.
El contenido o valor asociado al vértice *r* se trata de una instancia *ST* de la clase `SymbolTable`, donde esta representa el enfoque principal del código fuente. El conjunto de elementos en *ST* está conformado por cada uno de los símbolos declarados en el enfoque.
