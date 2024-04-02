"""La pizzería Restrepo ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""

# Imprimir un mensaje de bienvenida a la pizzería.
print("Se bienvenida como persona a la pizzeria Restrepo")
print("__________________________________________________")

# Solicitar al usuario que indique si quiere una pizza vegetariana o no vegetariana.
pizza = input("¿Quieres una pizza vegetariana o no vegetariana? Escribe 'Vegetariana' para una pizza vegetariana y 'no vegetariana' para una pizza no vegetariana: ")

# Comprobar la elección del usuario y mostrar el menú correspondiente de ingredientes disponibles.
if pizza.lower() == "vegetariana":
    print("""Estos son los ingredientes disponibles
Pimiento y tofu""")
    print("________________________________________")

    # Solicitar al usuario que elija un ingrediente para la pizza vegetariana.
    ingredientes = input("¿Cuál ingrediente te gustaría escoger?, escribe 'pimiento' o 'tofu': ")
    
    # Mostrar un mensaje indicando la preparación de la pizza seleccionada.
    if ingredientes.lower() == "pimiento":
        print("Tu pizza de pimiento va a ser preparada.")
    elif ingredientes.lower() == "tofu":
        print("Tu pizza de tofu va a ser preparada.")
elif pizza.lower() == "no vegetariana":
    print("""Estos son los ingredientes disponibles
Peperoni, Jamón y Salmón""")
    print("________________________________________")
    
    # Solicitar al usuario que elija un ingrediente para la pizza no vegetariana.
    ingredientes = input("¿Cuál ingrediente te gustaría escoger?, escribe 'peperoni', 'jamon' o 'salmon': ")
    
    # Mostrar un mensaje indicando la preparación de la pizza seleccionada.
    if ingredientes.lower() == "peperoni":
        print("Tu pizza de peperoni va a ser preparada.")
    elif ingredientes.lower() == "jamon":
        print("Tu pizza de jamon va a ser preparada.")
    elif ingredientes.lower() == "salmon":
        print("Tu pizza de salmon va a ser preparada.")
