def upscale_grades(student_grades):
    return {name: (grade + 1 if grade <= 9 else grade) for name, grade in student_grades.items()}

def filter_passed(student_grades):
    return {name: grade for name, grade in student_grades.items() if grade >= 5}
    # return {name: (grade >= 5) for name, grade in student_grades.items()}

def categorize_grades(student_grades):
    passed = {name: grade for name, grade in student_grades.items() if 5 <= grade < 10}
    failed = {name: grade for name, grade in student_grades.items() if grade < 5}
    honors = {name: grade for name, grade in student_grades.items() if grade == 10}
    
    # return a tuple with objects that are dicts
    # return passed, failed , honors  

    return {
        "passed" : passed,
        "failed" : failed,
        "honors" : honors
    }

def calculate_average(student_grades):
    if student_grades:
        return sum(student_grades.values()) / len(student_grades)
    return 0

def main():
    student_grades = {
        "Alice": 7,
        "Bob": 5,
        "Charlie": 9,
        "David": 10,
        "Eve": 3,
        "Frank": 6,
        "Grace": 8,
        "Heidi": 4,
        "Ivan": 10,
        "Judy": 2
    }

    print(f"Original grades: {student_grades}")

    print(f"Upscaled grades: {upscale_grades(student_grades)}")

if __name__ == "__main__":
    main()