

from databases import get_connection,init_db
from databases import pause, clear_screen, print_header,student_exists,get_int,get_float


def mark_attendance():
    print_header("Mark Attendance")
    roll_no = get_int("Enter roll no.: ")

    conn = get_connection()
    cur = conn.cursor()
    if not student_exists(cur, roll_no):
        print("Student not found.")
        conn.close()
        pause()
        return

    date = input("Date (YYYY-MM-DD): ").strip()
    status = ""
    while status not in ("Present", "Absent"):
        status = input("Status (Present/Absent): ").strip().capitalize()

    cur.execute("INSERT INTO attendance (roll_no, date, status) VALUES (?, ?, ?)", (roll_no, date, status))
    conn.commit()
    conn.close()

    print("Attendance recorded.")
    pause()


def view_attendance():
    print_header("View Attendance")
    roll_no = get_int("Enter roll no.: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT date, status FROM attendance WHERE roll_no = ? ORDER BY date", (roll_no,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No attendance records found.")
    else:
        total = len(rows)
        present = sum(1 for r in rows if r[1] == "Present")
        print(f"{'Date':<15}{'Status':<10}")
        print("-" * 25)
        for r in rows:
            print(f"{r[0]:<15}{r[1]:<10}")
        print(f"\nAttendance: {present}/{total} ({(present/total)*100:.1f}%)")

    pause()
