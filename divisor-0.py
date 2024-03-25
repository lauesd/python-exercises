#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numero_1 = float(input("¿Podrías poner un número para dividir, porfa?: "))
numero_2 = float(input("¿Podrías poner otro número para dividir, porfa?: "))

if numero_2 == 0:
    print("No se puede dividir por cero.")
else: 
    print("La división entre esos dos número es de: ", numero_1 / numero_2)