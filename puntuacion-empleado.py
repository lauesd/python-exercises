"""En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

   Nivel	      Puntuación
Inaceptable	         0.0
Aceptable	         0.4
Meritorio	       0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario."""

# Imprimir un mensaje de introducción para el usuario.
print("Este es un programa que según la puntuación que tengas como persona empleada, vas a recibir una cierta cantidad de dinero, las puntuaciones son estas. 0.0, 0.4 y 0.6 o más")
print("_____________________________________________________________________________________________________________________________________________________________________________")

# Solicitar al usuario que ingrese su puntuación como empleado y convertir la entrada en un número flotante.
puntuacion = float(input("¿Podrías poner tu puntuación como empleado, porfa?: "))

# Utilizar una serie de condicionales para determinar el nivel de rendimiento del empleado y calcular la cantidad de dinero que recibirá.
if puntuacion == 0.0:
    print("Tu nivel es: Inaceptable")
    print("La cantidad de dinero que vas a recibir es de: ", 2400 * puntuacion + 2400)
elif puntuacion == 0.4:
    print("Tu nivel es: Aceptable")
    print ("La cantidad de dinero que vas a recibir es de: ", 2400 * puntuacion + 2400)
else:
    print("Tu nivel es: Meritorio")
    print ("La cantidad de dinero que vas a recibir es de: ", 2400 * puntuacion + 2400)

