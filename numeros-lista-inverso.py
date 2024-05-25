#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

# Crear una lista vacía para almacenar los números del 1 al 10
numeros = []

# Inicializar un acumulador en 11 (ya que queremos empezar desde el 10 hacia atrás)
con = 11

# Utilizar un bucle while para agregar los números del 10 al 1 a la lista
while acumulador > 1:
    acumulador -= 1  # Restar 1 al acumulador en cada iteración
    numeros.append(acumulador)  # Agregar el número actual a la lista

# Mostrar los números en orden inverso (separados por comas por defecto)
print(numeros)
