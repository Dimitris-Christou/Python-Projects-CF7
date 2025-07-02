cities = ["london", "paris", "barcelona", "athens", "Casablanca"]

# filter city names longer than 5 characters (using filter and lambda)
long_cities = filter(lambda city: len(city) > 5, cities)

# print(long_cities)

cap_length_cities = list(map(lambda city: city.title(), long_cities))

# print(cap_length_cities)

# All in one...

clc = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities)))
print(clc)

# list comprehension

cap_title_cities_compr = [city.title() for city in cities if len(city) > 5]
print(cap_title_cities_compr)