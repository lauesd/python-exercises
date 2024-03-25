# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

key = "contraseña"

entrada = input("¿Podrías poner la contraseña para entrar, porfa?: ")

if key == entrada.lower():
    print("Felicitaciones, has entrado a tu recurso privado.")
else:
    print("Desafortunadamente tu contraseña es incorrecta.")

