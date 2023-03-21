#4.1
pizzas = ['Calabresa', 'Bahiana', 'Mussarela']
for pizza in pizzas:
    print("Gosto de pizza de " + pizza)
print("Eu gosto bastante de pizza")
#4.2
animals = ['Gato', 'Cachorro', 'Tartaruga']
for animal in animals:
    print("Um " + animal + " seria um ótimo animal de estimação")
print("Qualquer um desses animais seria um ótimo animal de estimação")
#4.3
numbers = list(range(1, 21))
print(numbers)
#4.4
#numbers = []
#for value in range(1, 1000001):
#    numbers.append(value)
#print(numbers) 
#4.5
print(min(numbers))
print(max(numbers))
print(sum(numbers))
#4.6
odd_numbers = list(range(1,20,2))
print(odd_numbers)
#4.7
multiple = []
for value in range(1,11):
    multiple.append(value*3)
print(multiple)
#4.8
cube = []
for value in range(1,11):
    cube.append(value**3)
print(cube)
#4.9
cube = [value**3 for value in range(1,11)]
print(cube)
#4.10
print("Três itens do meio da lista são: {}".format(cube[3:7]))
print("Os três ultimos itens da lista são {}".format(cube[-3:]))
#4.11
pizzas = ['Calabresa', 'Bahiana', 'Mussarela']
friend_pizzas = pizzas[:]
pizzas.append("Batata-palha")
friend_pizzas.append("Palmito")
for pizza in pizzas:
    print("Gosto de pizza de " + pizza)
print("Eu gosto bastante de pizza")
for pizza in friend_pizzas:
    print("As pizzas favoritas do meu amigo são " + pizza)
#4.13
foods = ("Prato feito", "Lasanha", "Feijoada", "Macarronada", "Panquecas")
for comida in foods:
    print("Temos " + comida)
#foods[0] = "Frango" - da erro
foods = ("Frango", "Lasanha", "Feijoada", "Sopa", "Panquecas")
for comida in foods:
    print("Agora temos " + comida)