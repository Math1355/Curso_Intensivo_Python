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

Teste'''