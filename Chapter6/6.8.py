pet_1 = {"type": "dog", "owner": "John"}
pet_2 = {"type": "cat", "owner": "Alice"}
pet_3 = {"type": "bird", "owner": "Bob"}

pets = [pet_1, pet_2, pet_3]    

for pet in pets:
    print()
    print(f"A {pet['type']} is owned by {pet['owner']}.")