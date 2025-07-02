my_list = [1, 2, 3, 4, 5]

# simple unpacking
a, b, c, d, e = my_list

print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")

# skipping some values
a, _, c, _, e = my_list
print(f"a = {a}, c = {c}, e = {e}")

# unpack the first element and the remaining elements
a, *b = my_list
print(f"a = {a}, b = {b}")

*a, b = my_list
print(f"a = {a}, b = {b}")

*a, b, c = my_list
print(f"a = {a}, b = {b}, c = {c}")

a, *b, c = my_list
print(f"a = {a}, b = {b}, c = {c}")

my_list = [1, 2, 3]
a, *b, c = my_list
print(f"a = {a}, b = {b}, c = {c}")

my_list = [1, 2]
a, *b, c = my_list
print(f"a = {a}, b = {b}, c = {c}")

my_list = (1, 2, 3, 4, 5)
a, *b, c = my_list
print(f"a = {a}, b = {b}, c = {c}")

my_list = (1, 2)
a, *b, c = my_list
print(f"a = {a}, b = {b}, c = {c}")
