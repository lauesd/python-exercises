#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "elpepe"
entrada_contraseña = input("¿Podrías poner tu contraseña, porfa?: ")
print("                                                    ")

while entrada_contraseña != contraseña:
    print("Contraseña incorrecta, vuelve a intentarlo.")
    print("                                                    ")
    entrada_contraseña = input("¿Podrías poner tu contraseña, porfa?: ")
    print("                                                    ")


print("Felicitaciones tu numero de tarjeta de credito es: 12341254235234")