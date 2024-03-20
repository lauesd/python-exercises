"""En una fábrica de computadoras se planea ofrecer a los clientes un
descuento que dependerá del número de computadoras que compre. Si las
computadoras son menos de cinco se les dará un 10% de descuento sobre
el total de la compra; si el número de computadoras es mayor o igual a
cinco pero menos de diez se le otorga un 20% de descuento; y si son 10 o
más se les da un 40% de descuento. El precio de cada computadora es de
$3.500.000"""

#Entrada
print("Hola, esta es una tienda de computadores y cada computador cuesta $3.500.000")

porcentaje1 = 0.10
porcentaje2 = 0.20
porcentaje3 = 0.40
precioComputadoras = 3500000
cantidadComputadoras = int(input("¿Cuantos computadoras te gustaría comprar?"))

#Proceso

if cantidadComputadoras < 5:
    totalCompra = cantidadComputadoras * precioComputadoras
    descuentoCompra = totalCompra * porcentaje1
    totalPago = totalCompra - descuentoCompra
    print("El total de la compra con el descuento incluido es de: ", totalPago)
elif(cantidadComputadoras >= 5 and cantidadComputadoras < 10):
    totalCompra = cantidadComputadoras * precioComputadoras
    descuentoCompra = totalCompra * porcentaje2
    totalPago = totalCompra - descuentoCompra
    print("El total de la compra con el descuento incluido es de: ", totalPago)
elif cantidadComputadoras >= 10:
    totalCompra = cantidadComputadoras * precioComputadoras
    descuentoCompra = totalCompra * porcentaje3
    totalPago = totalCompra - descuentoCompra
    print("El total de la compra con el descuento incluido es de: ", totalPago)

#Salida
    print("Gracias por su compra, que tenga un buen día y que programe mucho.")
    
