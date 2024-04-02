#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("¿Podrías poner un número, porfa?: "))

for i in range(numero, 0 - 1, -1):
    print(i, end=", ")

    
