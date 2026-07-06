

import sqlite3
import os




def get_connection():
    conn = sqlite3.connect("student_erp.db")
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
