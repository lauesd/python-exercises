"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
    Renta	             Tipo impositivo
Menos de 10000€	             5%
Entre 10000€ y 20000€	     15%
Entre 20000€ y 35000€	     20%
Entre 35000€ y 60000€	     30%
Más de 60000€	             45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde."""

# Imprimir un mensaje de introducción para el usuario.
print("Este es un programa que calcula tu renta anual para mostrarte cuál es tu tipo impositivo")
print("__________________________________________________________________________________________")

# Solicitar al usuario que ingrese su renta anual y convertir la entrada en un número flotante.
renta = float(input("¿Podrías poner tu renta anual, porfa?: "))

# Utilizar una serie de condicionales para determinar el tipo impositivo según la renta anual.
if renta < 10000:
    print("Tu tipo impositivo es de: 5%")
elif renta >= 10000 and renta < 20000:
    print("Tu tipo impositivo es de: 15%")
elif renta >= 20000 and renta < 35000:
    print("Tu tipo impositivo es de: 20%")
elif renta >= 35000 and renta < 60000:
    print("Tu tipo impositivo es de: 30%")
else:
    print("Tu tipo impositivo es de: 45%")
