import os

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

