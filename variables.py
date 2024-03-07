# -*- coding: utf-8 -*-
# Definición de una variable y su impresión
variable = 5
print(variable)

# Múltiples asignaciones y sus impresiones
primera_variable, segunda_variable, tercera_variable = 1, "dos", 3
print(primera_variable)
print(segunda_variable)
print(tercera_variable)

# Cambio de valor en una variable
mi_primera_variable = "Hola mundo"
mi_segunda_variable = "Adiós mundo"
mi_primera_variable = mi_segunda_variable
print(mi_primera_variable)

# Operaciones matemáticas y tipos de números
numero = 5
resultado = numero + 7
print(resultado)

entero_largo = 326582376578923657892346578923657892365978236578236952637592635782369562375892356
print(entero_largo)

numero_complejo = 34 + 5j
print(numero_complejo)

numero_octal = 0o165
print(numero_octal)

numero_binario = 0b1001
print(numero_binario)

numero_hexadecimal = 0xB16A
print(numero_hexadecimal)

numero = 12e5
print(numero)

otro_numero = 4567e7
print(otro_numero)

# Uso de booleanos
elpepe = False
print(elpepe)

# Manejo de cadenas de texto
cadena = """Esta cadena ocupa más de una línea.
Y más de dos
por eso le ponemos triples comillas"""
print(cadena)

cadena_con_comillas = 'El signo "comillas" (") se usa en Python para acotar cadenas.'
print(cadena_con_comillas)

cadena_raw = r"Los signos como \n y \t no serán interpretados y se mostrarán tal y como están"
print(cadena_raw)

cadena_unicode = u"Texto de la cadena."
print(cadena_unicode)

# Operaciones y tipos de variables
texto = "Hola mundo"
entero = 21
print(type(texto))
print(type("Hola"))
print(type(14.5))
print(type(entero))
print(type(120343485034853498529035230582390582390582390582390859023852390))
print(type(True))

# Conversión entre tipos de datos
texto = "10"
decimal = 21.15
un_entero = int(texto)
print(type(texto))
print(type(decimal))
print(type(un_entero))
print(type(int(decimal)))
print(un_entero)

flotante = float(4)
print(flotante)
print(type(flotante))

# Operaciones con listas y manipulación
saludo = "Hola " + "Mundo"
gallina = 4 * "Co"
print(saludo)
print(gallina)

# Listas y sus operaciones
lista = ["silla", "mesa", "armario", "taburete"]
print("silla" in lista)
print("sofa" in lista)
print("mesa" not in lista)
print("sofa" not in lista)

# Operaciones binarias
numero1 = 0b1011
numero2 = 0b101
print(numero1)
print(numero2)
print(numero1 & numero2)

numero1 = 0b1001
numero2 = 0b1100
print(numero1)
print(numero2)
print(numero1 | numero2)

numero1 = 0b1001
numero2 = 0b1100
print(numero1)
print(numero2)
print(numero1 ^ numero2)

# Precedencia de operadores
resultado = 5 + 4 * 7
resultado2 = (5 + 4) * 7
print(resultado, resultado2)

# Manipulación de listas
lista = ["primero", "segundo", "tercero", "cuarto"]
print(lista)
lista = []
print(lista)
lista = list(("Hola", "mundo", "palabra"))
print(lista)
print(lista[2])
lista[2] = "Nuevo Elemento"
print(lista[2])
print(lista)
del lista[2]
print(lista)

# Listas anidadas
lista = [[1, 2, 3], ["a", "b", "c"]]
print(lista[1][0])
print(lista[0][2])

# Uso de índices y slicing en listas
lista = ["primero", 2, "tercero", ["a", "b", "c"]]
print(lista[2])
print(lista[3][0])
print(lista[-1])
print(lista[1:4])
print(lista[:3])
print(lista[1:])

# Copia de listas
lista2 = lista[1:4]
print(lista2)
lista2[0:2] = ["otro", "Y otro"]
print(lista2)

# Operaciones con conjuntos y comprobación de identidad
cubiertos = {"tenedor", "cuchara", "cuchillo", "cucharilla"}
vajilla = set(["plato", "taza", "copa"])
print(cubiertos)
print(vajilla)

conjunto = set()
variable1 = "Hola"
variable2 = variable1
variable3 = "Adios"
print(id(variable1))
print(id(variable2))
print(id(variable3))

# Manipulación de variables y referencias
lista = ["Hola", "mundo", "palabra"]
print(id(lista))
lista[2] = "cosa"
print(id(lista))
copia_de_lista = lista
lista[2] = "cosa"
print(copia_de_lista[2])

# Creación de copias independientes
lista = ["Hola", "Chau"]
lista2 = list(lista)
print(id(lista))
print(id(lista2))
print(lista2)

# Manejo de diccionarios
diccionario = {"nombre": "Pablo"}
diccionario2 = dict(diccionario)
print(id(diccionario))
print(id(diccionario2))
print(diccionario2)
