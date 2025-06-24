fruits = ["Apple", "Banana", "Cherry", "Durian", "Apple"]

print(f"Initial list: {fruits}")

# Add a fruit at the end of the list
fruits.append("Elderberry")
print("After adding Elderberry:", fruits)

fruits.extend(["Fig", "Grapes"])
print("After adding Grapes, Fig:", fruits)

# insert an element in a specific position
fruits.insert(1, "Apricot")
print("After adding Apricot:", fruits)

# updating an element in a list
fruits[0] = "Avocado" #overwrites Apple
print("After updating the first element",fruits)

# Updupadateate a slice of a list
fruits[1:3] = ["A", "B", "C"]
print("After slicing", fruits)

# pop()
removed_items = fruits.pop(2)
print(f"Removed item: {removed_items}")
print("After popping:", fruits)

# remove
fruits.remove("A")
print("After remove('A'):", fruits)

idx = fruits.index('A')
print(idx)

item_to_remove = "Grapesss"
if item_to_remove in fruits:
    fruits.remove(item_to_remove)
    print(f"{item_to_remove} removed")
else:
    print("Not a valid fruit")