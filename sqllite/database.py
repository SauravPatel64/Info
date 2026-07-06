import sqlite3

conn = sqlite3.connect('test.db')
print("open successfully")

# command = "CREATE TABLE List (id int,task text,date text,status text)"

command = "insert into todo (id,task,date,status) values(1,'learning','1-10-2026','continue')"

conn.execute(command)
conn.commit()
print("table created")
