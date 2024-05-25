#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

# Definir una lista que almacene las asignaturas del curso
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Inicializar un contador para controlar el bucle while
contador = 1

# Inicializar un contador para acceder a los elementos de la lista asignaturas
contador_2 = -1

# Bucle principal para solicitar la nota de cada asignatura al usuario
for i in range(6):
    # Bucle while para solicitar la nota de una asignatura
    while contador <= 5:
        contador += 1
        contador_2 += 1

        print("                                                                                 ")
        
        # Solicitar al usuario la nota de la asignatura actual
        nota = float(input("¿Cuánto te sacastes en " + asignaturas[contador_2] + "?: "))
        
        # Imprimir el mensaje con la asignatura y la nota ingresada por el usuario
        print("En " + asignaturas[contador_2] + " te sacastes: " + str(nota))
