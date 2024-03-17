#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

peso_payaso = float(112)
peso_muñeca = float(75)
cantidad_payasos_vendidos = float(input("¿Cúanto es la cantidad de payasos vendidos?: "))
cantidad_muñecas_vendidas = float(input("¿Cúanta es la cantidad de muñecas vendidas?: "))
total_peso_pedido = (cantidad_payasos_vendidos * peso_payaso) + (cantidad_muñecas_vendidas * peso_muñeca)

print("El peso total del pedido es de: ", total_peso_pedido)