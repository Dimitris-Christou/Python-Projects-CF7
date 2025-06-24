# print list
ages = [19, 23, 34, 55, 19]

print("Initial list of ages:", ages)

# with enhanced for
for age in ages:
    print(age, end=", ")
print()    

# enumerate()

for index, value in enumerate(ages):
    print(f"Index: {index}, Value: {value}")
