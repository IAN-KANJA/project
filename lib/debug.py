from models.students import Student
Student.drop_table()
Student.create_table()
student1 = Student.create(
    "Cristian", "Olufsen", "Male", 19, "07123903634", "OlufsenBigMan", "Olufsen@gmail.com"
)
student2 = Student.create(
    "Agnes", "Gitau", "Female", 18, "0712345634", "Aggie", "agnes@example.com"
)
student3 = Student.create(
    "Ian", "Njau", "Male", 18, "0712345634", "Nian", "Nian@example.com"
)
student4 = Student.create(
    "Ian", "Njau", "Male", 18, "0712345634", "Nian", "Nian@example.com"
)
student5 = Student.create(
    "Ian", "Njau", "Male", 18, "0712345634", "Nian", "Nian@example.com"
)
student6 = Student.create(
    "Gian", "Njau", "Male", 18, "0712345634", "Nian", "Nian@example.com"
)

from models.courses import Courses
 
Courses.create_table()

courses1 = Courses.create(
    "Software Engerinering", "6months"
)
courses2 = Courses.create(
    "cyber security", "6months"
)
courses3 = Courses.create(
    "National security", "6months"
)