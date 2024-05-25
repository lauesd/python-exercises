#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Crear una nueva lista para almacenar las letras que no ocupen posiciones múltiplos de 3
abecedario_filtrado = []

# Iterar sobre cada letra en el abecedario
for i, letra in enumerate(abecedario, start=1):
    # Verificar si la posición de la letra es un múltiplo de 3
    if i % 3 != 0:
        # Si la posición no es múltiplo de 3, agregar la letra a la lista filtrada
        abecedario_filtrado.append(letra)

# Mostrar por pantalla la lista resultante
print(abecedario_filtrado)
