#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.


# Crear una lista vacía para almacenar los números ganadores
numeros = []

# Inicializar un contador para llevar el control de cuántos números se han ingresado
contador = 1

# Mientras el contador sea menor o igual a 6 (indicando que aún faltan números por ingresar):
while contador <= 6:
    # Solicitar al usuario que ingrese un número ganador y agregarlo a la lista
    numeros.append(int(input("¿Podrías poner los 6 números ganadores de la lotería primitiva?: ")))
    # Incrementar el contador en 1 para pasar al siguiente número
    contador = contador + 1

# Ordenar la lista de números ganadores de menor a mayor
numeros.sort()

# Mostrar los números ganadores ordenados por pantalla
print(numeros)
