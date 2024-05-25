"""
¿Qué es un diccionario en Python y cuál es su característica principal?

Respuesta: Un diccionario es una variable en donde se puede guardar tanto claves como valores y su caracteristica principal es que se puede guardar claves y valores

¿Cómo se crea un diccionario en Python? Proporciona un ejemplo.

Respuesta: diccionario = {'clave': 'valor'}

¿Qué tipos de datos se pueden utilizar como claves y valores en un diccionario?

Respuesta: string, int, float, bolean

Explica cómo se accede a los valores en un diccionario en Python.

Respuesta: diccionario['clave']

Menciona al menos tres métodos importantes disponibles para trabajar con diccionarios en Python.

Respuesta: pop(), remove(), append()
"""

#Escribe un programa que cree un diccionario para almacenar los nombres y las edades de algunas personas. Luego, solicita al usuario que ingrese un nombre y muestra la edad correspondiente si existe en el diccionario.
 
# Creación de dos diccionarios para almacenar información sobre dos personas
persona1 = {
    'Nombre': 'Steven',
    'Edad': 20
}

persona2 = {
    'Nombre': 'Alicia',
    'Edad': 40 
}

# Solicita al usuario que ingrese su nombre
nombre = input("¿Podrías poner tu nombre, porfa?: ")
 
# Compara el nombre ingresado (después de aplicar .capitalize()) con los nombres en los diccionarios
if nombre.capitalize() == persona1['Nombre']:
    print(f"Tu edad es de:", persona1['Edad'])  # Muestra la edad de Steven si el nombre coincide
elif nombre.capitalize() == persona2['Nombre']:
    print(f"Tu edad es de:", persona2['Edad'])  # Muestra la edad de Alicia si el nombre coincide
else:
    print("No apareces en el diccionario")  # Si no coincide con ningún nombre, muestra este mensaje



#No se como hacer los siguientes ejercicios
"""#Escribe un programa que cuente la frecuencia de las letras en una cadena de texto y almacene el resultado en un diccionario.

palabra = "elpepe"

if palabra.find("e"):
    print("a")

#Nota: No sé como hacerlo.

#Crea dos diccionarios con datos similares y combínalos en uno solo. Luego, elimina las claves duplicadas.
persona1 = {
    'Nombre': 'Sara',
}

persona2 = {
    'Nombre': 'Sara',
}

print(pow(persona1), pow(persona2))

#Nota: No sé como hacerlo.


Escribe un programa que solicite al usuario que ingrese una palabra y muestre el número de veces que aparece cada letra en esa palabra utilizando un diccionario.
#Nota: No sé como hacerlo.


Escribe un programa que genere un diccionario de números enteros como claves y sus raíces cuadradas como valores.

numeros = {
    1: 1,
    2: 4,
    3: 9
}

#Nota: No lo pude hacer"""