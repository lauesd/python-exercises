print("Esto es una cuenta de ahorros")
print("_______________________________")

dinero_depositado = float(input("¿Cúanto dinero te gustaria poner en tu cuenta de ahorros?: "))
interes = 0.04
intereses_primer_año = dinero_depositado * interes 
intereses_segundo_año = dinero_depositado * interes * 2
intereses_tercer_año = dinero_depositado * interes * 3
ahorro_total_primer_año = round(intereses_primer_año + dinero_depositado, 2)
ahorro_total_segundo_año = round(intereses_segundo_año + dinero_depositado, 2)
ahorro_total_tercer_año = round(intereses_tercer_año + dinero_depositado, 2)

print("La cantidad de ahorros total dentro de un año es de:", ahorro_total_primer_año, "de dos años es de:", ahorro_total_segundo_año, "de tres años es de:", ahorro_total_tercer_año)

"""
inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion + inversion*interes
print("Balance tras el primer año: " + str(round(balance1, 2))) 
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año: " + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año: " + str(round(balance3, 2)))
"""
