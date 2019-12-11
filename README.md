# symbol-table implementation
# Universidad Nacional de Costa Rica, Curso Estructuras de Datos - II Ciclo, 2019.
# Integrandes del grupo:
# Alvaro Daniel Delgado Brenes
# Isaac Touma Rodriguez
# Alexander Brenes Brenes

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
|    6   | Doble declaración de identificador <`identificador`>.                                                           |

# DISEÑO FINAL

## `SymbolTable`

Una clase que implementa las funcionalidades básicas de una tabla de símbolos:

- `lookup(<identificador>)`
- `insert(<identificador>, <tipo de dato>)`
- `concatenate_scopes(upper_scope)`
- `add_upper_scope(upper_scope)`

Los dos últimos utilizados para el manejo de los diferentes enfoques, es decir,por ejemplo para poder buscar si una variable utilizada en un método y no ha sido declarada ahí mismo, fue declarada en un enfoque superior (upper_scope) como lo sería en el enfoque global.

## `FileAnalizer`

Esta clase tiene la responsabilidad de leer un archivo de texto mientras carga su contenido en instancias de la clase SymbolTable. Siendo cada SymbolTable utilizada para representar los diferentes enfoques del código.
