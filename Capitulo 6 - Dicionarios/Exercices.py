#6.1
people_0 = {'first_name':'matheus', 'last_name':'Silva', 'age':18, 'city':'Osasco'}
print(people_0)

#6.2
favorite_number = {'João':10, 'Matheus':14, 'Lucas':12, 'Luan':30, 'Luiz':44}
print("Numero favorito do João e " + str(favorite_number['João']))
print("Numero favorito do Matheus e " + str(favorite_number['Matheus']))
print("Numero favorito do Lucas e " + str(favorite_number['Lucas']))
print("Numero favorito do Luan e " + str(favorite_number['Luan']))
print("Numero favorito do Luiz e " + str(favorite_number['Luiz']))

#6.3
glossary = {'Condicional':'Verifica se e verdadeiro ou falso',
    'lista':'Uma lista é uma coleção de itens em uma ordem em particular.',
    'Variáveis':'Toda variável armazena um valor, que é a informação associada a essa variável.'}

print("Condicional:\n" +
    glossary['Condicional'] + "\n" +
    "Lista:\n" + 
    glossary['lista'] + "\n" +
    "Variáveis:\n" + 
    glossary['Variáveis'])

#6.4
glossary_2 = {'Condicional':'Verifica se e verdadeiro ou falso',
    'lista':'Uma lista é uma coleção de itens em uma ordem em particular.',
    'Variáveis':'Toda variável armazena um valor, que é a informação associada a essa variável.'}

for palavra, descricao in glossary_2.items():
    print(palavra + "\n" + descricao + "\n")

#6.5
rios = {'nilo':'egito', 'Amazonas':'brasil', 'kuskokwim':'usa'}

for rio, pais in rios.items():
    print('\n O ' + rio.title() + " corre pelo " + pais.title())

for rio in rios.keys():
    print(rio.title())

for pais in rios.values():
    print(pais.title())

#6.6
favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
}

new_people = ['matheus', 'joao', 'sarah', 'luan', 'phil']

for name in favorite_languages.keys():
    if name in new_people:
        print('Muito obrigado por responder a pesquisa ' + name.title())
    else:
        print("Venha participar da enquete " + name.title())

#6.7
people_0 = {'first_name':'matheus', 'last_name':'Silva', 'age':18, 'city':'Osasco'}
people_1 = {'first_name':'Beatriz', 'last_name':'Lacerda', 'age':18, 'city':'Osasco'}
people_2 = {'first_name':'Luan', 'last_name':'Dias', 'age':18, 'city':'São Bernardo'}

peoples = [people_0, people_1, people_2]

for people in peoples:
    print(people)

#6.8
kitty = {'tipo':'gato', 'dono':'bia',}
floco = {'tipo':'cachorro', 'dono':'bine',}
estrela = {'tipo':'tartaruga', 'dono':'monik',}

pets = [kitty, floco, estrela]

for pet in pets:
    print(pet)

#6.9
favorite_places = {"Jose":"Praia", "Bia":"Restaurante", "Matheus":"Casa", }

for nome, lugar_favorito in favorite_places.items():
    print("\n O lugar favorito do {} e {}.".format(nome, lugar_favorito))

#6.10
favorite_number = {
    'João':[10, 11, 50], 'Matheus':[14, 16, 20], 'Lucas':[12, 15], 'Luan':[30], 'Luiz':[44, 51, 69, 70], }

for name, numbers in favorite_number.items():
    print("\nO numero favorito de {} e:".format(name.title()))
    for number in numbers:
        print("\t {}".format(number))


#6.11
cities = {
    'são paulo': {'country':'brazil', 'population':41262199, 'fact':'Melhor dogão e de osasco'}, 
    'rio de janeiro': {'country':'brazil', 'population':15989929, 'fact':'Lugares bonitos'}, 
    'pernambuco': {'country':'brazil', 'population':8796448, 'fact':'Melhor praia e porto de galinhas'},
}

for city, info_city in cities.items():
    print("\nNome: {}".format(city.capitalize()))
    country = info_city['country']
    population = info_city['population']
    fact = info_city['fact']
    print("\tLocalizado em: {}".format(country.title()))
    print("\tCom a população de: {}".format(population))
    print("\tCuriosidade: {}".format(fact))
