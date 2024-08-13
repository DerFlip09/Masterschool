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

######################## MASTERSCHOOL SOLUTION ############################

# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-03-23 17:51:14
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-03-25 23:17:28

"""
Help Your Teacher 2

Create student dictionaries and print student grade information
"""
from typing import Any, Dict, List, Tuple

SUBJECTS = ("English", "Math")


def get_grade(subject: str) -> float:
    """
    Returns grade of given subject entered by user

    Asks user enter a number until a non-negative number is given
    """
    while True:
        try:
            grade = float(input(f"Enter {subject} grade: "))
        except ValueError:
            print("Expected a number")
            continue

        if grade < 0:
            print("Grade cannot be negative")
            continue

        return grade


def get_student_info() -> Dict[str, Any]:
    """
    Returns a dictionary of student info containing his name and grades
    """
    student_info = {}
    student_info["Name"] = input("Enter student name: ")
    for subject in SUBJECTS:
        student_info[subject] = get_grade(subject)
    return student_info


def ask_number_of_students() -> int:
    """
    Returns a number of students

    Asks user enter a number until a positive integer is given
    """
    while True:
        try:
            nb_students = int(input("Enter the number of students: "))
        except ValueError:
            print("Expected a positive integer")
            continue

        if nb_students <= 0:
            print("Expected a positive integer")
            continue

        return nb_students


def ask_detail_of_students(nb_students: int) -> List[Dict[str, Any]]:
    """
    Returns a list of students
    """
    students = []
    for i in range(nb_students):
        print("", f"Enter details for student {i+1}:", sep="\n")
        students.append(get_student_info())
    return students


def print_student_info(students: List[Dict[str, Any]]):
    """
    Prints student information
    """
    print("", "Student Information:", sep="\n")
    for student in students:
        name = student["Name"]
        grades = [value for key, value in student.items() if key in SUBJECTS]
        best_grade = max(grades)
        avg_grade = sum(grades) / len(grades)
        print(
            f"Student: {name}, Best Grade: {best_grade}, Average Grade: {avg_grade:.2f}"
        )


def calculate_average_grades(
    students: List[Dict[str, Any]]
) -> Tuple[Dict[str, float], float]:
    """
    Returns tuple of average grades per subject and the overall average grade
    """
    # for each subject in the given tuple SUBJECTS
    # get list of grades of students on that subject
    # (list, dictionary comprehension technique)
    grades_per_subject = {
        subject: [student[subject] for student in students] for subject in SUBJECTS
    }

    # compute the average grade of a subject by dividing the total by number of grades
    # use dictionary comprehension technique to compute on all subjects
    avg_grades_per_subject = {
        subject: sum(grades_per_subject[subject]) / len(grades_per_subject[subject])
        for subject in SUBJECTS
    }

    # overall average grade is the mean of average grades of all subjects
    overall_avg_grade = sum(avg_grades_per_subject.values()) / len(avg_grades_per_subject)
    return avg_grades_per_subject, overall_avg_grade


def print_average_grades(students: List[Dict[str, Any]]):
    """
    Prints average grades per subject and overall average grade
    """
    avg_grades_per_subject, overall_avg_grade = calculate_average_grades(students)
    print("", "Average grades per subject:", sep="\n")
    for subject, avg_grade in avg_grades_per_subject.items():
        print(f"{subject}: {avg_grade:.2f}")

    print("", f"Overall average grade across all subjects: {overall_avg_grade:.2f}", sep="\n")


def main():
    """
    Main function
    """
    nb_students = ask_number_of_students()
    students = ask_detail_of_students(nb_students)
    print_student_info(students)
    print_average_grades(students)