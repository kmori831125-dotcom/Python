# 1. 文字列の等しい/等しくない
car = 'audi'
print(car == 'audi')   # True
print(car == 'bmw')    # False
print(car != 'bmw')    # True
print(car != 'audi')   # False

# 2. lower() を使ったテスト
name = 'Audi'
print(name.lower() == 'audi')   # True
print(name.lower() == 'Audi')   # False(小文字にした値は大文字を含む文字列と一致しない)

# 3. 数値の比較
age = 20
print(age == 20, age != 20)    # True False
print(age > 18, age < 18)      # True False
print(age >= 20, age <= 19)    # True False

# 4. and / or
print(age >= 18 and age < 65)   # True
print(age >= 18 and age < 20)   # False
print(age < 18 or age == 20)    # True
print(age < 18 or age > 65)     # False

# 5. in
toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in toppings)   # True
print('pepperoni' in toppings)   # False

# 6. not in
print('pepperoni' not in toppings)   # True
print('mushrooms' not in toppings)   # False