#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

nombre = input("¿Podrías poner tu nombre, por favor?: ")
edad = int(input("¿Podrías poner tu edad, por favor?: "))
direccion = input("¿Podrías poner tu dirección, por favor?: ")
telefono = int(input("¿Podrías poner tu número de teléfono, por favor?: "))

# Crear un diccionario con los datos ingresados por el usuario
persona = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

# Mostrar la información almacenada en el diccionario
print(f"{persona['nombre']} tiene {persona['edad']} años, vive en {persona['direccion']} y su número de teléfono es {persona['telefono']}.")

