print ("Hola"); print ("mundo")

variable = 7

if variable > 5:
    print ("La variable es mayor que cinco.")
    print ("Qué cosa mas notable.")

print ("Esto es muestra siempre")

if variable > 4:
    pass

variable = 2 

if variable > 3:
    print("La variable es mayor que tres.")
elif variable < 3:
    print("La variable es menor que tres.")
    print("Me parece poco")
else:
    print("La variable es tres.")

a = 0

while a < 10:
    a = a + 1
    if a == 3:
        continue
    print (a)

primero = 3

while primero <= 7:
    print("Tabla del " + str(primero))
    
    segundo = 1
    
    while segundo <= 10:
        print (str(primero) + " * " + str(segundo) + " = " + str(primero * segundo))
        
        segundo += 1
    primero += 1
print("###################")

lista = ["calcetín", "pantalón", "camisa", "camiseta", "otro calcetín", "gorra"]

for prenda in lista:
    print ("La lavadora se ha comido mi " + prenda)

saludo = "Hola mundo"

for letra in saludo[:]:
    print (letra)

datos = {
"Nombre": "José",
"Apellido": "Gonzales",
"Altura": "1,80"
}

for concepto in datos:
    print (concepto)
for concepto in datos:
    print (concepto + ": " + datos[concepto]) 
for concepto, valor in datos.items():
    print (concepto + ": " + valor)

dividendo = 1
divisor = 0

resultado = dividendo/dividendo
print ("La división resulta: ", resultado)
print ("Hemos terminado.")

try:
    resultado = dividendo/divisor
    print ("La división resulta: ", resultado)
except:
    if divisor == 0:
        print("Desafortunadamente, no puedes dividir por cero.")

print ("Hemos terminado.")

dividendo = "A"
divisor = 2

try:
    resultado = dividendo/divisor
except ZeroDivisionError:
    if divisor == 0:
        print ("Desafortunadamente, no puedes dividir por cero.")
except TypeError:
    print("Desafortunadamente, no se puede dividir textos con números")
    
else:
    print("La división resulta: ", resultado)