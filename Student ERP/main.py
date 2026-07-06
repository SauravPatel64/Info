
from databases import get_connection,init_db
from databases import pause,clear_screen,print_header,student_exists,get_int,get_float

from models import delete_student,update_student,search_student,add_student,view_students
from models import mark_attendance,view_attendance
from models import add_marks,view_report_card



from menues import attendance_menu, marks_menu, student_menu




def main_menu():
    init_db()
    while True:
        print_header("STUDENT ERP SYSTEM")
        print("1. Student Management")
        print("2. Attendance Management")
        print("3. Marks Management")
        print("4. Exit")
        choice = input("\nEnter choice: ").strip()

        if choice == "1": student_menu()
        elif choice == "2": attendance_menu()
        elif choice == "3": marks_menu()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice.")
            pause()


main_menu()

