# populate dict
products = {
    1:"apple",
    2:"banana",
    3:"honey", 
    4:"melon"
}

print(f"Initial dict: {products}")

# insert a new key:value pair
products[5] = "orange"
print(f"Dict after insertion: {products}")

# insert a new key:value pair, using an existing key (it "updates" it)
products[3] = "milk"
print(f"Dict after insertion: {products}")

# read an element(access)
# product_1 = products[1]
# print(product_1)

# product_10 = products[10] #Error
# print(product_10)

product_1 = products.get(1)
print(product_1)

product_10 = products.get(10, "Product not found")
print(product_10)

# delete function in dicts
del products[1]
print(f"After deleting key 1 : {products}")

# pop function in dicts
removed_item = products.pop(3, "Item not found")
print(f"Removed item: {removed_item}")
print(f"After popping: {products}")

# Delete: remove the 'last' in serted item with popitem
key, value = products.popitem()
print(f"key: {key}, value: {value}")
print(products)

key_to_check = 2

if key_to_check in products:
    print(f"Key: {key} exists")
else:
    print(f"key: {key_to_check} does not exist")

# iterate

for key in products:
    print(key, ":", products[key])

print("-"*10)
for key in products.keys():
    print(key, ":", products[key])

print("-"*10)
for value in products.values():
    print(value)

print("-"*10)
for key, value in products.items():
    print(f"{key}, {value}")