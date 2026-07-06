# Student ERP System (Terminal-based)

A simple command-line Student ERP (Enrollment Resource Planning) system built in pure Python.
No external libraries required — uses only the built-in `sqlite3` module.

## Features
- **Student Management**: Add, view, search, update, and delete student records
- **Attendance Management**: Mark and view attendance with percentage calculation
- **Marks Management**: Record subject-wise marks and generate a report card

## Requirements
- Python 3.7 or higher (no extra packages needed)

## How to Run
1. Open a terminal in this folder.
2. Run:
   ```
   python erp.py
   ```
   (On some systems it may be `python3 erp.py`)
3. A database file `student_erp.db` will be created automatically in the same folder on first run — all your data is saved there permanently.

## Menu Overview
```
STUDENT ERP SYSTEM
1. Student Management
   1. Add Student
   2. View All Students
   3. Search Student
   4. Update Student
   5. Delete Student
2. Attendance Management
   1. Mark Attendance
   2. View Attendance
3. Marks Management
   1. Add Marks
   2. View Report Card
4. Exit
```

## Project Structure
```
student_erp/
├── erp.py            # Main application (all logic)
├── student_erp.db    # Auto-created SQLite database (after first run)
└── README.md
```

## Notes / Ideas to Extend
- Add a "Course Management" module to track subjects per course
- Export report cards to PDF or CSV
- Add login/authentication for Admin vs Student roles
- Add grade calculation (A/B/C..) based on percentage
