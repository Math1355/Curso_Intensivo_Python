'''#7.1
car = input("Qual carro você gostaria de alugar? ")
print("Deixe ver se tenho um {} para você!".format(car))

#7.2
peoples = int(input("Mesa para quantas pessoas? "))

if peoples > 8:
    print("Vai ser preciso esperar uma mesa liberar!")
else:
    print("Sua mesa esta pronta, me siga!")

#7.3
number = int(input("Insira um numero inteiro: "))

if number % 10 == 0:
    print("O numero que você digitou e multiplo de 10!")
else:
    print("O numero que você digitou não e multiplo de 10!")

#7.4
prompt = "\nInsira um ingrediente para uma pizza!"
prompt += "\nEscreva 'quit' para finalizar o programa. "
loop = True

while loop:
    ingrediente = input(prompt)
    if ingrediente == 'quit':
        loop = False
    else:
        print("Você escolheu {}, boa escolha!".format(ingrediente))'''

#7.5
'''prompt = "\nVoce quer comprar um ingresso para assistir um filme?"
prompt += "\nEscreva 'quit' para finalizar o programa "
loop = True

while loop:
    opcao = input(prompt)
    if opcao != 'quit':
        idade = int(input("Insira a idade: "))
        if idade <= 3:
            print("O ingresso e de graça!")
        elif idade > 3 and idade <= 12:
            print("O ingresso custa 10 dolares!")
        else:
            print("O ingresso custa 15 dolares!")
    else:
        loop = False

#7.8
sandwich_orders = ['X-salada', 'X-Bacon', 'X-egg', 'X-buguer', 'X-tudo']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print("Preparei um {} para você!".format(sandwich))

#7.9
sandwich_orders = ['X-salada', 'pastrami', 'X-Bacon', 'pastrami', 'X-egg', 'X-buguer', 'X-tudo', 'pastrami']
finished_sandwiches = []

print("A lanchonete esta sem pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print("Preparei um {} para você!".format(sandwich))

#7.10
enquete = {}

flag =  True

while flag:
    nome = input("\nQual e o seu nome? ")
    resposta = input("\nSe pudesse visitar um lugar do mundo, para onde você iria? ")
    enquete[nome] = resposta
    repetir = input("Mais alguem gostaria de responder a pesquisa? (sim/nao) ")
    if repetir == 'nao':
        flag = False

print("\nResultado da pesquisa: ")
for nome, resposta in enquete.items():
    print("{} gostaria de ir para {}".format(nome, resposta))'''