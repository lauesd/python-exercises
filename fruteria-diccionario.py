#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.



# Mi versión
productos = {
    'Platano': 1.35, 
    'Manzana': 0.80, 
    'Pera': 0.85, 
    'Naranja': 0.70
}

print("Buenas, esta es una tienda de productos ")
print(" ")

# Solicitar al usuario que ingrese una fruta
seleccion = input("¿Qué producto te gustaría llevar?: ")

# Verificar si la fruta está en el diccionario y calcular el precio total si está disponible
if seleccion.capitalize() in productos:
    print("El kilo de ese producto cuesta: ", productos[seleccion])
    print(" ")
    cantidad = float(input("¿Cúantos kilos te gustaría llevar?: "))
    print(" ")
    precio_total = productos[seleccion] * cantidad
    print("El precio total de tu compra es de", precio_total)
else:
    # Si la fruta no está en el diccionario, mostrar un mensaje de error
    print("Ese producto no está en nuestra tienda")



# ChatGPT
# Diccionario que contiene los precios de las frutas
productos = {
    'Platano': 1.35, 
    'Manzana': 0.80, 
    'Pera': 0.85, 
    'Naranja': 0.70
}

# Mostrar un mensaje de bienvenida
print("Bienvenido a la tienda de frutas!")
print()

# Solicitar al usuario que ingrese una fruta
seleccion = input("¿Qué fruta te gustaría llevar?: ")

# Verificar si la fruta está en el diccionario
if seleccion.capitalize() in productos:
    # Si la fruta está en el diccionario, solicitar la cantidad de kilos
    cantidad = float(input("¿Cuántos kilos te gustaría llevar?: "))
    
    # Calcular el precio total y mostrarlo por pantalla
    precio_total = productos[seleccion.capitalize()] * cantidad
    print(f"El precio total de {cantidad} kilos de {seleccion.capitalize()} es de ${precio_total:.2f}")
else:
    # Si la fruta no está en el diccionario, mostrar un mensaje de error
    print("Lo siento, esa fruta no está disponible en nuestra tienda.")



# Solución del ejercicio
# Diccionario que contiene los precios de las frutas
frutas = {'Plátano': 1.35, 'Manzana': 0.8, 'Pera': 0.85, 'Naranja': 0.7}

# Solicitar al usuario que ingrese una fruta
fruta = input('¿Qué fruta quieres? ').title()

# Solicitar al usuario que ingrese la cantidad en kilos
kg = float(input('¿Cuántos kilos? '))

# Verificar si la fruta está en el diccionario
if fruta in frutas:
    # Si la fruta está en el diccionario, calcular el precio total y mostrarlo por pantalla
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else: 
    # Si la fruta no está en el diccionario, mostrar un mensaje de error
    print("Lo siento, la fruta", fruta, "no está disponible.")
