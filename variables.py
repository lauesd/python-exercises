# -*- coding: utf-8 -*-
# Variables 
variable = 5
print (variable)

primera_variable, segunda_variable, tercera_variable = 1, "dos", 3

print (primera_variable)
print (segunda_variable)
print (tercera_variable)

mi_primera_variable = "Hola mundo"
mi_segunda_variable = "Adiós mundo"

print (mi_primera_variable)

# Cambio de valor en una variable
mi_primera_variable = mi_segunda_variable

print (mi_primera_variable)


numero = 5 
resultado = numero + 7

print (resultado)

# Numero de tipo Long
entero_largo = 326582376578923657892346578923657892365978236578236952637592635782369562375892356

print(entero_largo)

# Número de tipo complejo
numero_complejo = 34 + 5j

print (numero_complejo)

# Número octal
numero_pctal = 0o165

print (numero_pctal)

# Número binario

numero_binario = 0b1001

print(numero_binario)

# Número hexadecimal
numero_hexadecimal = 0xB16A

print(numero_hexadecimal)

numero = 12e5

print (numero)
# Equivale a 12 * 10^5 = 1200000

otro_numero = 4567e7

print(otro_numero)
# Equivale a 4567 * 10^7 = 45670000000

elpepe = False

print(elpepe)

cadena = """Esta cadena ocupa más de una línea.
Y más de dos
por eso le ponemos triples comillas"""

print(cadena)

cadena_con_comillas = 'El signo "comillas" (") se usa en Python para acotar cadenas.'

print(cadena_con_comillas)

cadena_con_comillas = "El signo \"comillas\" (\") se usa e Python para acotar cadenas de texto"

print(cadena_con_comillas)

cadena = "Esto va a en una linea. \nY esto en la siguiente."

print(cadena)

cadena_raw = r"Los signos como \n y \t no serán interpretados y se mostrarán tal y como están"

print(cadena_raw)

cadena_unicode = u"Texto de la cadena."

print(cadena_unicode)

texto = "Hola mundo"
entero = 21

print (type(texto))
print (type("Hola"))
print (type(14.5))
print (type(entero))
print (type(120343485034853498529035230582390582390582390582390859023852390))
print (type(True))

texto = "10"
decimal = 21.15
un_entero = int(texto)

print("""
Nuevo bichito""")
print(type(texto))
print (type(decimal))
print (type(un_entero))
print (type(int(decimal)))
print (un_entero)
print("""
Flotante""")

flotante = float(4)

print (flotante)
print (type(flotante))
print("""
Cadena""")

entero = 5
decimal = 21.15
cadena_entero = str(entero)
cadena_decimal = str(decimal)

print (cadena_entero)
print (type(cadena_entero))
print (cadena_decimal)
print (type(cadena_decimal))
print("""
Binarios, octales y hexadecimales"""
)

entero = 500
hexadecimal = hex(entero)
octal = oct(entero)
binario = bin(entero)

print (hexadecimal)
print (type(hexadecimal))
print (octal)
print (type(octal))
print (binario)
print (type(binario))