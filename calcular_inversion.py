# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
print("""Hola, este es un programa en donde podrás invertir una cierta cantidad de dinero y a los años que esté ese dinero, cada año ese dinero se va a ir incrementado un 5%.""")

cantidad_invertir = float(input("¿Cuánto dinero te gustaría invertir?: "))
interes_anual = 0.05
año = float(input("¿A cuántos años sería?: "))
ganancia = cantidad_invertir * interes_anual * año
total_capital = ganancia + cantidad_invertir

print("El total de tu inversión sería de: ", total_capital)
