#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

# Definir la palabra de salida que indica que el programa debe terminar
salida = "salir"

# Solicitar al usuario que ingrese una frase
frase = input("¿Podrías poner una frase, porfa?: ")

# Iniciar un bucle que se ejecutará hasta que el usuario ingrese la palabra de salida
while frase.lower() != salida.lower():  # Verificar si la frase ingresada no es igual a la palabra de salida, ignorando mayúsculas y minúsculas
    # Imprimir la frase ingresada por el usuario
    print(frase)
    
    # Solicitar al usuario que ingrese otra frase
    frase = input("¿Podrías poner una frase, porfa?: ")

# Imprimir un mensaje para indicar que el programa ha terminado
print("                                                ")
print("Felicitaciones el programa ha terminado.")
