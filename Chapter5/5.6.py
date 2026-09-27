ages = [1, 3, 10, 15, 30, 70]   # いろいろな年齢でテスト

for age in ages:
    if age < 2:
        stage = "a baby"
    elif age < 4:
        stage = "a toddler"
    elif age < 13:
        stage = "a kid"
    elif age < 18:
        stage = "a teenager"
    elif age < 65:
        stage = "an adult"
    else:
        stage = "an elder"
    print(f"A person aged {age} is {stage}.")