#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

#Mi versión
# Diccionario que mapea nombres de divisas a sus símbolos
divisas = {'Euro':'€',
           'Dollar':'$', 
           'Yen':'¥'}

# Solicitar al usuario que ingrese una divisa
divisa = input("¿Podrías poner la divisa, porfa?: ")

# Verificar si la divisa está en el diccionario y mostrar su símbolo o un mensaje de aviso
if divisa.lower() == 'euro':
    print("Euro:", divisas['Euro'])
elif divisa.lower() == 'dollar':
    print("Dollar:", divisas['Dollar'])
elif divisa.lower() == 'yen':
    print("Yen:", divisas['Yen'])
else:
    print("Esa divisa no está almacenada en el diccionario.")



#Versión ChatGPT
# Diccionario que mapea nombres de divisas a sus símbolos
divisas = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}

# Solicitar al usuario que ingrese una divisa
divisa = input("¿Podrías poner la divisa, por favor?: ")

# Buscar la divisa ingresada en el diccionario
# Si se encuentra, imprimir su símbolo; de lo contrario, mostrar un mensaje de aviso
if divisa.capitalize() in divisas:
    print(divisa.capitalize() + ":", divisas[divisa.capitalize()])
else:
    print("Esa divisa no está almacenada en el diccionario.")



#Versión del ejercicio.
# Diccionario que mapea nombres de divisas a sus símbolos
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

# Solicitar al usuario que ingrese una divisa
moneda = input("Introduce una divisa: ")

# Buscar la divisa ingresada en el diccionario y mostrar su símbolo o un mensaje de aviso
print(monedas.get(moneda.title(), "La divisa no está."))
