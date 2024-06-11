from students import Student
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
student3 = Student.create(
    "Ian", "Njau", "Male", 18, "0712345634", "Nian", "Nian@example.com"
)
student3 = Student.create(
    "Ian", "Njau", "Male", 18, "0712345634", "Nian", "Nian@example.com"
)
student3 = Student.create(
    "Ian", "Njau", "Male", 18, "0712345634", "Nian", "Nian@example.com"
)

# update a recorde
# student1.age = 25
# student2.phone = "0712121212"

# student1.update()
# student2.update()


# delete record from the table
# student1.delete()
# student1.delete()
