
from databases import get_connection,init_db
from databases import pause,clear_screen,print_header,student_exists,get_int,get_float


from models import delete_student,update_student,search_student,add_student,view_students
from models import mark_attendance,view_attendance
from models import add_marks,view_report_card





def student_menu():
    while True:
        print_header("Student Management")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back to Main Menu")
        choice = input("\nEnter choice: ").strip()

        if choice == "1": add_student()
        elif choice == "2": view_students()
        elif choice == "3": search_student()
        elif choice == "4": update_student()
        elif choice == "5": delete_student()
        elif choice == "6": break
        else:
            print("Invalid choice.")
            pause()


def attendance_menu():
    while True:
        print_header("Attendance Management")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Back to Main Menu")
        choice = input("\nEnter choice: ").strip()

        if choice == "1": mark_attendance()
        elif choice == "2": view_attendance()
        elif choice == "3": break
        else:
            print("Invalid choice.")
            pause()


def marks_menu():
    while True:
        print_header("Marks Management")
        print("1. Add Marks")
        print("2. View Report Card")
        print("3. Back to Main Menu")
        choice = input("\nEnter choice: ").strip()

        if choice == "1": add_marks()
        elif choice == "2": view_report_card()
        elif choice == "3": break
        else:
            print("Invalid choice.")
            pause()
