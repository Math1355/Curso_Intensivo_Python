from audioop import reverse


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(1, 'harley')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# Exercicios parte 2
print('-'*20)
places = ['Japão', 'Alemanha', 'Suica', 'Canada', 'Russia']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
# Exercicios parte 3
print('-'*20)
list_people = ['Matheus', 'Joao', 'Bia', 'Lucas', 'Jose', 'Ian']
print("Quantidade de pessoas na lista: ")
print(len(list_people))
#print(list_people[6]) erro proposital
