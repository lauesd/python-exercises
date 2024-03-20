"""Un alumno desea saber cual será su calificación final en la materia de
Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
40% del promedio de sus tres calificaciones parciales, 50% de la
calificación del examen final y 10% de la calificación de un trabajo final."""

#Entrada
#Intento de la profe
porcentaje_notas = 0.40
porcentaje_examen = 0.50
porcentaje_trabajo = 0.10
nota1, nota2, nota3 = input("¿Podrías ingresar tus notas separadas por espacio, porfa?: ").split()
examen_final, trabajo_final = input("¿Podrías ingresar la nota del examen final y del trabajo final separadas por espacio, porfa?: ").split()

#Proceso
promedio_notas = ((float(nota1) + float(nota2) + float(nota3))/3)*porcentaje_notas
nota_examen = ((float(examen_final))*porcentaje_examen)
nota_trabajo = float(trabajo_final)*porcentaje_trabajo

nota_definitiva = promedio_notas + nota_examen + nota_trabajo

#Salida
print(f"Nota trabajos: {promedio_notas: .2f}")
print(f"Nota examen final: {nota_examen: .2f}")
print(f"Nota trabajo final: {nota_trabajo: .2f}")

print(f"Nota definitiva: {nota_definitiva: .2f}")

if nota_definitiva >= 3:
    print ("¡Felicitaciones has aprobado!")
else:
    print("Desafortunadamente, desaprobastes")

# Intento mio
"""porcentaje1 = 0.50
porcentaje2 = 0.40
porcentaje3 = 0.10
parcial_1_c = float(input("¿Podrías poner tu calificación del primer parcial, porfa?: "))
parcial_2_c = float(input("¿Podrías poner tu calificación del segundo parcial, porfa?: "))
parcial_3_c = float(input("¿Podrías poner tu calificación del tercer parcial, porfa?: "))

parcial_todos_calificacion = parcial_1_c + parcial_2_c + parcial_3_c
parcial_calificacion_definitiva = parcial_todos_calificacion * porcentaje2

print (parcial_calificacion_definitiva)"""