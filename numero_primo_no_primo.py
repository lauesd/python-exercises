#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

n = int(input("¿Podrías introducir un número entero positivo mayor o igual que 2, porfa?: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

