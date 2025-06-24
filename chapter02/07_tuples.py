# define a tuple of students

students = "Alice", "Bob", "Charlie" # when python encounters comma separated values it assumes by default it is a tuple , no () needed

print(f"{students}: {type(students)}")

# iteration
for index, student in enumerate(students, 1):
    print(f"{index}:{student}")

first_st, second_st, third_st = students  # students[0], students[1], students[2]
print(f"first student: {first_st}")
print(f"second student: {second_st}")
print(f"third student: {third_st}")

# changing an element in a tuple => convert it to list 
students = list(students)
students[0] = "Helen"
students = tuple(students)

print(f"{students} : {type(students)}")


