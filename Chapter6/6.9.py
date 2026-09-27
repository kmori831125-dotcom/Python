favorite_places = {"Alice": ["Paris", "Tokyo"], "Bob": ["New York", "London"], "Charlie": ["Sydney", "Rio de Janeiro"]}
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f"\t{place}")