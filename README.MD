#School Database Project

This project establishes a connection to a SQLite database named school.db. It demonstrates basic database connection setup using Python's sqlite3 library.

Usage

Ensure you have Python installed.

Run the script to connect to school.db.

import sqlite3
conn = sqlite3.connect("db/school.db")
cursor = conn.cursor()

2.
This code defines a Student class for interacting with a database table named students. The class         

includes methods for creating and dropping the table (create_table, drop_table), and for inserting 

(save), updating (update), and deleting (delete) student records. Each student instance has attributes 

such as first_name, last_name, gender, age, phone, username, and email. The save method inserts a new 

student into the database, while the create class method simplifies the creation and saving of new 

students. The update method modifies an existing student's record, and the delete method removes it from 

the database. The use of bound parameters in SQL queries helps prevent SQL injection

3.
PAYMENTS.PY

Initialization:

The __init__ method initializes a Payment instance with first_name, last_name, gender, and amount 

attributes.

The __repr__ method provides a string representation of the Payment object.

Database Connection:

The connection to the database (school.db) is established using sqlite3.connect, and a cursor is created 

for executing SQL commands.

Class Methods:

create_table: This method creates a payments table if it doesn't already exist, with columns for id, 

first_name, last_name, gender, and amount. The id column is an auto-incrementing primary key.

create: This method inserts a new payment record into the payments table and returns a new Payment 

instance with the provided attributes.

4.
COURSES.PY

Initialization:

The __init__ method initializes a Courses instance with first_course and duration attributes.

The __repr__ method provides a string representation of the Courses object, but it had an error with the 

attribute names which are fixed below.

Class Methods:

create_table: This method creates a courses table if it doesn't already exist, with columns for id, 

first_course, and duration. The id column is an auto-incrementing primary key.

create: This method inserts a new course record into the courses table and returns a new Courses instance 

with the provided attributes.

5.DEBUG.PY

Import the Student class from the models.students module.

Drop and recreate the students table:

Student.drop_table(): Drops the students table if it exists.

Student.create_table(): Creates the students table with the specified schema.

Create student records using the Student.create class method. This method inserts the provided student 

details into the students table and returns the newly created Student instance.

Six students (student1 to student6) are created with varying attributes.

Import the Courses class from the models.courses module.

Create the courses table:

Courses.create_table(): Creates the courses table with the specified schema.

Create course records using the Courses.create class method. This method inserts the provided course 

details into the courses table and returns the newly created Courses instance.

Three courses (courses1 to courses3) are created with varying attributes.

6.
helper.py

find_by_id and get_all Methods:

These methods are added to the Student and Courses classes to facilitate record retrieval and listing.

create_student and delete_student Functions:

These functions now handle user input, interact with the database, and provide feedback to the user.

display_students Function:

This function lists all students in the database.

Menu Loop:

A simple menu loop is provided to interact with the user and call the appropriate functions based on user 

input.

created by Njau(future pro football)



