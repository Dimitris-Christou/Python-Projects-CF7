# range(10)

a = range(10)
print(a)
print(f"Type of a: {type(a)}")

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
print()

for i in range(10):
    if i == 5:
        continue # break 
    print(i, end=" ")
else:
    print("Loop ended normally.")

# List of fruits
fruits = ["Banana".lower(), "Apple".lower(), "Grapes".lower(), "Orange".lower()]

fruit_to_check = input("Please name a fruit to check: ").lower()

# Java Style
for fruit  in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in the list")
        break
else:
    print(f"{fruit_to_check} not in list")


# challenge : write it in one line of code.
# Python Style
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} the list")