
from databases import get_connection,init_db
from databases import pause,clear_screen,print_header,student_exists,get_int,get_float

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

