car = 'subaru'
age = 19
toppings = ['mushrooms', 'onions']

# 各項目:(条件の文字列, 自分の予想, 実際の結果)
tests = [
    ("car == 'subaru'", True, car == 'subaru'),
    ("car == 'audi'", False, car == 'audi'),
    ("car != 'audi'", True, car != 'audi'),
    ("car != 'subaru'", False, car != 'subaru'),
    ("age >= 18", True, age >= 18),
    ("age < 18", False, age < 18),
    ("'mushrooms' in toppings", True, 'mushrooms' in toppings),
    ("'pepperoni' in toppings", False, 'pepperoni' in toppings),
    ("age > 10 and age < 20", True, age > 10 and age < 20),
    ("age > 30 or age < 10", False, age > 30 or age < 10),
]

for description, prediction, result in tests:
    print(f"Is {description}? I predict {prediction}. Actual: {result}")
    