students = {
    "Alice" : [85, 92, 100],
    "Bob" : [],
    "Charlie" : [90, 95, 94],
    "Diana" : [95, 98, 100],
    "Eve" : [50, 60, 55]
}

def main():
    while True:
        try:
            threshold = int(input("Please insert a threshold (int): "))
        except ValueError:
            print("Invalid input")
            break
        
        average_grades = {
            student : round(sum(grades) / len(grades), 2)
            for student,grades in students.items()
            if grades and (sum(grades) / len(grades)) > threshold
        }

        for student, average_grades in average_grades.items():
            print(f"{student}:{average_grades}")

if __name__ == "__main__":
    main()