favorite_language = {"John": "Python", "Alice": "JavaScript", "Bob": "C++"}
persons = ["John", "Alice", "Bob", "Eve", "Charlie"]

for person in persons:
    if person in favorite_language:
        print(f"{person.title()}'s favorite language is {favorite_language[person]}")
    else:
        print(f"{person.title()}, please take our poll!")