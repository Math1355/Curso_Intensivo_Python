my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

friend_foods = my_foods

#4.12
for food in my_foods:
    print("Minha comida favorita e " + food)