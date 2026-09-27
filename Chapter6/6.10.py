favorite_numbers = {"John": [7, 14], "Alice": [22, 33], "Bob": [5, 10, 15]}
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")