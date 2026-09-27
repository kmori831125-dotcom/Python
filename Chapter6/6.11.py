cities = {
    "New York": {"country": "USA", "population": 8000000, "fact": "The city that never sleeps."},
    "London": {"country": "UK", "population": 9000000, "fact": "Home to the Tower of London."},
    "Tokyo": {"country": "Japan", "population": 14000000, "fact": "The most populous city in the world."}
}

for city, info in cities.items():
    country = info["country"].title()
    population = info["population"]
    fact = info["fact"]
    
    print(f"{city.title()} is in {country}. It has a population of {population}. Fun fact: {fact}")