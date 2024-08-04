def get_grade(subject):
    """
    Asks for the grade of a student as long as it takes until the user enters a positive integer
    :param subject: string
    :return grade: float
    """
    while True:
        try:
            grade = float(input(f"Enter {subject} grade: "))
            if grade > 0:
                return grade
            else:
                raise ValueError
        except ValueError:
            print("Expected a number")


def get_student_info(place):
    """
    Asks for the Name and the Grades of a Student and puts this information in a dictionary
    :param place: int
    :return student: dict
    """
    student = {"Name": input(f"\nEnter detail student {place}:\nEnter student name: "),
               "English": get_grade("English"),
               "Math": get_grade("Math")}
    return student


def get_student_count():
    """
    Asks for count of students as long as it takes until the user enters a positive integer
    :return student_count: int
    """
    while True:
        try:
            student_count = int(input("Enter the number of students: "))
            if student_count > 0:
                return student_count
            else:
                raise ValueError
        except ValueError:
            print("Expect a positive Integer")


def print_student_info(students):
    """
    Prints the name, the best grade and the average grade of every student in the dictionary
    :param students:
    :return None:
    """
    print("\nStudent Information:")
    for student in students:
        name, english_grade, math_grade = student.values()
        max_grade = max(english_grade, math_grade)
        avg_grade = (english_grade + math_grade) / 2
        print(f"Student: {name}, Best Grade: {max_grade}, Average Grade: {avg_grade}")


def calculate_average_grades(students):
    """
    calculates the average grade of English and Math out of the students dictionary
    and also calculates the overall average grade
    :param students: dictionary
    :return average_grades: tuple
    """
    students_count = 0
    average_grades = [{"English": 0, "Math": 0}]
    for student in students:
        name, english_grade, math_grade = student.values()
        average_grades[0]["English"] += english_grade
        average_grades[0]["Math"] += math_grade
        students_count += 1
    # Calculate the averages of every subject
    average_grades[0]["English"] /= students_count
    average_grades[0]["Math"] /= students_count
    average_grades.append((average_grades[0]["English"] + average_grades[0]["Math"]) / 2)
    return tuple(average_grades)


def print_average_grades(students):
    """
    Prints the average grades of english and math and also the overall average grade
    :param students: dictionary
    :return: None
    """
    average_grades_per_subject, overall_average_grade = calculate_average_grades(students)
    print("\nAverage grades per subject:")
    for subject, average_grade in average_grades_per_subject.items():
        print(f"{subject}: {average_grade:.2f}")
    print(f"\nOverall average grade across all subjects: {overall_average_grade:.2f}")


def main():
    """
    Main Function to get and print student information and the average grades
    :return: None
    """
    student_information = []
    student_count = get_student_count()
    for i in range(student_count):
        student_information.append(get_student_info(i+1))
    print_student_info(student_information)
    print_average_grades(student_information)


if __name__ == "__main__":
    main()
