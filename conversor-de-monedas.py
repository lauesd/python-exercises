# Definir la tasa de cambio de dólares a pesos colombianos
tasa_cambio_peso_colombiano = 4000

# Solicitar al usuario que ingrese la cantidad de dólares a convertir a pesos colombianos
cantidad_origen_dolar = int(input("¿Cuántos dólares te gustaría cambiar a pesos colombianos?: "))

# Calcular el valor total en pesos colombianos utilizando la tasa de cambio
valor_total = cantidad_origen_dolar * tasa_cambio_peso_colombiano
                                                                              
# Convertir el valor total a una cadena para imprimirlo
valor_total = str(valor_total)

# Imprimir el resultado de la conversión
print("El valor de tus dólares convertidos a pesos colombianos es de: " + valor_total)

