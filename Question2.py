# ==========================================
#     PERSONAL POCKET CGPA CALCULATOR (PPC)
# ==========================================

print("==========================================")
print("     PERSONAL POCKET CGPA CALCULATOR")
print("==========================================")

while True:
    print("\nMENU")
    print("1. Calculate CGPA")
    print("2. Clear")
    print("3. OFF")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        num_courses = int(input("\nEnter the number of courses: "))

        total_grade_points = 0
        total_course_units = 0

        for i in range(1, num_courses + 1):
            print(f"\nCourse {i}")
            course = input("Course Code: ")
            unit = int(input("Course Unit: "))
            grade = input("Grade (A, B, C, D, E, F): ").upper()

            if grade == "A":
                point = 5
            elif grade == "B":
                point = 4
            elif grade == "C":
                point = 3
            elif grade == "D":
                point = 2
            elif grade == "E":
                point = 1
            elif grade == "F":
                point = 0
            else:
                print("Invalid grade! Grade point set to 0.")
                point = 0

            total_grade_points += point * unit
            total_course_units += unit

        if total_course_units > 0:
            cgpa = total_grade_points / total_course_units

            print("\n========== RESULT ==========")
            print("Total Course Units :", total_course_units)
            print("Total Grade Points :", total_grade_points)
            print("CGPA               :", round(cgpa, 2))

            if cgpa >= 4.50:
                print("Class of Degree    : First Class")
            elif cgpa >= 3.50:
                print("Class of Degree    : Second Class Upper")
            elif cgpa >= 2.40:
                print("Class of Degree    : Second Class Lower")
            elif cgpa >= 1.50:
                print("Class of Degree    : Third Class")
            elif cgpa >= 1.00:
                print("Class of Degree    : Pass")
            else:
                print("Class of Degree    : Fail")

        else:
            print("No course units entered.")

    elif choice == "2":
        print("\nCalculator Cleared!")

    elif choice == "3":
        print("\nThank you for using the Personal Pocket CGPA Calculator.")
        print("Calculator OFF.")
        break

    else:
        print("\nInvalid choice! Please select 1, 2, or 3.")
