#entrada

nombre = input("¿Podrías poner tu nombre, porfa?: ")
edad = int(input("¿Podrías poner tu edad, porfa?: "))
peso = float(input("¿Podrías poner tu peso en kilogramos, porfa?: "))

#proceso

año_actual = 2024
año_nacimiento = año_actual - edad

#salida

print("                                                           ")
print("Se bienvenida como persona,", nombre )
print("                                                           ")
print("Tu nacistes en el año: ", año_nacimiento)
print("Su peso es: ", peso, "kilos")
print("                                                           ")
print("Muchas gracias por usar esto, nos vemos,", nombre)
