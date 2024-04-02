#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

print("Buenas, este es un programa que muestra tu capital total con unos calculos")
print("                                                                           ")

cantidad_invertir = float(input("¿Cuanto te gustaría invertir?: "))
interes_anual = float(input("¿Cúanto es el interes anual, escribe de esta forma: 00.00?: "))
numero_años = int(input("¿Por cuantos años sería?: "))

for i in range(1, numero_años , 1):
    print("                                                        ")
    print(""""Tu capital total en ese lapso de tiempo
con los otros calculos es de: """, cantidad_invertir * interes_anual + cantidad_invertir)