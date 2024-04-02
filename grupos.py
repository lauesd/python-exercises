# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N,
# y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo,
# y muestre por pantalla el grupo que le corresponde.

# Solicitar al usuario que ingrese su nombre.
nombre = input("¿Podrías poner tu nombre, porfa?: ")

# Solicitar al usuario que ingrese su sexo, con la indicación de que ingrese 'F' si es femenino o 'M' si es masculino.
sexo = input("¿Cual es tu sexo, escribe F si es femenino o escribe M si es masculino?: ")

# Verificar si el nombre está en el grupo A.
# Comparamos el nombre convertido a minúsculas con las letras 'm' y 'n' para asegurarnos de que la comparación sea insensible a mayúsculas/minúsculas.
# Si el nombre está antes de 'm' y el sexo es femenino (F), o si el nombre está después de 'n' y el sexo es masculino (M),
# entonces el alumno pertenece al grupo A, de lo contrario pertenece al grupo B.
if (nombre.lower() < 'm' and sexo == "F") or (nombre.lower() > 'n' and sexo == "M"):
    grupo = "A"
else:
    grupo = "B"

# Imprimir el grupo al que pertenece el alumno.
print("Tu grupo es: " + grupo)
