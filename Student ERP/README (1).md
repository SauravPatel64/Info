# Student ERP System (Terminal-based, In-Memory)

A simple command-line Student ERP system built in pure Python. There's no database and
no file storage — all data lives in a single Python dictionary while the program runs.

On startup, the dictionary is auto-filled with **5 random sample students** (with random
attendance and marks) so you have something to explore right away.

⚠️ **Note:** Since there's no file or database, all data (including anything you add)
is lost when you close the program. Each run starts fresh with a new random set of students.

## Features
- **Student Management**: Add, view, search, update, and delete student records
- **Attendance Management**: Mark and view attendance with percentage calculation
- **Marks Management**: Record subject-wise marks and generate a report card

## Requirements
- Python 3.7 or higher — no external packages needed (only built-in `random` and `os`)

## How to Run
```
python erp.py
```

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
STUDENT ERP/
│
├── databases/
│   ├── __init__.py
│   ├── database.py
│   └── style.py
│
├── menues/
│   ├── __init__.py
│   └── features.py
│
├── models/
│   ├── __init__.py
│   ├── AttendanceManagement.py
│   ├── MarksManagement.py
│   └── StudentManagement.py
│
├── main.py
└── student.db
```

## Ideas to Extend
- Change `generate_random_students()` count/logic for more sample data
- Add persistence later (JSON file or database) if you decide you want data to survive restarts
- Add grade calculation (A/B/C..) based on percentage
- Add login/authentication for Admin vs Student roles
