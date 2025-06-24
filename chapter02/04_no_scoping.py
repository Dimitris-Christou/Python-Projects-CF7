import random
# populate the list with 10 random integers
random_numbers = []

for _ in range(10):             # _ placeholder instead "i"
    num = random.randint(1, 100)
    random_numbers.append(num)

print(random_numbers)

print(f"i = {_}")

# print the last even number in the list
for num in random_numbers:
    if num % 2 == 0:
        even = num

print(even)