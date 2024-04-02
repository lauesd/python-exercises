# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

# Definir los costos de entrada para diferentes rangos de edad.
costo_1 = 5  # Precio de entrada para clientes de 4 a 18 años.
costo_2 = 10  # Precio de entrada para clientes mayores de 18 años.

# Solicitar al usuario que ingrese su edad y convertir la entrada en un número entero.
edad = int(input("¿Podrías poner tu edad, porfa?: "))

# Utilizar una serie de condicionales para determinar el precio de entrada según la edad del cliente.
if edad < 4:
    print("Puedes entrar gratis.")
elif edad >= 4 and edad <= 18:
    print("El costo de tu entrada es de %s" % costo_1 + "€")
else:
    print("El costo de tu entrada es de %s" % costo_2 + "€")
