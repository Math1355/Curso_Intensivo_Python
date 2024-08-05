#8.1
'''def display_message():
    print("Estou aprendendo sobre funções")

display_message()'''

#8.2
'''def favorite_book(title):
    print("Um dos meus livros favoritos e " + title.title())

favorite_book('Harry Potter')'''

#8.3 
'''Camiseta: Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
A função deve exibir uma frase que mostre o tamanho da camiseta e a
mensagem estampada.
Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados.'''
'''def make_shirt(tamanho, msg):
    print('A estampa da camisa esta escrito: ' + msg)
    print('O tamanho da camisa e: ' + tamanho)

make_shirt('M', 'Eu odeio red-pill')
make_shirt(msg='Odeio de verdade red-pill', tamanho='G')'''

#8.4 
'''Camisetas grandes: Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta
de qualquer tamanho com uma mensagem diferente.'''
'''def make_shirt(msg='Eu amo Python', tamanho='G'):
    print('A estampa da camisa esta escrito: ' + msg)
    print('O tamanho da camisa e: ' + tamanho)

make_shirt()
make_shirt(tamanho='Media')
make_shirt('Odeio red-pill', 'Pequena')'''

#8.5 
'''Cidades: Escreva uma função chamada describe_city() que aceite o
nome de uma cidade e seu país. A função deve exibir uma frase simples, como
Reykjavik está localizada na Islândia. Forneça um valor default ao
parâmetro que representa o país. Chame sua função para três cidades
diferentes em que pelo menos uma delas não esteja no país default.'''
'''def describe_city(nome_cidade, pais='Brasil'):
    print(nome_cidade + " está localizada na " + pais)

describe_city('New York', 'EUA')
describe_city('São Paulo')
describe_city('Veneza', 'Italia')'''

#8.6
'''Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido.

def city_country(cidade, pais):
    print(cidade + ', ' + pais)

city_country("São Paulo", "Brasil")
city_country("New York", "EUA")
city_country("Veneza", "Italia")'''

#8.7
'''Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas
duas informações. Use a função para criar três dicionários que representem
álbuns diferentes. Apresente cada valor devolvido para mostrar que os
dicionários estão armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar
o número de faixas em um álbum. Se a linha que fizer a chamada incluir um
valor para o número de faixas, acrescente esse valor ao dicionário do álbum.
Faça pelo menos uma nova chamada da função incluindo o número de faixas
em um álbum.


def make_album(artista, album, faixas=""):
    info = {'artista': artista, 'album': album}
    if faixas:
        info['faixas'] = faixas
    return info

musica = make_album('michael jackson', 'Thriller')
print(musica)
musica = make_album('jorge rivera-herrans', 'The Troy Saga', '5')
print(musica)'''


#8.8
'''Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e
o título de um álbum. Depois que tiver essas informações, chame make_album()
com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir
um valor de saída no laço while.

def make_album(artista, album):
    info = {'artista': artista, 'album': album}

    return info


while True:
    print("\nInsira o nome de um artista e o album:")
    print("(Insira 'q' para sair)")
    p_name = input('Insira o nome do artista: ')
    if p_name == 'q':
        break
    a_name = input('insira o nome do album: ')
    if a_name == 'q':
        break
    musica = make_album(p_name, a_name)
    print(musica)
'''

#8.9
'''8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da
lista.

def show_magic(magics):
    print("\nHere is the list of Magic:")
    for magic in magics:
        print(magic)


magic = ['Houdini', 'Richiardi Jr', 'Jasper Maskelyne']
show_magic(magic)'''


#8.10
'''8.10 – Grandes mágicos: Comece com uma cópia de seu programa do
Exercício 8.9. Escreva uma função chamada make_great() que modifique a
lista de mágicos acrescentando a expressão o Grande ao nome de cada
mágico. Chame show_magicians() para ver se a lista foi realmente modificada.

def make_great(magic, great_magic):
    while magic:
        current_magic = 'The Great ' + magic.pop()
        great_magic.append(current_magic)


def show_magic(great_magic):
    print("Here is the list of Magic:")
    for magic in great_magic:
        print(magic)


magic = ['Houdini', 'Richiardi Jr', 'Jasper Maskelyne']
great_magic = []

make_great(magic, great_magic)
show_magic(great_magic)'''

#8.11
'''8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em
uma lista separada. Chame show_magicians() com cada lista para mostrar que
você tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico.

def make_great(magic, great_magic):
    while magic:
        current_magic = 'The Great ' + magic.pop()
        great_magic.append(current_magic)


def show_magic(great_magic):
    print("Here is the list of Magic:")
    for magic in great_magic:
        print(magic)


magic = ['Houdini', 'Richiardi Jr', 'Jasper Maskelyne']
great_magic = []

make_great(magic[:], great_magic)
show_magic(great_magic)
print(magic)'''

#8.12  
'''Sanduíches: Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
tantos itens quantos forem fornecidos pela chamada da função e deve
apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
um número diferente de argumentos a cada vez.

def make_sandwich(*toppings):
    print("\nMaking a sandwich with the follewing toppings:")
    for topping in toppings:
        print("- " + topping)

make_sandwich('Egg')
make_sandwich('lettuce', 'mozzarella', 'tomato')'''

#8.13 
'''Perfil do usuário: Comece com uma cópia de user_profile.py, da página
210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome
e o sobrenome, além de três outros pares chave-valor que o descrevam.

def build_profile(first, last, **user_info):
    """Constrói um dicionario contendo tudo que sabemos sobre um usuario."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Matheus', 'Silva', location='Brazil', field='Big Data')
print(user_profile)'''

#8.14 
'''Carros: Escreva uma função que armazene informações sobre um carro
em um dicionário. A função sempre deve receber o nome de um fabricante e um
modelo. Um número arbitrário de argumentos nomeados então deverá ser
aceito. Chame a função com as informações necessárias e dois outros pares
nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser
apropriada para uma chamada como esta: car = make_car(‘subaru’, ‘outback’,
color=’blue’, tow_package=True) Mostre o dicionário devolvido para garantir
que todas as informações foram armazenadas corretamente.

def build_car(producer, model, **car_info):
    profile = {}
    profile['producer_name'] = producer
    profile['model_name'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile

car_profile = build_car('subaru', 'outback', color='red', tow_packege=True)
print(car_profile)'''

#8.15 
'''Impressão de modelos: Coloque as funções do exemplo print_models.py
em um arquivo separado de nome printing_functions.py. Escreva uma instrução
import no início de print_models.py e modifique o arquivo para usar as funções
importadas.
import printing_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#print_models(unprinted_designs[:], completed_models)
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)'''

#8.16
'''Importações: Usando um programa que você tenha escrito e que
contenha uma única função, armazene essa função em um arquivo separado.
Importe a função para o arquivo principal de seu programa e chame-a usando
cada uma das seguintes abordagens: import nome_do_módulo from
nome_do_módulo import nome_da_função from nome_do_módulo import
nome_da_função as nf import nome_do_módulo as nm from nome_do_módulo import
*

#import pets_functions
#from pets_functions import describe_pet
#from pets_functions import describe_pet as dp
#import pets_functions as pf
from pets_functions import *

#pets_functions.describe_pet(animal_type='hamster', pet_name='harry')   
#describe_pet(animal_type='hamster', pet_name='harry')  
#dp(animal_type='hamster', pet_name='harry')
#pf.describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='hamster', pet_name='harry')'''

#8.17 
'''Estilizando funções: Escolha quaisquer três programas que você escreveu
neste capítulo e garanta que estejam de acordo com as diretrizes de estilo
descritas nesta seção.'''
#Estão ok