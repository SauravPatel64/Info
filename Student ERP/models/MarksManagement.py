
from databases import get_connection,init_db
from databases import pause,clear_screen,print_header,student_exists,get_int,get_float


def add_marks():
    print_header("Add Marks")
    roll_no = get_int("Enter roll no.: ")

    conn = get_connection()
    cur = conn.cursor()
    if not student_exists(cur, roll_no):
        print("Student not found.")
        conn.close()
        pause()
        return

    subject = input("Subject: ").strip()
    marks = get_float("Marks obtained: ")
    max_marks = get_float("Maximum marks (default 100): ") or 100

    cur.execute(
        "INSERT INTO marks (roll_no, subject, marks, max_marks) VALUES (?, ?, ?, ?)",
        (roll_no, subject, marks, max_marks)
    )
    conn.commit()
    conn.close()

    print("Marks added.")
    pause()


def view_report_card():
    print_header("Report Card")
    roll_no = get_int("Enter roll no.: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT name, course, year FROM students WHERE roll_no = ?", (roll_no,))
    student = cur.fetchone()

    if not student:
        print("Student not found.")
        conn.close()
        pause()
        return

    cur.execute("SELECT subject, marks, max_marks FROM marks WHERE roll_no = ?", (roll_no,))
    rows = cur.fetchall()
    conn.close()

    print(f"Name   : {student[0]}")
    print(f"Course : {student[1]}   Year: {student[2]}")
    print("-" * 40)

    if not rows:
        print("No marks recorded yet.")
    else:
        total_obtained = total_max = 0
        print(f"{'Subject':<20}{'Marks':<15}")
        for r in rows:
            print(f"{r[0]:<20}{r[1]}/{r[2]}")
            total_obtained += r[1]
            total_max += r[2]
        percentage = (total_obtained / total_max) * 100 if total_max else 0
        print("-" * 40)
        print(f"Total: {total_obtained}/{total_max}  ({percentage:.2f}%)")

    pause()

