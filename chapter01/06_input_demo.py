name = input("Please insert your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))

is_student = input("Are you a student? (Yes/No)").lower() =="yes" #(YES, Yes, yES, yes)

print(f"Hello {name}!")

if is_student:
    print("Your are a student")
else: 
    print("Your are not a student")

print("Your age is {0} and your height is {1:.2f} meters".format(age,height))