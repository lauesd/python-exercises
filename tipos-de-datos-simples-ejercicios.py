#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("¡Hola Mundo!")

"""Escribir un programa que almacene la cadena ¡Hola Mundo!
en una variable y luego muestre por pantalla el contenido de la variable."""
Hola = "¡Hola Mundo!"

print(Hola)

"""Escribir un programa que pregunte el nombre del usuario 
en la consola y después de que el usuario lo introduzca 
muestre por pantalla la cadena 
¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido."""
nombre = input("¿Podrías escribir tu nombre, porfa?: ")

print ("¡Hola", nombre + "!")

"""Escribir un programa que 
muestre por pantalla el resultado de la siguiente operación aritmética:
((3 + 2) / (2 * 5)) ** 2 """

operacion = ((3 + 2) / (2 * 5)) ** 2

print(operacion)

"""Escribir un programa que pregunte al usuario por el 
número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
"""
horas_trabajadas = int(input("¿Podrías poner la cantidad de horas trabajadas, porfa?: "))
costo_hora = float(input("¿Podrías poner el costo por hora, porfa?: "))
horas_trabajadas = float(horas_trabajadas)
total_paga = str(costo_hora * horas_trabajadas)

print("Tu paga es de: " + total_paga)

"""Escribir un programa que lea un entero positivo, n, 
introducido por el usuario y después muestre en pantalla la suma 
de todos los enteros desde 1 hasta n. La suma de los n primeros enteros 
positivos puede ser calculada de la siguiente forma: n * (n + 1) / 2"""

n = int(input("¿Podrías poner un número entero porfa?: "))
suma = n * (n + 1) / 2

print ("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))

"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> 
donde <imc> es el índice de masa corporal calculado redondeado con dos decimales."""

peso = float(input("¿Podrías poner el peso corporal que tienes, porfa?: "))
estatura = float(input("¿Podrías poner tu estatura, porfa?: "))
imc = round(peso / estatura ** 2,2)


print ("Tu índice de masa corporal es: ", imc)

"""Escribir un programa que pida al usuario dos números enteros y muestre
 por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m>
 son los números introducidos por el usuario, y <c> y <r> son el cociente
 y el resto de la división entera respectivamente."""

n = int(input("¿Podrías poner un número entero, porfa?: "))
m = int(input("¿Podrías poner un número entero, porfa?: "))
c = n // m
r = n % m

print (str(n) + " entre " + str(m) + " da un cociente " + str(c) + " y un resto " + str(r))



