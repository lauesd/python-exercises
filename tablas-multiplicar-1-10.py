#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

#Version mia
numero = 1

while numero <= 10:
    print(numero, "* 1 = ", numero * 1)
    print(numero, "* 2 = ", numero* 2)
    print(numero, "* 3 = ", numero * 3)
    print(numero, "* 4 = ", numero* 4)
    print(numero, "* 5 = ", numero * 5)
    print(numero, "* 6 = ", numero * 6)
    print(numero, "* 7 = ", numero * 7)
    print(numero, "* 8 = ", numero * 8)
    print(numero, "* 9 = ", numero * 9)
    print(numero, "* 10 = ", numero * 10)
    numero = numero + 1

#Version ChatGPT
for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
    print()