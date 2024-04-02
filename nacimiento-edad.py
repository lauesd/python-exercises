#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# Solicitar al usuario que ingrese su edad.
edad = int(input("¿Podrías poner tu edad, porfa?: "))
numero = 0

# Utilizar un bucle for para imprimir todos los años que ha cumplido la persona.
for i in range(edad):
    numero = numero + 1
    print(numero)