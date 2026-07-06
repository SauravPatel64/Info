"""
Student ERP System (Terminal-based)
------------------------------------
A simple command-line ERP system to manage:
  - Student records (add / view / update / delete / search)
  - Attendance tracking
  - Marks / grade management

Uses Python's built-in sqlite3 module, so no external installation is needed.
Run with:  python erp.py
"""

import sqlite3
import os

DB_FILE = "student_erp.db"


# ----------------------------------------------------------------------
# DATABASE SETUP
# ----------------------------------------------------------------------
def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            roll_no     INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT NOT NULL,
            course      TEXT NOT NULL,
            year        INTEGER NOT NULL,
            email       TEXT,
            phone       TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no     INTEGER NOT NULL,
            date        TEXT NOT NULL,
            status      TEXT NOT NULL CHECK(status IN ('Present', 'Absent')),
            FOREIGN KEY (roll_no) REFERENCES students(roll_no) ON DELETE CASCADE
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS marks (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no     INTEGER NOT NULL,
            subject     TEXT NOT NULL,
            marks       REAL NOT NULL,
            max_marks   REAL NOT NULL DEFAULT 100,
            FOREIGN KEY (roll_no) REFERENCES students(roll_no) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()


# ----------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------
def pause():
    input("\nPress Enter to continue...")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header(title):
    clear_screen()
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)


def student_exists(cur, roll_no):
    cur.execute("SELECT 1 FROM students WHERE roll_no = ?", (roll_no,))
    return cur.fetchone() is not None


def get_int(prompt):
    while True:
        val = input(prompt).strip()
        if val.isdigit():
            return int(val)
        print("Please enter a valid number.")


def get_float(prompt):
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except ValueError:
            print("Please enter a valid number.")


# ----------------------------------------------------------------------
# STUDENT MANAGEMENT
# ----------------------------------------------------------------------
def add_student():
    print_header("Add New Student")
    name = input("Name: ").strip()
    course = input("Course: ").strip()
    year = get_int("Year (1-4): ")
    email = input("Email (optional): ").strip()
    phone = input("Phone (optional): ").strip()

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, course, year, email, phone) VALUES (?, ?, ?, ?, ?)",
        (name, course, year, email, phone)
    )
    conn.commit()
    roll_no = cur.lastrowid
    conn.close()

    print(f"\nStudent added successfully! Roll No: {roll_no}")
    pause()


def view_students():
    print_header("All Students")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT roll_no, name, course, year, email, phone FROM students ORDER BY roll_no")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No students found.")
    else:
        print(f"{'Roll':<6}{'Name':<20}{'Course':<15}{'Year':<6}{'Email':<20}{'Phone':<12}")
        print("-" * 79)
        for r in rows:
            print(f"{r[0]:<6}{r[1]:<20}{r[2]:<15}{r[3]:<6}{(r[4] or ''):<20}{(r[5] or ''):<12}")

    pause()


def search_student():
    print_header("Search Student")
    keyword = input("Enter roll no. or name to search: ").strip()

    conn = get_connection()
    cur = conn.cursor()
    if keyword.isdigit():
        cur.execute("SELECT roll_no, name, course, year, email, phone FROM students WHERE roll_no = ?", (int(keyword),))
    else:
        cur.execute("SELECT roll_no, name, course, year, email, phone FROM students WHERE name LIKE ?", (f"%{keyword}%",))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No matching student found.")
    else:
        for r in rows:
            print(f"\nRoll No : {r[0]}\nName    : {r[1]}\nCourse  : {r[2]}\nYear    : {r[3]}\nEmail   : {r[4]}\nPhone   : {r[5]}")

    pause()


def update_student():
    print_header("Update Student")
    roll_no = get_int("Enter roll no. to update: ")

    conn = get_connection()
    cur = conn.cursor()
    if not student_exists(cur, roll_no):
        print("Student not found.")
        conn.close()
        pause()
        return

    print("Leave field blank to keep the current value.")
    name = input("New Name: ").strip()
    course = input("New Course: ").strip()
    year = input("New Year: ").strip()
    email = input("New Email: ").strip()
    phone = input("New Phone: ").strip()

    fields, values = [], []
    if name:
        fields.append("name = ?"); values.append(name)
    if course:
        fields.append("course = ?"); values.append(course)
    if year:
        fields.append("year = ?"); values.append(int(year))
    if email:
        fields.append("email = ?"); values.append(email)
    if phone:
        fields.append("phone = ?"); values.append(phone)

    if fields:
        values.append(roll_no)
        cur.execute(f"UPDATE students SET {', '.join(fields)} WHERE roll_no = ?", values)
        conn.commit()
        print("Student updated successfully.")
    else:
        print("No changes made.")

    conn.close()
    pause()


def delete_student():
    print_header("Delete Student")
    roll_no = get_int("Enter roll no. to delete: ")

    conn = get_connection()
    cur = conn.cursor()
    if not student_exists(cur, roll_no):
        print("Student not found.")
    else:
        confirm = input("Are you sure? This deletes attendance/marks too (y/n): ").strip().lower()
        if confirm == "y":
            cur.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
            conn.commit()
            print("Student deleted.")
        else:
            print("Cancelled.")
    conn.close()
    pause()


# ----------------------------------------------------------------------
# ATTENDANCE MANAGEMENT
# ----------------------------------------------------------------------
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


# ----------------------------------------------------------------------
# MARKS MANAGEMENT
# ----------------------------------------------------------------------
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


# ----------------------------------------------------------------------
# MENUS
# ----------------------------------------------------------------------
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


if __name__ == "__main__":
    main_menu()
