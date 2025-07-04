def upscale_grade(grades):
    upscaled = [grade + 1 if grade <= 9 else grade for grade in grades]
    return upscaled

def filter_passed(grades):
    passed = [grade for grade in grades if grade >= 5]
    return passed

def categrorize_grades(grades):
    passed = [grade for grade in grades if grade >= 5 and grade < 10]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]
    return passed, failed, honors

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def main():
    grades = [7, 5, 9, 10, 5, 3, 7, 8]
    print(f"Initial grades: {grades}")
    
    print(f"Upscaled grades: {upscale_grade(grades)}")

    passed_gd, failed_gd, honored_gd = categrorize_grades(grades)
    print(f"Passed Students: {passed_gd}")
    print(f"Failed Students: {failed_gd}")
    print(f"Honored Students: {honored_gd}")

    print(f"Average grade: {calculate_average(grades)}")



if __name__ == "__main__":
    main()