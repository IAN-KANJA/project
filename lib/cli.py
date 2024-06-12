
from helpers import exit_program,create_student,delete_student,display_Student,create_course



def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            display_Student()
        elif choice == "4":
            create_course()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1.create_student")
    print("2. delete_student")
    print("3. display_Student")
    print("4: create_course")



if __name__ == "__main__":
    main()