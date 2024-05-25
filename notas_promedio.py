#Crea un programa que solicite al usuario ingresar las notas de cinco asignaturas diferentes (por ejemplo, matemáticas, ciencias, historia, inglés y arte). Después, el programa debe calcular y mostrar el promedio de las notas ingresadas.

nota_matematicas =  (float(input("¿Podrías poner tu notas de matematicas, porfa?: ")))
nota_ciencias =  (float(input("¿Podrías poner tu nota de ciencas, porfa?: ")))
nota_historia =  (float(input("¿Podrías poner tu nota de historia, porfa?: ")))
nota_ingles =  (float(input("¿Podrías poner tu nota de inglés, porfa?: ")))
nota_arte = (float(input("¿Podrías poner tu nota de arte, porfa?: ")))

promedio_nota = (nota_historia + nota_ciencias + nota_historia + nota_ingles + nota_arte) / 5

print("El promedio de la nota total es de: ", promedio_nota)