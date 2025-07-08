numbers = [1, 2, 3, 4, 5, 6, 7]

squared_nums = {num : num**2 for num in numbers}
print(squared_nums)
print()

even_sq_nums = {num : num**2 for num in numbers if num % 2 == 0}
print(even_sq_nums)
print()

def squared(n):
    return n**2

sq_dict = {num: squared(num) for num in numbers}
print(sq_dict)
print()

