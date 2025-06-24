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