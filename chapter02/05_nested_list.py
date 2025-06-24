items = [1, 2, 3.14, True, "Hello there"]

for item in items:
    print(item, end=" ")
print()

nested_list = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# nested_list = [[1,2], [3,4], [5,6]]

print(f"first list item: {nested_list[0]}")

# print '3' from the nested list

print(f"third list item: {nested_list[1][0]}")

# print [3,4], [1,2]
print(f"{nested_list[1]}, {nested_list[0]}")
# with slicing?

#
