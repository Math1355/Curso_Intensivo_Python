'''def make_pizza(*toppings):
    """Exibe a lista de ingredientes pedidos"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('Pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')'''


def make_pizza(size, *toppings):
    """Exibe a lista de ingredientes pedidos"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'Pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')