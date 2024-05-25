print("Hola, este es un administrador de tareas, en donde puedes administrar tareas. ")
print(" ")
respuesta = "x"



while respuesta.lower() == "x":
    tareas = ["El pepe"]
    tarea = input("¿Cual es el nombre de tu tarea?: ")
    tareas.append(tarea)
    respuesta = input("Escribe x para seguir poniendo tareas y z para salir del programa: ")

print(tareas)
    