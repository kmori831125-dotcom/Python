my_pizzas = ['pepperoni', 'margherita', 'hawaiian', 'quattro formaggi', 'marinara']
friend_pizzas = my_pizzas[:]

my_pizzas.append('veggie')
friend_pizzas.append('bbq chicken')

print("My favorite pizzas are:")
for pizza in my_pizzas: 
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
    
    
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for food in my_foods:
    print(food)
    
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
    