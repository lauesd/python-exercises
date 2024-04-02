#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

# Pedir al usuario que ingrese una frase
frase = input("¿Podrías poner una frase, porfa?: ")

# Pedir al usuario que ingrese una letra
letra = input("¿Podrías poner una letra, porfa?: ")

# Inicializar un contador para contar el número de veces que aparece la letra en la frase
contador = 0

# Iterar sobre cada carácter en la frase
for i in frase:
    # Verificar si el carácter actual es igual a la letra ingresada, ignorando mayúsculas y minúsculas
    if i.lower() == letra.lower():
        # Incrementar el contador si la letra actual coincide con la letra ingresada
        contador += 1

# Imprimir el resultado
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
