def main():
    students = {
    "Alice" : 85,
    "Bob" : 90,
    "Charlie" : 94,
    "Diana" : 80,
    "Eve" : 81
}
    
    # Find the student with the lowest alphabetic order student_name 
    student_with_min_name = min(students)
    print(student_with_min_name)

    # Find the student with the lowest grade!
    student_with_min_grade = min(students, key=students.get)
    print(student_with_min_grade)

    # Find the student with shortest name by length
    student_with_shortest_name = min(students, key=len)
    print(student_with_shortest_name)
    

if __name__ == "__main__":
    main()