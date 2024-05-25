# Define una función que imprime varios mensajes
def saluda():
    print("Hola Mundo")
    print("Es bueno saludar")
    print("Resulta elegante")

# Llama a la función saluda
saluda()

# Define una función que retorna el valor de pi
def dame_pi():
    numero_pi = 3.14159
    return numero_pi

# Llama a la función dame_pi e imprime su retorno
print(dame_pi())

# Asigna el valor retornado por dame_pi a la variable pi
pi = dame_pi()

# Imprime el valor de la variable pi
print(pi)

# Redefine la función saluda para que retorne una tupla
def saluda():
    return "hola", "mundo"

# Llama a la función saluda y almacena su retorno en la variable hola
hola = saluda()

# Imprime el valor de la variable hola
print(hola)

# Define una función que calcula el cuadrado de un número
def cuadrado(numero):
    cuadrado = numero * numero
    return cuadrado

# Llama a la función cuadrado con el argumento 5 e imprime el resultado
resultado = cuadrado(5)
print(resultado)

# Define una variable número
numero = 5

# Redefine la función cuadrado (mismo código)
def cuadrado(numero):
    cuadrado = numero * numero
    return cuadrado

# Llama a la función cuadrado con la variable número e imprime el resultado
resultado = cuadrado(numero)
print(resultado)

# Define una función que saluda y personaliza el mensaje según el sexo
def saluda(nombre, sexo):
    print("Hola " + nombre)
    if sexo.lower() == "m":
        print("¿Cómo te va, persona de sexo masculino?")
    elif sexo.lower() == "f":
        print("¿Cómo te va, persona de sexo femenino?")
    else:
        print("¿Cómo te va?")

# Llama a la función saluda con los argumentos "Gabriel" y "M"
saluda("Gabriel", "M")

# Define una función que imprime la tabla de multiplicar de un número
def tabla_multiplicar(nombre, numero = 1):
    print("Tabla de multiplicar del " + str(numero))
    print("Impresa automaticamente por " + nombre)
    i = 0 
    while i < 11:
        print(str(numero) + " X " + str(i) + " = " + str(numero * i))
        i += 1

# Llama a la función tabla_multiplicar con el argumento "Gabriel"
tabla_multiplicar("Gabriel")

# Define una función que imprime una lista de elementos
def imprime_lista(nombre_lista, *cosas):
    print("Lista de " + nombre_lista)
    for cosa in cosas:
        print(cosa)

# Llama a la función imprime_lista con varios argumentos
imprime_lista("Piezas", "tornillo", "tuerca", "otro tornillo", "cable")

# Define una función que imprime datos con nombres de clave y valor
def imprime_datos(nombre, **datos):
    print("Datos de " + nombre)
    for clave in datos:
        print(clave + ": " + datos[clave])

# Llama a la función imprime_datos con varios pares clave-valor
imprime_datos("Pablo", edad="mucha", estado="Enloquecido", guapo="no")

# Define una variable global
variable = "Fuera de la función"

# Define una función que imprime una variable local
def una_funcion():
    variable = "Dentro de la función"
    print(variable)

# Llama a la función una_funcion
una_funcion()

# Imprime la variable global
print(variable)

# Redefine la variable global
variable = "Fuera de la función"

# Define una función que imprime la variable global (sin redefinirla)
def una_funcion():
    #No asignamos valor a "variable dentro de la función"
    print(variable)

# Llama a la función una_funcion
una_funcion()

# Imprime la variable global
print(variable)

# Redefine la variable global
variable = "Fuera de la función"

# Define una función que usa la variable global y la modifica
def una_funcion():
    global variable
    variable = "Dentro de la función"
    print(variable)

# Llama a la función una_funcion
una_funcion()

# Imprime la variable global, que ha sido modificada por la función
print(variable)

# Define una lista de números
lista = [1, 2, 3, 4, 5]

# Recorre la lista e imprime cada elemento
for i in lista:
   print(i)

# Define una función que genera una lista de números hasta el argumento num
def genera_lista(num):
    lista = []
    i = 1
    while i <= num:
        lista.append(i)
        i += 1
    return lista

# Llama a la función genera_lista y recorre e imprime cada elemento de la lista generada
for i in genera_lista(10):
    print(i)

# Define una función que genera una lista y usa yield para retornarla (generador)
def genera_lista(num):
    lista = []
    i = 1
    while i <= num:
        lista.append(i)
        i += 1
    yield lista

# Llama a la función genera_lista y recorre e imprime cada elemento de la lista generada
for i in genera_lista(10):
    print(i)

# Define un decorador que modifica la función de entrada
def decorador(funcion_entrada):
    def funcion_salida():
        funcion_entrada()
        print("Esto no estaba en la función original")
    return funcion_salida

# Aplica el decorador a la función saludo
@decorador
def saludo():
    print("Hola")

# Llama a la función saludo, ahora decorada
saludo()

# Define un decorador que modifica la función de entrada en base a un parámetro
def decorador(funcion_entrada):
    def funcion_salida(param):
        if param == "Lidia":
            print("Buenos días, guapa")
        elif param == "Pablo":
            print("Buenos días, guapo")
        else:
            funcion_entrada(param)
        print("Qué tengas un buen día")
    return funcion_salida

# Aplica el decorador a la función saludo
@decorador
def saludo(nombre):
    print("Hola " + nombre)

# Llama a la función saludo con el argumento "Pablo"
saludo("Pablo")

# Define una función lambda que calcula el cuadrado de un número
cuadrado = lambda x: x**2

# Llama a la función lambda cuadrado y almacena el resultado
resultado = cuadrado(2)

# Imprime el resultado
print(resultado)

# Define otra función lambda para sumar dos números
suma = lambda x, y: x + y

# Llama a las funciones lambda anidadamente y almacena el resultado
resultado = cuadrado(suma(cuadrado(2), 5))

# Imprime el resultado
print(resultado)
