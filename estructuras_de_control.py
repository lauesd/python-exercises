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


