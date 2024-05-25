#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# Lista de asignaturas del curso
materias = ["Matemáticas", "Español", "Historia", "Informática", "Ciencias"]

# Inicializar un contador
contador = 0

# Iterar sobre cada asignatura en la lista
while contador < len(materias):
    # Solicitar la nota al usuario para la asignatura actual
    nota = float(input(f"¿Cuál es tu nota en {materias[contador]}?: "))
    
    # Verificar si la nota es mayor o igual a 3.0 (aprobado)
    if nota >= 3.0:
        # Si la nota es aprobatoria, eliminar la asignatura de la lista
        materias.pop(contador)
    else:
        # Si la nota es reprobatoria, pasar a la siguiente asignatura
        contador += 1


# Mostrar por pantalla las asignaturas que el usuario tiene que repetir
print("  ")
print("Debes repetir las siguientes asignaturas:")
print("  ")
for asignatura in materias:
    print(asignatura)

print("  ")
