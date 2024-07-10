#5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.") 
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.") 
print(car == 'audi')

car = 'bmw'
print("\nIs car == 'bmw'? I predict True.") 
print(car == 'bmw')
print("\nIs car == 'fusca'? I predict False.") 
print(car == 'fusca')

car = 'Jip'
print("\nIs car == 'Jip'? I predict True.") 
print(car == 'Jip')
print("\nIs car == 'Carreto'? I predict False.") 
print(car == 'Carreto')

car = 'Honda'
print("\nIs car == 'Honda'? I predict True.") 
print(car == 'Honda')
print("\nIs car == 'Corsa'? I predict False.") 
print(car == 'Corsa')

car = 'Corsa'
print("\nIs car == 'Jip'? I predict True.") 
print(car == 'Corsa')
print("\nIs car == 'Caminhonete'? I predict False.") 
print(car == 'Caminhonete')

#5.2
game = 'Dark Souls'
print("\nIs game == 'Dark Souls'? I predict True")
print(game == 'Dark Souls')
print("\nIs game == 'Elden Ring'? I predict False")
print(game == 'Elden Ring')

rpg = 'Tormenta20'
print("\nIs rpg == 'Tormenta20'? I predict False")
print(rpg.lower() == 'Dark Souls')
print("\nIs rpg == 'tormenta20'? I predict True")
print(rpg.lower() == 'tormenta20')

number = 7
print("\nIs number == 7? I predict True")
print(number == 7)
print("\nIs number == 8? I predict False")
print(number == 8)
print("\nIs number > 5? I predict True")
print(number > 5)
print("\nIs number < 1? I predict False")
print(number < 1)
print("\nIs number >= 3? I predict True")
print(number >= 7)
print("\nIs number <= 10? I predict True")
print(number <= 10)

game = 'Dark Souls 1'
secund_game = 'Dark Souls 2'
print("\nIs game == 'Dark Souls' or secund game == 'Elden ring'? I predict True")
print(game == 'Dark Souls' or secund_game == 'Elden ring')
print("\nIs game == 'Dark Souls' and secund game == 'Elden ring'? I predict False")
print(game == 'Elden Ring' and secund_game == 'Elden ring')


#5.3
alien_color = 'green'

if alien_color == 'green':
    print("Você ganhou 5 pontos!")

if alien_color == 'yellow':
    print("")

#5.4
alien_color = 'green'

if alien_color == 'green':
    pontos = 5 
else:
    pontos = 10
print("Você ganhou {} pontos!".format(pontos))

alien_color = 'yellow'

if alien_color == 'green':
    pontos = 5 
else:
    pontos = 10
print("Você ganhou {} pontos!".format(pontos))

#5.5
alien_color = 'red'

if alien_color == 'green':
    pontos = 5
elif alien_color == 'yellow':
    pontos = 10
else:
    pontos = 15
print("Você ganhou {} pontos!".format(pontos))

#5.6
age = 50

if age >= 2 and age < 4:
    status = "Criança"
elif age >= 4 and age < 13:
    status = "Garoto(a)"
elif age >= 13 and age < 20:
    status = "Adolecente"
elif age >= 20 and age < 65:
    status = "Adulto"
elif age >= 65:
    status = "Idoso"
print("Voce e um {}".format(status))

#5.7
frustas_favoritas = ['Banana', 'Pera', 'Melão']

if 'uva' in frustas_favoritas:
    print("Voce realmente gosta de uvas")
if 'Banana' in frustas_favoritas:
    print("Voce realmente gosta de Bananas")
if 'Maça' in frustas_favoritas:
    print("Voce realmente gosta de Maças")
if 'Melão' in frustas_favoritas:
    print("Voce realmente gosta de Melão")
if 'Pera' in frustas_favoritas:
    print("Voce realmente gosta de Peras")

#5.8
users = ['admin', 'matheus', 'bia', 'lucas', 'luan']

for user in users:
    if user == 'admin':
        print("Ola {}, gostaria de ver um relatorio de status?".format(user))
    else:
        print("Ola {}!".format(user))

#5.9
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Ola {}, gostaria de ver um relatorio de status?".format(user))
        else:
            print("Ola {}!".format(user))
else:
    print("Precisamos encontrar alguns usuarios!")

#5.10
current_users = ['joao', 'luiz', 'rafael', 'gabriel']
new_users = ['matheus','joao','bia','jose','rafael']

for user in new_users:
    if user.lower() in current_users:
        print("Por favor use um nome diferente de {}!".format(user))
    else:
        print("Nome {}, disponivel!".format(user))

#5.11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        posicao = 'st'
    elif number == 2:
        posicao = 'nd'
    elif number == 3:
        posicao = 'rd'
    elif number >= 4:
        posicao = 'th'
    print("{}{}".format(number,posicao))
