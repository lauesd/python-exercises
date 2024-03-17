# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas_trabajadas = int(input("¿Podrías poner la cantidad de horas trabajadas, porfa?: "))
costo_hora = float(input("¿Podrías poner el costo por hora, porfa?: "))
total_paga = str(costo_hora * horas_trabajadas)
print("Tu paga es de: " + total_paga)
