def enroll_students(*students, min_grade=50, department="Computer Science", **kwargs):
    print(f"Min grade: {min_grade}")
    print(f"Department: {department}")
    
    print("\nEnrolled Students")
    for student in students:
        print(f" - {student}")

    print("\nAdditional information")
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    
    print("---End of enrollment")

def main():
    enroll_students("Chris", "Marinos")
    print("="*10)

    enroll_students("Hellen", "Nick", "Jack", min_grade=70, academinc_year=2026, semester="Fall")


if __name__ == "__main__":
    main()