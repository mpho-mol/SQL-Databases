import sqlite3
import json
import xml.etree.ElementTree as ET
import os

def execute_query(query):
    conn = sqlite3.connect('HyperionDev.db')
    cur = conn.cursor()

    cur.execute(query)
    results = cur.fetchall()

    conn.close()

    return results


def display_courses_by_student_id(student_id):
    query = """
    SELECT Course.course_name
    FROM Course
    INNER JOIN StudentCourse ON Course.course_code = StudentCourse.course_code
    WHERE StudentCourse.student_id = {}
    """.format(student_id)

    results = execute_query(query)

    print("\nCourses taken by the student:")
    for result in results:
        print(result[0])

    return results


def display_address_by_name(first_name, last_name):
    query = """
    SELECT  Address.street, Address.city
    FROM Student
    INNER JOIN Address ON Student.address_id = Address.address_id
    WHERE Student.first_name = '{}' AND Student.last_name = '{}'
    """.format(first_name, last_name)

    results = execute_query(query)

    print("\nAddress:")
    for result in results:
        print("Street:", result[0])
        print("City:", result[1])

    return results


def display_reviews_by_student_id(student_id):
    query = """
    SELECT Review.completeness, Review.efficiency, Review.style, Review.documentation, Review.review_text
    FROM Review
    INNER JOIN Student ON Review.student_id = Student.student_id
    WHERE Review.student_id = {}
    """.format(student_id)

    results = execute_query(query)

    print("\nReviews given to the student:")
    for result in results:
        print("Completeness:", result[0])
        print("Efficiency:", result[1])
        print("Style:", result[2])
        print("Documentation:", result[3])
        print("Review Text:", result[4])

    return results


def display_courses_by_teacher_id(teacher_id):
    query = """
    SELECT Course.course_name
    FROM Course
    WHERE Course.teacher_id = {}
    """.format(teacher_id)

    results = execute_query(query)

    print("\nCourses being given by the teacher:")
    for result in results:
        print("Course Name:", result[0])

    return results

def display_students_who_have_not_completed():
    query = """SELECT Student.student_id, Student.first_name, Student.last_name, Student.email, Course.course_name
    FROM Student
    INNER JOIN StudentCourse ON Student.student_id = StudentCourse.student_id
    INNER JOIN Course ON StudentCourse.course_code = Course.course_code
    WHERE StudentCourse.is_complete = 0
    """

    results = execute_query(query)

    print("\nStudents who have not completed their course:")
    for result in results:
        print("Student Number:", result[0])
        print("First Name:", result[1])
        print("Last Name:", result[2])
        print("Email:", result[3])
        print("Course Name:", result[4])

    return results


def display_students_with_low_marks():
    query = """
    SELECT Student.student_id, Student.first_name, Student.last_name, Student.email, Course.course_name, StudentCourse.mark
    FROM Student
    INNER JOIN StudentCourse ON Student.student_id = StudentCourse.student_id
    INNER JOIN Course ON StudentCourse.course_code = Course.course_code
    WHERE StudentCourse.is_complete = 1 AND StudentCourse.mark <= 30
    """

    results = execute_query(query)

    print("\nStudents who have completed their course and achieved a mark of 30 or below:")
    for result in results:
        print("Student Number:", result[0])
        print("First Name:", result[1])
        print("Last Name:", result[2])
        print("Email:", result[3])
        print("Course Name:", result[4])
        print("Mark:", result[5])

    return results

def get_save_option():
    while True:
        save_option = input("Do you want to save the results? (Y/N): ").strip().upper()
        if save_option in ['Y', 'N']:
            return save_option
        else:
            print("Invalid option. Please enter 'Y' for Yes or 'N' for No.")

def save_results(results, filename, format):
    valid_formats = ["json", "xml"]
    format = format.lower()
    if format not in valid_formats:
        print("Invalid format specified. Results not saved.")
        return

    if format == "json":
        with open(filename, 'w') as file:
            json.dump(results, file, indent=4)
        print("Results saved successfully in JSON format.")
    elif format == "xml":
        root = ET.Element("root")
        for row in results:
            if isinstance(row, dict):
                element = ET.SubElement(root, "item")
                for key, value in row.items():
                    sub_element = ET.SubElement(element, key)
                    sub_element.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename)
        print("Results saved successfully in XML format.")

def main():
    while True:
        print("\nPlease select an option:")
        print("vs: View all courses taken by a student (search by student_id in the following format: 'JV00100200304')")
        print("la: Look up an address given a first name and last name")
        print("lr: List all reviews given to a student (search by student_id in the following format: 'JV00100200304')")
        print("lc: List all courses being given by a teacher (search by teacher_id in the following format: 'MP001')")
        print("lnc: List all students who haven't completed their course")
        print("lf: List all students who have completed their course and achieved a mark of 30 or below")
        print("e: Exit Program")

        choice = input("Enter your choice: ")

        if choice == "vs":
            student_id = input("Enter the student_id: ")
            results = display_courses_by_student_id(student_id)

            save_option = get_save_option()
            if save_option == "Y":
                filename = input("Enter the filename (including extension) e.g results.xml: ")
                file_format = input("Enter the desired format (json/xml): ")
                save_results(results, filename, file_format)

        elif choice == "la":
            first_name = input("Enter the first name: ")
            last_name = input("Enter the last name: ")
            results = display_address_by_name(first_name, last_name)

            save_option = get_save_option()
            if save_option == "Y":
                filename = input("Enter the filename (including extension) e.g results.xml: ")
                file_format = input("Enter the desired format (json/xml): ")
                save_results(results, filename, file_format)

        elif choice == "lr":
            student_id = input("Enter the student_id: ")
            results = display_reviews_by_student_id(student_id)

            save_option = get_save_option()
            if save_option == "Y":
                filename = input("Enter the filename (including extension) e.g results.xml: ")
                file_format = input("Enter the desired format (json/xml): ")
                save_results(results, filename, file_format)

        elif choice == "lc":
            teacher_id = input("Enter the teacher_id: ")
            results = display_courses_by_teacher_id(teacher_id)

            save_option = get_save_option()
            if save_option == "Y":
                filename = input("Enter the filename (including extension) e.g results.xml: ")
                file_format = input("Enter the desired format (json/xml): ")
                save_results(results, filename, file_format)


        elif choice == "lnc":
            results = display_students_who_have_not_completed()

            save_option = get_save_option()
            if save_option == "Y":
                filename = input("Enter the filename (including extension) e.g results.xml: ")
                file_format = input("Enter the desired format (json/xml): ")
                save_results(results, filename, file_format)


        elif choice == "lf":
            results = display_students_with_low_marks()

            save_option = get_save_option()
            if save_option == "Y":
                filename = input("Enter the filename (including extension) e.g results.xml: ")
                file_format = input("Enter the desired format (json/xml): ")
                save_results(results, filename, file_format)

        elif choice == 'e':
            print("Programme exited successfully!")
            break

        else:
            print(f"Invalid choice: '{choice}'")

if __name__ == "__main__":
    main()