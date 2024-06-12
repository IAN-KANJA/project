from models.students import Student
from models.courses import Courses
from models.payment import Payment


def exit_program():
    print("Goodbye!")
    exit()


def create_student():
    first_name = input("Enter firstname: ")
    second_name = input("Enter secondname: ")
    gender = input("Enter gender ")
    age = int(input("Enter age: "))
    phone = input("Enter phone")
    username =input ("Enter username")
    email = input ("Enter email")
    print(create_student)

def delete_student():
    Student_id= input("Enter the Student's id: ")
    try:
        if Student := Student.find_by_id(Student_id):
            Student.delete()
            print(f'Student {Student_id} deleted')
        else:
             print(f'Student{Student_id} not found')
    except Exception as e:
        print(f"Error deleting Student: {e}")

def display_Student():
    Student = Student.get_all()
    for Student in Student:
        print(Student)  

def create_course():
    first_course = input("enter firstcourse") 


# def delete_course():